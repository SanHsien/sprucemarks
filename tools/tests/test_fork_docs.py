from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import check_links

ROOT = Path(__file__).resolve().parents[2]


def test_maintainer_markdown_links_resolve() -> None:
    failures = 0
    for path in check_links.iter_documents():
        problems = check_links.check_document(path)
        failures += len(problems)
        for problem in problems:
            print(f"{path}: {problem}")
    assert failures == 0


def test_required_overlay_files_exist() -> None:
    required = (
        "README.md",
        "README.en.md",
        "FORK.md",
        "NOTICE.md",
        "AGENTS.md",
        "CLAUDE.md",
        "GEMINI.md",
        "CODEX.md",
        "CONTRIBUTING.md",
        "SECURITY.md",
        "REVIEW.md",
        "docs/DEVELOPMENT.md",
        "docs/DECISIONS.md",
        "docs/UPSTREAM.md",
        "docs/PRIVACY_POLICY.md",
        "docs/STORE.md",
        "docs/STORE_LISTING.md",
        "docs/privacy.html",
        "tools/dev_check.ps1",
        "tools/bootstrap_dev.ps1",
        "tools/test_product.ps1",
        "tools/pack_extension.ps1",
        "tools/pack-extension.mjs",
        "requirements-dev.txt",
        "pytest.ini",
        "LICENSE",
    )
    missing = [name for name in required if not (ROOT / name).is_file()]
    assert missing == []


def test_store_listing_declares_fork() -> None:
    listing = (ROOT / "docs" / "STORE_LISTING.md").read_text(encoding="utf-8")
    assert "nightmode/sprucemarks" in listing
    assert "Fork" in listing or "fork" in listing
    store = (ROOT / "docs" / "STORE.md").read_text(encoding="utf-8")
    assert "nightmode/sprucemarks" in store


def test_readme_pair_cross_links_and_names_the_fork() -> None:
    zh = (ROOT / "README.md").read_text(encoding="utf-8")
    en = (ROOT / "README.en.md").read_text(encoding="utf-8")
    assert "README.en.md" in zh
    assert "README.md" in en
    assert "nightmode/sprucemarks" in zh
    assert "nightmode/sprucemarks" in en
    assert "FORK.md" in zh
    assert "CC0" in zh
    assert "tools\\bootstrap_dev.ps1" in zh or "tools/bootstrap_dev.ps1" in zh


def test_gitignore_covers_user_data_and_reports() -> None:
    text = (ROOT / ".gitignore").read_text(encoding="utf-8")
    assert ".env" in text
    assert ".venv" in text
    assert "dist/" in text
    assert "node_modules/" in text


def test_review_snapshot_has_required_sections() -> None:
    text = (ROOT / "REVIEW.md").read_text(encoding="utf-8")
    assert "## 結論" in text
    assert "## 已修 findings" in text
    assert "## 接受、不改契約" in text
    assert "## 尚未宣稱範圍" in text


def test_ci_covers_windows() -> None:
    workflow = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    assert '"3.14"' in workflow
    assert "windows / py" in workflow
    assert "tools/dev_check.ps1" in workflow or "tools\\dev_check.ps1" in workflow
    assert "ubuntu" not in workflow
