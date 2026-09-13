# AGENTS.md

給 Codex、Claude Code、Cursor、Antigravity 與其他自動化代理在本專案工作時的指引。產品與使用方式先讀 [`README.md`](README.md)；開發與驗收細節見 [`docs/DEVELOPMENT.md`](docs/DEVELOPMENT.md)。

## 專案定位

這是 [`nightmode/sprucemarks`](https://github.com/nightmode/sprucemarks) 的 CC0 1.0 Universal fork。
核心功能是輕量、無追蹤、背景自動排序書籤的瀏覽器擴充功能（Manifest V3）。

- `origin` 是 `SanHsien/sprucemarks`（預設分支 `main`），為自主長期維護線。
- `upstream` 是 `nightmode/sprucemarks`（已於 2026-08-28 封存歸檔，完全唯讀）。
- 保留上游作者、CC0 1.0 授權與擴充功能核心。本 fork 的維護差異記在 [`FORK.md`](FORK.md) 與 [`docs/DECISIONS.md`](docs/DECISIONS.md)。
- 主要開發與完整驗收環境是 **Windows 11 + PowerShell**。本專案為純 Windows 原生維護線，門禁與工作流程皆於 Windows 原生環境執行。

---

## 硬性邊界

- 不提交使用者個人資料、私人書籤、API key、token、私鑰或 `.env`。
- 上游已封存唯讀，不要嘗試向 `upstream` 推送。所有 push 與 PR 一律指向 `SanHsien/sprucemarks`。
- 維護環境保持輕量：維護相依（`requirements-dev.txt`）僅安裝 pytest 與 ruff。
- 維持 CC0 1.0 Universal 授權與公眾領域標示，不移除原作者或歷史歸屬。

---

## 技術與資料流

- 發行版擴充功能：`deploy/`（包含 `manifest.json`、`background.js`、`page/`、`css/`、`images/`、`fonts/`），可直接在 Edge / Chrome / Firefox 以開發者模式載入。
- 原始代碼：`source/`（以 feri 預處理結構組織）。
- 維護工具：`tools/`（`dev_check.ps1`、`bootstrap_dev.ps1`、`test_product.ps1`、`check_links.py`）。
- 維護測試：`tools/tests/`（契約測試，驗證文件與擴充功能規格）。

---

## 開發原則

- 一般變更在本地跑過 gate 後直接推 `origin/main`。若遇高風險架構變動，可走 PR 讓 CI 驗證。
- 修復 bug 先建立可重現失敗的測試，再做最小修改。
- 使用繁體中文回覆；使用者文件以繁體中文為主，公開入口同步維護 [`README.en.md`](README.en.md)。
- 提交訊息採用 Conventional Commits（如 `feat: ...`、`fix: ...`、`docs: ...`）。
- [`REVIEW.md`](REVIEW.md) 是風險快照，不是每個一般 bug 的流水帳。

---

## 驗證流程

提交或回報完成前，必須於 Windows 原生 PowerShell 完整執行：

```powershell
pwsh -NoProfile -File tools\dev_check.ps1
pwsh -NoProfile -File tools\test_product.ps1
```

沒有實際跑過 Windows gate 並確認輸出綠燈前，不要宣稱完成。
