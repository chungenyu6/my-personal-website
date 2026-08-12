# 維護與內容更新手冊

這份文件讓未來的 agent 或使用者能用最小變更更新網站，而不破壞架構。開始前仍須先閱讀根目錄的 `AGENTS.md`。

## 常見內容更新

### 新增 news

1. 編輯 `index.html` 的 `.news-list`。
2. 使用 `<time datetime="YYYY-MM-DD">` 保存 machine-readable 日期。
3. 最新項目放在最上方，首頁維持約 5 項；較完整紀錄可留在 CV。

### 新增 publication

1. 在 `publications/index.html` 的正確年份區塊新增 `.publication-item`。
2. 核對 title、author order、venue、status、DOI／paper／code link。
3. 若是重要工作，再決定是否加入首頁 `.research-list`；首頁維持 3–5 個 selected works。
4. 不確定的 acceptance status 或日期要標記給使用者 review，不可自行推測。

### 更新 CV

以新 PDF 覆蓋 `assets/documents/cv-chung-en-johnny-yu.pdf`，保持檔名不變，再檢查首頁與所有 subpages 的 CV link。

### 新增 notebook

1. 在相鄰的 `../ai-learning-notebooks/` repository 更新 notebook 與 `myst.yml` TOC。
2. 在 `learn/index.html` 加入 rendered MyST、GitHub source 與 Colab link。
3. 執行 MyST build；預設不要加 `--execute`，避免 CI 執行耗時或 network-dependent code。

## 變更後驗證

```bash
python3 scripts/validate_site.py
python3 scripts/build_site.py
python3 -m http.server 8000 --directory _site
```

至少檢查：

- mobile、tablet、desktop 沒有 horizontal overflow。
- keyboard focus 清楚，skip link 可用。
- 沒有 broken local links、missing images 或 browser console errors。
- `assets/images/social-card.jpg` 與 Open Graph metadata 仍正確。
- GitHub Pages repository base path 下的 links 正確。

教材網站另外執行：

```bash
cd ../ai-learning-notebooks
BASE_URL=/ai-learning-notebooks npx --yes mystmd build --html
```

## 不要做的事

- 不要引入 framework、CMS、analytics、database 或 animation library，除非有明確需求與使用者核准。
- 不要直接編輯 `_site/` 或 MyST 的 `_build/`；它們都是 generated artifacts。
- 不要把 `ai-learning-notebooks` 放進主站形成 nested repository；兩者維持相鄰且獨立的 checkouts。
- 不要將 secrets、SSH private keys、tokens、cookies 或 `.env` commit 到 repository。

## Handoff 最低資訊

完成更新後，回報 changed files、執行過的 checks、結果、所做 assumptions、尚未解決的風險，以及建議的 next step。
