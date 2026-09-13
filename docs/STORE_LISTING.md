# Chrome Web Store 上架包與審查手冊 (STORE_LISTING)

更新日期：2026-09-11  
狀態：**準備上架中**（套件版本：v2026.8.28.0）  
目標後台：[Chrome Developer Dashboard (控制台)](https://chrome.google.com/webstore/devconsole)  
公開隱私政策網址：https://sanhsien.github.io/sprucemarks/privacy.html  
開源溯源：本專案為 [`nightmode/sprucemarks`](https://github.com/nightmode/sprucemarks) 之開源維護 Fork  

> [!IMPORTANT]
> **Agent 無法代為執行的項目**：
> - 登入您的 Google 帳號與通過 2FA 兩步驟驗證。
> - 代為支付 Google 開發者一次性註冊費（5 美元，若尚未開通）。
> - 進入 Chrome Developer Console 點擊「提交審查」按鈕。
>
> 其餘所有上架材料、打包 zip、驗證腳本、欄位文案、權限理由與靜態隱私站點，皆已準備就緒。

---

## 1. 快速打包指令

在專案目錄下執行：

```powershell
pwsh -NoProfile -File tools\pack_extension.ps1
```

產出檔案：
- **上架 ZIP**：`dist/sprucemarks-2026.8.28.0.zip`
- **校驗檔**：`dist/sprucemarks-2026.8.28.0.zip.sha256`

> [!TIP]
> 上架 zip 的根目錄已直接包含 `manifest.json` 與所有必要資源，可直接上傳至 Google 控制台。

---

## 2. Store listing（商店商品資訊，可直接複製貼上）

### 商品名稱（≤ 45 字元）

```text
Sprucemarks - 自動書籤排序 (Bookmark Sorter)
```

英文備選：
```text
Sprucemarks - Auto Bookmark Sorter
```

### 簡短說明（Summary，≤ 132 字元）

> [!NOTE]
> 依規範已於簡短說明與詳細說明中明確標示本擴充功能為上游專案之維護 Fork。

```text
自動整理與排序瀏覽器書籤（fork 自 nightmode/sprucemarks）。支援標題、日期、網址排序，純本機執行零外部連線。
```

英文備選（122 字元）：
```text
Automatically sort bookmarks by title, date, or URL. Maintenance fork of nightmode/sprucemarks. 100% local, no telemetry.
```

### 詳細說明（Detailed Description，總覽全文）

```text
【專案來源與開源維護聲明】
本擴充功能為 nightmode/sprucemarks 的開源維護 Fork（採 CC0 1.0 Universal 公眾領域授權）。
原上游專案於 2026 年 8 月宣告封存歸檔後，本專案由 SanHsien 接手作為獨立維護與長期保存版本，持續提供安全、無追蹤的書籤排序服務。
• 原作品開源倉庫：https://github.com/nightmode/sprucemarks
• 本維護專案倉庫：https://github.com/SanHsien/sprucemarks

--------------------------------------------------

Sprucemarks 是一款輕量、安全且高效的瀏覽器擴充功能，能夠在背景自動且持續地整理並排序您的書籤，讓混亂的書籤列隨時保持井然有序。

主要特色與功能：
• 全自動背景排序：當您新增、移動或匯入書籤時，擴充功能在背景自動重新排列順序。
• 多維度排序規則：支援依「標題（Title，A-Z / Z-A）」、「新增日期（Date Added，新到舊 / 舊到新）」或「網址（URL）」進行排序。
• 資料夾自訂控制：可針對特定書籤目錄套用不同排序規則，亦可設定排除不需排序的目錄。
• 完整介面主題：提供深色（Dark）與淺色（Light）模式，並支援 Green、Dark、Light 等重點配色。
• 內建書籤檢視工具：提供重複書籤檢測與歷史變更查看輔助工具。

隱私與安全承諾：
• 零外部連線：本擴充功能無任何後端伺服器，不含任何外部網路請求權限，絕不上傳任何書籤內容。
• 100% 本機執行：所有排序演算法與偏好設定完全保留於您的本機設備中。
• 無追蹤代碼：無 Google Analytics、無遙測（Telemetry）、無廣告。
• 開源與公共領域：採 CC0 1.0 Universal 授權開放。

官方資訊與支援：
• 隱私權政策：https://sanhsien.github.io/sprucemarks/privacy.html
• 開源專案與原始碼：https://github.com/SanHsien/sprucemarks
• 問題回報與支援：https://github.com/SanHsien/sprucemarks/issues
```

### 類別（Category）

建議選擇：`Productivity`（生產力）或 `Workflow & Planning`（工作流程與規劃）

### 語言（Language）

預設語系：`English`  
支援語系：已內建 `en`（英文）與 `zh_TW`（繁體中文）

### 隱私權政策網址（Privacy Policy URL，必填）

```text
https://sanhsien.github.io/sprucemarks/privacy.html
```

> [!WARNING]
> Google Chrome Web Store 審查機制嚴格要求隱私政策必須為**可公開直接存取之獨立 HTML 頁面**。切勿填寫 GitHub blob 連結或 raw 連結，否則會遭審查機器人直接判定無效退件。本專案已透過 GitHub Pages 自動部署靜態 HTML 站點。

### 支援與首頁網址（Support URL）

```text
https://github.com/SanHsien/sprucemarks/issues
```

---

## 3. Privacy 分頁（隱私權規範與資料用途勾選）

### Single purpose（單一用途說明，必填）

```text
在後台自動且持續地依據使用者指定規則（標題、日期或網址）整理與排序瀏覽器書籤（fork 自 nightmode/sprucemarks）。
```

### 處理的使用者資料（Data usage declaration）

請於 Dashboard 各項目中依實際運作如實勾選：

| 項目 | 勾選 | 說明 |
|---|---|---|
| **網站內容（Web Content / Bookmarks）** | **是 (Yes)** | 僅於本機讀取書籤標題、網址與建立時間，並調用 bookmarks API 重新排列順序。 |
| **個人通訊（Personal communications）** | **否 (No)** | 本擴充功能不涉及任何通訊內容。 |
| **身分／驗證資訊（Authentication）** | **否 (No)** | 不收集任何帳號、密碼或 Cookie。 |
| **位置資訊（Location）** | **否 (No)** | 不讀取地理位置。 |
| **使用者活動（User activity）** | **否 (No)** | 不做任何行為追蹤或點擊分析。 |
| **網站瀏覽紀錄（Browsing history）** | **否 (No)** | 不讀取亦不儲存使用者的瀏覽歷史。 |

### 遠端程式碼（Remote code）

選擇：**否（No，本擴充功能不使用遠端代碼）**  
所有 JavaScript 代碼皆包含在擴充套件 ZIP 中，符合 Manifest V3 安全政策。

### 資料用途詳細說明（Data usage justification）

```text
所有書籤資料讀取與排序操作 100% 於使用者本機瀏覽器內進行。本擴充功能沒有後端伺服器，無外部網路請求權限，絕不上傳、不收集、不共享且不販售任何使用者資料。
```

---

## 4. 權限說明（Permissions Justification）

若 Dashboard 要求提供權限用途說明，請填入：

| 宣告權限 | 權限理由說明（Justification） |
|---|---|
| `bookmarks` | 核心功能必備：本機讀取書籤之標題、網址與建立日期，並在使用者啟用自動排序時調用 `chrome.bookmarks.move` 重新調整書籤在資料夾內的排列順序。所有操作皆在本機沙箱內執行。 |
| `storage` | 於使用者本機之 `chrome.storage.local` 儲存排序偏好設定（排序依據、排序方向、深淺色外觀主題與排除不排序之目錄清單）。不儲存任何個人隱私資訊。 |

---

## 5. 視覺資產準備（Visual Assets）

### 1. 商店圖示（Store Icon）
- **尺寸**：128 × 128 像素 PNG
- **路徑**：`deploy/images/icon/icon-default-128.png`

### 2. 截圖（Screenshots，至少 1 張）
- **規格**：1280 × 800 或 640 × 400 像素 PNG 或 JPEG。
- **建議畫面**：
  1. **設定選項頁（深色主題）**：展示排序依據（Title / Date / URL）、排序方向與自動排序開關。
  2. **設定選項頁（淺色主題）**：展示淺色介面與排除目錄管理。
  3. **工具箱頁面（Tools）**：展示重複書籤檢測與歷史變更記錄。

---

## 6. 上架操作流程步驟

1. 開啟 [Chrome 應用程式商店開發人員資訊主頁](https://chrome.google.com/webstore/devconsole)。
2. 點擊右上角「**新增項目**」（Add new item）。
3. 將本機打包產出的 `dist/sprucemarks-2026.8.28.0.zip` 拖曳上傳。
4. 在「**商店資訊**」（Store listing）分頁：
   - 貼上名稱、簡短說明與詳細說明（開頭已包含 Fork 宣告）。
   - 上傳 128×128 圖示與至少 1 張截圖。
   - 填寫類別（生產力）、語言（English）與支援網址。
5. 在「**隱私權**」（Privacy）分頁：
   - 貼上單一用途說明。
   - 勾選「網站內容（書籤）」，其餘勾選「否」。
   - 填寫權限說明（`bookmarks` 與 `storage`）。
   - 宣告「不使用遠端代碼」。
   - 貼上隱私權政策網址：`https://sanhsien.github.io/sprucemarks/privacy.html`。
6. 點擊「**發布**」分頁，檢查無缺失項目後點擊「**提交以供審查**」（Submit for review）。
