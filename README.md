# Chung-En (Johnny) Yu — 個人網站

> 狀態：Option A 主網站已部署至 GitHub Pages；MyST 教材站更新已完成 build 與 branch validation，等待核准 fast-forward 至教材 repository 的 `main`。

這個 repository 是 Chung-En (Johnny) Yu 的研究者個人網站。公開頁面以英文呈現；提供給使用者與 agents 閱讀的 planning、decision、operation 文件則預設使用繁體中文。

## 網站設計

- 視覺方向：以 Allen Wu、Reza Salehi 類型的清楚研究者網站為資訊基礎，加入較成熟的 editorial typography 與留白。
- 字體：self-hosted `Newsreader`（display）與 `Inter`（body），不依賴 Google Fonts 或 runtime CDN。
- 技術：semantic HTML、modern CSS、零 client-side JavaScript、零 production dependency。
- 主內容：研究定位、selected research、publications、news、Learn、CV 與聯絡方式。
- Hosting：主網站與教材網站皆使用 GitHub Pages，但維持獨立 repository 與 deployment lifecycle。

```mermaid
flowchart LR
    V["訪客"] --> P["my-personal-website<br>研究者個人網站"]
    P --> H["首頁／研究定位"]
    P --> R["Research／Publications"]
    P --> C["CV／Profiles／Email"]
    P --> L["Learn 入口"]
    L --> M["ai-learning-notebooks<br>獨立 MyST 教材網站"]
    M --> N["Rendered notebooks"]
    M --> G["GitHub source"]
    M --> B["Open in Colab"]
```

## 專案結構

```text
.
├── index.html                 # 主首頁
├── publications/index.html   # 完整 publications
├── research/scoop/index.html # SCoOP project page
├── learn/index.html           # 教材導覽與 GitHub／Colab links
├── assets/                    # CSS、fonts、images、CV
├── scripts/                   # validation 與 build scripts
├── docs/                      # planning、decisions、design、operations
├── .github/workflows/         # GitHub Pages workflow
└── my-old-web/jbook_file/     # 獨立的 legacy／MyST nested repository
```

`my-old-web/jbook_file/` 具有自己的 Git history 與 remote。主網站不會在 build 時依賴它；需要的文字、圖片與 CV 已經 migration 到主站自己的 `assets/` 與 HTML。

## 本機執行

主網站不需要安裝 package：

```bash
python3 scripts/validate_site.py
python3 scripts/build_site.py
python3 -m http.server 8000 --directory _site
```

接著開啟 `http://localhost:8000/`。`_site/` 是 generated artifact，已加入 `.gitignore`，不可 commit。

MyST 教材網站：

```bash
cd my-old-web/jbook_file
npx --yes mystmd start
```

驗證實際 GitHub Pages base path：

```bash
cd my-old-web/jbook_file
BASE_URL=/ai-learning-notebooks npx --yes mystmd build --html
```

MyST build 只 render 已存在的 notebook outputs，不在 CI 執行昂貴或需要 network 的 notebook code。

## Deployment 流程

```mermaid
flowchart TD
    E["修改 source files"] --> V["python3 scripts/validate_site.py"]
    V --> B["python3 scripts/build_site.py"]
    B --> Q["local responsive／accessibility QA"]
    Q --> C["commit 與 push main"]
    C --> A["GitHub Actions"]
    A --> P["GitHub Pages production"]
```

主站 workflow 會重新執行 validation、建立乾淨的 `_site/` artifact，再透過官方 Pages actions 發布。GitHub Pages 不需要 long-lived deploy key；workflow 只使用 repository 提供的 `GITHUB_TOKEN` 與 least-privilege permissions。

## 文件入口

- [內容與舊站盤點](docs/planning/01-content-inventory.md)
- [設計研究與 skill 候選清單](docs/planning/02-design-research.md)
- [網站架構、notebooks 與部署方案](docs/planning/03-architecture-and-deployment.md)
- [實作與驗證計畫](docs/planning/04-implementation-and-validation-plan.md)
- [已核准網站方向](docs/decisions/0001-approved-site-direction.md)
- [已安裝 skills 與安全紀錄](docs/decisions/0002-installed-skills.md)
- [視覺系統](docs/design/visual-system.md)
- [維護與內容更新手冊](docs/operations/maintenance.md)
- [Agent 作業規範](AGENTS.md)

## 保護舊站與 credentials

- 新版 production 完成並經使用者 review 前，不刪除 `my-old-web/`。
- 不得 reset、覆寫或 commit nested repository 內既有的 `.DS_Store` 變更。
- 不得將 SSH keys、tokens、cookies、`.env` 或其他 credentials 寫入 repository。
- GitHub SSH credentials 只能留在使用者的 global environment；repository 內不保存副本。
