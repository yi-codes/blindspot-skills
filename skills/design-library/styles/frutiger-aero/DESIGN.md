---
version: alpha
name: Frutiger Aero｜晴空拟物
description: >-
  把 2004–2013 年"科技与自然和谐相处"的乐观想象做成一套可直接用的界面语言：
  天蓝到草绿的通透渐变、带高光条的玻璃按钮、气泡与水滴、人文无衬线字。
  用于怀旧品牌活动页、消费电子与饮品官网、音乐与媒体播放器、健康与工具类 App 的展示型界面。
  参数提炼自 chrislemke 设计参考库、designmd.app 风格卡、design-ontology 与 anti-boring 四份来源的交叉验证；
  标为 beta/variant。为符合本库 The Floor，把来源里"纯白背景""全盘发光""品牌专属拟物图标"改造成偏主色的浅蓝底、
  有偏移的柔和阴影与可复现的 CSS 气泡。
cues: 怀旧科技与 Y2K 品牌活动页、消费电子与饮品官网、音乐与媒体播放器、健康与天气类工具 App、游戏启动器、需要乐观亲和气的展示型界面
avoid: 数据密集型后台与大表格、扁平/极简/单色品牌、需要严肃权威的金融医疗政务、长文与论文阅读、表单密集的办事流程、以打印为主的文档
surface: light
density: medium
register: story
family: retro
tier: variant
sourceRefs: frutiger-aero
status: beta

colors:
  canvas: "#EAF6FF"
  surface: "#F5FBFF"
  surface-alt: "#DDF1FF"
  ink: "#0B2A4A"
  ink-muted: "#2F6B57"
  ink-faint: "#3F6678"
  line: "#8FD3FF"
  line-strong: "#0288D1"
  primary: "#0288D1"
  secondary: "#43A047"
  accent: "#7ED957"
  highlight: "#FFD54F"
  water: "#00BCD4"
  deep: "#0A4C8C"
  on-primary: "#0B2A4A"
typography:
  display:
    fontFamily: "Nunito, PingFang SC, sans-serif"
    fontSize: 64px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -0.02em
  headline:
    fontFamily: "Nunito, PingFang SC, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.01em
  cardTitle:
    fontFamily: "Nunito, PingFang SC, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  body:
    fontFamily: "Nunito Sans, PingFang SC, Noto Sans SC, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: 0
  label:
    fontFamily: "Nunito Sans, PingFang SC, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0.02em
rounded:
  card: 16px
  button: 999px
  tag: 8px
  panel: 24px
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
    backgroundColor: "{colors.line}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.button}"
    padding: 12px 24px
  tag:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.deep}"
    typography: "{typography.label}"
    rounded: "{rounded.tag}"
    padding: 6px 12px
elevation:
  lightSource: top-left
  steps: 3
  e1: "inset 0 1px 0 rgba(255,255,255,0.85), 0 4px 12px rgba(10,76,140,0.12)"
  e2: "inset 0 1px 0 rgba(255,255,255,0.9), 0 8px 20px rgba(10,76,140,0.18)"
  e3: "inset 0 1px 0 rgba(255,255,255,0.9), 0 16px 32px rgba(10,76,140,0.22)"
  topHighlight: "inset 0 1px 0 rgba(255,255,255,0.9)"
  borderLight: "{colors.surface}"
  borderDark: "{colors.line}"
  separator: border
media:
  logoType: wordmark
  logoRule: "字标用 {typography.display}，右侧留 0.5em；只写规则，不搬任何品牌 logo 或吉祥物"
  imageRadius: "{rounded.card}"
  imageRatio: "4:3"
  imageTreatment: "轻微提亮并去饱和 6%，叠 {colors.water} 8% 正片叠底，使照片像透过玻璃看"
  background: "全幅垂直渐变 {colors.canvas} 到 {colors.line} 再到 {colors.accent}，光从左上；气泡与水滴作 20%–60% 面积的环境装饰"
  iconRule: "1.6px 描边，20px 基准，和 {colors.ink} 同色"
  emptyState: "{colors.surface-alt} 底 + 一行 {colors.ink-muted} 说明，不放插画"
motion:
  easing: "cubic-bezier(0.4, 0, 0.2, 1)"
  durationFast: 160ms
  durationBase: 480ms
  hover: "玻璃高光增一档，translateY -2px，圆角不变"
  focusRing: "3px solid {colors.primary}，offset 2px"
  openTransition: "opacity 0→1 且 translateY 12px→0，480ms"
  reducedMotion: "全部过渡降到 1ms，关闭气泡浮动与高光扫过"
  dragUsesSpring: false
---

## Overview

给怀旧科技品牌、消费电子与饮品官网、音乐与媒体播放器、健康与天气工具、游戏启动器用。它要确认的不是"这条信息准确"，而是"这个产品让人友好、可信、对未来抱有希望"：界面像能被触摸的玻璃与水，背景是天蓝到草绿的通透渐变，气泡与光斑缓慢漂浮。它适合情绪先行的展示型界面，不适合承载密集数据或严肃流程。

性格来自五个具体选择。底色 `{colors.canvas}` 是浅天蓝 #EAF6FF 而不是纯白，制造"晴空"而非"空白页"；`{colors.primary}` 用深青 #0288D1 而非来源的亮蓝 #38B6FF，把强调色对比度从 2.06:1 提到 3.51:1，同时保留蓝天感；`{colors.ink}` 用海军蓝 #0B2A4A 而不是黑，正文对画布 13.24:1；`{typography.display}` 用 Nunito 的圆头人文无衬线，不用几何或像素字；按钮是顶部带白色高光条的玻璃胶囊，阴影一律带偏移，光从 `{elevation.lightSource}` 左上统一照下来。

读者应当先感到"明亮、可触摸、有生命"，再读到内容。渐变、玻璃高光与气泡共同产生这种乐观拟物感；只要把渐变换成平涂、把高光去掉、把浅蓝换成纯白，风格立刻垮成普通扁平页。

**Key Characteristics**

- 画布 `{colors.canvas}`（#EAF6FF）：浅天蓝偏主色而非纯白，满足本库"浅色底不用大面积纯白、向主色偏一档"，也是"晴空"的来源。
- 天蓝到草绿渐变：`{colors.canvas}` → `{colors.line}` → `{colors.accent}` 的全幅垂直渐变是本风格唯一签名，承担"科技与自然和谐"的语义，不是装饰。
- 玻璃按钮：`{colors.line}` 填充 + 顶部白色高光条 + `{elevation.topHighlight}` 内描边 + `{rounded.button}` 胶囊，来源明确要求"垂直渐变、上半部白色高光、1px 浅边"。
- 文字用海军蓝 `{colors.ink}`（#0B2A4A）而非纯黑；主色 `{colors.primary}`（#0288D1）为可访问的深一档青蓝，链接与焦点环都用它。
- 圆角分层：`{rounded.tag}` 8px、`{rounded.card}` 16px、`{rounded.panel}` 24px、`{rounded.button}` 999px；胶囊只给主按钮，不做全站统一圆角。
- 层级靠底色差、玻璃描边与带偏移的柔和阴影表达，主分隔手段是 `border`，不靠居中发光。

## Colors

**Canvas & Surface**

- `{colors.canvas}` — #EAF6FF，页面底色；来源 designmd.app 显式值 `bg`，偏蓝的浅底，不触犯 The Floor 的纯白禁令。
- `{colors.surface}` — #F5FBFF，玻璃卡片底；来源 `surface` 是 rgba(255,255,255,0.55)，落在浅蓝底上合成后近似此实色，写成 hex 便于 token 对齐。
- `{colors.surface-alt}` — #DDF1FF，玻璃面板与标签底；比 surface 深一档的推断值，靠明度分层。

**Ink**

- `{colors.ink}` — #0B2A4A，主文字；来源 anti-boring 的 "Navy text" 显式值，对画布 13.24:1、对卡片 13.93:1。
- `{colors.ink-muted}` — #2F6B57，次要说明；来源 designmd.app 的 `text-muted` 显式值，对画布 5.69:1。
- `{colors.ink-faint}` — #3F6678，编号与元信息；推断值，对画布 5.65:1，仍高于 3:1 硬线。

**Line**

- `{colors.line}` — #8FD3FF，常规玻璃描边与按钮填充；来源 designmd.app 的 `sky` 显式值。
- `{colors.line-strong}` — #0288D1，强调描边；与 primary 同值，来源 chrislemke 的 "Cerulean" 显式值。

**Accent**

- `{colors.primary}` — #0288D1，深青主色，链接、焦点环、强调；来自来源色板 Cerulean，比 designmd.app 的 #38B6FF 深一档，把对画布对比度从 2.06:1 提到 3.51:1。
- `{colors.secondary}` — #43A047，叶绿，成功态与自然点缀；来源 chrislemke 的 "Leaf Green" 显式值。
- `{colors.accent}` — #7ED957，亮青柠，渐变末端与 CTA 辅色；来源 designmd.app 的 `accent` 显式值，海军蓝压在上面 8.27:1。
- `{colors.highlight}` — #FFD54F，日光黄，只用于小面积高亮；来源 chrislemke 的 "Sunlit Yellow"。
- `{colors.water}` — #00BCD4，水青，玻璃混色与水滴；来源 chrislemke 的 "Water Cyan"。
- `{colors.deep}` — #0A4C8C，深海蓝，标签字与阴影色；来源 chrislemke 的 "Teal Deep / Deep Ocean" 显式值。
- `{colors.on-primary}` — #0B2A4A，压在浅蓝玻璃按钮上的深字；对 `{colors.line}` 7.26:1，达到正文级。

## Typography

字号只设 display 64px、headline 40px、cardTitle 28px、body 20px、label 16px 五档。相邻比值 16→20→28→40→64 为 1.25、1.40、1.43、1.60，全部不低于 1.25；不出现 18、24、32、48 这类中间档。字重只有 400 与 700 两档，来源里的 800 降到 700，不模拟 500/600。

Nunito 管标题，圆头终端与开放字腔对应来源反复强调的"人文、温暖、可读"；Nunito Sans 管正文与标签，是 Nunito 的直终端伴侣。来源点名的 Frutiger / Myriad Pro 是商业字体且品牌辨识过强，按"不照抄品牌专属字体"改造成可自由使用的 Nunito 家族，并在 NOTES 的「弃」记录。中文按各档回退 PingFang SC；display 的 -0.02em 负字距对中文减半到 -0.01em，避免挤字。

## Layout

- 桌面 12 列网格，最大宽 960px 居中，列距 20px；来源 design-ontology 明确给出"960px 居中、12 列、20px 栏距"。
- 结构自上而下：导航栏 → 360–480px 主视觉带 → 3 或 4 个玻璃卡片；主视觉占满宽度但不强行 100vh。
- 留白 25%–40% 的版面保持空；区块之间 `{spacing.section}`，标题与正文之间 `{spacing.xl}`，卡内 Padding `{spacing.md}` 到 `{spacing.lg}`。
- 卡片组用 3 列等宽栅格，768px 以下折成单列，不留水平溢出；来源 designmd.app 明确要求 768px 断点。
- 正文最大宽度 `{spacing.measure}`；主视觉与标志居中，卡片内正文左对齐，同一页不混用。

## Elevation & Depth

三层材质。贴面 `{elevation.e1}` 是一条白色内高光加 4px 柔和偏移影；卡片 `{elevation.e2}` 升到 8px；浮层 `{elevation.e3}` 到 16px，光从 `{elevation.lightSource}` 左上统一照下来，四处发光就是 slop，因此同一屏最多一层出现 e3。所有阴影都有偏移，禁止 `0 0 Npx` 的居中发光；高光只加在玻璃容器的上边缘，不给正文。主分隔手段是 `border`，描边用 `{colors.line}`，需要被指认的边界升到 `{colors.line-strong}`。

## Shapes

标签 `{rounded.tag}` 8px、卡片 `{rounded.card}` 16px、面板 `{rounded.panel}` 24px、主按钮 `{rounded.button}` 999px；来源要求"容器 6–12px、仅主按钮全胶囊"，本库把容器阶取到 8/16/24 以适配更大卡片，胶囊仍只给主按钮。同一页不出现第二种卡片圆角，不做尖角卡、不做方形主按钮。气泡与光斑是唯一允许的正圆，因为它们是图像不是容器。图标统一 1.6px 描边、20px 基准，与 `{colors.ink}` 同色。

## Material & Elevation

浅色画布上层级靠明度、玻璃描边与带偏移的柔和阴影三层叠加：画布 #EAF6FF → 面板 #DDF1FF → 卡片 #F5FBFF，再用 `{elevation.topHighlight}` 补一条左上顶边高光，模拟来源里的 "specular highlight strip"。玻璃面板用半透明底加 `{colors.surface}` 描边，来源的 blur 只在确有背景可透时启用，且强度受控。阴影色用 `{colors.deep}` 的低透明度版本而非中性黑，保持"晴空"色调统一。

## Mark & Media

标识：`{media.logoRule}`（`{media.logoType}`），只写规则不写品牌资产；来源里的 Windows 徽标、iOS 图标与品牌吉祥物一律不搬。图片：比例 `{media.imageRatio}`、圆角 `{media.imageRadius}`、处理 `{media.imageTreatment}`；水滴、气泡、草地、热带鱼只描述物件类型，不指定图源。背景：`{media.background}`，渐变与气泡用 CSS 生成，不引用真实品牌壁纸；图标：`{media.iconRule}`。空态：`{media.emptyState}`。

每张图要能通过删除测试：气泡与水滴若删掉会让页面失去"可触摸的乐观感"，才留下；纯装饰的图删掉。所有图都有静止替代帧，未加载时渐变背景、标题与正文仍成立。文字、按钮、表单与数据标签一律真实 HTML/CSS 排版，不让生图模型画字；来源强调的"自动发光"效果只用在装饰气泡，不落在文字上。

## Motion & States

过渡曲线 `{motion.easing}`，快档 `{motion.durationFast}`、基准 `{motion.durationBase}`，来源 anti-boring 把这一 era 的动效描述为"缓慢、循环、像屏保"，因此比常规界面慢一档。hover：`{motion.hover}`；焦点：`{motion.focusRing}`，深青在浅蓝底上足够醒目且 offset 2px 不被裁切；展开：`{motion.openTransition}`。交互组件逐项覆盖 default / hover / focus-visible / active / disabled / error 六态，error 用 `{colors.line-strong}` 描边而非新增红。

气泡浮动与高光扫过用 CSS keyframes，且只作用于装饰元素；`prefers-reduced-motion` 时执行 `{motion.reducedMotion}`。本风格没有拖拽排序组件，不使用弹簧过渡。

## Components

### card

`{components.card}` 是 `{colors.surface}` 底的玻璃卡，靠 `{rounded.card}` 16px、白色内高光 `{elevation.e1}` 与 `{colors.line}` 描边成形。卡标题用 `{typography.cardTitle}`，正文用 `{typography.body}`，右上角可放一个 `{components.tag}`；悬浮时描边升到 `{colors.line-strong}` 并加 e2，不放大字号。

### button-primary

`{components.button-primary}` 是浅蓝玻璃填充、海军蓝深字、白色高光条的胶囊按钮，承担一屏唯一主行动，只出现一次。hover 高光增一档并上移 2px；次按钮用透明底与 `{colors.line-strong}` 描边，尺寸一致；禁用态降到 `{colors.line}` 描边与 `{colors.ink-faint}` 字。

### tag

`{components.tag}` 用 `{colors.surface-alt}` 底、`{colors.deep}` 字表示状态与元信息，8px 圆角。它只标注事实，不放在标题前当装饰序言，也不承担正文。

## Do's and Don'ts

### Do

- 天蓝到草绿渐变、玻璃高光胶囊、气泡或水滴三者至少同时出现两项。
- 文字用 `{colors.ink}` 海军蓝而非黑、纯白；强调色用深青 `{colors.primary}` 保证对比度。
- 阴影一律带偏移、光从左上；层级靠明度与玻璃描边。
- hover 放慢到 480ms 档，并保留 reduced-motion 降级。

### Don't

- 不要用纯白大面积背景，也不要把玻璃做成全盘居中发光——前者破 The Floor，后者是 slop。
- 不要把玻璃与渐变当装饰堆在没有功能层级的页面上；每个气泡要能说出自己承担的空间或叙事职责。
- 不要放进数据密集后台、表单流程或严肃金融医疗政务界面，乐观拟物会削弱可信度。
- 不要照搬 Windows / iOS 徽标、品牌壁纸上真实存在的鱼与吉祥物、Frutiger / Myriad 等商业字体。
- 不要用硬偏移黑影、粗黑描边、破损纸纹或像素字，这些是来源明确列出的破功项。

## Chinese Typography

- 中文正文行高不低于 1.7，标签可降到 1.5，但不低于 1.5。
- 中西文之间留四分之一个空格：`一个气泡`、`用 Nunito`。
- 中文标签的 0.02em 正字距可归零，避免汉字被拉散；display 的 -0.02em 负字距对中文减半到 -0.01em，防止挤字。
- 使用全角标点，段落不首行缩进，启用避头尾。
- 中文只有 400 与 700 两档有效字重，不强行模拟 500/600。
- Nunito 与 Nunito Sans 都不含中文，中文回退 PingFang SC；标题的负字距在中文上要复核。
- 64px 展示标题用于中文时降到 40px（headline 档），避免宽字面撑破 960px 容器。
- 玻璃按钮上的中文标签用 700 字重保证在半透明底上可读，不靠加发光。

## When to Use

**用**：怀旧科技与 Y2K 品牌活动页、消费电子与饮品官网、音乐与媒体播放器、健康与天气工具 App、游戏启动器、任何需要乐观亲和气的展示型界面。

**别用**：数据密集型后台与大表格、扁平/极简/单色品牌、需要严肃权威的金融医疗政务、长文与论文阅读、表单密集的办事流程、以打印为主的文档。

## Iteration Guide

1. 一次只改一个组件，用 `{components.card}` 指代它。
2. 所有值走 token，不要内联十六进制；需要新色先确认天蓝到草绿的渐变是否真的不够。
3. 想加强风格时先让渐变更通透或把玻璃高光提亮一档，最后才考虑加新颜色——加色基本等于破功。
4. 新增装饰前先问：它能不能用现有气泡 + 渐变表达。不能，再谈别的。

## Known Gaps

- 只覆盖浅色展示型界面；深色 Frutiger Aero 变体与复杂表单、长列表、大表格未定义。
- 来源点名的 Frutiger / Myriad Pro 是商业字体，已用 Nunito 家族替代；截图在无 Nunito 的环境会回退到系统无衬线，圆头感会打折。
- 来源的 "auto-glow" 与品牌专属拟物图标（Windows 徽标、iOS 图标、真实热带鱼壁纸）未迁移，只保留可复现的 CSS 气泡与玻璃规则。
- 渐变与玻璃高光在低端设备或关闭 GPU 合成时可能出现色带；已提供 reduced-motion 降级但未做逐项开关。
- 半透明玻璃在极浅背景上层级差异会变小，需要靠描边补偿；超宽屏（>1920px）的渐变 stops 未单独标定。
