# Sprucemarks (English Mirror)

> [!NOTE]
> [繁體中文說明（README.md）](README.md) ｜ [Fork 維護說明 (FORK.md)](FORK.md) ｜ [版權聲明 (NOTICE.md)](NOTICE.md)

**This software is no longer being tested or updated by the original upstream author.**
This repository is a Windows-first maintenance and preservation fork of [`nightmode/sprucemarks`](https://github.com/nightmode/sprucemarks), dedicated to the public domain under CC0 1.0 Universal.

---

# Sprucemarks

A web browser extension that automatically sorts your bookmarks.

## Navigation

* [Install](#install)
* [Development](#development)
* [Test](#test)
* [License](#license)

## Install

Sprucemarks is intended to be used as a developer addon.

For Chrome, navigate to `chrome://extensions` and enable developer mode. Then use `load unpacked` to select the `deploy` folder of Sprucemarks as the extension directory.

For Edge, navigate to `edge://extensions/` and enable developer mode. Then use `load unpacked` to select the `deploy` folder of Sprucemarks as the extension directory.

For Firefox, navigate to `about:debugging` and enable `add-on debugging`. Then use `load temporary add-on` and select the `manifest.json` file within the `deploy` folder of Sprucemarks. If FireFox does not load the extension, you may need to replace the background object inside `source/manifest.json` with the following code:

```json
"background": {
    "scripts": ["background.js"]
}
```

If you change any source files, use Feri to publish to the `deploy` directory.

## Development

Use the `log` setting inside `source/js/shared.js` to enable or disable console logs for various events and operations.

Use Feri to continually publish from the `source` directory to the `deploy` directory.

For Windows 11 native development and validation tooling:
```powershell
pwsh -NoProfile -File tools\bootstrap_dev.ps1
pwsh -NoProfile -File tools\dev_check.ps1
pwsh -NoProfile -File tools\test_product.ps1
```

## Test

From the background service worker, run `await test()` to use the test suite.

## License

[CC0 1.0 Universal](LICENSE)

This work has been marked as dedicated to the public domain.
