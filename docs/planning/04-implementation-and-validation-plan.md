# 實作與驗證計畫

建立日期：2026-08-11

只有在使用者核准設計與架構決策後，才能開始執行本計畫。

## Phase 0 — 決策確認

需要核准的事項：

- 視覺方向 A、B 或 C。
- 採用雙網站架構，或改用較簡單的 notebook-link fallback。
- 主要 GitHub repository 名稱與預計公開 URL。
- 公開 CV 的 privacy 選擇。
- 是否允許安裝任何第三方 design skill。

完成條件：將決策記錄在 `docs/decisions/`，並更新 `AGENTS.md` 中的 planning phase gate。

## Phase 1 — Workspace 與內容基礎

1. 確認新的 top-level repository 應如何與 nested legacy repository 共存。
2. 初始化或連接經核准的 personal-site repository，不修改 legacy history。
3. 在 `.gitignore` 加入 legacy directory、OS files、build output、caches 與 secrets 規則。
4. 為 profile、news、publications 與 projects 建立小型 structured content source。
5. 統一 publication metadata，並標記尚未解決的研究狀態或內容衝突。
6. 記錄且驗證 local preview 與 build commands。

完成條件：project structure 乾淨，不包含 secrets 或 build artifacts，而且無需讀取 component code 就能 review content data。

## Phase 2 — 視覺 prototype

1. 只建立 homepage shell 與一項 selected-research entry。
2. 實作 typography、color tokens、spacing、focus states 與 responsive behavior。
3. Portrait 只有在 image quality 與 crop 獲得核准後才能重用。
4. 提供 mobile 與 desktop visual evidence。
5. 先依選定的 design direction 完成 review，再建立其他頁面。

完成條件：使用者核准 core visual system 與 first viewport。

## Phase 3 — 網站內容

1. 加入 selected research 與 publication listing。
2. 加入 recent news 與 archive behavior。
3. 只依核准的詳細程度加入 teaching／service。
4. 加入 CV 與 contact links，並完成 privacy checks。
5. 只有在 project detail page 比 paper／code link 更能幫助理解時，才新增詳細研究頁。
6. 加入 metadata、social preview image、favicon 與 structured data。

完成條件：所有約定內容皆已建立、proofread，且具有明確來源。

## Phase 4 — Learn site 決策與處理

建議方案：

1. 維持現有 notebook repository 獨立存在。
2. 修正其 repository metadata，並更新 MyST Pages workflow。
3. 維持 `_build` ignored。
4. CI 不執行 notebooks，只 render 已儲存的 outputs。
5. 加入 GitHub 與 Colab links。
6. 最佳化 10 MB MLP notebook 與任何過大的 embedded images。
7. 加入輕量的共用 branding，以及返回個人網站的連結。

備選方案：

- 暫時不部署 MyST；在主網站建立 curated Learning page，連結至 Notebook source 與 Colab。

完成條件：每一份公開 notebook 都能穩定在網頁中開啟，並有清楚的 source／Colab 入口。

## Phase 5 — 驗證

### 功能

- 檢查所有 navigation、publication、code、paper、profile、email、CV、GitHub 與 Colab links。
- 不存在 missing files、case-sensitive path errors 或 GitHub Pages base-path failures。
- 使用文件中的 commands，可以從 clean checkout 完成 preview 與 build。
- Deployed artifact 不包含只應存在於 source 的 files 或 secrets。

### 響應式設計（Responsive）與視覺

- 約在 360、768、1280 與 1600 CSS pixels 下進行 review。
- 檢查較長的 paper titles、author lists、URLs 與 news entries 是否 overflow。
- 檢查 portrait crop、image sharpness、content rhythm 與閱讀 line length。
- 只有在 dark mode 獲得核准時，才檢查 light／dark rendering。
- 比較 deployed Pages URL 與 local rendering。

### 無障礙（Accessibility）

- Keyboard-only navigation 與 visible focus。
- Skip link 與 semantic landmarks。
- 合理的 heading order。
- Informative alt text 與 decorative-image handling。
- 足夠的 text、link 與 focus contrast。
- 適合 mobile 的 touch target size。
- Reduced-motion behavior。
- 對 screen reader 友善的 publication 與 icon-link labels。

### 效能（Performance）與品質

- 不包含不必要的 JavaScript framework payload。
- Images 具有明確 dimensions，並使用最佳化的 responsive images。
- Below-the-fold images 使用 lazy loading。
- 不 commit 430 MB generated build output。
- 在 deployed URL 執行 Lighthouse／Core Web Vitals audit。
- Review console 與 network errors。

### SEO 與學術搜尋能見度

- 每個 page 都有獨立的 title 與 description。
- Canonical URL 與 social preview metadata。
- Sitemap 與 robots behavior。
- 使用安全 public identifiers 的 Person／profile structured data。
- 穩定的 publication links，以及 accessible paper／code labels。
- 清楚呈現姓名變體：`Chung-En (Johnny) Yu` 與 scholarly citation form。

### 安全性（Security）與隱私（Privacy）

- 對 tracked files 執行 secret scan 與 manual review。
- 除非明確核准，否則不公開電話號碼。
- 預設不加入 private analytics identifiers 或 third-party trackers。
- 在新分頁開啟的 external links 必須使用安全的 relationship attributes。
- GitHub Actions 使用 least-privilege permissions。

## Version one 驗收條件

- 訪客能在十秒內理解 Johnny 的研究方向與目前身分。
- Selected research、完整 publications、Scholar、GitHub、email、CV 與 Learn 都能在一至兩次互動內抵達。
- 核心閱讀與 navigation 不依賴 JavaScript 也能運作。
- 主頁在 mobile 與 desktop 都具有完整且精緻的視覺呈現。
- 更新內容時，不需要在多個 files 重複修改同一筆資料。
- GitHub Pages deployment 可重現且有清楚文件。
- Notebook material 可透過 MyST 閱讀，或能清楚透過 GitHub／Colab 開啟。
- 不公開 credentials、generated builds 或未經同意的個人資料。

## 實作完成後預期交接內容

負責 implementation 的 agent 必須提供：

- 最終 file tree 與 architecture summary。
- 精確的 install、preview、build、test 與 deploy commands。
- Mobile 與 desktop 的 visual QA evidence。
- Link、accessibility 與 performance check results。
- GitHub Pages URL 與 deployment workflow status。
- 尚待確認的 content questions，以及提供給未來 agents 的安全更新 instructions。
