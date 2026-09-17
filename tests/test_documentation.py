import runpy
from pathlib import Path

DocumentationTests = runpy.run_path(
    str(Path(__file__).resolve().parents[1] / "examples/check.py")
)["DocumentationTests"]
