import json
import os
import subprocess
import sys
import tarfile
import threading
import unittest
import zipfile
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

ROOT = Path(__file__).resolve().parents[1]
CHECK_PACKAGE = "--package" in sys.argv
if CHECK_PACKAGE:
    sys.argv.remove("--package")


class DocumentationTests(unittest.TestCase):
    def test_documentation_contains_exact_sources(self):
        for document, scripts in (
            ("README.md", ("first_request.py", "async_first_request.py")),
            ("docs/usage.md", ("pagination.py", "errors.py")),
        ):
            content = (ROOT / document).read_text()
            for script in scripts:
                self.assertIn((ROOT / "examples" / script).read_text().strip(), content)

    @unittest.skipUnless(CHECK_PACKAGE, "package inspection runs after building")
    def test_built_package(self):
        import sellapp_sdk

        self.assertNotIn(str(ROOT / "src"), sellapp_sdk.__file__)
        wheels = list((ROOT / "dist").glob("*.whl"))
        sdists = list((ROOT / "dist").glob("*.tar.gz"))
        self.assertEqual(len(wheels), 1)
        self.assertEqual(len(sdists), 1)
        with zipfile.ZipFile(wheels[0]) as archive:
            names = archive.namelist()
            metadata = archive.read(
                next(name for name in names if name.endswith("/METADATA"))
            ).decode()
            self.assertIn("Name: sellapp-sdk", metadata)
            self.assertIn("Description-Content-Type: text/markdown", metadata)
            self.assertIn((ROOT / "README.md").read_text().strip(), metadata)
            self.assertTrue(any(name.endswith("/LICENSE.txt") for name in names))
            self.assertFalse(
                any(name.startswith(("tests/", "examples/")) for name in names)
            )
        with tarfile.open(sdists[0]) as archive:
            names = [name.split("/", 1)[-1] for name in archive.getnames()]
            for required in (
                "README.md",
                "LICENSE.txt",
                "NOTICE.txt",
                "docs/usage.md",
                "docs/methods.md",
                "examples/first_request.py",
            ):
                self.assertIn(required, names)
            self.assertFalse(any(name.startswith("tests/") for name in names))

    def test_exact_examples(self):
        fixture = json.loads(
            (
                ROOT
                / "tests/fixtures/list_products_response_value_200_application_json_property_data_item.json"
            ).read_text()
        )
        calls = []
        state = {"mode": "products"}

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                calls.append((self.path, dict(self.headers)))
                self.send_response(403 if state["mode"] == "error" else 200)
                self.send_header("Content-Type", "application/json")
                self.send_header("X-Request-ID", "req_documentation")
                self.end_headers()
                page = int(parse_qs(urlparse(self.path).query).get("page", ["1"])[0])
                product = dict(fixture, id=page, title=f"Example product {page}")
                payload = (
                    {
                        "message": "Store access denied",
                        "code": "forbidden",
                        "status": 403,
                    }
                    if state["mode"] == "error"
                    else {
                        "data": [] if state["mode"] == "empty" else [product],
                        "meta": {"current_page": page, "last_page": 2},
                    }
                )
                self.wfile.write(json.dumps(payload).encode())

            def log_message(self, *_args):
                pass

        server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        env = dict(
            os.environ,
            SELLAPP_API_KEY="documentation_dummy",
            SELLAPP_STORE="example-store",
            SELLAPP_API_BASE_URL=f"http://127.0.0.1:{server.server_port}/api",
            NO_PROXY="127.0.0.1",
            no_proxy="127.0.0.1",
        )
        env.pop("PYTHONPATH", None)

        def run(name):
            return subprocess.run(
                [sys.executable, str(ROOT / "examples" / name)],
                env=env,
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=True,
                timeout=15,
            ).stdout

        try:
            for name in ("first_request.py", "async_first_request.py"):
                self.assertIn("1 Example product 1", run(name))
                state["mode"] = "empty"
                self.assertIn("No products yet", run(name))
                state["mode"] = "products"
            output = run("pagination.py")
            self.assertEqual(
                output.splitlines(), ["1 Example product 1", "2 Example product 2"]
            )
            state["mode"] = "error"
            self.assertIn("Request ID: req_documentation", run("errors.py"))
            self.assertEqual(len(calls), 7)
            for path, headers in calls:
                self.assertTrue(path.startswith("/api/v2/products?"))
                self.assertEqual(headers["Authorization"], "Bearer documentation_dummy")
                self.assertEqual(headers["X-STORE"], "example-store")
            for script in (
                "first_request.py",
                "async_first_request.py",
                "pagination.py",
                "errors.py",
            ):
                for empty in (None, "", " "):
                    env.pop("SELLAPP_API_BASE_URL", None)
                    if empty is not None:
                        env["SELLAPP_API_BASE_URL"] = empty
                    result = subprocess.run(
                        [sys.executable, str(ROOT / "examples" / script)],
                        env=env,
                        capture_output=True,
                        timeout=15,
                    )
                    self.assertNotEqual(result.returncode, 0)
                    self.assertEqual(len(calls), 7)
        finally:
            server.shutdown()
            server.server_close()
            thread.join()


if __name__ == "__main__":
    unittest.main()
