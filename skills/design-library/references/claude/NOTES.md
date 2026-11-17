# Claude（claude.com）

## 来源

- 仓库：`VoltAgent/awesome-design-md`（127.6k★）
- 路径：`design-md/claude/DESIGN.md`
- 抓取：2026-11-15，589 行
- 上游说明：Anthropic 官网营销面的视觉分析

## 取（吸收了什么，落到哪）

### 1. 墨色不用纯黑

它用 `#141413` 而不是 `#000000`，正文 `#3d3d3a`。理由写在 Overview 里：纯黑在屏幕上过硬，印刷感的黑是带一点暖的。

→ **已落到** `editorial-serif` 的 `colors.ink`（#1A1714），本来就是这个思路，现在有了外部佐证。
→ **已落到** `principles.md` 第 3 节：中性色是一根灰阶，不是一个 #000。

### 2. 背景不用纯白

`#faf9f5` 暖奶油色，它明说这是"对抗所有 AI 品牌都用冷灰白"的定位选择。

→ 佐证了 `editorial-serif` 的 `canvas` #FBF8F3。两个值只差一点点，说明这个暖度区间是经过实践检验的。

### 3. 衬线标题 + 无衬线正文

Copernicus 衬线 400 + StyreneB 无衬线正文。注意它是 **400 而不是 700**，靠字号和字距建立重量。

→ **反例价值**：我的 `editorial-serif` 用的是 700。对中文衬线来说 700 更安全（中文字形复杂，400 的小字重容易糊）。但大字号（54px+）确实可以试 400。**暂不改，记在待观察。**

### 4. 三层表面交替形成节奏

cream canvas → cream card → dark navy mockup，三个表面模式**逐段交替**，明暗对比本身就是版面的呼吸。

→ **待吸收**：`editorial-serif` 目前是单层（canvas + 白卡片），没有"深色段落"。如果以后要做长落地页，可以引入一个 `surface-dark` 做引文或结论区。

### 5. Known Gaps 这一章节

它诚实标注"字体是授权的买不到""动效没覆盖""产品面没覆盖"。

→ **已吸收为范式**：我三个风格的 DESIGN.md 都加了 `## Known Gaps`。这一节让文件可信——因为读者知道边界在哪。

### 6. Iteration Guide 的命令式写法

"Focus on ONE component at a time""Use token.refs everywhere — never inline hex"。

→ **已吸收**：三个风格都有 `## Iteration Guide`，写成给下一个人（或 agent）的操作指令，不是描述。

## 弃（明确不吸收，为什么）

- **Coral #cc785c 这个色本身**：它是 Anthropic 的品牌资产，抄色等于抄身份。我的对应物是赭红 #A63D2F，色相接近但更深、更旧，是"铁锈"不是"珊瑚"。
- **Copernicus / StyreneB 字体**：授权字体，买不到。它的 Known Gaps 自己也说了。
- **"radial-spike mark" logo 用法**：品牌标识，与我无关。
- **96px 的 section 间距**：它定位是 SaaS 营销页，需要紧凑的叙事节奏。`editorial-serif` 是长文阅读，用了 104px，更松。
- **深色产品卡（code mockup）**：这是"展示产品截图"的手法，属于营销页专属。阅读型风格不需要。

## 待观察

- 大字号衬线用 400 字重，中文能不能成立？需要在真实标题上试（54px 以上，宋体 400）。
- 三层表面交替的节奏，能不能用在博客长文里？可能过于花哨，需要验证。
- 它的 `caption-uppercase` 用 13px + 0.1em 字距。我用的是 12px + 0.18em，更接近"栏目名"而不是"图注"。两种都成立，取决于用途。
