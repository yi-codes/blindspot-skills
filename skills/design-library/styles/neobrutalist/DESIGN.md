---version: alpha
name: Neobrutalist
description: >-
  新粗野。2px 实黑边、4px 零模糊硬阴影、5px 圆角、浅蓝底。
  悬停时元素整体平移进自己的阴影里，像一块被按下去的纸板。
  没有渐变、没有模糊、没有半透明，所有东西都是实心的。
# ---------------------------------------------------------------- 选择条件
family: expressive
tier: core
sourceRefs: neobrutalism
cues: 作品集、活动页、创意工具、需要"有态度"的产品官网、年轻用户、独立产品
avoid: 金融/医疗/政务、长文阅读、需要效率感的工具界面、企业后台
surface: light
density: medium
register: story

colors:
  canvas: "#DCEBFE"
  surface: "#FFFFFF"
  ink: "#000000"
  main: "#5294FF"
  chart-1: "#5294FF"
  chart-2: "#FF4D50"
  chart-3: "#FACC00"
  chart-4: "#05E17A"
  chart-5: "#7A83FF"

typography:
  headline-lg:
    fontFamily: "DM Sans, Noto Sans SC, PingFang SC, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-md:
    fontFamily: "DM Sans, Noto Sans SC, PingFang SC, system-ui, sans-serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.02em
  headline-sm:
    fontFamily: "DM Sans, Noto Sans SC, PingFang SC, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.02em
  body-md:
    fontFamily: "DM Sans, Noto Sans SC, PingFang SC, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "DM Sans, Noto Sans SC, PingFang SC, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.55
    letterSpacing: 0
  label-md:
    fontFamily: "DM Sans, Noto Sans SC, PingFang SC, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0

rounded:
  base: 5px
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
  measure: 38em

components:
  button:
    backgroundColor: "{colors.main}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.base}"
    height: 40px
    padding: 0 16px
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.base}"
    padding: 24px
  field:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.base}"
    height: 40px
    padding: 0 12px
  tag:
    backgroundColor: "{colors.chart-3}"
    textColor: "{colors.ink}"
    typography: "{typography.label-md}"
    rounded: "{rounded.base}"
    padding: 4px 8px
  dialog:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.base}"
    width: 440px
    padding: 24px

elevation:
  lightSource: top-left
  steps: 3
  e1: "0 1px 2px rgba(15,23,42,0.06)"
  e2: "0 4px 12px rgba(15,23,42,0.10)"
  e3: "0 12px 32px rgba(15,23,42,0.14)"
  topHighlight: "inset 0 1px 0 rgba(255,255,255,0.60)"
  borderLight: "{colors.surface}"
  borderDark: "{colors.canvas}"
  separator: shadow
media:
  logoType: wordmark
  logoRule: "字标沿用显示字族，右侧留 0.5em；图形标只用单色 {colors.ink}，最小 24px"
  imageRadius: "{rounded.base}"
  imageRatio: "4:3"
  imageTreatment: "去饱和 6%，不加投影；与底色相接处用 1px 描边收口"
  background: "纯色 {colors.canvas}，无纹理、无氛围渐变"
  iconRule: "1.6px 描边，20px 基准，与正文同色，不使用彩色图标"
  emptyState: "淡底 + 一行说明文字，不放装饰插画和大号图标"
motion:
  easing: "cubic-bezier(0.2, 0.8, 0.2, 1)"
  durationFast: 120ms
  durationBase: 200ms
  hover: "背景升一档明度，位移 0；有阴影时抬高一级"
  focusRing: "3px solid {colors.main}，offset 2px，不被圆角裁切"
  openTransition: "scaleY 0→1，transform-origin top，120ms"
  reducedMotion: "全部过渡降到 1ms，去掉位移"
  dragUsesSpring: false
---
## Overview

Neobrutalist 是从**网页的粗野主义**（brutalist web）进化来的一支：它接受了粗野主义"不假装"的态度，但把"难看"换成了"有力"。

具体到实现上，它只做三件事，而且三件事都做到极端：

1. **所有边界都是 2px 实黑线。** 不是 1px 灰线，不是 `rgba(0,0,0,.08)`。边界必须被看见，因为这套界面的可信感来自"每一块都分得清"。
2. **所有阴影都是 4px 位移、0 模糊的实色块。** 阴影不是模拟光，是一块真的偏移的纸板。所以悬停时元素会**平移进自己的阴影里**，阴影消失——它在物理上被按下去了。
3. **所有颜色都是实心的。** 没有渐变、没有模糊、没有半透明叠色。图表五色（蓝、红、黄、绿、紫）全部是原色相，不降饱和。

这套风格的原始素材是 `neobrutalism-components`（5.6k★，一个把 neobrutalism 做成 shadcn 组件库的项目）。圆角 5px、2px 边、4px 阴影、正文 500 字重这些值都是照抄的，包括那个"悬停平移"的交互。

**Key Characteristics**

- 浅蓝画布 `{colors.canvas}`（#DCEBFE）+ 白纸板块 `{colors.surface}` + 纯黑边线 `{colors.ink}`。
- **圆角只有一个值**：5px `{rounded.base}`。不是 4、不是 6、不是 8。
- **正文 500 字重** `{typography.body-md}`，不是 400。这是这套风格最容易被抄错的一条——粗体正文是必要的，因为 2px 黑边的重量需要更沉的笔画来配。
- **阴影零模糊**：`4px 4px 0 0` 黑。模糊半径一出现，粗野感立刻消失。
- **悬停 = 平移进阴影**，不是变色、不是变亮。
- 动效 100ms、`linear`。**不用缓动曲线**——这套风格要的是硬切，不是顺滑。
- 图表五色是原色相：蓝 #5294FF / 红 #FF4D50 / 黄 #FACC00 / 绿 #05E17A / 紫 #7A83FF。

## Colors

这套颜色不讲克制，讲**分明**。每一块颜色都必须能被一眼指认为"那一块"。

### Canvas & Surface

- **Canvas** (`{colors.canvas}` — #DCEBFE): 页面底。浅蓝，`hsl(214 95% 93%)`。用浅蓝而不是米黄/浅灰，是为了让白色的卡板能"跳"出来——这是这套风格的层次手段。
- **Surface** (`{colors.surface}` — #FFFFFF): 卡片、按钮底、表格底。纯白是故意的：它要像一张没印刷的纸板。

### Ink

- **Ink** (`{colors.ink}` — #000000): 文字与所有边线。**这里用纯黑是对的**，理由见下面「对 Floor 规则 2 的豁免」。
- **弱化文字**：没有第二级灰。需要弱化时用 `rgba(0,0,0,0.65)`，或者干脆靠字号变小。引入一个"灰色文字"会立刻破坏这套风格的硬边。

### Main

- **Main** (`{colors.main}` — #5294FF): 主按钮底。**注意它是配黑字的**，不是白字——白字在这个蓝上只有 2.98:1，黑字是 7.05:1。这是原项目的原样做法（`--main-foreground: oklch(0% 0 0)`）。

### 图表五色

`{colors.chart-1}` / `{colors.chart-2}` / `{colors.chart-3}` / `{colors.chart-4}` / `{colors.chart-5}`。

这一整套是原样搬的，**顺序也没动**。它们的存在说明了一个立场：这套风格不认为"多色 = 乱"。它认为多色是好的，前提是每个色都是实心原色、并且都被黑边圈住。

### 对 Floor 规则 2 的豁免（留痕）

`principles.md` 的 Floor 规则 2 说「浅色底不许大面积 #fff」。这个风格在白卡片的面积上接近违规，而且正文是纯黑 #000。

理由：**粗野主义的全部表达就是"不调制"**。把黑调成 #0B0C0C、把白调成 #FAFAFA，这套风格就变成了"柔和的卡片式设计"——那是另一个风格（是 `swiss-grid`，甚至是 `quiet-dark` 的浅色版）。这里的纯黑纯白不是偷懒，是这套风格唯一诚实的做法。

范围限定：**纯黑只用于文字和 2px 边线，纯白只用于卡板底**。不做整屏纯白、不做整屏纯黑。

## Typography

**DM Sans** 是原项目的正文字体，几何无衬线、字腔大方、在粗字重下不糊。中文退到 PingFang SC。

字号：12 / 14 / 16 / 20 / 24 / 30 / 48。

**字重只有 500 和 700 两档，而且正文是 500。** 这是最容易抄错的地方：

- 用 400 做正文，2px 黑边会显得"边框比字重"——视觉上字被框压住了。
- 用 700 做正文，就分不出标题了。
- 500 是唯一能跟 2px 线条平分秋色的字重。

标题字距 `-0.02em`。DM Sans 在大字号下字距偏松，收一点才能聚成块——这套风格的标题要像印上去的色块，不是排出来的句子。

## Layout

- 版心 `{spacing.measure}` 1300px。宽，因为这套风格的页面通常是"几块大板子并排"。
- 间距：4 / 8 / 12 / 16 / 24 / 32 / 48。
- **块与块之间靠阴影的 4px 拉开，不靠留白。** 这是关键：这套风格的"呼吸"来自阴影投出的那 4px 黑边，不是来自 48px 的空白。所以它可以在很窄的间距下依然分得清。

## Elevation & Depth

**只有一层深度，而且是假的。**

`4px 4px 0 0` 的黑色实块 —— 它不是阴影，是一块偏移的色块。所以：

- **模糊半径恒为 0。** 一旦有模糊，它就从"纸板"变成"投影"，整套语言的物理逻辑崩了。
- **阴影方向恒为右下。** 不随光源变，因为这里没有光源。
- **悬停时元素平移到阴影的位置、阴影消失。** 这是唯一允许的"动"，它表达的是"被按下去"。
- 对话框用 8px（双倍）阴影，因为它"更厚"。

## Shapes

**圆角 5px，一个值。** 加 `{rounded.full}` 用于头像和开关这类必须是圆的东西。

5px 是个奇怪的值：它比 0 软，比 8 硬。这个尺寸刚好让 2px 的直角转弯处不显得"割手"，又不会让矩形变成"胶囊"。

线宽只有 **2px**。不用 1px（在浅蓝底上像铅笔线），不用 3px（会抢字）。

## Components

### button

`{colors.main}` 底 + **黑字** + 2px 黑边 + 5px 圆角 + 4px 硬阴影。高度 40px，左右内边距 16px。

悬停：`translate(4px, 4px)` + `box-shadow: none`。按钮整体移到阴影原来的位置。
按下：平移 2px，阴影缩到 2px。
禁用：透明度 50%，不平移。

**这三个状态是一条连续的物理叙事**：纸板浮着 → 被按下去 → 按到底 → 不能按。不要改成变色。

### card

白底 + 2px 黑边 + 5px 圆角 + 4px 硬阴影 + 24px 内边距。

可点的卡片用同一个交互（平移到阴影位置）。不可点的卡片**不动**——动的东西一定是能点的。

### field

白底 + 2px 黑边 + 5px 圆角 + 4px 硬阴影，高 40px，左右 12px。

聚焦时**不移除阴影**，而是在阴影外面加一圈 2px 白 + 2px 黑的环。这样"纸板"还在，只是多了一圈聚焦标记。
错误时**阴影变红**（`{colors.chart-2}` 的 4px 实块），边线也变红。

### tag

实色块（默认黄 `{colors.chart-3}`）+ 2px 黑边 + 12px 700 字重 + 4px/8px 内边距。

**不透明、不淡、不加圆角超过 5px。** 标签在这套风格里是一个"贴纸"，不是一个"提示"。

### table

2px 外框 + 行间 2px 黑线 + 表头浅蓝底。**不用斑马纹**——斑马纹是柔和的替代品，这里不需要柔和。

### dialog

白底 + 2px 黑边 + **8px 硬阴影**（比卡片厚一倍）+ 遮罩 `rgba(0,0,0,0.8)`（0.8 是原值，比常见的 0.5 重得多，因为这套风格的遮罩要真的把后面压暗）。

## Do's and Don'ts

### Do

- 所有边界 2px 实黑。所有阴影 4px 零模糊。
- 圆角只有 5px 和全圆两个值。
- 正文 500 字重。不是 400。
- 悬停让元素平移进阴影，不要变色。
- 主色配黑字（#5294FF 上白字只有 2.98:1）。
- 图表用原色相，不降饱和。
- 动效 100ms、linear。硬切。
- 块与块靠阴影分开，不靠大留白。

### Don't

- 不要给阴影加模糊。一处都不要。
- 不要用渐变、半透明叠色、毛玻璃。
- 不要引入第二级灰色文字。
- 不要让主按钮配白字。
- 不要用 1px 边框（太细）或 3px 以上（抢字）。
- 不要用缓动曲线（`ease`、`cubic-bezier`）。这个风格要硬切。
- 不要用斑马纹表格。
- 不要做"柔和的卡片式设计"——那是别的风格。

## Chinese Typography

- **中文需要降一档字号**。DM Sans 16px 的观感接近中文 17-18px，所以 `{typography.body-md}` 的 16px 用在中文上会偏大。建议中文正文字号用 15px，或接受 16 但把行高从 1.55 提到 1.65。
- **中文不要用 `letter-spacing: -0.02em`**。汉字是满方块，负字距会压笔画。标题的负字距只对拉丁有效，中文要写回 0。
- **500 字重对中文是可用的**：PingFang SC 有 Medium（500），渲染稳定。这一点比拉丁更幸运——很多中文字体只有 400 和 700。
- **2px 边框对中文有利**：汉字笔画密，边框粗一点才不会被字的重量压住。这是这套风格少见地"对中文更友好"的地方。
- **不要给中文加 `text-transform: uppercase`**：无效，只会把混排的拉丁拉宽。
- **标签里的中文不需要加宽字距**：短标签加字距在中文里读起来像"逐字念"。

## When to Use

**用**：独立产品官网、创意工具落地页、作品集、活动页、面向年轻用户的产品、需要"这个团队有态度"的第一印象。

**别用**：金融、医疗、政务（轻浮）、长文阅读（密度和对比度都不适合）、需要效率感的工具界面（阴影和平移会增加认知负担）、企业后台。

## Iteration Guide

1. 加任何元素前先问：它有边界吗？没有边界的东西在这套风格里不存在。
2. 边界 2px、阴影 4px、圆角 5px。三个值是固定的。
3. 颜色从五色图表里选，不要调出新色相。
4. 需要强调时：先加粗，再用色块，最后才考虑加粗边框。
5. 每个可交互元素都要有"浮着 → 按下"这两个状态。

## Known Gaps

- **DM Sans 需要自托管或走 Google Fonts**，离线环境会退到系统无衬线，几何感会掉一半。
- 没有定义暗色版。粗野主义的暗色版很容易变成"霓虹赛博"，那不是同一套语言，所以暂不做。
- 没有定义移动端。1300px 版心和小屏的适配需要重排成单列，规则未写。
- 没有定义表单校验的错误文案层级（只有红色阴影，没有错误文字样式）。
- 没有定义空状态和加载态。
- 图表五色里有三个（红 #FF4D50、黄 #FACC00、绿 #05E17A）**对白底对比度不足 3:1**，只能做填充块、不能做文字。要用它们做文字时必须配黑边。
- 生图侧说明在 `prompt.md`——这套风格的配图应该像"印刷品"，不像照片。


## Material & Elevation

光从 `{elevation.lightSource}` 来，固定这一个方位。共 `{elevation.steps}` 级：
`{elevation.e1}` 贴面、`{elevation.e2}` 卡片、`{elevation.e3}` 浮层。
深色上层级靠明度与内描边，浅色上靠带偏移的阴影——不做居中发光。
主分隔手段是 `{elevation.separator}`，其余只做辅助。

## Mark & Media

标识：`{media.logoRule}`（`{media.logoType}`）。
图片：比例 `{media.imageRatio}`、圆角 `{media.imageRadius}`、处理 `{media.imageTreatment}`。
背景：`{media.background}`。图标：`{media.iconRule}`。空态：`{media.emptyState}`。
只写规则不写品牌资产；图片处理都是可复现参数。

## Motion & States

过渡曲线 `{motion.easing}`，快档 `{motion.durationFast}`、基准 `{motion.durationBase}`。
hover：`{motion.hover}`；焦点：`{motion.focusRing}`；展开：`{motion.openTransition}`。
交互组件逐项覆盖 default / hover / focus-visible / active / disabled / error 六态。
`prefers-reduced-motion` 时 `{motion.reducedMotion}`。
