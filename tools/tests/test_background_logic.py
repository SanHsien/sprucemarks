from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest

JS_DIR = Path(__file__).resolve().parent / "js"
NODE = shutil.which("node")

# A missing node must fail the gate, not silently skip the regression tests
# (a skipped suite looks green). Opt out explicitly with SPRUCEMARKS_ALLOW_NO_NODE=1.
ALLOW_NO_NODE = os.environ.get("SPRUCEMARKS_ALLOW_NO_NODE") == "1"

pytestmark = pytest.mark.skipif(
    NODE is None and ALLOW_NO_NODE,
    reason="node not installed (SPRUCEMARKS_ALLOW_NO_NODE=1)",
)


def test_node_is_available() -> None:
    assert NODE is not None, (
        "node not found on PATH; install Node.js, or set SPRUCEMARKS_ALLOW_NO_NODE=1 "
        "to deliberately skip the background logic tests"
    )


def run(name: str) -> dict:
    proc = subprocess.run(
        [NODE, str(JS_DIR / "scenarios.mjs"), name],
        capture_output=True, text=True, encoding="utf-8", timeout=60, check=False,
    )
    assert proc.returncode == 0, proc.stderr
    return json.loads(proc.stdout.strip().splitlines()[-1])


def test_sort_reorders_when_index_digits_concatenate_identically() -> None:
    titles = run("collision")["titles"]
    assert titles == sorted(titles)

