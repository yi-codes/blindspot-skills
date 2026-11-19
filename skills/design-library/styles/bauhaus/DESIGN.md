---
version: alpha
name: Bauhaus Grid｜包豪斯几何
description: >-
  用三原色、圆方三角与不对称网格做构图的海报式页面。几何形状是结构而不是贴纸：
  大红方块压住一屏的视觉重心，蓝圆与黄三角负责次级节奏，2px 黑色实线把网格显出来。
  参数提炼自 aesthetic.fyi、vocab.design 与 stellae.design 的 Bauhaus 分析；
  暖纸底色、对比度与中文排版由本库补齐。
cues: 设计工作室与建筑事务所作品集、文化机构与美术馆页面、字体展示与设计教育、品牌发布与主视觉页、需要强烈设计主张的落地页
avoid: 大目录电商、内容密集型新闻与博客、高密度后台与表单、需要温暖亲和的消费产品、金融医疗与政务、多人协作的复杂工具界面
surface: light
density: roomy
register: story
family: expressive
tier: variant
sourceRefs: bauhaus
status: beta

colors:
  canvas: "#F4F0E6"
  surface: "#FBF8F0"
  ink: "#1A1A1A"
  ink-muted: "#5A5852"
  ink-faint: "#7C796F"
  hairline: "#CFC8B8"
  primary: "#D40000"
  secondary: "#003DA5"
  accent: "#FFD500"
  on-primary: "#FBF8F0"
typography:
  display:
    fontFamily: "DM Sans, Futura, PingFang SC, sans-serif"
    fontSize: 80px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: -0.04em
  headline:
    fontFamily: "DM Sans, Futura, PingFang SC, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.02em
  cardTitle:
    fontFamily: "DM Sans, Futura, PingFang SC, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.01em
  body:
    fontFamily: "Inter, PingFang SC, Noto Sans SC, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.75
    letterSpacing: 0
  label:
    fontFamily: "DM Sans, Futura, PingFang SC, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0.08em
rounded:
  none: 0px
  circle: 50%
spacing:
  base: 8px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  section: 96px
  measure: 36em
components:
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 24px
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: 16px 40px
  tag:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: 8px 16px
elevation:
  lightSource: top-left
  steps: 1
  e1: "none，层级靠 2px 实线与色块面积"
  e2: "none，不用投影表达浮起"
  e3: "none，弹层用实线边框与底色差"
  topHighlight: "none，没有高光与内描边"
  borderLight: "{colors.hairline}"
  borderDark: "{colors.ink}"
  separator: border
media:
  logoType: combo
  logoRule: "字标用 {typography.headline} 700，左侧先放 24px 红方块，间距 16px；方块是几何系统的一部分，不是图标"
  imageRadius: "{rounded.none}"
  imageRatio: "4:3"
  imageTreatment: "none，图像保持直角；需要收口时加 2px {colors.ink} 实线，不做混色与滤镜"
  background: "纯色 {colors.canvas} 暖纸白，无纹理、无渐变"
  iconRule: "只用圆、方、三角三种几何，2px {colors.ink} 描边，24px 基准；颜色分类旁边必须有文字标签"
  emptyState: "{colors.surface} 底 + 一个 64px {colors.secondary} 圆 + 一行说明，不放插画"
motion:
  easing: "cubic-bezier(0.2, 0, 0.2, 1)"
  durationFast: 120ms
  durationBase: 200ms
  hover: "几何形状沿对角线平移 8px，底色不变；按钮由实色翻到 {colors.ink}"
  focusRing: "3px solid {colors.secondary}，offset 2px，方形焦点框不被圆角裁切"
  openTransition: "clip-path 从 inset(0 100% 0 0) 到 inset(0 0 0 0)，200ms"
  reducedMotion: "全部过渡降到 1ms，取消位移"
  dragUsesSpring: false
---
## Overview

给作品集、建筑事务所、美术馆、字体展示和品牌发布用。页面首先是一张海报，其次才是一组控件：形状和标题先建立构图张力，正文与按钮退到网格里。它不适合承载大量并发操作或长表单。

性格来自四个具体选择：80px／700 的展示标题与 16px／400 的正文拉开极端尺度差；红 `{colors.primary}`、蓝 `{colors.secondary}`、黄 `{colors.accent}` 三色只作实色块；圆、方、三角用 `border-radius` 与 `clip-path` 做成真实布局元素；2px 黑色实线把 `{spacing.md}` 网格显出来。层级靠面积、位置和张力，不靠阴影与渐变。

这份规范吸收 aesthetic.fyi 的三原色与形状即结构、vocab.design 的形状—颜色配对与单条对角线、stellae.design 的 8px 网格与直角组件。它不是任一品牌的复刻；暖纸底色、对比度与中文排版由本库重定。

**Key Characteristics**

- 画布 `{colors.canvas}`：暖纸白而不是纯白，让三原色像印在纸上而不是发光的屏幕。
- 三原色各司其职：红负责主行动和最大色块，蓝负责次级结构与焦点，黄只用于标签与小面积三角；同屏不出现第四个彩色。
- 几何形状是结构：圆、方、三角承担分区标记、空态和视觉重心，每个形状旁边都有文字标签。
- 双字族分工：DM Sans 管标题与标签的几何感，Inter 管正文的易读性；中文回退到 PingFang SC。
- 8px 基础网格，区块间距跳到 40／64／96px；卡片内部保持 16／24px。
- 全局零圆角（唯一例外是 50% 的正圆），零阴影；层级由 2px 实线和色块面积表达。

## Colors

**Canvas & Surface**

- `{colors.canvas}` — #F4F0E6，页面底色；带暖黄调的纸白，避免纯白和三原色互相抢亮度。
- `{colors.surface}` — #FBF8F0，卡片与空态底；比画布亮一档，靠底色差而不是投影分层。
- `{colors.hairline}` — #CFC8B8，辅助细线；只用于不承载关键信息的内部分隔。

**Ink**

- `{colors.ink}` — #1A1A1A，标题、正文与 2px 主分隔线；接近黑但不取纯黑，保留纸张感。
- `{colors.ink-muted}` — #5A5852，次级说明；与画布对比度 6.25:1，可连续阅读。
- `{colors.ink-faint}` — #7C796F，编号与元信息；仅用于非关键内容。

**Primaries**

- `{colors.primary}` — #D40000，红：主按钮、最大色块、方形；对画布 4.86:1，暖纸白字按钮 5.21:1。
- `{colors.secondary}` — #003DA5，蓝：圆形、焦点环与次级结构；对画布 8.35:1。
- `{colors.accent}` — #FFD500，黄：三角与标签底；只配 `{colors.ink}` 文字，绝不当正文色。
- `{colors.on-primary}` — #FBF8F0，红色块上的文字；沿用暖纸白，不引入纯白。

## Typography

展示标题 80px／700／行高 1，章标题 32px／700，卡片标题 24px／700，正文 16px／400／行高 1.75，标签 12px／700／字距 0.08em。模数从 16 到 24 到 32 是 1.5，再跳到 80；只设这五档，不出现 18、20、28 这类中间值。

字重只有 400 和 700 两档，没有 500、600。拉丁展示用 DM Sans／Futura，正文用 Inter——几何无衬线为展示而生，正文换成开放字腔的字族；中文按各档回退到 PingFang SC。英文标题可全小写，中文标题不强行大写或加宽字距。

## Layout

- 桌面 12 列网格，槽沟 `{spacing.md}`；首屏让一个形状占 4 列以上，文字压在剩余列，靠不对称取得平衡，不做左右等分。
- 内容最大宽 1440px；正文测量宽 `{spacing.measure}`。
- 顶部导航一条 2px `{colors.ink}` 实线到底；区段之间 64 或 96px；卡片之间 24px。
- 卡片网格允许 1.6:1:1 的不等宽组合，但同一行底边必须对齐。
- 768px 以下降为 4 列，首屏形状退到文字上方，保留标签和文字说明。

## Elevation & Depth

不使用投影。共 `{elevation.steps}` 级材质：所有块都贴面（`{elevation.e1}`），卡片靠 2px `{colors.ink}` 实线与底色差浮出，弹层也只用实线边框和 `{colors.surface}` 底。光从 `{elevation.lightSource}` 来，但只体现在形状色块的落位逻辑上，不做高光。主分隔手段是 `{elevation.separator}`，细线只做辅助。

## Shapes

全局 `{rounded.none}`；唯一例外是 `{rounded.circle}` 的正圆，仅用于圆本身。三角形用 `clip-path: polygon(50% 0, 100% 100%, 0 100%)` 生成，不加圆角。禁止 pill 按钮、圆角卡片、带描边的"相框"和有机曲线；形状与文字之间至少留 `{spacing.sm}`。

## Material & Elevation

光从 `{elevation.lightSource}` 来，固定这一个方位。本风格只有 `{elevation.steps}` 级：贴面（`{elevation.e1}`）、卡片（`{elevation.e2}`）、弹层（`{elevation.e3}`）都不用投影，改用 2px 实线、底色差与色块面积。深色上靠明度与内描边，浅色上靠带偏移的阴影——这里刻意都不用，因为 Bauhaus 的层级由构图承担。主分隔手段是 `{elevation.separator}`，其余退到辅助位。

## Mark & Media

标识：`{media.logoRule}`（`{media.logoType}`）。图片：比例 `{media.imageRatio}`、圆角 `{media.imageRadius}`、处理 `{media.imageTreatment}`。背景：`{media.background}`。图标：`{media.iconRule}`。空态：`{media.emptyState}`。

只写规则不写品牌资产。圆=蓝、方=红、三角=黄是默会配对，但颜色不能单独承载含义：每个形状旁必须有文字标签，避免把红误读成错误、蓝误读成链接。

## Motion & States

过渡曲线 `{motion.easing}`，快档 `{motion.durationFast}`、基准 `{motion.durationBase}`。hover：`{motion.hover}`；焦点：`{motion.focusRing}`；展开：`{motion.openTransition}`。交互组件逐项覆盖 default / hover / focus-visible / active / disabled / error 六态。

`prefers-reduced-motion` 时 `{motion.reducedMotion}`。拖拽与手势不使用 CSS 过渡；本风格不提供拖拽组件。焦点环用方形而不是圆形，避免被几何裁切吞掉。

## Components

### card

`{components.card}` 是直角、2px 黑边的实色块，不是悬浮卡片。标题 24px／700 先于正文；卡片可以承载一个小三角形作为分类标记，但文字标签不可省略。

### button-primary

`{components.button-primary}` 是红色无圆角矩形，只承担一个主动作。次按钮用透明底和 2px `{colors.ink}` 实边，尺寸与主按钮一致；一屏最多一个红按钮。

### tag

`{components.tag}` 用黄底黑字表示事实状态，不是标题前的装饰序言。黄色面积不超过标签本身，不拿它做整块背景。

## Do's and Don'ts

### Do

- 先定构图中最大的那个形状，再排文字和按钮。
- 让红、蓝、黄各司其职，并在形状旁放文字标签。
- 用 2px 实线和面积差建立层级。
- 中文正文换成 Inter／PingFang SC 的易读字族，不用 DM Sans 排版长段。

### Don't

- 不要加投影、渐变、玻璃模糊或纹理，它们会破坏"形状即结构"的前提。
- 不要把三原色铺成四个以上色块，也不要用粉彩或二次色。
- 不要用圆角卡片或 pill 按钮，那会把海报变成通用后台。
- 不要把黄色当正文色，对比度不够；不要只靠颜色表达分类。

## Chinese Typography

- 中文正文行高 1.75，标签可降到 1.5，但不低于 1.5。
- 中西文之间留四分之一个空格：`12 个文件`、`用 DM Sans`。
- 使用全角标点，段落不首行缩进，启用避头尾。
- 中文标题字距不小于 −0.04em；正文不做负字距。
- 中文只有 400 与 700 两档有效字重，不强行模拟 500／600。
- 中文引号使用“”，不要用直引号模拟海报标语。
- 80px 展示标题用于中文时降到 64px，避免字面撑破网格。

## When to Use

**用**：设计工作室作品集、建筑与室内设计、美术馆与画廊、字体展示、设计教育、强调设计主张的品牌发布页。

**别用**：大目录电商、内容密集的新闻与博客、表格与表单密集型后台、需要温暖亲和的消费产品、金融医疗政务、复杂协作工具。

## Iteration Guide

1. 一次只改一个组件，用 `{components.card}` 指代它。
2. 所有值走设计 token，不要内联十六进制。
3. 需要更强调时先放大一级字号或增加一个形状面积，最后才考虑加新颜色。
4. 新增组件前先问：它能不能用 2px 实边 + 留白表达。不能，再谈别的。

## Known Gaps

- 只覆盖浅色海报式落地页；深色变体、复杂表单和多步流程未定义。
- DM Sans 与 Futura 不含中文，中文标题气质依赖系统字体，需真机复核。
- 红/蓝在界面里原本已被"错误/链接"占用，本风格把它们重新分配为结构色，表单与错误态需单独复核语义。
- 这是二手设计分析的提炼，所有参数已重新适配，不能声称是 Bauhaus 学校或其官方规范。
