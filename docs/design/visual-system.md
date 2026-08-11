# Visual System — Research Field Notes

## 設計命題

網站的單一工作是讓訪客快速理解：Johnny 研究如何讓 multimodal agentic AI 在高風險場景中更可靠，並能立即前往 publications、code、CV 或教材。

## Design tokens

### Color

- `paper` — `#F5F3EC`：帶有紙張感的主背景，不使用常見偏橘 cream。
- `ink` — `#17212B`：帶藍色的深墨色，提升研究與工程感。
- `slate` — `#52606D`：metadata 與 secondary copy。
- `signal` — `#2156D9`：paper links、focus 與 research signals。
- `mist` — `#E6EAF0`：rules、quiet surfaces 與 publication separation。
- `sage` — `#DDE5DD`：Learn 與 teaching 的低調區隔色。

### Type

- Display／research thesis：`Newsreader`，強調學術與 editorial character，只用於少數關鍵句。
- Body／navigation：`Inter`，提供 Allen Wu／Reza Salehi 類型的清楚、現代可讀性。
- Utility／metadata：`Inter`，使用 uppercase、較寬 letter spacing 與 tabular numerals。

### Layout

- 最大 content width：`1180px`。
- 主要閱讀欄：`680–760px`。
- Desktop hero 使用不對稱雙欄：研究命題佔較大空間，portrait 與 researcher metadata 形成較窄 anchor。
- Publications 使用水平 editorial records，而不是 card grid。

## Signature

每一項 featured research 都帶有一條細長的 `research signal`：由 venue／status label、研究問題與 paper title 組成，像研究筆記中的索引標記。這個元素同時承載資訊與視覺辨識，不只是裝飾。

## 自我檢查

- Option A 容易落入 cream + serif + terracotta 的通用 AI design；因此本設計改用 ink blue、cobalt signal 與 gray-green teaching surface，避免 terracotta。
- Serif 只用於 thesis 與少數 display text；大部分內容使用高可讀性的 sans-serif，保持接近 Allen Wu／Reza Salehi 的使用體驗。
- 不使用 animation 作為主要特色；只保留在 hover／focus 上有功能意義的 micro-interactions。

