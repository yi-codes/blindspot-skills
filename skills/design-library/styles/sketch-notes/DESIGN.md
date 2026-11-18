---version: alpha
name: Sketch Notes｜手绘笔记
description: >-
  面向解释、教学和工作坊的纸上草图风格。不规则双描边、20px 笔记字号、
  一处荧光笔标记，让内容显得是“正在解释”而不是正式规范。不规则圆角、配色和投影
  提炼自 PaperCSS；图形生成建议来自 Rough.js；中文正文回退由本库补齐。
cues: 教学解释、工作坊、知识卡片、概念图解、儿童教育、轻量 onboarding、创意原型、个人学习笔记
avoid: 法律与合同、金融医疗、正式企业后台、精密数据表、长文出版、需要严肃权威的安全流程
surface: light
density: medium
register: technical
family: illustration
tier: variant
status: beta

colors:
  canvas: "#F7F3E8"
  surface: "#FFFCF5"
  ink: "#343331"
  ink-muted: "#62666A"
  ink-faint: "#777C7A"
  hairline: "#B9B3A7"
  primary: "#0B74D5"
  primary-soft: "#E2EEF7"
  highlight: "#DDCD45"
  on-primary: "#FFFCF5"
typography:
  display:
    fontFamily: "Patrick Hand SC, Noto Sans SC, sans-serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  headline:
    fontFamily: "Patrick Hand SC, Noto Sans SC, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  body:
    fontFamily: "Neucha, PingFang SC, Noto Sans SC, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.75
    letterSpacing: 0
  label:
    fontFamily: "Neucha, PingFang SC, Noto Sans SC, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
rounded:
  card: "255px 15px 225px 15px / 15px 225px 15px 255px"
  button: "15px 225px 15px 255px / 225px 15px 255px 15px"
  tag: "20px 115px 20px 105px / 15px 105px 25px 80px"
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  section: 48px
  measure: 34em
components:
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: 24px
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.button}"
    padding: 12px 24px
  tag:
    backgroundColor: "{colors.primary-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.tag}"

elevation:
  lightSource: top-left
  steps: 3
  e1: "0 1px 2px rgba(15,23,42,0.06)"
  e2: "0 4px 12px rgba(15,23,42,0.10)"
  e3: "0 12px 32px rgba(15,23,42,0.14)"
  topHighlight: "inset 0 1px 0 rgba(255,255,255,0.60)"
  borderLight: "{colors.hairline}"
  borderDark: "{colors.ink-faint}"
  separator: border
media:
  logoType: wordmark
  logoRule: "字标沿用显示字族，右侧留 0.5em；图形标只用单色 {colors.ink}，最小 24px"
  imageRadius: "{rounded.card}"
  imageRatio: "16:10"
  imageTreatment: "去饱和 6%，不加投影；与底色相接处用 1px 描边收口"
  background: "纯色 {colors.canvas}，无纹理、无氛围渐变"
  iconRule: "1.6px 描边，20px 基准，与正文同色，不使用彩色图标"
  emptyState: "淡底 + 一行说明文字，不放装饰插画和大号图标"
motion:
  easing: "cubic-bezier(0.2, 0.8, 0.2, 1)"
  durationFast: 120ms
  durationBase: 200ms
  hover: "背景升一档明度，位移 0；有阴影时抬高一级"
  focusRing: "3px solid {colors.primary}，offset 2px，不被圆角裁切"
  openTransition: "scaleY 0→1，transform-origin top，120ms"
  reducedMotion: "全部过渡降到 1ms，去掉位移"
  dragUsesSpring: false
---
## Overview

给教学、概念解释、工作坊、学习笔记和轻量 onboarding 用。它传达的是“我画给你看”，不是“这是定稿规范”。适合允许涂改、箭头和批注的内容，不适合合同、支付和精密参数。

不规则圆角直接来自 PaperCSS 的双轴半径组合，而不是随手旋转卡片。正文使用 18px／1.75；蓝色 `{colors.primary}` 只用于动作与箭头，黄色 `{colors.highlight}` 只作局部荧光笔标记。层级靠 2px 墨线和轻微错位投影。

PaperCSS 提供可复现的组件形状、色彩和阴影；Rough.js 提供图形侧的 roughness、bowing、hachure 等参数。手写字体没有可靠中文字形，所以中文必须回退到清晰无衬线，不能假装手写。

**Key Characteristics**

- `{colors.canvas}` 暖纸底与 `{colors.surface}` 纸片形成很小明度差。
- 2px 墨色边线，卡片使用不规则双轴圆角；页面内容本身不旋转。
- 正文 18px，比常规工具界面大；每行 34em 以内。
- 蓝色只用于动作，黄色只用于少量标记，不做多色荧光笔大杂烩。
- 投影使用 PaperCSS 的小幅负 spread，不用悬浮玻璃效果。

## Colors

- `{colors.canvas}` — #F7F3E8，笔记本纸面。
- `{colors.surface}` — #FFFCF5，卡片与可交互纸片。
- `{colors.ink}` — #343331，铅笔／钢笔的主墨色。
- `{colors.ink-muted}` — #62666A，解释文字。
- `{colors.ink-faint}` — #777C7A，页码与非关键批注。
- `{colors.hairline}` — #B9B3A7，次要草线和表格。
- `{colors.primary}` — #0B74D5，来自 PaperCSS 的动作蓝。
- `{colors.primary-soft}` — #E2EEF7，选中与提示底。
- `{colors.highlight}` — #DDCD45，荧光笔黄；每屏最多标记一处。
- `{colors.on-primary}` — #FFFCF5，蓝底按钮文字。

## Typography

英文标题可用 Patrick Hand SC，正文可用 Neucha；中文一律回退 Noto Sans SC／PingFang SC。字号 16／18／24／28／40，中文正文不小於 18px，行高 1.75。

手写字体只用 400，不靠伪造粗体。标题不倾斜、不加随机字距；手绘感由线条和插图承担，不能牺牲文字识别。

## Layout

- 内容宽 960px，解释页以“文字 + 草图”两列为主，比例 5:7 或 7:5。
- 间距 4／8／16／24／32／48；同组批注靠近对应内容，不做三列等宽卡片。
- 正文最大 `{spacing.measure}`；箭头、圈注可以越出卡片，但不能覆盖文字。
- 768px 以下先文字后图，所有越界批注回到文档流。
- 图形若用 Rough.js，固定 seed；建议 roughness 1.3、bowing 1.2、strokeWidth 1.6，避免每次构建改变图形。

## Elevation & Depth

卡片用 `10px 19px 17px -13px rgba(0,0,0,0.20)`，按钮 hover 用 `2px 8px 8px -5px rgba(0,0,0,0.30)`。两者都来自 PaperCSS；禁止额外叠加柔光和悬浮大阴影。

## Shapes

只允许 front matter 的三组不规则半径，分别对应 card、button、tag。不要给容器再旋转随机角度；不要用 pill 代替手绘形状。图像和图表边线可通过 Rough.js 生成双描边。

## Components

### card

`{components.card}` 是一张可写的纸，不是立体商品卡。标题、解释、图注和一处批注足够，不在里面堆多个操作。

### button-primary

`{components.button-primary}` 使用蓝底和手绘边线。按下仅下移 2px，保持文字不抖动；焦点轮廓不能被不规则边框吞掉。

### tag

`{components.tag}` 表达步骤、难度或媒介等事实。黄色荧光笔另用 `.ds-highlight`，不要把所有标签都变黄。

## Do's and Don'ts

### Do

- 让草图真正解释一个概念或步骤。
- 固定随机种子，确保同一页面重渲染一致。
- 用清晰中文无衬线承载所有关键文字。
- 保留正常焦点、错误文字和移动端阅读顺序。

### Don't

- 不要旋转整段正文或给每个元素随机抖动。
- 不要用黄色小字承担关键说明。
- 不要把正式错误、支付和安全确认做成玩笑式草稿。
- 不要混用多套不规则边框或同时加入多种手写字体。

## Chinese Typography

- 中文正文使用 18px／1.75 的 PingFang SC／Noto Sans SC，不强用 Neucha。
- 中文标题 28–40px／400，字距 0；避免用伪造斜体。
- 中西文之间留四分之一空格，步骤编号单独占位。
- 使用全角标点、避头尾、不首行缩进；批注可用中文引号“”。
- 中文不使用全大写宽字距规则，重点靠 `{colors.highlight}` 的局部底色。

## When to Use

**用**：课程、概念解释、教学卡片、白板图解、学习笔记、创意工作坊、轻量引导。

**别用**：正式合同、医疗金融、关键安全操作、精密数据、企业后台、长篇正式出版物。

## Iteration Guide

1. 先验证文字和图形是否更易懂，再增加手绘细节。
2. 太乱时先去掉批注和黄色标记，不缩小正文。
3. 图形抖动过强时降低 Rough.js 的 roughness／bowing，不动文字。
4. 修改 `{components.card}` 后检查焦点、错误态和中文回退字体。

## Known Gaps

- tokens.css 只提供近似纸面组件；真正的手绘 SVG 需要 Rough.js 或预生成资源。
- PaperCSS 手写字体不覆盖中文，英文与中文灰度会有差异。
- 未定义复杂表单、数据表和企业级错误流程。
- 不规则边框可能放大点击区域外的视觉空白，需要实际触摸设备复核。


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
