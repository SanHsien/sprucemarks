# 安全政策 (SECURITY)

## 支援版本

本維護 fork 目前僅對下列分支提供安全維護與修復：

| 版本 | 支援狀態 |
|---|---|
| `main` (SanHsien/sprucemarks) | :white_check_mark: 支援 |
| 上游 (nightmode/sprucemarks) | :x: 已於 2026-08-28 封存，不再維護 |

---

## 安全範圍與架構特性

Sprucemarks 具有以下安全性與隱私防護特點：

1. **零外部網路請求**：擴充功能未宣告任何 `declarativeNetRequest`、`webRequest` 或跨域主機權限，絕不向外部網路發送請求。
2. **最小權限原則**：僅宣告 `bookmarks`（讀寫書籤以供排序）與 `storage`（本機儲存排序偏好設定）兩項必要權限。
3. **無追蹤代碼**：本專案不含任何遙測、第三方分析或追蹤腳本。

---

## 回報安全漏洞

若您在程式碼中發現安全疑慮或潛在漏洞，請透過 GitHub Issue 或 Private Vulnerability Reporting 回報至 `SanHsien/sprucemarks`。

請在報告中提供：
- 問題描述與影響範圍
- 重現步驟或 PoC
- 建議之緩解或修復方案
