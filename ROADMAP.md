# 路線圖

> 本 repo 後續工作的單一真相源。做完一項，就在同一個 commit 刪掉那一列；新工作只加在這裡。
> 現況段的數字是 2026-10-29 依 `main` `2ee3dfa2fcc0` 查的快照，開工前先重查 GitHub。

## 現況
自動排序書籤的瀏覽器擴充功能（Windows 原生維護 fork，原始碼在 `source/`，發行檔在 `deploy/`）。2026-10-29 `gh` 查詢（`main` `2ee3dfa2fcc0`）：open PR 0、Dependabot 與 code scanning 告警 0；CI、CodeQL 最近一次 success，GitHub Pages 最近一次 success 在 2026-09-11；issues 已停用，open issue 數記為「未查到」；無 GitHub Release。上游 `nightmode/sprucemarks` 已 archived（`docs/DECISIONS.md` ADR-01），所以不設上游檢查（`.github/dependabot.yml` 的 fleet-waiver）。商店狀態見 `docs/STORE_LISTING.md:4`。

## 近期：可以直接動手
| 項目 | 為什麼 | 驗收方式 | 建議執行者 | 證據 |
| --- | --- | --- | --- | --- |
| 無 | 2026-10-26 深掃已修 `bookmark_sort` 缺陷（`2ee3dfa`），沒有 open PR／告警，也沒有停在一半的工作；`actions` 釘版由 Dependabot 每週一自動開 PR | 無（有新缺陷時加在這裡） | 無 | `2ee3dfa`；深掃報告（2026-10-26）；`.github/dependabot.yml` |

## 中期：等條件成立再做
| 項目 | 觸發條件 | 驗收方式 | 建議執行者 | 證據 |
| --- | --- | --- | --- | --- |
| 上架 Chrome Web Store 或 Edge Add-ons | 維護者決定公開發佈（帳戶登入與送審由維護者本人操作） | 商店審查通過並上架；發布 GitHub Release；`docs/STORE_LISTING.md` 狀態行在同一 commit 更新 | 維護者 | `docs/STORE.md`、`docs/STORE_LISTING.md:4`（準備上架中）；2026-10-29 `gh` 查詢：無 release |
| 補強書籤匯入例外處理（`import_active` 狀態守護） | 成功重現匯入拋例外導致 `import_active` 卡在 true 的具體情境 | 新增修前會失敗的測試案例；修復後 `tools/tests/test_background_logic.py` 通過；`source/js/-background.js` 與 `deploy/background.js` 同步 | Claude Sonnet | 深掃報告（2026-10-26）「刻意不修」第一條（未能重現）；`listener_bookmark_import_ended`（`source/js/-background.js:1425`） |

## 刻意不做
| 不做什麼 | 理由 | 什麼情況下重新考慮 |
| --- | --- | --- |
| 同步上游 nightmode/sprucemarks | 上游已於 2026-08-28 封存，不再有提交（`docs/DECISIONS.md` ADR-01） | 上游解除封存並恢復維護；屆時拿掉 `.github/dependabot.yml` 的 fleet-waiver 並補上檢查器 |
| 改動 `bookmark_get_hashes` 的 `join('')` 串接 | 只影響 About 頁疑難排解顯示，無功能副作用，修改易引入未知回歸（`source/js/-background.js:612`；深掃報告（2026-10-26）「刻意不修」第二條） | 有實證碰撞案例影響書籤正常排序 |
| 強推或改寫 Git 歷史以對齊上游祖先 | 已於 2026-10-24 建立乾淨獨立基準，歷史分離不影響擴充套件運作 | 不重新考慮 |

## 維護方式
- 依賴：Dependabot 每週一追 `github-actions`，合併前先讀 diff。
- 修改後執行 `python tools/tests/test_background_logic.py`（記憶體 Chrome mock），並確認 CI、CodeQL 綠。