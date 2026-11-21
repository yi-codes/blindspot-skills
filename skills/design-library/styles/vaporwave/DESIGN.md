---
version: alpha
name: Vaporwave｜蒸汽波
description: >-
  把 1980–90 年代消费电子与早期互联网的记忆做成一场慢速霓虹梦：深紫黑底上粉与青两束霓虹、
  退向地平线的透视网格、条纹落日与轻微色差 glitch。用于音乐与演出、创意作品集、游戏与活动落地页，
  追求情绪冲击而非企业式清晰。参数提炼自 designmd.app 两份 vaporwave 风格卡、designforai.dev 的
  UI prompt、stealthis.dev 的风格页与 chrislemke 设计参考页的交叉验证；标为 beta/variant，
  且为符合本库 The Floor，把来源里标志性的紫粉渐变与渐变文字改造成粉青渐变加霓虹 text-shadow。
cues: 音乐人与专辑/演出落地页、synthwave 与 retrowave 活动页、创意作品集首屏、复古游戏与 Game Jam 页面、潮流服饰与周边、需要强情绪与怀旧感的展示型界面
avoid: 企业官网与后台、表单密集的办事流程、金融医疗政务、长文阅读与论文、需要严肃权威与高信息效率的界面、打印为主的单栏文档
surface: dark
density: medium
register: story
family: retro
tier: variant
sourceRefs: vaporwave
status: beta

colors:
  canvas: "#1A0B2E"
  surface: "#2D1B4E"
  surface-alt: "#3D2566"
  ink: "#FFFBFC"
  ink-muted: "#C4B7C9"
  ink-faint: "#8B7E96"
  line: "#5B3A8C"
  line-strong: "#B967FF"
  primary: "#FF71CE"
  secondary: "#01CDFE"
  accent: "#05FFA1"
  highlight: "#FFFB96"
  on-primary: "#1A0B2E"
typography:
  display:
    fontFamily: "Orbitron, PingFang SC, sans-serif"
    fontSize: 80px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: 0.12em
  headline:
    fontFamily: "Orbitron, PingFang SC, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0.08em
  cardTitle:
    fontFamily: "Cormorant Garamond, PingFang SC, serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.02em
  body:
    fontFamily: "Space Mono, PingFang SC, Noto Sans SC, monospace"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: 0
  label:
    fontFamily: "Space Mono, PingFang SC, monospace"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0.18em
rounded:
  card: 4px
  button: 2px
  tag: 0px
spacing:
  base: 8px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 40px
  section: 64px
  measure: 36em
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
    textColor: "{colors.secondary}"
    typography: "{typography.label}"
    rounded: "{rounded.tag}"
    padding: 6px 12px
elevation:
  lightSource: top
  steps: 3
  e1: "inset 0 1px 0 rgba(255,113,206,0.18)"
  e2: "0 6px 18px rgba(1,205,254,0.10)"
  e3: "0 12px 32px rgba(185,103,255,0.18)"
  topHighlight: "inset 0 1px 0 rgba(255,251,252,0.10)"
  borderLight: "{colors.line}"
  borderDark: "{colors.line-strong}"
  separator: border
media:
  logoType: wordmark
  logoRule: "字标用 {typography.display} 全大写 + {typography.label} 字距，纯文字不加图形标；外缘霓虹用 {colors.primary} 与 {colors.secondary} 各偏 2px"
  imageRadius: "{rounded.card}"
  imageRatio: "4:3"
  imageTreatment: "去饱和 12%，叠 {colors.primary} 14% 正片叠底，边缘做 2px 青粉错位色差"
  background: "深紫 {colors.canvas}；底部透视网格由 {colors.secondary} 1px 线在 rotateX(62deg) 平面上生成并向上淡出；不放真实雕像照片与品牌商标"
  iconRule: "1.5px 描边，20px 基准，和 {colors.ink} 同色或 {colors.secondary}"
  emptyState: "{colors.surface} 底 + 一行 {colors.ink-muted} 说明，不放插画"
motion:
  easing: "cubic-bezier(0.25, 0.8, 0.25, 1)"
  durationFast: 160ms
  durationBase: 480ms
  hover: "霓虹辉光增一档，translateY -2px，圆角不变"
  focusRing: "3px solid {colors.secondary}，offset 2px"
  openTransition: "opacity 0→1 且 translateY 16px→0，480ms"
  reducedMotion: "全部过渡降到 1ms，关闭 glitch 抖动与扫描线动画"
  dragUsesSpring: false
---

## Overview

给音乐人、演出与专辑页、创意作品集、复古游戏与活动落地页用。它做的不是"把信息讲清楚"，而是把观众放进一段关于 1980–90 年代电子消费品的慢速记忆里：粉与青两束霓虹、退向地平线的网格、带横纹的落日、偶尔抖动的色差。它适合情绪先行的展示型界面，不适合承载流程、表单或密集数据。

性格来自五个具体选择。底色 `{colors.canvas}` 是深紫黑 #1A0B2E 而不是纯黑，让霓虹有可以发光的暗场；`{colors.primary}` 粉与 `{colors.secondary}` 青成对出现，是所有渐变与辉光的固定搭配；`{typography.display}` 用 Orbitron 的几何字面、0.12em 宽字距与全大写，衬以 `{typography.cardTitle}` 的 Cormorant Garamond 衬线，制造"电子屏 + 古典胸像"的错位；底部透视网格把视线拉向单一地平线灭点；动效统一放慢到 `{motion.durationBase}`，只让辉光与位移变化。

读的人应当先感到"被罩在一台旧显示器里"，再读到内容。深场、霓虹与慢速位移共同产生这种失真怀旧感；只要把网格换成普通留白、把辉光换成实色，风格立刻垮成普通深色页。

**Key Characteristics**

- 画布 `{colors.canvas}`（#1A0B2E）：深紫偏主色而非纯黑，给霓虹留出可发光的暗场。
- 粉青成对：`{colors.primary}`（#FF71CE）与 `{colors.secondary}`（#01CDFE）同时出现，所有渐变与辉光只用这一对；薄荷 `{colors.accent}` 与淡黄 `{colors.highlight}` 是面积很小的点缀。
- 三档字体分工：Orbitron 管霓虹几何标题，Cormorant Garamond 管衬线对比，Space Mono 管正文与标签；中文回退 PingFang SC。
- 透视网格：1px 青线在 rotateX 62° 平面上退向单一灭点，向上淡出，是页面最强的方向性线索。
- 圆角极小且统一：`{rounded.card}` 4px、`{rounded.button}` 2px、`{rounded.tag}` 0，保留早期系统 UI 的硬边感。
- 层级靠底色差与霓虹描边表达，不靠居中发光投影；主分隔手段是 `border`。

## Colors

**Canvas & Surface**

- `{colors.canvas}` — #1A0B2E，页面底色；来源 designforai.dev 显式值。深紫偏主色，满足本库"深色底不用大面积纯黑、向主色偏一档"。
- `{colors.surface}` — #2D1B4E，卡片与面板底；来源 chrislemke 参考页的 Grid Purple，比画布亮约一档，靠明度分层。
- `{colors.surface-alt}` — #3D2566，悬浮态与标签底；比 surface 再亮一档，为推断值（来源未给），用于表达层级。

**Ink**

- `{colors.ink}` — #FFFBFC，主文字；来源 chrislemke 的 VHS White，对画布 18.08:1、对卡片 14.84:1。
- `{colors.ink-muted}` — #C4B7C9，次级说明；来源 Marble Gray，对画布 9.69:1。
- `{colors.ink-faint}` — #8B7E96，编号与元信息；来源 Static，对画布 4.88:1，关键文字不用这一档。

**Line**

- `{colors.line}` — #5B3A8C，常规细描边；推断值，比 surface 略亮，勾出硬边。
- `{colors.line-strong}` — #B967FF，强调描边与焦点辅助；来源色板 Purple，只用于需要被指认的边界。

**Accent**

- `{colors.primary}` — #FF71CE，霓虹粉，主色与主按钮；来源色板共识值，对画布 7.52:1。
- `{colors.secondary}` — #01CDFE，霓虹青，链接、网格与焦点环；来源共识值，对画布 9.87:1。
- `{colors.accent}` — #05FFA1，薄荷，仅用于成功态与小面积点缀；来源共识值。
- `{colors.highlight}` — #FFFB96，淡黄，仅用于数字与高亮词；来源 designforai.dev 的前景色。
- `{colors.on-primary}` — #1A0B2E，压在粉底上的深字；对粉底 7.52:1，达到正文级。

## Typography

字号只设 display 80px、headline 40px、cardTitle 28px、body 20px、label 14px 五档。相邻比值 14→20→28→40→80 为 1.43、1.40、1.43、2.0，全部不低于 1.25；不出现 16、18、24、32 这类中间档。字重只有 400 与 700 两档，不模拟 500/600。

Orbitron 管全大写霓虹标题并给 0.12em 正字距，Space Mono 管正文与标签等宽字，Cormorant Garamond 只出现在卡片标题与引文，用来和几何字面形成年代错位。中文按各档回退 PingFang SC；标签的 0.18em 字距对中文减半到 0.09em，避免字散。

## Layout

- 桌面 12 列网格，最大宽 1280px，两侧留白 `{spacing.md}`；Hero 占满一屏高度但不强行 100vh，保证移动端可读。
- 透视网格只铺在页面下部约 35% 高度，灭点水平居中；上部留给标题与内容，网格不穿过正文。
- 内容区块之间 `{spacing.section}`；标题与正文之间 `{spacing.xl}`；卡内 Padding `{spacing.lg}`。
- 卡片组用 2 列不对称栅格（宽卡跨 7 列、窄卡跨 5 列），不做三等分；移动端在 768px 以下全部折成单列。
- 正文最大宽度 `{spacing.measure}`；元信息统一右对齐或左对齐，同一页不混用。

## Elevation & Depth

三层材质。贴面 `{elevation.e1}` 给卡片一条粉色内描边高光，卡片 `{elevation.e2}` 是带偏移的青色辉光，浮层 `{elevation.e3}` 是带偏移的紫色辉光；光从 `{elevation.lightSource}` 顶部落日方向来，四处发光就是 slop，因此同一屏最多一层出现 e3。所有阴影都有偏移，禁止 `0 0 Npx` 的居中发光。主分隔手段是 `border`，描边用 `{colors.line}`，只有需要被指认的边界才升到 `{colors.line-strong}`。

## Shapes

卡片 `{rounded.card}` 4px、按钮 `{rounded.button}` 2px、标签 `{rounded.tag}` 0；同一页不出现第二种卡片圆角，不做圆形卡、不做胶囊按钮。落日与几何装饰是唯一允许的正圆，因为它们是图像不是容器。图标统一 1.5px 描边、20px 基准，与 `{colors.ink}` 或 `{colors.secondary}` 同色。

## Material & Elevation

深色画布上层级靠明度与内描边，不靠投影：画布 #1A0B2E → 卡片 #2D1B4E → 悬浮 #3D2566，每升一档约 +8% 明度，再用 `{elevation.topHighlight}` 补一条极淡顶边光。霓虹辉光是这里唯一的"光"，从顶部落日方向统一照射；它只加在标题、按钮和选中态上，不给大面积背景。扫描线与色差是表面质感，强度控制在 3% 以下，且可一键关闭。

## Mark & Media

标识：`{media.logoRule}`（`{media.logoType}`），只写规则不写任何品牌资产。图片：比例 `{media.imageRatio}`、圆角 `{media.imageRadius}`、处理 `{media.imageTreatment}`；色差只做 2px 偏移，避免把主体糊掉。背景：`{media.background}`，透视网格用 CSS 生成，不引用真实照片或商标。图标：`{media.iconRule}`。空态：`{media.emptyState}`。

每张图要能通过删除测试：胸像、棕榈或产品图若删掉会让页面失去年代错位感或信息，才留下；纯装饰的图删掉。所有图都有静止替代帧，未加载时标题与正文仍成立。文字、按钮、表单与数据标签一律真实 HTML/CSS 排版，不让生图模型画字。

## Motion & States

过渡曲线 `{motion.easing}`，快档 `{motion.durationFast}`、基准 `{motion.durationBase}`，比常规界面慢一档以贴合"梦"的节奏。hover：`{motion.hover}`；焦点：`{motion.focusRing}`，青色在深底上足够醒目，且 `outline-offset` 留 2px 不被裁切；展开：`{motion.openTransition}`。交互组件逐项覆盖 default / hover / focus-visible / active / disabled / error 六态，error 用 `{colors.primary}` 描边而非新增红。

glitch 抖动只作用在标题，且用可关闭的 CSS 动画实现；`prefers-reduced-motion` 时执行 `{motion.reducedMotion}`。本风格没有拖拽排序组件，不使用弹簧过渡。

## Components

### card

`{components.card}` 是 `{colors.surface}` 底的硬边卡，靠 `{rounded.card}` 4px 与粉色内描边 `{elevation.e1}` 成形。卡标题用 `{typography.cardTitle}` 衬线，正文用 `{typography.body}`，右上角可放一个 `{components.tag}`；悬浮时升到 `{colors.surface-alt}` 并加青色辉光，不放大字号。

### button-primary

`{components.button-primary}` 是粉底深字的硬边按钮，承担一屏唯一主行动，只出现一次。hover 辉光增一档并上移 2px；次按钮用透明底与 `{colors.line-strong}` 描边，尺寸一致；禁用态降到 `{colors.line}` 描边与 `{colors.ink-faint}` 字。

### tag

`{components.tag}` 用 `{colors.surface-alt}` 底、`{colors.secondary}` 字表示状态与元信息，字距放宽、无圆角。它只标注事实，不放在标题前当装饰序言，也不承担正文。

## Do's and Don'ts

### Do

- 粉与青始终成对出现，所有渐变与辉光只用这一对。
- 深紫底、透视网格与宽字距霓虹标题三者至少同时出现两项。
- 层级靠底色差与霓虹描边，发光只给标题、按钮与选中态。
- 动效放慢到 480ms 档，并保留 reduced-motion 降级。

### Don't

- 不要用紫到蓝或紫到粉的渐变，也不要用 `background-clip: text` 做渐变字——前者触犯 The Floor，后者无法降级且对比度不可控。
- 不要让霓虹铺满背景或给每层都加辉光，会变成 slop；同屏 e3 最多一次。
- 不要放进企业后台、表单流程或密集数据页，慢速与失真会让效率崩塌。
- 不要把网格穿过正文，也不要让 glitch 抖动正文；可读性优先于风格纯度。
- 不要照搬任何品牌商标、真实雕像照片或授权字体，只写可迁移的规则。

## Chinese Typography

- 中文正文行高不低于 1.7，标签可降到 1.5，但不低于 1.5。
- 中西文之间留四分之一个空格：`一张专辑`、`用 Orbitron`。
- 中文标签的 0.18em 字距减半到 0.09em；标题的 0.12em 减半到 0.06em，避免字面过散。
- 使用全角标点，段落不首行缩进，启用避头尾。
- 中文只有 400 与 700 两档有效字重，不强行模拟 500/600。
- Orbitron、Cormorant Garamond 与 Space Mono 都不含中文，中文回退 PingFang SC；霓虹发光对中文只加在标题，不加在正文。
- 霓虹描边用 1px，不要给中文加 2px 以上 text-shadow，否则小字号糊成一团。
- 80px 展示标题用于中文时降到 40px（headline 档），避免宽字距把字面撑破容器。

## When to Use

**用**：音乐人与专辑/演出页、synthwave 与 retrowave 活动页、创意作品集首屏、复古游戏与 Game Jam 页面、潮流服饰与周边、任何需要强情绪与怀旧感的展示型界面。

**别用**：企业官网与后台、表单密集的办事流程、金融医疗政务、长文阅读与论文、需要严肃权威与高信息效率的界面、打印为主的单栏文档。

## Iteration Guide

1. 一次只改一个组件，用 `{components.card}` 指代它。
2. 所有值走 token，不要内联十六进制；需要新色先确认粉青对是否真的不够。
3. 想加强风格时先加深透视网格或加宽标题字距，最后才考虑加新颜色——加色基本等于破功。
4. 新增装饰前先问：它能不能用现有网格 + 霓虹描边表达。不能，再谈别的。

## Known Gaps

- 只覆盖深色一屏展示型界面；浅色 vaporwave（粉彩底）与复杂表单、长列表未定义。
- 三种字体都是 Google Fonts，不含中文；中文气质依赖 PingFang SC 回退，霓虹效果在无衬线中文上会打折，需真机复核。
- 来源里标志性的紫粉渐变与 `background-clip: text` 渐变字为遵守本库 The Floor 被改造；与严格复刻来源的页面会有明显色差。
- glitch 动画在低端设备上可能掉帧；扫描线与色差对色觉敏感用户不友好，已提供 reduced-motion 降级但未做逐项开关。
- 透视网格的灭点位置随容器宽度变化，超宽屏（>1920px）未标定。
