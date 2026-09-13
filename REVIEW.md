# Repository review（Windows-only）

- Review date: 2026-09-11
- Review baseline: `9525101dc4b029daa7eabc998c3838c2b0524bab`
- Remediation: 同日 fork-local overlay
- Upstream reviewed through: `9525101dc4b029daa7eabc998c3838c2b0524bab`
- Primary environment: Windows 11、PowerShell、Node.js 26.7.0、Python 3.14.7
- Status: 維護骨架與擴充功能發行包全面可用。已完成建立 Windows 原生門禁與驗收。

---

## 結論

這個 fork 適合作為 Windows 11 本機使用、長期保存與獨立維護的 Sprucemarks 瀏覽器擴充功能線。產品代碼跟隨 `nightmode/sprucemarks` `9525101`（`v2026.8.28.0`），並注入完整的 Windows-first 維護骨架：繁體中文維護文件、Edge/Chrome/Firefox 一鍵載入指引、Windows 原生 1-click 門禁（`dev_check.ps1`）、擴充功能產品驗收（`test_product.ps1`）以及純 Windows 原生 CI 工作流程。

由於原作者已於 2026-08-28 將上游倉庫封存歸檔（Archived）並關閉 Issues，本線採自主獨立維護，免除定時輪詢上游之非必要排程開銷。

---

## 本輪實證

### 審查當下（`9525101`）

```text
git rev-parse HEAD
→ 9525101dc4b029daa7eabc998c3838c2b0524bab

gh repo set-default --view
→ SanHsien/sprucemarks
```

實查結果：
- 上游 repository 為 `nightmode/sprucemarks`，採 CC0 1.0 Universal 授權。
- 上游狀態為 `isArchived: true`，最後提交訊息為 `archive`。
- 上游 PR 水位為 0，Issue 功能已關閉。
- 擴充功能為 Manifest V3 規格，宣告必要權限僅為 `bookmarks` 與 `storage`，不含任何外部連線權限。
- 經 `node --check` 驗證，全專案 15 支 JavaScript 腳本無任何語法錯誤。
- `deploy/images/icon` 具備 16px 至 128px 共 7 款尺寸圖示，資產完整。

---

## 已修 findings

| ID | 嚴重度 | 做了什麼 |
|---|---|---|
| R-01 | P2 | `.gitignore` 加入 `.env`、`.venv/`、`__pycache__/`、`.ruff_cache/`、`.pytest_cache/`、`*-report.md` |
| R-02 | P2 | 建立獨立維護測試目錄 `tools/tests/` 與獨立 `tools/pytest.ini`，避免產品環境污染 |
| R-03 | P2 | 建立完整規範文件庫（`FORK.md`、`NOTICE.md`、`LICENSE`、`SECURITY.md`、`AGENTS.md`、`CLAUDE.md`、`GEMINI.md`） |
| R-04 | P3 | `README.md`（繁體中文）與 `README.en.md`（英文鏡像）雙向互指，標明 CC0 條款與 Windows 瀏覽器安裝手冊 |
| R-05 | P2 | 建立 `tools/dev_check.ps1` 與 `tools/bootstrap_dev.ps1`，規範 Windows 11 原生 PowerShell 驗收門禁 |
| R-06 | P2 | 建立 `tools/test_product.ps1` 驗證擴充功能 Manifest V3 規格、圖示資產完整性與 JavaScript 語法 |
| R-07 | P2 | 建立純 Windows 原生 CI（`ci.yml`、`codeql.yml`），移除無效跨平台假設 |
| R-08 | P2 | 確認並記錄上游封存狀態，基準鎖定至 `9525101`，省除無效之上游定時輪詢工作流程 |
| R-09 | P2 | 修復 `options.js` 第 504 行 typo，避免次目錄預覽圖版本字串誤加於主圖 `img.src` |
| R-10 | P1 | 修復 `options.js` 與 `tools.js` 自訂元素樣板複製時閉包鎖定與空屬性存取崩潰，改為動態讀取與安全初始化 |
| R-11 | P3 | 修復 `about.js` 版本字串替換邏輯（改用結尾正則 `/\.0$/`，防範誤傷前面版本段） |
| R-12 | P2 | `bootstrap_dev.ps1` 與 `pack_extension.ps1` 加入 `$LASTEXITCODE` 嚴格檢查與 `powershell.exe` 回退 |
| R-13 | P2 | 修復 `pack-extension.mjs` 之 PowerShell 平台呼叫邏輯與錯誤日誌輸出 |
| R-14 | P3 | 修正 `tools/pytest.ini` testpaths 並於根目錄新增 `pytest.ini` 支援直接裸跑 |
| R-15 | P1 | MV3 Service Worker 事件監聽器改為腳本評估期頂層同步註冊，非同步監聽器內部 `await start_done()`，避免背景喚醒事件遺失 |
| R-16 | P2 | 修復 `bookmark_resort()` 競態條件與死鎖風險，提前鎖定旗標並以 `try ... finally` 確保安全復原 |
| R-17 | P2 | `refresh_about`、`refresh_tools` 與 `port_message_all` 之 `port.postMessage` 增加 `try ... catch` 防禦斷線崩潰 |
| R-18 | P3 | 發行設定將 `shared.setting.log` 設為 `false`，停止開發除錯日誌傾印並符合內建單元測試預期 |

---

## 接受、不改契約

| ID | 嚴重度 | 處理 |
|---|---|---|
| - | - | （無。所有已識別項目皆已妥善處理完畢） |

---

## 尚未宣稱範圍

- **不宣稱** 上游原作者恢復維護或提供新版發布（上游已於 2026-08-28 封存歸檔，本專案為自主獨立維護線）。
- **不宣稱** 包含 Chrome Web Store 或 Firefox Add-ons 上架之私密 API 金鑰或簽章憑證。
