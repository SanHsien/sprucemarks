# 隱私權政策 (Privacy Policy)

**產品名稱**：Sprucemarks（自動書籤排序擴充功能）  
**開發維護者**：SanHsien  
**專案網址**：https://github.com/SanHsien/sprucemarks  
**最新更新日期**：2026-09-11  

本文件為 Sprucemarks 瀏覽器擴充功能之隱私權政策。靜態 HTML 公開頁面請見 [https://sanhsien.github.io/sprucemarks/privacy.html](https://sanhsien.github.io/sprucemarks/privacy.html)。

---

## 1. 核心隱私承諾

Sprucemarks 堅持**零收集、零追蹤、零外部連線**原則：

- **無自有伺服器**：本擴充功能沒有後端伺服器，不會將任何資料上傳或傳輸至開發者或任何第三方伺服器。
- **無追蹤代碼**：本軟體不包含任何分析工具（Analytics）、追蹤標籤、廣告或遙測代碼（Telemetry）。
- **不販售資料**：我們不收集亦絕不販售、出租或轉讓任何使用者資料。

---

## 2. 我們處理的資料

本擴充功能僅在使用者本機端調用瀏覽器提供的原生 API：

### 書籤資料（`bookmarks` API）
- **讀取**：本機讀取書籤標題（Title）、網址（URL）、建立日期（Date Added）與資料夾結構。
- **寫入／重排**：僅在需要時調用 `chrome.bookmarks.move` 重新調整書籤於資料夾內的順序。
- **儲存與傳輸**：書籤資料完全保留於您的本機瀏覽器內，絕不上傳或同步至任何外部伺服器。

### 擴充功能設定（`storage` API）
- **內容**：儲存您的排序偏好（如：按名稱 A-Z、按日期新至舊）、主題設定（深色／淺色）與排除資料夾清單。
- **位置**：儲存於本機之 `chrome.storage.local`。

---

## 3. 權限宣告用途

| 權限項目 | 用途說明 |
|---|---|
| `bookmarks` | 讀取書籤中之標題、日期與網址以供排序演算法計算，並調用 move API 移動書籤位置。 |
| `storage` | 於使用者本機儲存書籤排序規則、選項與介面主題偏好。 |

---

## 4. 第三方共享與傳輸

本擴充功能**不與任何第三方共享任何資訊**。所有操作皆於您本機設備的瀏覽器沙箱內完成。

---

## 5. 政策變更

若本隱私權政策有任何修改，將更新於本專案之開源倉庫與公開頁面，並記錄於版本歷史中。

---

## 6. 聯絡方式

若您對本隱私權政策有任何疑問，請透過 GitHub Issue 與我們聯繫：  
https://github.com/SanHsien/sprucemarks/issues
