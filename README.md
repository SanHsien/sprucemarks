**This software is no longer being tested or updated.**

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

For Firefox, navigate to `about:debugging` and enable `add-on debugging`. Then use `load temporary add-on` and select the `manifest.json` file within the `deploy` folder of Sprucemarks. If FireFox does not load the extension, you may need to replace the background object inside `source/manifest.json` with the following code.

```
"background": {
    "scripts": ["background.js"]
},
```

If you change any source files, use Feri to publish to the `deploy` directory.

## Development

Use the `log` setting inside `source/js/shared.js` to enable or disable console logs for various events and operations.

Use Feri to continually publish from the `source` directory to the `deploy` directory.

## Test

From the background service worker, run `await test()` to use the test suite.

## License

[CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)

This work has been marked as dedicated to the public domain.