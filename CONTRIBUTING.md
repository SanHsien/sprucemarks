# 貢獻指南 (CONTRIBUTING)

感謝您對 Sprucemarks 維護 fork 的關注！

本專案為 [`nightmode/sprucemarks`](https://github.com/nightmode/sprucemarks) 的獨立維護線。
原作者已於 2026-08-28 封存上游，因此所有功能改進、錯誤修復與現代化相容性調整，皆集中於 `SanHsien/sprucemarks`。

## 貢獻原則

1. **對象明確**：Pull Request 與 Issue 一律提交至 `SanHsien/sprucemarks`。
2. **Windows-first 驗證**：提交變更前，請確保在 Windows 11 原生環境中通過門禁驗收：
   ```powershell
   pwsh -NoProfile -File tools\dev_check.ps1
   pwsh -NoProfile -File tools\test_product.ps1
   ```
3. **無斷鏈原則**：若修改或新增 Markdown 文件，所有相對連結必須通過 `tools/check_links.py` 檢查。
4. **提交格式**：提交訊息建議遵循 Conventional Commits 規範（如 `fix: ...`、`feat: ...`、`docs: ...`）。
5. **授權條款**：所有提交之程式碼與文件皆同意在 [CC0 1.0 Universal](LICENSE) 條款下貢獻至公眾領域。

詳細架構與除錯指引請參閱 [`docs/DEVELOPMENT.md`](docs/DEVELOPMENT.md)。
