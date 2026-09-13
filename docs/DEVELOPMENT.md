# 開發與除錯指南 (DEVELOPMENT)

本文件說明如何在 Windows 11 原生環境中進行 Sprucemarks 擴充功能的除錯、測試與功能維護。

## 開發環境前置需求

- **作業系統**：Windows 11（原生 PowerShell，非 WSL）
- **PowerShell**：PowerShell 7+（`pwsh`）
- **Python**：Python 3.10 或更新版本（供維護門禁工具鏈使用）
- **Node.js**：Node.js（供 `test_product.ps1` 進行 JavaScript 語法靜態檢查）
- **瀏覽器**：Microsoft Edge、Google Chrome 或 Mozilla Firefox

---

## 快速上手

在專案目錄下執行一鍵初始化腳本：

```powershell
pwsh -NoProfile -File tools\bootstrap_dev.ps1
```

此指令將建立 `.venv` 虛擬環境、安裝測試相依套件，並自動執行全量門禁與擴充功能驗收。

---

## 擴充功能架構剖析

Sprucemarks 採用標準 WebExtension Manifest V3 架構：

```text
瀏覽器書籤事件 (onCreated, onMoved, etc.)
                   │
                   ▼
┌────────────────────────────────────────┐
│   Background Service Worker            │
│   (deploy/background.js)               │
│                                        │
│   ├── browser-polyfill (Promise 封裝) │
│   ├── shared (排序邏輯與偏好定義)       │
│   ├── background (事件監聽與佇列處理)   │
│   └── background-test (內建測試套件)   │
└────────────────────────────────────────┘
                   │
                   ▼
       Chrome / Edge Bookmarks API
```

### 1. 目錄結構職責
- `deploy/`：
  - 發行目錄，包含已打包完成的 `manifest.json`、`background.js`、樣式表與多主題頁面。
  - **瀏覽器開發者模式直接載入此目錄**。
- `source/`：
  - 模組化源代碼目錄，透過 `.jss` 範本組織不同模組。
- `tools/`：
  - Windows 11 門禁與驗證工具。

### 2. 核心模組功能
- **`browser-polyfill.js`**：將 `chrome.bookmarks`、`chrome.storage` 等回呼式 API 封裝為標準 Promise，確保非同步操作可使用 `async/await`。
- **`shared.js`**：定義書籤排序的核心比對邏輯（依標題、網址或時間排序，處理數字與字母順序）以及預設偏好設定。
- **`-background.js`**：監聽書籤變更事件（`onCreated`、`onMoved`、`onChanged`、`onRemoved`、`onChildrenReordered`、`onImportEnded`），並維護排序工作佇列。
- **`-background-test.js`**：內建單元測試套件。

---

## 瀏覽器載入與即時除錯

### 載入未封裝擴充功能
1. 開啟 Edge（`edge://extensions/`）或 Chrome（`chrome://extensions/`）。
2. 開啟「開發人員模式」。
3. 點擊「載入解壓縮的擴充功能」／「載入未封裝項目」，選擇本專案的 `deploy` 目錄。

### 檢查背景 Service Worker 與執行測試
1. 在擴充功能管理頁面中，找到 Sprucemarks。
2. 點擊「**檢查檢視：Service Worker**」，開啟開發者工具主控台（DevTools Console）。
3. 在主控台中輸入以下指令並按 Enter：
   ```javascript
   await test()
   ```
4. 擴充功能將自動執行涵蓋 `local` 與 `shared` 物件之完整單元測試套件，並輸出測試通過結果。

---

## 品質門禁指令

在提交代碼或 PR 前，請於本機執行驗收門禁：

```powershell
# 1. 執行維護門禁（編譯工具、Ruff 語法檢查、Pytest 契約測試、相對連結無斷鏈）
pwsh -NoProfile -File tools\dev_check.ps1

# 2. 執行擴充功能規格驗收（Manifest V3、圖示完整性、JS 語法）
pwsh -NoProfile -File tools\test_product.ps1
```
