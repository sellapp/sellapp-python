"""Check retained Python distributions without executing package code or rebuilding."""

import argparse
import email.parser
import hashlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import tarfile
import zipfile

REPOSITORY = "sellapp/sellapp-python"
MAX_PACKAGE_BYTES = 50 * 1024 * 1024


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def validate_manifest(raw, expected_hash, source, ownership, sdk_commit, tag):
    require(
        bool(re.fullmatch(r"[a-f0-9]{64}", expected_hash)),
        "Expected a SHA-256 manifest digest",
    )
    require(
        len(raw) <= 65536 and sha256(raw) == expected_hash,
        "Publication manifest hash differs",
    )
    manifest = json.loads(raw)
    version = manifest.get("version", "")
    require(
        bool(re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version)) and tag == "v" + version,
        "Release tag/version differs",
    )
    require(
        manifest.get("schemaVersion") == 1 and manifest.get("repository") == REPOSITORY,
        "Unexpected publication repository/schema",
    )
    require(
        bool(re.fullmatch(r"[a-f0-9]{40}", sdk_commit))
        and manifest.get("sdkCommit") == sdk_commit,
        "SDK commit differs from workflow checkout",
    )
    require(
        ownership.get("repository") == REPOSITORY
        and ownership.get("language") == "python",
        "Unexpected source ownership",
    )
    require(
        source.get("sdkVersion") == version and source.get("language") == "python",
        "Generated SDK language/version differs",
    )
    require(
        source.get("generatorDirty") is False,
        "Source was generated from a dirty checkout",
    )
    require(
        manifest.get("sourceSha")
        == source.get("generatorCommit")
        == ownership.get("sourceSha"),
        "Generator source identity differs",
    )
    require(
        bool(re.fullmatch(r"[a-f0-9]{40}", manifest.get("sourceSha", ""))),
        "Invalid generator source identity",
    )
    require(
        manifest.get("specSha256")
        == source.get("specSha256")
        == ownership.get("specSha256"),
        "Specification identity differs",
    )
    require(
        bool(re.fullmatch(r"[a-f0-9]{64}", manifest.get("specSha256", ""))),
        "Invalid specification digest",
    )
    files = manifest.get("files", [])
    expected = {
        f"sellapp_sdk-{version}-py3-none-any.whl",
        f"sellapp_sdk-{version}.tar.gz",
    }
    require(
        len(files) == 2 and {f.get("name") for f in files} == expected,
        "Expected exactly the wheel and source distribution",
    )
    for item in files:
        require(
            bool(re.fullmatch(r"[a-f0-9]{64}", item.get("sha256", ""))),
            "Invalid package digest",
        )
        require(
            type(item.get("size")) is int and 0 < item["size"] <= MAX_PACKAGE_BYTES,
            "Invalid package size",
        )
    return manifest


def validate_package(data, item, version):
    require(
        len(data) == item["size"] and sha256(data) == item["sha256"],
        "Package bytes differ from validated manifest",
    )
    if item["name"].endswith(".whl"):
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            names = archive.namelist()
            metadata_path = f"sellapp_sdk-{version}.dist-info/METADATA"
            require(
                names.count(metadata_path) == 1, "Missing or duplicated wheel metadata"
            )
            require(
                archive.getinfo(metadata_path).file_size <= 1024 * 1024,
                "Oversized wheel metadata",
            )
            metadata = archive.read(metadata_path)
    else:
        with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as archive:
            entries = archive.getmembers()
            metadata_path = f"sellapp_sdk-{version}/PKG-INFO"
            selected = [entry for entry in entries if entry.name == metadata_path]
            require(
                len(selected) == 1
                and selected[0].isfile()
                and selected[0].size <= 1024 * 1024,
                "Invalid source-distribution metadata",
            )
            metadata = archive.extractfile(selected[0]).read()
    info = email.parser.BytesParser().parsebytes(metadata)
    require(
        info["Name"] == "sellapp-sdk" and info["Version"] == version,
        "Distribution name/version differs",
    )


def github(resource, binary=False):
    command = ["gh", "api", "--hostname", "github.com", resource]
    if binary:
        command.extend(["--header", "Accept: application/octet-stream"])
    result = subprocess.run(command, capture_output=True, timeout=120)
    require(result.returncode == 0, "GitHub asset/metadata read failed")
    return result.stdout if binary else json.loads(result.stdout)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tag", required=True)
    parser.add_argument("--sha256", required=True)
    args = parser.parse_args()
    require(
        bool(re.fullmatch(r"v[0-9]+\.[0-9]+\.[0-9]+", args.tag)),
        "Expected release tag vX.Y.Z",
    )
    require(
        os.environ.get("GITHUB_REPOSITORY") == REPOSITORY
        and os.environ.get("GITHUB_REF") == "refs/heads/main",
        "Run this workflow from the official repository main branch",
    )
    commit = os.environ.get("GITHUB_SHA", "")
    prefix = "repos/" + REPOSITORY
    release = github(prefix + "/releases/tags/" + args.tag)
    require(release.get("tag_name") == args.tag, "GitHub release tag differs")
    ref = github(prefix + "/git/ref/tags/" + args.tag)["object"]
    for _ in range(3):
        if ref.get("type") == "commit":
            break
        require(
            ref.get("type") == "tag"
            and bool(re.fullmatch(r"[a-f0-9]{40}", ref.get("sha", ""))),
            "Unexpected Git tag object",
        )
        ref = github(prefix + "/git/tags/" + ref["sha"])["object"]
    require(
        ref.get("type") == "commit" and ref.get("sha") == commit,
        "Release tag differs from workflow checkout",
    )
    assets = release.get("assets", [])

    def download(name, maximum):
        matches = [asset for asset in assets if asset.get("name") == name]
        require(len(matches) == 1, "Missing or duplicated release asset: " + name)
        asset = matches[0]
        require(
            type(asset.get("id")) is int
            and type(asset.get("size")) is int
            and 0 < asset["size"] <= maximum,
            "Invalid release asset size/identity",
        )
        data = github(prefix + "/releases/assets/" + str(asset["id"]), binary=True)
        require(len(data) == asset["size"], "Downloaded release asset size differs")
        return data

    manifest = validate_manifest(
        download("publication-manifest.json", 65536),
        args.sha256,
        json.loads(Path("generation-manifest.json").read_text()),
        json.loads(Path(".sellapp-sdk-sync.json").read_text()),
        commit,
        args.tag,
    )
    require(not Path("dist").exists(), "Output directory already exists")
    packages = []
    for item in manifest["files"]:
        data = download(item["name"], MAX_PACKAGE_BYTES)
        validate_package(data, item, manifest["version"])
        packages.append((item["name"], data))
    Path("dist").mkdir()
    for name, data in packages:
        Path("dist", name).write_bytes(data)
    print("Verified both retained distributions for " + args.tag + " at " + commit)


if __name__ == "__main__":
    main()
