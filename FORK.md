# Fork 維護說明

本 repo fork 自 [`nightmode/sprucemarks`](https://github.com/nightmode/sprucemarks)，
沿用 [CC0 1.0 Universal](LICENSE) 授權與完整 Git 歷史。

## 為什麼維護 fork

1. **上游已停止開發並封存**：
   - 原作者 nightmode 於 2026-08-28 建立最後提交 `9525101`（`v2026.8.28.0`）並將 repository 設為 Archived。
   - 上游關閉了 Issues 功能且不再接受任何更新，本 fork 作為獨立維護與長期保存線。
2. **免除上游追蹤開銷**：
   - 由於上游已經唯讀封存，本 fork 不設置排程輪詢 CI（無 `upstream-check`），所有變更聚焦於本 repo 的獨立維護與現代化相容。
3. **Windows 11 原生標準化**：
   - 採 Windows-first 維護：Windows 11 + PowerShell 為主要開發、驗收與除錯環境。
   - 建立 1-click Windows 門禁（`dev_check.ps1`）與擴充功能驗收腳本（`test_product.ps1`）。
4. **雙語入口與無斷鏈治理**：
   - 公開入口以繁體中文（[`README.md`](README.md)）為主，英文鏡像放於 [`README.en.md`](README.en.md)。
   - 維護文件之間建立嚴格的相對連結無斷鏈自動化測試。

---

## 與上游的差異

| 項目 | 說明 |
|---|---|
| `README.md` | 繁體中文主入口；加入擴充功能特色、Edge/Chrome/Firefox 安裝步驟與維護門禁指引 |
| `README.en.md` | 原版英文鏡像；加入 fork 維護資訊 |
| `AGENTS.md` / `CLAUDE.md` / `GEMINI.md` | 本 fork 的 AI 維護單一真相源 |
| `NOTICE.md` / `FORK.md` / `LICENSE` | 來源、授權（CC0 1.0）與保存說明 |
| `tools/dev_check.ps1` | Windows 本機一鍵門禁（Python 編譯、Ruff 語法檢查、Pytest 契約測試、連結檢查） |
| `tools/bootstrap_dev.ps1` | Windows 本機一鍵環境初始化與全量驗收 |
| `tools/test_product.ps1` | 擴充功能專用產品測試（驗證 Manifest V3、圖示、Options 頁面與 JS 語法） |
| `tools/check_links.py` | 14 份維護文件無斷鏈自動化檢查工具 |
| `tools/tests/` | 維護契約測試（涵蓋文件規範、擴充功能結構） |
| `requirements-dev.txt` | 本機維護依賴清單（pytest、ruff） |
| `.github/workflows/ci.yml` | 純 Windows 原生 CI（`windows-latest` Python 3.10–3.14 矩陣）：執行 `dev_check.ps1` 與 `test_product.ps1` |
| `.github/workflows/codeql.yml` | CodeQL 安全掃描工作流程（JavaScript 與 Python） |
| `docs/DEVELOPMENT.md` | 本地開發、主題切換與 WebExtension 除錯手冊 |
| `docs/DECISIONS.md` | 專案決策記錄（ADR-01 上游封存自主維護、ADR-02 門禁設計等） |
| `docs/UPSTREAM.md` | 上游封存紀錄與水位基準記錄 |
| `REVIEW.md` | 全庫品質與風險快照 |

核心擴充功能代碼在 `deploy/`（發行版）與 `source/`（來源版）。

---

## 分支與 remote

- `origin/main`：SanHsien 維護線，也是唯一長期分支。
- `upstream`：nightmode 原始專案（已封存唯讀，僅作歷史溯源）。
- 日常修改在本機跑過 gate 後直接推送到 `origin/main`。

---

## 換一台電腦怎麼開發

在全新 Windows 11 電腦上下載並初始化：

```powershell
git clone https://github.com/SanHsien/sprucemarks.git
cd sprucemarks
pwsh -NoProfile -File tools\bootstrap_dev.ps1
```

要將擴充功能載入至瀏覽器進行實際除錯，請參考 [`README.md`](README.md) 或 [`docs/DEVELOPMENT.md`](docs/DEVELOPMENT.md)。
