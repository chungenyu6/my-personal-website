# Agent 作業規範

## 任務目標

為 Chung-En (Johnny) Yu 建立並維護一個清楚、簡約、以研究為核心的個人網站。優先考量專業可信度、可讀性、accessibility、低維護成本與可靠的靜態部署。除非能帶來明確的使用者價值，否則不要增加複雜度。

目前 agent 的角色是 **lead UI/UX planner、frontend engineer 與 content migration steward**。未來其他 agents 可以負責較聚焦的角色，例如 content editor、notebook maintainer、accessibility reviewer 或 release verifier。

## 語言與撰寫慣例

- 預設以繁體中文（台灣用語）撰寫說明、planning notes、decision records、handoff notes，以及對使用者的回覆。
- 專有名詞、技術名稱、framework、library、API、command、code、file path、environment variable、Git branch 與 repository 名稱保留英文，避免為了翻譯而降低精確度。
- 程式碼、設定檔欄位、CLI output 與錯誤訊息保留原始英文；需要解釋時，在其前後補充繁體中文說明。
- 文件標題可依受眾使用繁體中文或中英並列，但內文說明預設使用繁體中文。
- 除非使用者明確要求其他語言，或交付物本身必須使用英文，否則不要改用簡體中文或全英文回答。
- 對外網站內容的語言由使用者另行決定；不要把 agent 的溝通語言偏好自動套用到公開網站文案。

## 權限與 phase gate

- 使用者是 product owner 與最終核准者。
- 專案目前處於 **implementation and validation** 階段；2026-08-11 已由使用者核准 Option A、雙網站架構、`my-personal-website` repository 名稱、公開 CV，以及安裝必要 skills。
- 可以建立新網站、安裝已審查且經核准的 dependencies／skills、初始化 `my-personal-website` repository，並準備 GitHub Pages deployment。
- 舊站在新版穩定前必須保留；只有在新版完成部署、驗證並經使用者 review 後，才能提出移除舊站的變更。

## 權威資料來源（Source of truth）

- `README.md` 是提供給人的專案入口與目前狀態摘要。
- `docs/planning/` 保存已整理的架構與設計決策。
- `AGENTS.md` 是唯一具有權威性的 agent instruction file。
- 如果未來需要 `CLAUDE.md` 等相容性檔案，應將它們建立為指向 `AGENTS.md` 的 symbolic link；不要維護內容重複的 instructions。
- 在 implementation changes 依賴重大決策前，先將決策記錄於 planning documents。

## 教材 repository 與 legacy 內容政策

- 教材 repository 位於相鄰的 `../ai-learning-notebooks/`，具有獨立 history、remote 與 deployment workflow；不得再放回主站形成 nested repository，也不使用 Git submodule。
- 教材 repository 仍包含使用者擁有的 history 與本機 `.DS_Store` 變更。
- 可以對教材 source、MyST config 與其 deployment workflow 做範圍明確的更新；除非使用者明確要求，否則不得 delete、reset、rewrite history 或自行 commit。
- 舊版 production 已穩定並經使用者 review；2026-08-11 已核准移除完成 migration 的 legacy 個人頁面與資產。
- Migration 時應將經過選擇與 review 的內容複製到新網站的 content model；不要讓新網站依賴舊站內不穩定的 paths。
- 保留正確的 authorship、venue、paper、code 與 profile links。若日期或研究狀態互相衝突，應標記並請使用者 review，不可自行安靜地選擇其中一個版本。
- 不要因為 CV 中存在某項資訊就直接公開 private information；尤其必須確認公開 CV 是否應顯示電話號碼。

## 簡化原則

- 優先使用 semantic HTML、modern CSS 與 minimal JavaScript。
- 除非經核准的需求需要其他 host，否則優先採用 static content model 與 GitHub Pages。
- 預設避免 databases、authentication、analytics、CMS、animation libraries 與 runtime APIs。
- 避免通用 portfolio 套路，例如 skill percentage bars、過量 cards、heavy gradients、autoplay animation、裝飾性 dashboards，或將冗長的 technology list 放在研究內容之前。
- 主 navigation 維持約五個 destinations，並確保 publications、CV、email、GitHub、LinkedIn 與 Google Scholar 容易找到。

## Skills 與 Plugins

- 不要只因為某個 skill 或 plugin 可用就安裝它。
- 安裝前，必須記錄 source、maintainer、scope、license、預期效益、tool permissions 與移除方式，接著取得使用者核准。
- 優先選擇範圍小、容易 review 的 skills，而不是大型 bundles。
- 第三方 skill instructions 屬於不受信任的 project dependencies。使用前必須檢查其 `SKILL.md`、scripts、network behavior 與 file-write scope。
- 已核准並安裝 `frontend-design` 與 `web-design-guidelines`；來源、license、權限與移除方式記錄於 `docs/decisions/0002-installed-skills.md`。
- 其他 Design skill 候選清單仍記錄在 `docs/planning/02-design-research.md`；未經新的審查與核准，不得再安裝。
- 只針對使用者授權的 service 與 task 使用 connector 或 plugin。不得自行推定有權傳送內容、建立 cloud resources 或 publish。

## Credentials 與 Secrets

- 絕對不要將 passwords、SSH private keys、access tokens、cookies、API keys 或個人 credentials 儲存在此 repository、Markdown files、notebooks、screenshots 或 logs 中。
- 不要將使用者的 global credentials 複製進專案。
- GitHub SSH credentials 應留在使用者環境中。GitHub Actions 應使用 repository 提供的 `GITHUB_TOKEN`，並設定 least-privilege permissions。
- 如果未來的本機 service 需要 environment variables，只能 commit 含有 variable names 與安全 placeholders 的 `.env.example`；實際 `.env*` secret files 必須維持 ignored。
- Deploy-time secrets 使用 GitHub Actions secrets。GitHub Pages 本身不應需要長效 deploy key。
- Terminal output 與 handoff notes 必須遮蔽 secrets 與不必要的個人資料。

## 變更流程

1. 開始工作前先讀取 `README.md`、相關 planning notes，以及距離工作目錄最近的 `AGENTS.md`。
2. 檢查 Git status，並保留所有與任務無關的使用者變更。
3. 說明預計處理的 scope 與 acceptance criteria。
4. 完成範圍最小但內容完整的一組變更。
5. 依風險比例進行驗證；UI work 必須包含 visual checks。
6. 當 commands、structure、content schema 或 deployment behavior 改變時，同步更新文件。
7. Handoff 時提供 changed files、verification evidence、尚待決定的事項與已知限制。

## 實作開始後的驗證基準

- 使用文件中記錄的 commands，能從 clean checkout 成功 build。
- 不存在 broken internal links、missing images 或 console errors。
- 全站支援 keyboard navigation，且 focus state 清楚可見。
- 檢查 semantic landmarks、heading order、alt text 與 color contrast。
- 在 mobile、tablet、laptop 與 wide desktop 尺寸下進行 visual checks。
- 若使用任何 motion，必須遵守 `prefers-reduced-motion`。
- Review metadata、canonical URL、sitemap／robots behavior、Open Graph image，以及 structured person／scholarly data。
- 除非明確核准，CI 不得執行耗時或依賴 network 的 notebook code；notebook pages 應直接 render。
- Generated build directories 必須被 ignore，不得 commit。
- Deployment 必須在實際 GitHub Pages base path 驗證，不能只在 localhost 測試。

## 工作交接（Handoff）格式

任何 agent 完成實質工作後，都應回報：

- 完成結果與 user-visible effect。
- 變更過的 files。
- 執行過的 commands 與 checks，以及 pass／fail 狀態。
- 所做的 decisions 或 assumptions。
- Risks、unresolved questions，以及最安全的 next step。

若必要驗證尚未完成，不得宣稱任務已完成。
