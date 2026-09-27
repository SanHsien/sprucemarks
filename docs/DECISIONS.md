# 架構決策記錄 (DECISIONS)

本文檔記錄 Sprucemarks Windows 原生維護 fork 之關鍵技術與維護架構決策。

---

## ADR-01: 上游封存處理與自主維護方針

- **日期**：2026-09-11
- **狀態**：已採納 (Accepted)

### 背景脈絡
[`nightmode/sprucemarks`](https://github.com/nightmode/sprucemarks) 原作者於 2026-08-28 建立最後提交 `9525101`（`v2026.8.28.0`），將倉庫狀態變更為封存（Archived），關閉了 Issues，並於說明文件中註記不再測試或更新。

### 決策內容
1. **自主獨立維護線**：將 `SanHsien/sprucemarks` 作為該擴充功能之長期維護與保存線。
2. **免除上游追蹤排程**：依據使用者指示，省略每週定時輪詢上游之工作流程（無 `upstream-check.yml`），將基準水位永久鎖定於封存提交 `9525101`。
3. **安全對齊**：設定 `gh repo set-default SanHsien/sprucemarks`，確保日常工具指令預設對齊本維護線。

### 影響與效益
- 避免 GitHub Actions 消耗在對已封存倉庫的無效定時輪詢。
- 確立本專案為完全自給自足的獨立開源擴充套件。

---

## ADR-02: Windows 11 原生門禁與擴充功能驗收標準

- **日期**：2026-09-11
- **狀態**：已採納 (Accepted)

### 背景脈絡
本專案開發者主要於 Windows 11 原生環境（PowerShell 7+）進行工作。維護此 JavaScript/WebExtension 專案時，需要可靠的自動化門禁機制，同時避免引入龐大複雜的前端建置工具鏈。

### 決策內容
1. **Windows 11 原生 PowerShell 門禁**：
   - `tools/dev_check.ps1`：執行維護工具編譯、Ruff 語法檢查、Pytest 契約測試與相對連結檢查。
   - `tools/bootstrap_dev.ps1`：提供新設備上的一鍵環境初始化與驗收。
2. **專屬擴充功能產品驗收**：
   - `tools/test_product.ps1`：獨立驗證 `deploy/manifest.json` 與 `source/manifest.json` 的 JSON 格式與 Manifest V3 規範；驗證 7 款圖示資產存在性；調用本機 `node --check` 驗證所有 JavaScript 檔案之語法正確性。
3. **純 Windows CI 矩陣**：
   - GitHub Actions `ci.yml` 統一採用 `windows-latest` 與 Python 3.10–3.14 矩陣，徹底消除 Linux/POSIX 假設。

### 影響與效益
- 確保所有代碼與文件在 Windows 11 上均能以一鍵指令完成驗證。
- 維持維護依賴極簡化（僅需要 Python、Pytest、Ruff 與可選 Node.js）。

---

## ADR-03: 雙語入口與公眾領域宣告延續

- **日期**：2026-09-11
- **狀態**：已採納 (Accepted)

### 背景脈絡
原專案採 CC0 1.0 Universal 條款釋出。為了方便繁體中文使用者安裝與閱讀，需要建立以繁體中文為主的說明文件，同時妥善保存原作者英文內容。

### 決策內容
1. [`README.md`](../README.md) 作為繁體中文主要入口，收錄完整擴充功能特色、Edge/Chrome/Firefox 圖文式安裝流程與開發門禁指引。
2. [`README.en.md`](../README.en.md) 保留原作者英文內容，並加上維護線標註與相互連結。
3. 全庫文件維持在 [CC0 1.0 Universal](../LICENSE) 條款下持續釋出。
