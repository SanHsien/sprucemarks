# Sprucemarks

[![CI](https://github.com/SanHsien/sprucemarks/actions/workflows/ci.yml/badge.svg)](https://github.com/SanHsien/sprucemarks/actions/workflows/ci.yml)
[![CodeQL](https://github.com/SanHsien/sprucemarks/actions/workflows/codeql.yml/badge.svg)](https://github.com/SanHsien/sprucemarks/actions/workflows/codeql.yml)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg)](LICENSE)
[![Platform: Windows 11](https://img.shields.io/badge/Platform-Windows%2011-blue.svg)](docs/DEVELOPMENT.md)

> [!NOTE]
> 本 repo 為 [`nightmode/sprucemarks`](https://github.com/nightmode/sprucemarks) 之 Windows-first 獨立維護與保存 fork。
> 原上游已於 2026-08-28 宣告封存歸檔（Commit `9525101`，Tag `v2026.8.28.0`）。本專案依 [CC0 1.0 Universal 公眾領域貢獻宣言](LICENSE) 進行自主維護與現代化標準化。
> 英文原版鏡像請見 [README.en.md](README.en.md)；維護方針請見 [FORK.md](FORK.md) 與 [NOTICE.md](NOTICE.md)。

---

## 關於 Sprucemarks

Sprucemarks 是一款輕量、高效的瀏覽器擴充功能（WebExtension Manifest V3），能夠在後台自動且持續地整理並排序您的瀏覽器書籤。

### 主要特色

- **全自動背景排序**：新增、移動或匯入書籤時，後台 Service Worker 自動依指定規則重新排序。
- **多維度排序規則**：支援依「標題（Title）」、「新增日期（Date Added）」或「網址（URL）」排序，並可自訂遞增（A-Z / 舊到新）或遞減（Z-A / 新到舊）。
- **目錄層級控制**：可針對特定書籤資料夾設定不同排序規則，亦可設定排除目錄。
- **完整深淺主題**：支援深色（Dark）、淺色（Light）模式，並提供多種重點配色（Green、Dark、Light）。
- **隱私與安全**：零外部伺服器連線，純本機使用 Chrome / WebExtension Bookmarks API 與 Storage API，採 CC0 公眾領域授權。

---

## Windows 11 瀏覽器安裝指南

本擴充功能提供已編譯好的 `deploy/` 目錄，可直接載入各主流 Chromium 與 Firefox 瀏覽器中：

```text
專案根目錄
   │
   ├── deploy/                ◄── 瀏覽器直接載入此目錄
   │     ├── manifest.json
   │     ├── background.js
   │     ├── page/ ...
   │     └── ...
   └── source/                ◄── 原始開發代碼
```

### 1. Microsoft Edge
1. 開啟 Edge，網址列輸入 `edge://extensions/` 並按 Enter。
2. 開啟左側側邊欄的「**開發人員模式**」（Developer mode）開關。
3. 點擊頂部的「**載入解壓縮的擴充功能**」（Load unpacked）。
4. 在檔案選擇視窗中，選取本專案的 `deploy` 目錄即可完成安裝。

### 2. Google Chrome
1. 開啟 Chrome，網址列輸入 `chrome://extensions/` 並按 Enter。
2. 開啟右上角的「**開發人員模式**」開關。
3. 點擊左上角的「**載入未封裝項目**」（Load unpacked）。
4. 選取本專案的 `deploy` 目錄即可完成安裝。

### 3. Mozilla Firefox
1. 開啟 Firefox，網址列輸入 `about:debugging`。
2. 點擊左側「**此 Firefox**」（This Firefox）。
3. 點擊「**載入暫時性附加元件...**」（Load Temporary Add-on...）。
4. 選取本專案 `deploy` 目錄下的 `manifest.json` 檔案即可載入。

---

## Windows 11 本機開發與門禁驗收

本專案採用 Windows 11 原生 PowerShell 與 Python 門禁工具鏈進行品質治理。

### 一鍵初始化與門禁驗收

在專案目錄下開啟 PowerShell 執行：

```powershell
pwsh -NoProfile -File tools\bootstrap_dev.ps1
```

該指令會自動：
1. 檢測本機 Python 與 Node.js 環境。
2. 建立 Python 虛擬環境 `.venv` 並安裝維護相依套件（`pytest`、`ruff`）。
3. 執行 Windows 門禁（`tools/dev_check.ps1`），包含語法編譯、Ruff 靜態檢查、Pytest 契約測試與文件連結檢查。
4. 執行擴充功能產品驗收（`tools/test_product.ps1`），驗證 Manifest V3 規範、7 種尺寸圖示與全部 JavaScript 語法。

### 日常門禁指令

```powershell
# 執行維護門禁（Python、Ruff、Pytest、文件檢查）
pwsh -NoProfile -File tools\dev_check.ps1

# 執行擴充功能結構與 JS 語法驗證
pwsh -NoProfile -File tools\test_product.ps1

# 打包 Chrome Web Store 上架 zip
pwsh -NoProfile -File tools\pack_extension.ps1
```

---

## Chrome Web Store 上架包與發行

本專案已為 Chrome Web Store 審查準備好完整的上架文案、獨立靜態隱私權政策與打包工具：

- **一鍵打包指令**：`pwsh -NoProfile -File tools\pack_extension.ps1`（產出 `dist/sprucemarks-<version>.zip` 與 SHA256）
- **商店文案手冊**：[`docs/STORE_LISTING.md`](docs/STORE_LISTING.md)（含名稱、簡介、總覽開頭之 Fork 溯源宣告、資料用途與權限理由）
- **上架策略與檢核表**：[`docs/STORE.md`](docs/STORE.md)
- **公開隱私權政策**：[privacy.html](https://sanhsien.github.io/sprucemarks/privacy.html)（Markdown 原文見 [`docs/PRIVACY_POLICY.md`](docs/PRIVACY_POLICY.md)）

---

## 專案結構導覽

```text
sprucemarks/
├── deploy/                     # 預先編譯可直接載入之擴充功能發行包
│   ├── _locales/               # 多國語系訊息（en、zh_TW）
│   ├── css/                    # 樣式表（shared.css）
│   ├── fonts/                  # 本地字型（Inter、National Park）
│   ├── images/                 # 圖示與介面資源
│   ├── js/                     # 執行期腳本（polyfill、shared、page 腳本）
│   ├── page/                   # 選項與設定 HTML 頁面（深色/淺色主題）
│   ├── background.js           # MV3 Service Worker 背景腳本
│   └── manifest.json           # WebExtension Manifest V3
├── source/                     # 模組化原始碼（供 feri 建置）
├── tools/                      # Windows 11 維護與測試工具
│   ├── bootstrap_dev.ps1       # 一鍵初始化
│   ├── dev_check.ps1           # 門禁執行器
│   ├── test_product.ps1        # 擴充功能產品驗證
│   ├── pack_extension.ps1      # Chrome Web Store 一鍵打包
│   ├── pack-extension.mjs      # Node.js 打包包裝腳本
│   ├── check_links.py          # 相對連結無斷鏈檢查
│   └── tests/                  # 維護契約測試
├── docs/                       # 規格決策、上架手冊與隱私文件
│   ├── DEVELOPMENT.md          # 架構與除錯指引
│   ├── DECISIONS.md            # 架構決策記錄 (ADR)
│   ├── UPSTREAM.md             # 上游歸檔現況與水位記錄
│   ├── STORE_LISTING.md        # Chrome Web Store 上架文案手冊
│   ├── STORE.md                # 商店上架策略與檢核表
│   ├── PRIVACY_POLICY.md       # 隱私權政策說明
│   └── privacy.html            # 商店專用公開靜態隱私網頁
├── AGENTS.md                   # AI 代理維護單一真相源
├── CLAUDE.md / GEMINI.md       # 工具指引
├── FORK.md                     # Fork 維護方針與差異說明
├── NOTICE.md                   # 版權與貢獻聲明
├── REVIEW.md                   # 全庫品質快照
└── LICENSE                     # CC0 1.0 Universal 授權文本
```

---

## 授權條款

本作品依據 [CC0 1.0 Universal](LICENSE)（公眾領域貢獻宣言）釋出，原作者夜模（nightmode）已將其標記並貢獻至公眾領域。
更多資訊請見 [NOTICE.md](NOTICE.md)。