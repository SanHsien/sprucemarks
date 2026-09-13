# GEMINI.md

請先完整閱讀並遵守 [`AGENTS.md`](AGENTS.md)。本檔只補充 Gemini / Antigravity 的最小入口：

- 這是保留上游歷史的 CC0 fork；不要移除原作者或 CC0 1.0 Universal 授權標示。
- 上游已停止開發並封存，所有改動以 `SanHsien/sprucemarks` 為準。
- 提交前跑 `pwsh -NoProfile -File tools\dev_check.ps1` 與 `pwsh -NoProfile -File tools\test_product.ps1`。
- Chrome Web Store 上架欄位與文案（已宣告 Fork）見 [`docs/STORE_LISTING.md`](docs/STORE_LISTING.md)；架構對照見 [`docs/STORE.md`](docs/STORE.md)。
- 擴充套件打包產出 ZIP：`pwsh -NoProfile -File tools\pack_extension.ps1`。
- 測試檔案、使用者個人書籤、`.env` 一律不可提交。
- 使用繁體中文，直接交付可驗證結果，避免冗長背景鋪陳。
- PR、push、release 一律指向 `SanHsien/sprucemarks`。

