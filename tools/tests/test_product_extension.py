from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_manifests_valid_json_and_mv3() -> None:
    for rel_path in ("deploy/manifest.json", "source/manifest.json"):
        manifest_file = ROOT / rel_path
        assert manifest_file.is_file(), f"missing {rel_path}"
        data = json.loads(manifest_file.read_text(encoding="utf-8"))
        assert data.get("manifest_version") == 3
        assert data.get("name") == "Sprucemarks"
        assert "version" in data
        assert "permissions" in data
        assert "bookmarks" in data["permissions"]
        assert "storage" in data["permissions"]


def test_all_icon_assets_exist() -> None:
    manifest_file = ROOT / "deploy" / "manifest.json"
    data = json.loads(manifest_file.read_text(encoding="utf-8"))
    icons = data.get("icons", {})
    assert len(icons) >= 7
    for size, rel_path in icons.items():
        icon_path = ROOT / "deploy" / rel_path
        assert icon_path.is_file(), f"missing icon {size}: {rel_path}"
        assert icon_path.stat().st_size > 0


def test_options_ui_page_exists() -> None:
    manifest_file = ROOT / "deploy" / "manifest.json"
    data = json.loads(manifest_file.read_text(encoding="utf-8"))
    options_page = data.get("options_ui", {}).get("page")
    assert options_page is not None
    page_path = ROOT / "deploy" / options_page
    assert page_path.is_file(), f"missing options page: {options_page}"
    assert page_path.stat().st_size > 0


def test_background_service_worker_exists() -> None:
    manifest_file = ROOT / "deploy" / "manifest.json"
    data = json.loads(manifest_file.read_text(encoding="utf-8"))
    worker = data.get("background", {}).get("service_worker")
    assert worker == "background.js"
    worker_path = ROOT / "deploy" / worker
    assert worker_path.is_file()
    assert worker_path.stat().st_size > 100_000


def test_locales_exist() -> None:
    for locale in ("en", "zh_TW"):
        for base in ("deploy", "source"):
            loc_file = ROOT / base / "_locales" / locale / "messages.json"
            assert loc_file.is_file(), f"missing locale: {base}/_locales/{locale}/messages.json"
            data = json.loads(loc_file.read_text(encoding="utf-8"))
            assert "extensionDescription" in data
            assert "extensionName" in data
