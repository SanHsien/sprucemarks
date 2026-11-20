from __future__ import annotations

from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SOURCE_JS = ROOT / "source" / "js"
DEPLOY = ROOT / "deploy" / "background.js"
JSS = ROOT / "source" / "background.js.jss"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


def _included_sources() -> list[str]:
    # deploy/background.js is built by feri from source/background.js.jss, which
    # include()s these files in order. Derive the list from the .jss so a new
    # include is covered automatically.
    names = []
    for line in _read(JSS).splitlines():
        if "include('" in line:
            names.append(line.split("include('", 1)[1].split("'", 1)[0])
    return names


def test_jss_includes_are_discovered() -> None:
    assert "/js/-background.js" in _included_sources()


@pytest.mark.parametrize("name", _included_sources())
def test_deploy_background_contains_each_source_file_verbatim(name: str) -> None:
    source = _read(ROOT / "source" / name.lstrip("/")).strip()
    deploy = _read(DEPLOY)
    assert source in deploy, (
        f"source{name} diverged from deploy/background.js; "
        "rebuild deploy (feri) or apply the same edit to both"
    )
