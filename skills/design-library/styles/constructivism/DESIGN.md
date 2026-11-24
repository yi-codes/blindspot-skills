---
version: alpha
name: Constructivism｜构成主义海报
description: >-
  把 1910–30 年代构成主义海报的视觉语法做成展示型网页：
  泛黄纸底 #F2E8D5、革命红 #CC0000 与暖墨 #1A1A1A 三色硬边，
  -2° 倾斜的号令式大标题、-12° 斜切红楔与 4px 墨线，
  按钮用「色块侵入」横扫与红黑反转制造机械感。
  用于行动号召强烈的活动页、文化展览、发布页与宣言式落地页。
  参数提炼自 luckymaomi 风格卡的显式 CSS 变量与交互规则、indexstyle 辞典条目的三色规格、
  stylekit 动力学构成主义卡的完整字阶与动效禁令；标为 beta/variant。
  为符合本库 The Floor，把来源 font-black 收进 900/700 两档、正文提到 18px/1.7，
  并把来源的金/棕/群青等补充色全部去掉，只保留红、墨、纸三色。
cues: 文化活动与展览活动页、产品/影片/演出发布页、主张鲜明的宣言式落地页、体育与音乐赛事宣传页、需要一屏建立强烈态度的作品集首屏
avoid: 长文阅读与论文、产品文档与帮助中心、高密度后台与数据表格、表单密集的办事流程、金融医疗法律等需要克制可信的场景、政务与官方公告、需要平等比较多个选项的页面
surface: light
density: medium
register: story
family: expressive
tier: variant
sourceRefs: constructivism
status: beta

colors:
  canvas: "#F2E8D5"
  surface: "#F7F0E1"
  surface-alt: "#E7D7B8"
  ink: "#1A1A1A"
  ink-muted: "#4A433A"
  ink-faint: "#6B6255"
  line: "#1A1A1A"
  primary: "#CC0000"
  on-primary: "#F2E8D5"
typography:
  display:
    fontFamily: "Impact, Haettenschweiler, Arial Narrow, PingFang SC, sans-serif"
    fontSize: 72px
    fontWeight: 900
    lineHeight: 0.95
    letterSpacing: -0.03em
  headline:
    fontFamily: "Impact, Haettenschweiler, Arial Narrow, PingFang SC, sans-serif"
    fontSize: 36px
    fontWeight: 900
    lineHeight: 1
    letterSpacing: 0.02em
  cardTitle:
    fontFamily: "Impact, Haettenschweiler, Arial Narrow, PingFang SC, sans-serif"
    fontSize: 24px
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: 0.02em
  body:
    fontFamily: "Arial, PingFang SC, Noto Sans SC, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.7
    letterSpacing: 0
  label:
    fontFamily: "Arial, PingFang SC, Noto Sans SC, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0.08em
rounded:
  card: 0px
  tag: 0px
  button: 0px
spacing:
  base: 8px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  section: 96px
  measure: 34em
components:
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: 24px
    border: "4px solid {colors.line}"
    shadow: "{elevation.e2}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.button}"
    padding: "12px 28px"
  tag:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.label}"
    rounded: "{rounded.tag}"
    padding: "6px 12px"
elevation:
  lightSource: top-left
  steps: 3
  e1: "2px 2px 0 {colors.ink}"
  e2: "4px 4px 0 {colors.ink}"
  e3: "6px 6px 0 {colors.ink}"
  topHighlight: "none —— 刀切硬边、实色平涂，不加内高光，避免把版画压印做成玻璃拟物"
  borderLight: "{colors.line}"
  borderDark: "{colors.ink}"
  separator: border
media:
  logoType: wordmark
  logoRule: "字标用 {typography.headline}，右留 0.5em；只写排字规则，不搬历史海报、政治标识或任何真实品牌资产"
  imageRadius: "{rounded.card}"
  imageRatio: "3:2"
  imageTreatment: "硬边矩形裁切，filter: grayscale(1) contrast(1.15)，外框 4px {colors.ink}；不使用插画、3D 拟物与柔和景深"
  background: "{colors.canvas} 实色底 + 一处 -12deg 斜切红楔（clip-path 多边形，宽度 ≤38%）+ 一条 -2deg {colors.ink} 粗线；粗网点只在图片块内，面积 ≤20%，不压正文"
  iconRule: "只用 4px 实色方块与直条，24px 基准，颜色取 {colors.ink} 或 {colors.primary}；不引入圆润图标与拟物符号"
  emptyState: "{colors.surface-alt} 底 + 4px {colors.ink} 描边 + 一行 {colors.ink-muted} 说明，不放插画"
motion:
  easing: linear
  durationFast: 75ms
  durationBase: 100ms
  hover: "色块侵入：按钮内墨色覆盖层 translateX(-100%) → 0；元素整体沿对角线 translate(4px, 4px)，硬影 6px → 2px"
  focusRing: "2px solid {colors.primary}，offset 2px；在纸底与红底上都可见"
  openTransition: "覆盖层 translateX(-100%) → 0，100ms linear；分隔线 -2deg → 0，75ms linear"
  reducedMotion: "所有过渡降到 1ms；侵入层停在覆盖终态，倾斜与斜楔保留静态原样，信息零丢失"
  dragUsesSpring: false
---

## Overview

给文化活动、展览、演出与产品发布、宣言式落地页，以及任何需要「先让人站队，再让人细读」的展示型页面用。它要确认的不是「这条信息完整」，而是「这件事重要，而且现在就要行动」。

性格来自五个可指认的选择。纸底 `{colors.canvas}`（#F2E8D5）是泛黄印刷纸而不是纯白；唯一彩色 `{colors.primary}`（#CC0000）只给主行动与红楔；`{colors.ink}`（#1A1A1A）同时承担文字、4px 边框与硬影；标题用 Impact 一类的窄黑体压到 `{typography.display}` 72px / 行高 0.95 并倾斜 -2°；按钮与卡片只给 0px 圆角。`{elevation.e2}` 是 4px 4px 0 的零模糊硬影，来源是风格卡里明确写出的「版画压印」，不是塑料贴面。

读者先看到红与墨相撞的斜楔和超大标题，再读到号令式短句，最后才看到正文。动效也服从同一套机械语法：侵入层横扫 100ms linear、按下时红黑反转，不用弹性曲线。把三色扩成五色、把斜楔改成居中渐变、把 4px 边框换成软阴影，风格立刻垮成普通促销页。

它和库内其他强风格的分工：`bauhaus` 用几何当结构、`memphis` 用图案当装饰、`neobrutalist` 用规整卡片加粗描边；本风格用**对角线当力**、文字本身当建筑构件，色块是冲进版面的，不是摆上去的。

**Key Characteristics**

- 三色封顶：纸 `{colors.canvas}`、墨 `{colors.ink}`、红 `{colors.primary}`；来源风格卡把「超过三色体系」写进绝对禁止。
- 4px 墨线 + 2/4/6px 零模糊硬影：风格卡显式值，层级靠边框与压印表达，不靠渐变。
- 72px/900 窄黑体标题、-2° 倾斜、-12° 红楔：来源的 `text-6xl md:text-8xl font-black -rotate-2 skew-x-12` 收进本库字号阶。
- 号令式字距：来源 `tracking-[0.2em]` / `tracking-[0.3em]` 显式值，只给短标签与拉丁大字，中文归零。
- 交互机械感：色块侵入 100ms linear、按下红黑反转、hover 沿对角线位移 4px，来源逐条写明。
- 左对齐、非对称、允许色块溢出容器：辞典要求「文字与照片沿对角主轴相撞」，居中对称会直接破功。

## Colors

**Canvas & Surface**

- `{colors.canvas}` — #F2E8D5，页面底。来源风格卡 `--cstv-paper` 显式值，泛黄印刷纸色，对 `{colors.ink}` 14.32:1。
- `{colors.surface}` — #F7F0E1，卡片与正文容器底。由纸色向浅一档稀释得到的推断值，避免纯白大色块，对 `{colors.ink}` 15.34:1。
- `{colors.surface-alt}` — #E7D7B8，空态、次级面板与网点块的底。由纸色加深的推断值，对 `{colors.ink}` 12.27:1。

**Ink**

- `{colors.ink}` — #1A1A1A，正文、描边、投影与黑底按钮同色。来源风格卡 `--cstv-black` 显式值（原文写作「纯黑」，实际 hex 是近黑），不是 #000000。
- `{colors.ink-muted}` — #4A433A，次要说明；由墨色与纸色混合得到的推断值，对画布 8.02:1。
- `{colors.ink-faint}` — #6B6255，编号、日期、元信息；推断值，对画布 4.93:1，仍高于 4.5:1，不再往下调。

**Line**

- `{colors.line}` — #1A1A1A，4px 实线边框与分隔条，来源 `border-4 border-[#1a1a1a]` 显式规格；不引入浅灰发丝线。

**Accent**

- `{colors.primary}` — #CC0000，革命红，只给主按钮、红楔、焦点环与极少数标记；来源风格卡 `--cstv-red` 显式值，对画布 4.84:1，过 WCAG AA 4.5:1。
- `{colors.on-primary}` — #F2E8D5，红底上的字；与画布同值，对 `{colors.primary}` 4.84:1。来源 `bg-[#cc0000] text-[#f2e8d5]` 显式组合，不用白字。

三色之外不再设 `accent` / `highlight` / `secondary`。来源金星色 #D4A843（对纸底仅 1.82:1）与棕色 #8B4513 都作为「点缀」出现在风格卡里，本库按「严格三色体系」的硬规则弃用，详见 NOTES「弃」。

## Typography

字号五档：display 72px、headline 36px、cardTitle 24px、body 18px、label 14px。相邻比值为 2.00、1.50、1.33、1.29，全部不低于 1.25；不设 16、20、32、48px 这类中间档。72px 与 16px/22px 附近的值分别来自 stylekit 的显式字阶和风格卡的 `text-6xl/8xl`，36px 来自风格卡 `md:text-4xl`；本库按 24/18/14 重新落阶，是为了让中文正文达到 18px/1.7。

字重只取两档：900 给 display / headline / cardTitle，700 给 body / label。来源要求 `font-black` 与 `font-bold`，没有 400/500/600，本库也不引入。标题族用 Impact / Haettenschweiler / Arial Narrow 的窄黑字面，正文用 Arial；中文回退 PingFang SC / Noto Sans SC。display 的 -0.03em 负字距来自 stylekit，中文减半到 -0.015em；label 的 0.08em 正字距来自风格卡 `tracking-wider`，中文归零，避免把小字拉散。

拉丁大写内容是**写在文案里的**，不靠 `text-transform: uppercase`；这既符合来源的号令式字体，也避免给中文正文误加全大写规则。

## Layout

- 页面最大宽 1200px、容器内边距 24px，来自 stylekit 的显式布局值；风格卡的 `px-6 md:px-12 lg:px-16` 作为 24/48/64px 侧边距依据。
- 首屏左对齐：主标题占约 8 列，右侧给红楔与粗线，不做居中对称。红楔用 `clip-path` 斜切 -12°，允许溢出容器右边。
- 区块间距 `{spacing.section}` 96px（stylekit `--section-gap`），标题与正文之间 `{spacing.xl}` 64px，卡内 Padding `{spacing.md}` 24px，元信息到标题 `{spacing.sm}` 16px。
- 三张卡用 1.2fr / 1fr / 0.8fr 不等宽，第一张 -2° 静态倾斜；来源是风格卡的「几何块面碰撞」与「左对齐为主」，不是三等分网格。
- 正文最大宽度 `{spacing.measure}` 34em；768px 以下折成单列，红楔缩到 20% 宽，倾斜归零，不产生横向溢出。
- 主分隔手段只有 4px `border`；硬影是材质，不承担分隔职责。

## Elevation & Depth

三级硬影，光从 `{elevation.lightSource}` 左上统一照下来，偏移恒向右下：`{elevation.e1}` 2px 2px 0 给标签与小按钮，`{elevation.e2}` 4px 4px 0 给卡片（来源显式值），`{elevation.e3}` 6px 6px 0 只给红楔压过来的首屏主块，一屏最多一处。模糊半径恒为 0；任何 `0 8px 20px` 软影都会把版画压印变成 Material Design。

层级主要靠 4px 描边与纸/浅纸/深纸三档底色差表达，阴影只补一层「印上去」的重量。`{elevation.topHighlight}` 明确为 none——不像 Aero 那样加内高光。

来源 stylekit 的动力学变体完全禁止阴影；本库取风格卡的 4/6px 零模糊硬影，因为它是静态海报变体的显式规格，且零模糊不触犯本库 slop S7。冲突已记入 NOTES「弃」与 `Known Gaps`。

## Shapes

容器 `{rounded.card}` 0px、标签 `{rounded.tag}` 0px、按钮 `{rounded.button}` 0px，来源 `rounded-none` 是绝对规则。正圆、胶囊、圆角、有机曲线、波浪线一律不进内容与组件层；只允许矩形、直角三角（红楔）与直条三种形状。

红楔用 `clip-path: polygon(0 0, 100% 0, 62% 100%, 0 100%)` 配 `skewX(-12deg)` 生成；分隔条是 `height: 4px` 的实线矩形，静态 `rotate(-2deg)`。来源 `rotate-45` 的黑方块只作为装饰几何，面积不超过首屏 15%，且不得压住标题。

## Material & Elevation

材质是印刷纸上的实色版画：纸底无渐变、无颗粒滤镜、无景深；粗网点用 `radial-gradient(circle, var(--co-ink) 1px, transparent 1.2px) 0 0 / 4px 4px` 画在图片块内，面积 ≤20%，不铺到正文底下。光源统一左上，四级表面只有纸 #F2E8D5 → 浅纸 #F7F0E1 → 深纸 #E7D7B8 三档明度差加墨与红两个实色，不用第四色。

分隔手段只有 `border`：4px 墨线勾出卡片、导航与主块边界；阴影和网点都是材质，不拿来当分割器。页面里任何一处出现模糊发光、玻璃高光或紫蓝/紫粉渐变，就不再是构成主义。

## Mark & Media

标识：`{media.logoRule}`（`{media.logoType}`）；不搬 El Lissitzky、Rodchenko 的海报构图，不搬政治标识、红星、锤镰或任何真实品牌字体与商标。图片：比例 `{media.imageRatio}`、圆角 `{media.imageRadius}`、处理 `{media.imageTreatment}`；只用硬边裁切的黑白摄影做蒙太奇，不用插画替代照片，也不让图片抢走红楔的主角位。背景：`{media.background}`。图标：`{media.iconRule}`。空态：`{media.emptyState}`。

删除测试：删掉红楔，页面仍有 4px 墨线与超大标题，但会失去「力从对角线来」的方向感——所以红楔保留一处、不承担信息；删掉粗网点，信息零丢失，就把它限制在图片块内。所有装饰都有静止帧；素材未加载时纸底、墨字与主行动仍成立。文字、按钮、表单与数据标签一律真实 HTML/CSS 排版，不让生图模型画字。

## Motion & States

过渡曲线是 `linear`（`{motion.easing}`），快档 `{motion.durationFast}` 75ms、基准 `{motion.durationBase}` 100ms；来源风格卡明确写「不超过 duration-100」「机械的，不是流畅的」，所以不用 ease-in-out、不用弹簧。hover：`{motion.hover}` 的色块侵入层从 -100% 横扫到 0，同时元素沿右下 4px 位移、硬影从 6px 收到 2px；分隔线从 -2° 归零。焦点：`{motion.focusRing}`，2px 红环在纸底 4.84:1，offset 2px 不会被 4px 描边吞掉。展开：`{motion.openTransition}`。

交互组件逐项覆盖六态：default 为红底纸字、4px 墨边与 4px 硬影；hover 为墨色侵入层横扫；focus-visible 为红色 2px 外环；active 执行「苏维埃反转」——红底按钮翻成墨底红字、墨底按钮翻成红底墨字，阴影归零；disabled 用 `{colors.surface-alt}` 底、`{colors.ink-faint}` 字、无硬影，不靠变淡的红；error 用 4px `{colors.primary}` 描边加一行 `{colors.ink}` 说明，不新增警示色。组合框另有 open 态：覆盖层停在终态、分隔线归零。

`prefers-reduced-motion` 时执行 `{motion.reducedMotion}`：过渡降到 1ms，侵入层停在覆盖终态，倾斜与红楔保持静态原样。本风格没有拖拽/手势组件，`motion.dragUsesSpring` 为 false；stylekit 的圆盘公转、三角钟摆与方块行进不迁移到本静态变体。

## Components

### card

`{components.card}` 是 `{colors.surface}` 底、4px `{colors.line}` 描边、`{elevation.e2}` 硬影的方角卡。卡标题用 `{typography.cardTitle}`，正文用 `{typography.body}`，右上角可放 `{components.tag}`。三张卡分别取 1.2fr / 1fr / 0.8fr 宽度，第一张 -2° 静态倾斜；hover 时倾斜归零并沿右下位移 4px，不放大字号。

### button-primary

`{components.button-primary}` 是红底纸字、4px 墨边、`{elevation.e2}` 硬影的直角按钮，承担一屏唯一主行动，只出现一次。来源 `bg-[#cc0000] text-[#f2e8d5]` 与 `padding 12px 28px` 原样落进 token；内部必须有 `group` 包裹的绝对定位覆盖层，从 -100% 横扫到 0，文字保持在 `relative z-10` 的层里。次按钮用墨底纸字，尺寸一致；按下时两色互换。

### tag

`{components.tag}` 用 `{colors.ink}` 底、`{colors.canvas}` 字、0px 圆角、4px 墨边，只标注事实。它不放在标题前当装饰序言，也不承担正文；中文标签把 0.08em 字距归零。

## Do's and Don'ts

### Do

- 纸底上同时出现红、墨两色，红色只给一个主行动与一处斜楔。
- 所有内容容器用 4px 墨线、0px 圆角；硬影模糊半径恒为 0。
- 标题压到 72px/900、行高 0.95、静态倾斜 -2°；拉丁大字直接写大写。
- hover 用 100ms linear 的色块侵入与 4px 斜向位移，按下做红黑反转。
- 图片只做 3:2 硬边黑白裁切，粗网点只在图片块内、面积 ≤20%。

### Don't

- 不要用 #FFFFFF 画布或 #000000 墨色——前者触犯本库 The Floor，后者来源风格卡的显式 hex 其实是 #1A1A1A。
- 不要引入第四种颜色（金星 #D4A843、棕色 #8B4513、群青、金黄）；来源把「超过三色体系」列为绝对禁止。
- 不要用圆角、柔和阴影、居中发光、渐变、玻璃高光、模糊与有机曲线——来源逐条点名。
- 不要把过渡做成长于 100ms 或使用 ease-in-out / 弹簧——来源要求「机械的，不是流畅的」。
- 不要把历史海报、政治标识、真实品牌商标或号令式政治口号搬进页面；辞典明确提醒宣传联想需要伦理检查。
- 不要居中对称三等分、不要让装饰压住正文、不要三张卡同时倾斜不同角度——那会消解对角线主轴。
- 不要拿它做长文、文档、密集后台、表单流程与金融医疗政务页面——号令式字体会直接损害扫读与可信度。

## Chinese Typography

- 中文正文行高不低于 1.7（18px × 1.7），标签 14px/1.5 也不低于 1.5。
- 中西文之间留四分之一个空格：`三色封顶`、`用 Impact`。
- 使用全角标点，段落不首行缩进，启用避头尾；标题不用引号包整句。
- display 的 -0.03em 负字距对中文减半到 -0.015em，label 的 0.08em 正字距在中文归零，避免挤字与拉散。
- 中文字重只有 400/700 两档可靠；本风格取 700 作正文、900 作标题，后者靠 Pascal/Arial Narrow 回退到中文字库时的合成重量，真机需复核。
- 72px display 只给拉丁短词；中文标题降到 `{typography.headline}` 36px，避免宽字面撑破 1200px 容器。中文标题同样保留 -2° 静态倾斜，但不加旋转动画。

## When to Use

**用**：文化活动与展览活动页、产品/影片/演出发布页、主张鲜明的宣言式落地页、体育与音乐赛事宣传页、需要一屏建立强烈态度的作品集首屏。

**别用**：长文阅读与论文、产品文档与帮助中心、高密度后台与数据表格、表单密集的办事流程、金融医疗法律等需要克制可信的场景、政务与官方公告、需要平等比较多个选项的页面。

## Iteration Guide

1. 一次只改一个组件，用 `{components.button-primary}` 指代它；不要同时动配色、字阶与斜楔角度。
2. 所有值走 token，不写裸 hex；想加第四种颜色前，先确认红与墨哪一个是被误用成了装饰。
3. 想加强风格时先把 4px 边框、-2° 倾斜与 100ms linear 调准，最后才考虑加图元——加色和加图元都容易破功。
4. 新增装饰前先跑删除测试：删掉它读者会不会失去方向或主行动理解；不会就删掉。
5. 改完必须重跑 `designlib check` 并重新截图；红楔面积与网点密度是否过头只能靠真实渲染判断。

## Known Gaps

- 只覆盖静态海报变体；stylekit 的圆盘公转、三角钟摆、方块行进与 expo-out 入场未迁移，若要做动态版本应另开风格而不是改本风格的 token。
- 三份来源的色板互相冲突：风格卡是 #CC0000/#F2E8D5/#1A1A1A 加金棕点缀，indexstyle 是 #d8251d/#e8ddc7/#11100e，stylekit 是 #E0231B/#EFE9DC/#17130E 加群青与金黄。本库以面向网页、给出完整 CSS 变量的风格卡为准，已在 NOTES「弃」记录。
- 来源对阴影的态度冲突：风格卡给 4px/6px 零模糊硬影，stylekit 完全禁止阴影，indexstyle 说 heavy shadows 默认关闭。本库取硬影，理由是零模糊不触犯 slop S7 且能区分于 memphis 的塑料贴面。
- Impact / Haettenschweiler / Arial Narrow 都不含中文；回退到 PingFang SC 后 900 字重靠合成，72px 中文标题的窄黑字面需在真机复核。
- 来源没有给出输入框、下拉、弹窗与错误态的规格；`Motion & States` 里的 disabled / error / open 三态是按本库六态要求推断的，不是来源显式值。
- 粗网点在高端屏与低端屏的呈现差异明显，关闭 GPU 合成时可能出现摩尔纹；只做静态降级，未做逐项性能开关。
- 辞典明确提醒构成主义带有强烈宣传联想；本风格只取视觉语法，不提供政治口号、历史人物与宣传画的迁移方案，使用者需自行做语境伦理判断。
