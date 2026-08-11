# 0001 — 核准的網站方向

日期：2026-08-11

狀態：Accepted

## 決策

- 採用 Option A 的 warm editorial minimal 視覺方向。
- 資訊結構以 [Allen Wu](https://wpr001.github.io/) 與 [Reza Salehi](https://homes.cs.washington.edu/~mrsalehi/) 的清楚、研究優先、低干擾模式為基礎。
- 不直接複製參考網站；新網站要使用更完整的 type scale、更穩定的 spacing、更清楚的 publication hierarchy 與更有辨識度的 research-led signature。
- 採用雙網站架構：`my-personal-website` 負責個人首頁；現有 `chung_en_johnny_yu_website` repository 改為 MyST／Notebook 教材用途。
- 可以公開目前 CV。
- 舊站在新版穩定、部署並通過 review 前保留，不進行刪除。

## Implementation 約束

- 主網站使用 semantic HTML、modern CSS 與 minimal JavaScript。
- 主網站部署目標為 GitHub Pages project site：`/my-personal-website/`。
- 不引入 database、CMS、analytics、authentication 或 frontend framework。
- Core reading 與 navigation 在 JavaScript 關閉時仍需可用。
