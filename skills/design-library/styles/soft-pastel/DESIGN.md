---
version: alpha
name: Soft Pastel
description: >-
  低对比柔色界面。浅色是 Latte（灰紫纸 + 墨水紫），深色是 Mocha（暖夜色 +
  薰衣草紫）。颜色的量很大——14 个色相——但全部压在同一明度带上，
  所以看起来是"柔和"而不是"花"。只有一个字重差，没有阴影，全是圆角。
# ---------------------------------------------------------------- 选择条件
family: companion
tier: variant
sourceRefs: catppuccin
cues: 消费级 app、陪伴型产品、笔记与阅读工具、社区、需要"温和不催促"的界面
avoid: 数据看板、高密度后台、需要紧迫感的场景、对色觉障碍要求严格的场景
surface: mixed
density: roomy
register: tool

colors:
  # ---- Latte（浅色）----
  canvas: "#EFF1F5"
  surface: "#E6E9EF"
  sunken: "#DCE0E8"
  surface-raised: "#FFFFFF"
  line: "#CCD0DA"
  line-strong: "#ACB0BE"
  ink: "#4C4F69"
  ink-soft: "#6C6F85"
  ink-faint: "#7C7F93"
  accent: "#8839EF"
  danger: "#D20F39"
  rosewater: "#DC8A78"
  flamingo: "#DD7878"
  pink: "#EA76CB"
  maroon: "#E64553"
  peach: "#FE640B"
  yellow: "#DF8E1D"
  green: "#40A02B"
  teal: "#179299"
  sky: "#04A5E5"
  sapphire: "#209FB5"
  blue: "#1E66F5"
  lavender: "#7287FD"
  # ---- Mocha（深色）----
  mocha-canvas: "#1E1E2E"
  mocha-surface: "#181825"
  mocha-sunken: "#11111B"
  mocha-surface-raised: "#313244"
  mocha-line: "#45475A"
  mocha-ink: "#CDD6F4"
  mocha-ink-soft: "#A6ADC8"
  mocha-ink-faint: "#7F849C"
  mocha-accent: "#CBA6F7"
  mocha-danger: "#F38BA8"
  mocha-green: "#A6E3A1"
  mocha-yellow: "#F9E2AF"
  mocha-peach: "#FAB387"
  mocha-blue: "#89B4FA"
  mocha-rosewater: "#F5E0DC"
  mocha-flamingo: "#F2CDCD"
  mocha-pink: "#F5C2E7"
  mocha-maroon: "#EBA0AC"
  mocha-teal: "#94E2D5"
  mocha-sky: "#89DCEB"
  mocha-sapphire: "#74C7EC"
  mocha-lavender: "#B4BEFE"

typography:
  headline-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, PingFang SC, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.01em
  headline-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, PingFang SC, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, PingFang SC, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.01em
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, PingFang SC, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, PingFang SC, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  label-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, PingFang SC, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  sm: 8px
  md: 12px
  full: 9999px

spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  xxl: 32px
  section: 48px
  measure: 40em

components:
  button:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 18px
  button-soft:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 18px
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 24px
  field:
    backgroundColor: "{colors.sunken}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
  tag:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.accent}"
    typography: "{typography.label-md}"
    rounded: "{rounded.full}"
    padding: 4px 9px
  row:
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 14px
---

## Overview

先说清楚一件事：**Catppuccin 不是设计语言，是一组调色板。**

它有 26 个颜色 × 4 个 flavor（Latte / Frappé / Macchiato / Mocha），每个色都带 `order` 字段，版本化管理得很规范。但它**没有定义**字号、圆角、间距、组件形态——它只回答"用什么颜色"，不回答"怎么排版"。

所以这个风格里，**颜色是可复现的，形状是补的**。我在下面每一条形状规则旁都标了来源性质。这样做比假装整份文档都同样"硬"要诚实——就像 `references/chatgpt-ios/NOTES.md` 里说的：它能教你气质，教不了实现。

**Key Characteristics**

- **14 个色相**，全库最多。全部压在同一明度带上，所以柔和而不花。
- 浅色 Latte 的墨是 `{colors.ink}`（#4C4F69），一个**带紫的近黑**，不是灰。这是 Catppuccin 最容易被忽略的身份：整套色都在紫色相邻区。
- 深色 Mocha 的底是 `{colors.mocha-canvas}`（#1E1E2E），**带紫的深蓝**，比 `quiet-dark` 的纯灰暖一档。
- 主色 `{colors.accent}` 是 mauve（#8839EF / #CBA6F7）——不是蓝、不是绿，是紫。这是全库唯一以紫为主的风格。
- 只有 400 和 600 两个字重。**没有 700**：低对比配色配粗字重会互相打架。
- **零阴影。** 层级只靠三档底色（canvas / surface / raised）。
- 行高 1.6，比工具界面松——"柔"有一半来自行距。

## Colors

26 个色里，这个风格只用了 22 个（Frappé / Macchiato 两个 flavor 没用）。挑的原则是：一套浅色、一套深色，两套共用同一个结构。

### Latte 的三层表面

- **Canvas** (`{colors.canvas}` — #EFF1F5): base。页面底，灰紫白。
- **Surface** (`{colors.surface}` — #E6E9EF): mantle。卡片。
- **Sunken** (`{colors.sunken}` — #DCE0E8): crust。输入框、代码块——比 canvas **暗**，形成下凹。
- **Surface Raised** (`{colors.surface-raised}` — #FFFFFF): 弹层。**这是唯一一个不在调色板里的值**，因为 Latte 没有比 base 更亮的色，而弹层必须比底亮。

注意这套的方向和 `quiet-dark` 相反：**深色下 raised 是变亮，浅色下 sunken 是变暗，而 raised 只能借纯白。**

### Mocha 的三层表面

- **Canvas** (`{colors.mocha-canvas}` — #1E1E2E): base。
- **Surface** (`{colors.mocha-surface}` — #181825): mantle。**比 canvas 暗**（0x18 比 0x1e 暗）——卡片是"陷进去"的，不是浮起来的。
- **Sunken** (`{colors.mocha-sunken}` — #11111B): crust。最深。
- **Surface Raised** (`{colors.mocha-surface-raised}` — #313244): surface0。弹层才用它。

### Ink

- **Ink** (`{colors.ink}` — #4C4F69): 正文。5.5:1 上下，Purple-tinted 近黑。
- **Ink Soft** (`{colors.ink-soft}` — #6C6F85): 次要文字。**4.37:1，刚好在 4.5 线下**——用在 14px 以上没问题，13px 以下不要用。
- **Ink Faint** (`{colors.ink-faint}` — #7C7F93): 3.49:1，**只给占位符和禁用态**。这里本来想用 overlay1（#8C8FA1），但它只有 2.83:1，连"最弱一级"该守的 3:1 都过不了，所以退一档到 overlay2。

### 14 个 accent 里，只有两个能当文字用

这是整套配色最重要的一条事实，也是最多人抄错的地方：

| 色 | Latte 对底 | 能不能当文字 |
|---|---|---|
| mauve | 4.79 | ✅ |
| red | 4.80 | ✅ |
| blue | 4.34 | ⚠️ 勉强，只用于 ≥18px |
| maroon | 3.48 | ❌ 只做填充 |
| teal | 3.31 | ❌ |
| green | 2.96 | ❌ |
| lavender | 2.81 | ❌ |
| sapphire | 2.78 | ❌ |
| flamingo | 2.64 | ❌ |
| peach | 2.64 | ❌ |
| sky | 2.47 | ❌ |
| rosewater | 2.34 | ❌ |
| pink | 2.34 | ❌ |
| yellow | 2.31 | ❌ |

**所以 Latte 里能写字的彩色只有 `{colors.accent}`（mauve）和 `{colors.danger}`（red）。** 其余 12 个是"填充色和图标色"，不是"文字色"。如果你在浅色版里用绿色写一行字，它在对比度上是不合格的——而它看起来"还行"，这才是最危险的地方。

Mocha 的情况完全不同：14 个 accent 对 #1E1E2E 全部在 **7:1 以上**，全部可以当文字色。所以深色版的规则松得多。这个差异不是设计选择，是配色的客观事实。

## Typography

系统无衬线（SF Pro / PingFang），因为柔色 + 定制字体会变成"品牌感过载"。

字号 12 / 14 / 16 / 18 / 22 / 28。**18px 这一档是刻意留的**：柔色的界面里，"稍微大一点的正文"比"加粗的正文"更合适。

字重只有 400 和 600。**没有 700**——这不是遗漏。低对比配色下，700 会让文字从柔和的底上"跳"出来，破坏整体。要强调时用 600 + 颜色，不用 700。

行高 1.6（正文）。对比 `quiet-dark` 的 1.5——这 0.1 就是"柔"和"紧"的差别。

## Layout

- 版心 40em，间距 4 / 8 / 12 / 16 / 24 / 32 / 48。
- **卡片内边距 24px**，比工具界面松（工具是 16）。
- 列表行 12px / 14px，比 `quiet-dark` 的 10/12 松。
- 块与块之间靠 24px 留白，不靠分隔线。**这个风格几乎不用线**——线是硬的。

## Elevation & Depth

**零阴影，零边框。** 层级只用明度：

| 层 | Latte | Mocha |
|---|---|---|
| 凹陷 | #DCE0E8 | #11111B |
| 底 | #EFF1F5 | #1E1E2E |
| 卡片 | #E6E9EF | #181825 |
| 弹层 | #FFFFFF | #313244 |

注意 Mocha 的卡片比底**暗**，Latte 的卡片比底**暗**——两套是一致的（都是"卡片陷进纸里"），只有弹层是浮的。这和 `quiet-dark`（卡片比底亮）是相反的做法，两种都成立，但不要混用。

## Shapes

三档圆角，全部偏大：

- `{rounded.sm}` 8px — 输入框、列表行、代码块
- `{rounded.md}` 12px — 卡片、面板
- `{rounded.full}` — 按钮、标签、头像、分段控件

**按钮是全圆的。** 圆角在这套风格里不是装饰，是"这个东西不锋利"的声明。12px 的卡片配全圆的按钮，是两个不同半径的柔，不冲突。

## Components

### button

`{colors.accent}` 底 + `{colors.canvas}` 字 + 全圆 + 10/18 内边距。

悬停用 `filter: brightness(1.08)`，**不加阴影、不位移**。按下 `scale(0.98)`。
这两条是本库补的（Catppuccin 没有组件规范），选择理由是：低对比配色下，位移和阴影都太"响"，只有亮度和轻微缩放不破坏柔和。

### card

`{colors.surface}` 底 + 12px 圆角 + 24px 内边距，**加一条 1px `{colors.line}` 内描边**。

这条描边是画完才发现的必需品：Latte 的 mantle（#E6E9EF）和 base（#EFF1F5）之间只有 **1.04:1**，纯靠明度根本分不出卡片边界。所以"零边框零阴影"这句话在浅色版执行不了——必须留一条线。深色版同理（#181825 对 #1E1E2E，也接近）。

**教训记在这里**：一个纯配色方案（palette）转成设计语言时，最先崩的往往是"层级"。颜色本身没说"这两层要怎么分"，那是排版的工作。

### field

`{colors.sunken}` 底 + 8px 圆角 + 1px `{colors.line}` 内描边，10/14 内边距。

聚焦时描边变 2px `{colors.accent}`，**不加外发光**——柔色配发光会变成"赛博"。
错误时描边变 2px `{colors.danger}`，同样不加发光。

### tag

用 `color-mix` 把 accent 混 18% 到透明做成底色，文字用 accent 本身。这是**五个值里唯一一个"派生"而非"取色"的做法**，理由：Catppuccin 没有定义"浅色标签底"，用官方色混出来比新编一个色更安全。

但成功/警告两个变体是例外：**文字用 `{colors.ink}`，不用绿也不黄**。因为绿在 Latte 里只有 2.96:1、黄只有 2.31:1，都不够当文字。它们只能做底色——这正是上面那张表的意思。

### row / seg / avatar

行 12/14 内边距；分段控件用 `{colors.sunken}` 做槽、`{colors.surface-raised}` 做选中块；头像用 accent 混 22% 做底。

## Do's and Don'ts

### Do

- 14 个 accent 里，浅色版只让 mauve 和 red 当文字色。
- 层级用三层底色，不用阴影、不用边框。
- 按钮全圆，卡片 12px。
- 字重只用 400 / 600。
- 强调用颜色 + 600，不用 700。
- 需要浅色标签底时用 `color-mix` 从官方色混，不要新编色值。

### Don't

- 不要在 Latte 里用绿/黄/粉写文字。它们只有 2.3-2.9:1。
- 不要加阴影。一处都不要。
- 不要用 700 字重。
- 不要给聚焦态加外发光。
- 不要用纯灰。这套配色的所有中性色都带紫，去掉紫就变成另一套风格了。
- 不要混用 Frappé / Macchiato。只用 Latte 和 Mocha，两套足够，多一套就乱。
- 不要把 14 个色平铺在一屏上。柔色的前提是**同一屏最多三个色相**。

## Chinese Typography

- **1.6 行高对中文刚好**。这套风格比 `quiet-dark` 松，中文在这里比在工具界面里舒服。
- **`ink-soft` 4.37:1 对中文偏危险**：汉字的笔画密度比拉丁高，同样对比度下更难读。中文的次要文字建议直接用 `{colors.ink}`，不要降一档。
- **不要把 700 用在中文标题上**：PingFang SC 的 Bold 在低对比底上会显得"糊"。600（Semibold）是这套风格的上限。
- **中西文之间留 1/4 空格**：`共 12 项`、`用 Markdown 写`。
- **中文标签不需要字距**：全圆标签里加字距会让中文读起来断断续续。
- **14 个彩色对中文更危险**：汉字比拉丁更依赖笔画与底的明度差。给中文上彩色时，只选 mauve / red 两个。

## When to Use

**用**：消费级 app、陪伴型产品（日记、冥想、习惯）、笔记与阅读工具、社区、面向非专业用户的产品、需要"不催促"的界面。

**别用**：数据看板（14 个色相会变成噪声）、高密度后台（对比度不够扫读）、需要紧迫感的场景（报警红在这套配色里不够响）、对色觉障碍要求严格的场景（紫绿搭配是红绿色盲的高危区）。

## Iteration Guide

1. 加色之前先查对比度表。Latte 里 12 个 accent 不能当文字色。
2. 需要新底色时，用 `color-mix` 从官方色混，不要新编十六进制。
3. 圆角只有 8 / 12 / full 三档。
4. 需要强调时：先加颜色，再升到 600，最后才考虑加粗到 700（基本不该到）。
5. 一屏最多三个色相。

## Known Gaps

- **形状规则是本库补的，不是 Catppuccin 的。** 这句话要一直带着——它只定义了颜色。
- 只做了 Latte 和 Mocha 两个 flavor。Frappé / Macchiato 是中间调，加进来会让"该选哪个"变复杂。
- 没有定义表单的错误文案层级、空状态、加载态。
- 没有定义图表配色方案。14 个色里挑 5 个做图表需要单独决定（建议按 `order` 跳着取，不要取相邻色）。
- **无障碍是这套风格的弱项**：14 个色相里有 12 个在浅色版不能做文字，紫绿组合对色觉障碍不友好。如果项目有 WCAG AA 硬要求，改用 `quiet-dark` 或 `civic`。
- 生图侧说明在 `prompt.md`——这套风格的配图应该柔和、低对比、像水彩或晨雾。
