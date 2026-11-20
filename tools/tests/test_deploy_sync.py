from __future__ import annotations

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
SOURCE_JS = ROOT / "source" / "js"
DEPLOY = ROOT / "deploy" / "background.js"
JSS = ROOT / "source" / "background.js.jss"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8").replace("\r\n", "\n")


INCLUDE_RE = re.compile(r"""include\(\s*(['"])(?P<name>[^'"]+)\1\s*\)""")


def _included_sources() -> list[str]:
    # deploy/background.js is built by feri from source/background.js.jss, which
    # include()s these files in order. Derive the list from the .jss so a new
    # include is covered automatically. Both quote styles are accepted, and any
    # line that mentions include( but cannot be parsed fails loudly.
    names = []
    for line in _read(JSS).splitlines():
        if "include" not in line:
            continue
        m = INCLUDE_RE.search(line)
        assert m, f"unparseable include line in background.js.jss: {line!r}"
        names.append(m.group("name"))
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


def test_deploy_background_has_nothing_but_the_included_sources() -> None:
    # Code appended to (or injected between) the included files must be caught:
    # after removing every included source, only whitespace may remain.
    deploy = _read(DEPLOY)
    for name in _included_sources():
        source = _read(ROOT / "source" / name.lstrip("/")).strip()
        assert source in deploy
        deploy = deploy.replace(source, "", 1)
    assert deploy.strip() == "", f"deploy/background.js has extra content: {deploy.strip()[:200]!r}"


def test_include_parser_accepts_both_quote_styles() -> None:
    assert INCLUDE_RE.search("<js>include('/js/a.js')</js>").group("name") == "/js/a.js"
    assert INCLUDE_RE.search('<js>include("/js/a.js")</js>').group("name") == "/js/a.js"
