---version: alpha
name: Gallery Wall｜展陈画廊
description: >-
  让作品而不是界面成为主角的展陈系统。12 列网格、24px 槽沟、64px 轻字重大标题，
  作品图不加卡片投影；唯一红色只负责行动。参数提炼自 The Broad 与 Awwwards 的展陈页面，
  中文字体回退与正文行高由本库补齐。
cues: 艺术展览、博物馆与画廊、摄影作品集、艺术家档案、拍卖目录、文化机构官网、图片主导的作品展示
avoid: 高密度后台、长文正文、复杂表单、促销电商、数据看板、以操作为主的工具界面
surface: light
density: roomy
register: story
family: gallery
tier: variant
status: beta

colors:
  canvas: "#F3F3F0"
  surface: "#FAFAF7"
  ink: "#333F48"
  ink-muted: "#596574"
  ink-faint: "#747B82"
  hairline: "#D6D8D5"
  primary: "#D6001C"
  primary-soft: "#F3D9DC"
  on-primary: "#FAFAF7"
typography:
  display:
    fontFamily: "Inter Tight, Arial, PingFang SC, sans-serif"
    fontSize: 64px
    fontWeight: 300
    lineHeight: 1
    letterSpacing: -0.02em
  headline:
    fontFamily: "Inter Tight, Arial, PingFang SC, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.01em
  body:
    fontFamily: "Inter Tight, Arial, PingFang SC, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.75
    letterSpacing: 0
  label:
    fontFamily: "Inter Tight, Arial, PingFang SC, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0.02em
rounded:
  none: 0px
  sm: 2px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  gutter: 24px
  lg: 48px
  xl: 64px
  section: 96px
  measure: 36em
components:
  card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 0px 0px 16px
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: 12px 24px
  tag:
    backgroundColor: "{colors.primary-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"

elevation:
  lightSource: top-left
  steps: 3
  e1: "0 1px 2px rgba(15,23,42,0.06)"
  e2: "0 4px 12px rgba(15,23,42,0.10)"
  e3: "0 12px 32px rgba(15,23,42,0.14)"
  topHighlight: "inset 0 1px 0 rgba(255,255,255,0.60)"
  borderLight: "{colors.hairline}"
  borderDark: "{colors.ink-faint}"
  separator: shadow
media:
  logoType: wordmark
  logoRule: "字标沿用显示字族，右侧留 0.5em；图形标只用单色 {colors.ink}，最小 24px"
  imageRadius: "{rounded.sm}"
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
  focusRing: "3px solid {colors.primary}，offset 2px，不被圆角裁切"
  openTransition: "scaleY 0→1，transform-origin top，120ms"
  reducedMotion: "全部过渡降到 1ms，去掉位移"
  dragUsesSpring: false
---
## Overview

给展览、藏品、摄影作品和艺术家档案用。页面首先是一面墙，其次才是一组控件；作品图、标题和展签是主角，导航与按钮退到边缘。它不适合把大量操作塞进一屏。

性格来自四个具体选择：12 列网格配 24px 槽沟；64px／300 的展示标题与 12px 展签形成尺度差；作品图保持直角且无投影；行动色只有 `{colors.primary}`。层级由图片面积、位置和留白表达，而不是靠一堆卡片。

这份规范吸收 The Broad 的机构化无衬线、红色行动点和作品优先策略，也吸收 Awwwards 的超大轻字重标题与全幅图像。它不是任一品牌的复刻；中文排版和可访问性参数由本库重定。

**Key Characteristics**

- 画布 `{colors.canvas}`：带少量暖灰，避免纯白抢走作品的亮度层次。
- 唯一行动色 `{colors.primary}`：只用于主按钮、当前展期和关键链接。
- 单一无衬线家族：标题靠字号与字重，不靠换字体制造气氛。
- 4px 基础网格，区段间距跳到 64／96px；展项内部保持 8／16／24px。
- 图像与卡片直角；只允许展签使用 2px 小圆角。
- 不使用装饰阴影，作品之间靠槽沟和基线对齐。

## Colors

**Canvas & Surface**

- `{colors.canvas}` — #F3F3F0，页面与作品之间的“墙”。
- `{colors.surface}` — #FAFAF7，只用于必须独立于画布的说明板，不作为每张图片的默认底色。

**Ink & Line**

- `{colors.ink}` — #333F48，标题与正文；冷灰墨色与中性作品兼容。
- `{colors.ink-muted}` — #596574，展签、日期与次要说明。
- `{colors.ink-faint}` — #747B82，只用于不承载关键信息的编号。
- `{colors.hairline}` — #D6D8D5，分隔展区，不框住每件作品。

**Accent**

- `{colors.primary}` — #D6001C，每屏最多一个红色主行动。
- `{colors.primary-soft}` — #F3D9DC，只作展期标签底，不作大色块。
- `{colors.on-primary}` — #FAFAF7，红色按钮上的文字。

## Typography

展示标题 64px／300，展区标题 32px／600，正文 16px／400，展签 12px／500。只用 300、400、500、600 四档；不用超粗标题压过作品。

英文可用 Inter Tight；中文回退到 PingFang SC 或 Noto Sans SC。中文展示标题不沿用 64px 的极端压缩感，可降到 48px，但仍是 300／400，不改成粗黑体。

## Layout

- 桌面最大内容宽 1440px，12 列，24px 槽沟；768px 以下降为 4 列，槽沟 16px。
- 首页首屏优先一个主作品或一个展览，不做三列等宽营销卡。
- 作品列表允许 2:1、1:1、1:2 的跨列组合，但同一行底边或图注基线必须对齐。
- 图注与图片间距 8px；作品之间至少 24px；展区之间 64 或 96px。
- 正文说明最大 `{spacing.measure}`；不为了填满墙而拉长文本。

## Elevation & Depth

默认无阴影。图片、文字和墙之间的关系由网格与留白表达。只有悬浮导览或购票抽屉可使用 `0 13px 20px rgba(20,24,28,0.10)`，且不能投在作品图上。

## Shapes

作品、主按钮、信息面板全部 `{rounded.none}`。2px 只用于小型状态标签。禁止 pill 按钮、圆形图片和带厚边框的“相框卡片”。

## Components

### card

`{components.card}` 是作品与展签的组合，不是带阴影的容器。图片先于标题，展签包含作品名、作者、年份三项；不要在图上叠加多层文字。

### button-primary

`{components.button-primary}` 只承担“预约参观／查看展览”这类主动作。次按钮用透明底和 1px `{colors.ink}` 描边，尺寸保持一致。

### tag

`{components.tag}` 只表达“展出中／已结束／馆藏”等事实。标签不是标题前的装饰序言。

## Do's and Don'ts

### Do

- 先确定作品图的面积与节奏，再放导航和文字。
- 给每件作品保留可读展签和替代文本。
- 让红色只出现在真正可执行或当前状态的位置。
- 移动端按作品顺序堆叠，保留图注，不裁掉作品主体。

### Don't

- 不要把作品装进三张等宽、图标在上的营销卡片。
- 不要用渐变、玻璃模糊或厚投影遮盖作品。
- 不要给每张图加不同颜色的标签。
- 不要把展陈页改成高密度商品瀑布流。

## Chinese Typography

- 中文正文行高 1.75；展签可降到 1.5，但不低于 1.5。
- 中西文之间留四分之一空格；年份、尺寸与媒介分行写，不用连续中点拼接。
- 使用全角标点，段落不首行缩进；启用避头尾。
- 中文标题字距不小于 −0.01em；正文不做负字距。
- 中文引号使用“”，不要用直引号模拟海报警示。

## When to Use

**用**：展览首页、线上展厅、摄影集、艺术家档案、拍卖图录、文化机构项目页。

**别用**：新闻流、管理后台、密集表单、数据比较、促销货架、长篇技术文档。

## Iteration Guide

1. 先改作品网格与图片比例，再改标题；不要先加装饰。
2. 若层级不够，优先增加留白或调整图片跨列，不加阴影。
3. 新颜色只能是作品本身的颜色，界面仍保持单色行动点。
4. 每次修改后检查移动端图注和键盘焦点。

## Known Gaps

- 目前没有藏品筛选、拍卖出价和复杂购票流程的组件约束。
- Inter Tight 不包含中文；中文标题的实际气质依赖系统字体，需要真机复核。
- 响应式规则只覆盖 12 列到 4 列，尚未验证超宽屏与横屏平板。
- 这是二手设计分析的提炼，所有参数已重新适配，不能声称是 The Broad 或 Awwwards 官方规范。


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
