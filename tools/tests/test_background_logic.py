from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import pytest

JS_DIR = Path(__file__).resolve().parent / "js"
NODE = shutil.which("node")

pytestmark = pytest.mark.skipif(NODE is None, reason="node not installed")


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

