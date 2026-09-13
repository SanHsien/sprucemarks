# Chrome Web Store 上架策略與檢核表 (STORE)

更新日期：2026-09-11  
上架專案：Sprucemarks（`SanHsien/sprucemarks`）  
上游來源：[`nightmode/sprucemarks`](https://github.com/nightmode/sprucemarks)（CC0 1.0 Universal）  

---

## 1. 上架策略方針

1. **上游封存保存線**：
   - 上游原專案已於 2026-08-28 封存歸檔並停止維護。
   - 本 fork 在 CC0 1.0 Universal 授權基礎上，由 SanHsien 獨立維護並向 Google 申請發布至 Chrome Web Store，讓 Chrome / Edge 使用者能直接從官方商店一鍵安裝與取得更新。
2. **總覽透明標註 Fork 溯源**：
   - 依商店政策與誠信原則，在商品總覽（Store Listing Overview）與詳細說明首段明確宣告：本產品為 `nightmode/sprucemarks` 之開源維護 Fork。
3. **極致隱私架構**：
   - 零伺服器、無網路連線權限、純本機執行。對比商店中常見含有遙測與分析代碼的書籤工具，Sprucemarks 具備高度安全性與極高過審率。
4. **雙軌發行並行**：
   - **商店發行**：Chrome Web Store 公開上架，由 Google 託管自動更新。
   - **本機發行**：GitHub Release 與 `deploy/` 目錄（支援 Edge、Chrome、Firefox 開發者模式載入）。

---

## 2. 上架文件與工具矩陣

| 項目 | 檔案 / 連結 | 說明 |
|---|---|---|
| **商店文案手冊** | [`STORE_LISTING.md`](STORE_LISTING.md) | 可直接複製貼入 Chrome Console 之名稱、簡介、詳細說明（含 Fork 宣告）、隱私勾選與權限理由 |
| **公開隱私權政策** | [privacy.html](https://sanhsien.github.io/sprucemarks/privacy.html) | 專為商店審查爬蟲設計之純靜態 HTML 頁面（Markdown 原文見 [`PRIVACY_POLICY.md`](PRIVACY_POLICY.md)） |
| **自動站點部署** | [pages.yml](../.github/workflows/pages.yml) | GitHub Pages 自動發布工作流程 |
| **一鍵打包工具** | [`tools/pack_extension.ps1`](../tools/pack_extension.ps1) | 驗收後自動打包 `dist/sprucemarks-<version>.zip` 與 SHA256 校驗檔 |
| **Node 打包包裝** | [`tools/pack-extension.mjs`](../tools/pack-extension.mjs) | Node.js 跨平台調用入口 |

---

## 3. Chrome Web Store 審查準備檢核表

- [x] **Manifest V3 規格規範**：`manifest_version: 3`，已配置 `service_worker: background.js`。
- [x] **最小必要權限**：僅宣告 `bookmarks` 與 `storage`，零主機權限（無 `http://*/*` 等）。
- [x] **無遠端代碼 (No Remote Code)**：全量 JavaScript 本地打包，不使用 `eval` 或動態外部腳本載入。
- [x] **獨立靜態隱私權政策**：已具備公開靜態 HTML 網址，非 GitHub blob / raw 頁面。
- [x] **總覽透明聲明**：文案已清楚說明 Fork 自上游開源專案與 CC0 授權。
- [x] **資產完整性**：128×128 圖示（`deploy/images/icon/icon-default-128.png`）與多尺寸圖示就緒。
- [x] **發行包測試通過**：ZIP 根目錄直接包含 `manifest.json`，通過 `tools/test_product.ps1` 驗收。
- [ ] **人工操作步驟**：由開發者登入 [Chrome Developer Dashboard](https://chrome.google.com/webstore/devconsole) 上傳 ZIP 並提交審查。
