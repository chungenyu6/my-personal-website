# 0002 — 已安裝 Skills

日期：2026-08-11

狀態：Accepted

## `frontend-design`

- Source：[Anthropic `skills/frontend-design`](https://github.com/anthropics/skills/tree/main/skills/frontend-design)
- Maintainer：Anthropic
- License：Apache-2.0
- Scope：visual direction、typography、layout、design self-critique 與避免 template-like UI。
- Files／permissions：只有 `SKILL.md` 與 license text；沒有 executable scripts，不需要 network 或 file-write tools。
- 預期效益：讓 Option A 具有針對 Johnny 研究定位的視覺決策，而不是通用 portfolio styling。
- 移除方式：刪除使用者 Codex skills 目錄中的 `frontend-design/`。

## `web-design-guidelines`

- Source：[Vercel `skills/web-design-guidelines`](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines)
- Maintainer：Vercel
- License：Repository README 宣告 MIT；截至安裝時，repository 未提供 top-level LICENSE file。
- Scope：review accessibility、focus、typography、images、interaction、responsive behavior 與 web quality。
- Files／permissions：只有 `SKILL.md`；audit 時會 read-only fetch 最新的 Vercel Web Interface Guidelines，不包含 project-write scripts。
- 預期效益：在 release 前提供一致、可重複的 UI audit。
- 移除方式：刪除使用者 Codex skills 目錄中的 `web-design-guidelines/`。

## 未安裝項目

沒有安裝 deployment bundles、cloud plugins、analytics skills 或其他大型 skill collections。

