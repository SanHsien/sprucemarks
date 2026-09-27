# CODEX.md

請先完整閱讀並遵守 [`AGENTS.md`](AGENTS.md)。本檔只補充 OpenAI Codex / Codex CLI 的最小入口：

- 這是保留上游歷史的 CC0 1.0 Universal 維護 fork；不要移除原作者或授權標示。
- 上游已停止開發並封存，所有改動與 PR 一律指向 `SanHsien/sprucemarks`。
- Chrome Web Store 上架所有欄位與文案（已宣告 Fork）請見 [`docs/STORE_LISTING.md`](docs/STORE_LISTING.md)；架構對照見 [`docs/STORE.md`](docs/STORE.md)。
- 擴充套件一鍵打包產出 ZIP：`pwsh -NoProfile -File tools\pack_extension.ps1`。
- 提交或回報完成前，必須在 Windows 原生環境跑過：
  `pwsh -NoProfile -File tools\dev_check.ps1`
  `pwsh -NoProfile -File tools\test_product.ps1`
- 隱私政策靜態 HTML 已發布於 `https://sanhsien.github.io/sprucemarks/privacy.html`。
- Agent 做不到的事：無法代登 Google 帳號/Passkey/2FA 進行網頁點擊發布。
