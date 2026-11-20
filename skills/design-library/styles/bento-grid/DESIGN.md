---
version: alpha
name: Bento Grid｜便当格
description: >-
  用大小不等、圆角一致的卡片紧密拼成一屏，每格只装一个信息点，卡片跨度代表信息优先级。
  是产品功能墙、发布会规格页与作品集首屏的默认布局：先排阅读顺序，再定格子大小。
  参数提炼自 cusps.net 的 Bento Grid 趋势指南、vibe-hub.org 的风格卡与
  awesomeskills.dev 的 bento-grid-ui 硬护栏（三份交叉验证）；中性灰阶梯、
  对比度修正与中文排版由本库补齐。
cues: 产品功能总览与发布会规格墙、SaaS 营销落地页与作品集首屏、App 仪表盘首页与设置总览、需要一屏并列展示多个同级能力
avoid: 长表单与密集数据表格、必须从上到下线性阅读的流程、少于五格的内容、长篇散文与论文、需要严肃权威气质的金融医疗政务、打印为主的单栏文档
surface: light
density: medium
register: story
family: expressive
tier: variant
sourceRefs: bento-grid
status: beta

colors:
  canvas: "#F4F4F5"
  surface: "#FFFFFF"
  surface-alt: "#E8E8EC"
  ink: "#18181B"
  ink-muted: "#52525B"
  ink-faint: "#71717A"
  line: "#E4E4E7"
  line-strong: "#D4D4D8"
  primary: "#4F46E5"
  accent: "#F59E0B"
  on-primary: "#FFFFFF"
typography:
  display:
    fontFamily: "Plus Jakarta Sans, Inter, PingFang SC, sans-serif"
    fontSize: 64px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.03em
  headline:
    fontFamily: "Plus Jakarta Sans, Inter, PingFang SC, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.02em
  cardTitle:
    fontFamily: "Plus Jakarta Sans, Inter, PingFang SC, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.01em
  body:
    fontFamily: "Inter, PingFang SC, Noto Sans SC, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.75
    letterSpacing: 0
  label:
    fontFamily: "Inter, PingFang SC, Noto Sans SC, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0.06em
rounded:
  card: 24px
  button: 14px
  tag: 8px
spacing:
  base: 8px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 40px
  section: 64px
  measure: 34em
components:
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: 24px
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.button}"
    padding: 12px 24px
  tag:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.tag}"
    padding: 6px 12px
elevation:
  lightSource: top-left
  steps: 3
  e1: "0 1px 2px rgba(24,24,27,0.04)"
  e2: "0 2px 8px rgba(24,24,27,0.06)"
  e3: "0 12px 32px rgba(24,24,27,0.12)"
  topHighlight: "inset 0 1px 0 rgba(255,255,255,0.7)"
  borderLight: "{colors.line}"
  borderDark: "{colors.line-strong}"
  separator: whitespace
media:
  logoType: wordmark
  logoRule: "字标用 {typography.headline} 700，纯文字不加图形标；主色格用 {colors.primary}，其余用 {colors.ink}"
  imageRadius: "{rounded.card}"
  imageRatio: "16:10"
  imageTreatment: "去饱和 6%，按 {rounded.card} 圆角裁切，不做混色；需要统一色调时叠 {colors.primary} 8% 正片叠底"
  background: "纯色 {colors.canvas} 浅灰，无纹理无渐变"
  iconRule: "1.75px 描边，24px 基准，和 {colors.ink} 同色；单格只放一个图标"
  emptyState: "{colors.surface-alt} 底 + 一行说明，不放插画"
motion:
  easing: "cubic-bezier(0.2, 0.8, 0.2, 1)"
  durationFast: 120ms
  durationBase: 220ms
  hover: "格子抬升到 {elevation.e2}，translateY -2px，底色与圆角不变"
  focusRing: "3px solid {colors.primary}，offset 2px，跟随格子圆角"
  openTransition: "transform scaleY 0→1，transform-origin top，220ms"
  reducedMotion: "全部过渡降到 1ms，取消位移"
  dragUsesSpring: false
---
## Overview

给产品功能墙、发布会规格页、SaaS 落地页和作品集首屏用。页面是一屏紧密拼起的信息模块：每格回答一个问题，格子的面积和跨度直接说明它有多重要。它适合并列展示多个同级能力，不适合承载有先后顺序的流程或长文。

性格来自四个具体选择：64px／700 的展示标题与 16px／400 的正文拉开尺度差；浅灰画布 `{colors.canvas}` 托白色卡片 `{colors.surface}`，靠底色差和均匀格距分层；卡片统一 `{rounded.card}` 圆角，不混用半径；卡片跨度按 12 列网格取 2、3、4 列，主功能占 4 列×2 行，其余 2×1 或 3×1 填充。层级由**面积、跨度和位置**表达，不靠阴影和边框。

这份规范吸收 cusps.net 的「每格一个点、一致圆角与间距不可妥协」、vibe-hub.org 的「大格放核心、小格补信息、颜色用来分组」与 awesomeskills.dev 的硬护栏（4/12 列、12–16px 统一格距、20–28px 圆角、首屏不超过 8 格、单格不超过 30 词、无厚边框硬阴影）。它不是任何一个品牌的复刻；中性灰阶梯、靛蓝主色的对比度修正和中文排版由本库重定。

**Key Characteristics**

- 画布 `{colors.canvas}`：浅灰而不是纯白，让白卡 `{colors.surface}` 有可辨认的边界；纯白只出现在卡片内。
- 每格一个信息点：一个不超过 8 词的标题，配一个数字、一个图标或一张小图；单格正文不超过 30 词。
- 卡片跨度即优先级：核心功能占 4 列×2 行，次级 3×1 或 2×2，补充信息 2×1；首屏格子数控制在 5–8。
- 统一圆角与统一格距：`{rounded.card}` 圆角、`{spacing.md}` 格距全页一致，绝不混用；格距是唯一分组手段。
- 同色系 2–4 档填色，加 1–2 个强调格；主色格 `{colors.primary}` 白字，琥珀格 `{colors.accent}` 只用深字。
- 双字族分工：Plus Jakarta Sans 管标题的几何感，Inter 管正文与数字的可读性；中文回退 PingFang SC。

## Colors

**Canvas & Surface**

- `{colors.canvas}` — #F4F4F5，页面底色；来源 Base 显式值，浅灰托白卡，不用纯白铺底。
- `{colors.surface}` — #FFFFFF，卡片底；来源 Ground 显式值，白卡与灰底形成唯一必要的边界。
- `{colors.surface-alt}` — #E8E8EC，次级格与空态底；比画布深一档，用于不需要白卡强调的格子。

**Ink**

- `{colors.ink}` — #18181B，标题、正文与关键数字；来源 Text 显式值，对画布 16.12:1、对白卡 17.72:1。
- `{colors.ink-muted}` — #52525B，次级说明；对画布 7.03:1，可连续阅读。
- `{colors.ink-faint}` — #71717A，元信息与编号；对画布 4.40:1，仅用于非关键内容。

**Line**

- `{colors.line}` — #E4E4E7，卡片内部分隔细线；只做辅助，不承担主分组。
- `{colors.line-strong}` — #D4D4D8，强调边界；用于需要比细线更清楚的轮廓处。

**Primaries**

- `{colors.primary}` — #4F46E5，主色：主按钮、主色格与焦点环；来源 Highlight #6366F1 调深一档，白字 6.29:1、对画布 5.72:1，达到正文级对比度。
- `{colors.accent}` — #F59E0B，琥珀：只做 1–2 个小面积强调格与数字，配 `{colors.ink}` 深字 8.25:1；绝不承载正文与白字。
- `{colors.on-primary}` — #FFFFFF，主色格上的文字；不引入第二种白。

## Typography

展示标题 64px／700／行高 1.05，章标题 32px／700，卡片标题 24px／700，正文 16px／400／行高 1.75，标签 12px／700／字距 0.06em。字号从 16 到 24 到 32 是 1.5 与 1.33，再跳到 64；只设这五档，不出现 18、20、28 这类中间值。

字重只有 400 和 700 两档。拉丁展示用 Plus Jakarta Sans／Inter，正文与数字用 Inter——几何无衬线为标题定性格，开放字腔的字族负责阅读与表格数字；中文按各档回退 PingFang SC。卡片内的大数字用 `{typography.headline}` 并开启等宽数字，保证纵向对齐。

## Layout

- 桌面 12 列网格，统一格距 `{spacing.md}`；核心卡跨 4 列×2 行，次级卡 3×1 或 2×2，补充卡 2×1；所有格子严丝合缝，不出现破坏矩形的空洞。
- 移动端降为 4 列，格子按优先级重排为单列或 2 列，阅读顺序不变；格距仍为 `{spacing.md}`。
- 内容最大宽 1280px；首屏只放一组 bento，格数 5–8，卡片内边距 `{spacing.lg}`。
- 区块之间 `{spacing.section}`；标题区与卡片组之间 `{spacing.xl}`。
- 卡片文字锚定左上或左下，同一屏保持一致；格内元素对齐到同一内边距。

## Elevation & Depth

共 `{elevation.steps}` 级材质。主分隔手段是 `{elevation.separator}`——靠均匀格距分组，不靠边框和投影。贴面 `{elevation.e1}`、卡片 `{elevation.e2}`、浮层 `{elevation.e3}`；光从 `{elevation.lightSource}` 来，卡片有轻微上浮但投影很淡，禁止居中发光。高光 `{elevation.topHighlight}` 只给白卡一条极淡顶边；正常态不描边，`{colors.line}` 只用于卡内分隔，`{colors.line-strong}` 仅用于需要强调的轮廓。

## Shapes

卡片统一 `{rounded.card}` 圆角，按钮 `{rounded.button}`，标签 `{rounded.tag}`；同一页面不出现第二种卡片圆角。格子是矩形，不做圆形卡、不做斜切、不做玻璃拟态；主色格靠填色区分而不是靠改形状。图标统一 1.75px 描边、24px 基准，与 `{colors.ink}` 同色。

## Material & Elevation

光从 `{elevation.lightSource}` 来，固定这一个方位。三级材质靠浅灰画布托白卡加极淡投影实现：层级差主要来自底色与格距，阴影只给一点点浮起感。深色上本风格未定义；浅色上阴影必须有偏移，禁止 `0 0 Npx` 的居中发光。主分隔手段是 `{elevation.separator}`，边框退到卡内辅助位。

## Mark & Media

标识：`{media.logoRule}`（`{media.logoType}`）。图片：比例 `{media.imageRatio}`、圆角 `{media.imageRadius}`、处理 `{media.imageTreatment}`。背景：`{media.background}`。图标：`{media.iconRule}`。空态：`{media.emptyState}`。

只写规则不写品牌资产。图片在一格里只承担一个职责：产品截图说明功能、人像说明团队、图表说明数据；删掉图片若不影响理解，就换成一个数字或图标。所有图都有静止替代帧，素材未加载时该格仍以标题与文字成立。文字、按钮、表单和数据标签一律真实 HTML/CSS 排版，不让生图模型画字。

## Motion & States

过渡曲线 `{motion.easing}`，快档 `{motion.durationFast}`、基准 `{motion.durationBase}`。hover：`{motion.hover}`；焦点：`{motion.focusRing}`；展开：`{motion.openTransition}`。交互组件逐项覆盖 default / hover / focus-visible / active / disabled / error 六态。

`prefers-reduced-motion` 时 `{motion.reducedMotion}`。本风格没有拖拽排序组件，不使用弹簧过渡。焦点环跟随卡片圆角但不能被裁切，`outline-offset` 留出 2px 空间。

## Components

### card

`{components.card}` 是白底 `{rounded.card}` 圆角格，靠 `{spacing.md}` 格距与邻格分开。每格一个标题配一个信息点：标题 `{typography.cardTitle}`，正文不超过 30 词；主色格把底色换成 `{colors.primary}`、文字换成 `{colors.on-primary}`，同一屏最多两个彩色格。

### button-primary

`{components.button-primary}` 是靛蓝 `{rounded.button}` 圆角按钮，承担一屏唯一主行动。它只出现在主色格里或卡片组之后，不重复堆叠；次按钮用透明底与 `{colors.line-strong}` 描边，尺寸一致。

### tag

`{components.tag}` 用 `{colors.surface-alt}` 底、`{colors.ink-muted}` 字表示事实状态，放在卡片左上或数值旁；不做标题前的装饰序言，不用琥珀以外的彩色做标签底。

## Do's and Don'ts

### Do

- 先按优先级排出格的跨度，再往格里填内容。
- 全页统一 `{rounded.card}` 圆角与 `{spacing.md}` 格距。
- 每格一个信息点，核心功能给 4 列×2 行的大格。
- 用 2–4 档中性填色加 1–2 个强调格，彩色格配足对比度的文字。

### Don't

- 不要让格子之间格距不一致，或出现填不满的空洞。
- 不要在一格里放多段正文或多个号召性操作。
- 不要混用圆角、加厚边框或硬阴影；平铺感是本风格的前提。
- 不要把琥珀 `{colors.accent}` 当正文色或配白字，对比度不足。
- 首屏不要超过 8 格；格子太少（少于 5）会露出空洞，说明不该用本风格。

## Chinese Typography

- 中文正文行高 1.75，标签可降到 1.5，但不低于 1.5。
- 中西文之间留四分之一个空格：`12 个模块`、`用 Inter`。
- 使用全角标点，段落不首行缩进，启用避头尾。
- 中文标题字距不小于 −0.03em；正文不做负字距。
- 中文只有 400 与 700 两档有效字重，不强行模拟 500／600。
- 64px 展示标题用于中文时降到 48px，避免字面撑破 4 列宽的大格。
- 卡片内的大数字用等宽数字（`font-variant-numeric: tabular-nums`），中文单位另起一个标签。

## When to Use

**用**：产品功能总览、发布会规格墙、SaaS 落地页、作品集首屏、App 仪表盘首页、设置项总览、需要一屏并列多个同级能力的页面。

**别用**：长表单与密集数据表、必须线性阅读的流程、少于五格的内容、长篇散文与论文、金融医疗政务等需要严肃权威气质的场景、打印为主的单栏文档。

## Iteration Guide

1. 一次只改一个格子，用 `{components.card}` 指代它。
2. 所有值走设计 token，不要内联十六进制。
3. 需要更强调时先增大一档跨度或换一次填色，最后才考虑加新颜色。
4. 加格前先问：它能不能用 1×1 加一个数字表达。不能，再谈别的形式。

## Known Gaps

- 只覆盖浅色一屏总览；深色变体、超过 8 格的长页与复杂表单未定义。
- Plus Jakarta Sans 不含中文，中文标题气质依赖 PingFang SC 回退，需真机复核。
- 主色 #4F46E5 是对来源 #6366F1 的对比度修正，不是来源原值；与严格照抄趋势指南的页面会有色差。
- 格子跨度的语义（面积=优先级）在含表单的页面上可能与阅读顺序冲突，这类场景需回到 swiss-grid 之类的线性风格。
