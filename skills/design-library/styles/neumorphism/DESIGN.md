---
version: alpha
name: 新拟态｜Neumorphism
description: >-
  把 2019–2021 年的 Soft UI / Neumorphism 做成一套可直接用的触控界面语言：单色暖灰底上，控件与底同色，
  靠左上高光与右下暗影这一对双向投影把按钮、卡片「压」出底面、「按」回凹槽，没有边框也没有彩色描边。
  色值取 bergside/awesome-design-skills 的 neumorphism DESIGN.md（surface #E7E5E4、text #1E2938、primary #006666、
  success #00A63D）与 stitchprompt 中文风格卡（#F1F2F5 底、左上高光右下暗影的定义、4/8/12px 圆角、8/12/24px 间距、
  Inter 字族、Good/Not-Good），圆角基准与字体分工取 opendesigner 的 Neumorphism 系统（22px 圆角、Inter/SF Mono、
  16px base）；阴影的偏移—模糊关系由 neumorphism.io 官方生成器默认参数（20px 偏移 / 60px 模糊、双向异色）标定。
  为符合本库 The Floor，纯白高光只走阴影不走背景、纯绿 #00A63D 调深到 #0B7A32、中文正文上提到 18px/1.7、
  等宽不当正文戏服、色板收敛到「一族中性 + 青 + 绿」三族，标为 beta/variant。
cues: 智能家居与硬件伴侣 App、音频播放器与可调旋钮界面、趣味小工具与计算器、需要温柔触感隐喻的展示型页面、健康与睡眠类 calm 界面
avoid: 信息密集后台与长表格、长文阅读与论文、需要精确扫读的数据看板、表单密集的办事流程、无障碍优先的长表单默认皮、高对比导向的金融医疗政务、打印为主的单栏文档
surface: light
density: medium
register: tool
family: companion
tier: variant
sourceRefs: neumorphism
status: beta

colors:
  canvas: "#E7E5E4"
  surface: "#E7E5E4"
  surface-alt: "#DAD7D3"
  ink: "#1E2938"
  ink-muted: "#4A515C"
  ink-faint: "#6B7280"
  primary: "#006666"
  on-primary: "#F4F2EA"
  accent: "#0B7A32"
  shadow-dark: "#B9B6B3"
  shadow-light: "#FFFFFF"
typography:
  display:
    fontFamily: "Inter, 'PingFang SC', 'Noto Sans SC', sans-serif"
    fontSize: 44px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.02em
  heading:
    fontFamily: "Inter, 'PingFang SC', 'Noto Sans SC', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.01em
  subheading:
    fontFamily: "Inter, 'PingFang SC', 'Noto Sans SC', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body:
    fontFamily: "Inter, 'PingFang SC', 'Noto Sans SC', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: 0
  label:
    fontFamily: "Inter, 'PingFang SC', 'Noto Sans SC', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.02em
  micro:
    fontFamily: "Inter, 'PingFang SC', 'Noto Sans SC', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
rounded:
  none: 0px
  sm: 8px
  md: 16px
  card: 22px
  pill: 999px
spacing:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  xxl: 32px
  section: 56px
  sidebar: 224px
  page: 1080px
  measure: 34em
components:
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: 24px
    shadow: "{elevation.e2}"
  button-primary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "12px 24px"
    shadow: "{elevation.e1}"
  tag:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.micro}"
    rounded: "{rounded.pill}"
    padding: "6px 12px"
    shadow: "{elevation.e3}"
  panel-inset:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: 16px
    shadow: "{elevation.e3}"
elevation:
  lightSource: top-left
  steps: 3
  e1: "6px 6px 12px {colors.shadow-dark}, -6px -6px 12px {colors.shadow-light} —— 小按钮与开关的凸起"
  e2: "12px 12px 24px {colors.shadow-dark}, -12px -12px 24px {colors.shadow-light} —— 卡片与面板的凸起"
  e3: "inset 5px 5px 10px {colors.shadow-dark}, inset -5px -5px 10px {colors.shadow-light} —— 输入框、凹槽与按下态"
  topHighlight: "-1px -1px 2px {colors.shadow-light} —— 左上受光的一条高光"
  separator: shadow
media:
  logoType: wordmark
  logoRule: "字标用 {typography.heading} 的 Inter 粗体短词，右侧留 0.5em；不缩放不小于 96px；不搬任何品牌徽标"
  imageRadius: "{rounded.card}"
  imageRatio: "1:1"
  imageTreatment: "图片压进内凹面板，去饱和 8%，只保留自然光影；不描边、不加投影"
  background: "单色 {colors.canvas} 铺满视口，无纹理无渐变；层级全靠双向阴影与同色明度差"
  iconRule: "1.8px 线性描边、24px 基准，与 {colors.ink} 同色；旋钮与滑杆用同色光影不用彩色填充"
  emptyState: "{colors.surface-alt} 凹槽底 + 一行 {colors.ink-muted} 说明，不放插画与吉祥物"
motion:
  easing: "cubic-bezier(0.2, 0.8, 0.2, 1)"
  durationFast: 120ms
  durationBase: 200ms
  hover: "凸起阴影微增一档，位移 0；不换色不放大"
  focusRing: "2px solid {colors.primary}，offset 3px，画在双向阴影之外"
  openTransition: "面板凸起态从 {elevation.e3} 切到 {elevation.e2}，200ms 过渡"
  reducedMotion: "过渡降到 1ms，凸起与凹槽保留静态终态，信息零丢失"
  pressUsesInset: true
---

## Overview

新拟态给智能家居控制面板、音频播放器、健康与睡眠类 calm 界面、趣味小工具，以及需要「温柔触感」隐喻的展示型页面用。它要确认的不是「这条信息被读到」，而是「这块界面是可以摸、可以按、按下去会陷进去的实体」。

性格来自四个可指认的选择。第一，控件与底同色——画布 `{colors.canvas}`（#E7E5E4）、按钮面 `{colors.surface}`（#E7E5E4）取同一个值，界面里几乎没有色差，层级全靠光影；这是 stitchprompt 说的「同色系底上让元素像从界面里长出来」。第二，一对方向相反的投影：凸起用 `{elevation.e2}`（右下暗影 + 左上高光），凹陷用 `{elevation.e3}`（右下内阴影 + 左上内高光），两者只是把阴影翻进内侧，这就是 neumorphism.io 生成器的核心参数关系。第三，光源固定在 top-left：高光永远在左上、暗影永远在右下，四处都有光就是 slop。第四，克制的一族字体与三族色彩：Inter 一族到底，中性暖灰 + 青 + 绿，青只给主操作与焦点，绿只给成功状态点。实测对比：墨色对底 11.70:1、青色对底 5.41:1、次要色 6.38:1、最弱文字 3.85:1。

读者先看到暖灰底上「浮起」的卡片与胶囊按钮，再按「侧栏导航 → 主标题 → 一排凸起卡片 → 凹槽状态区」的顺序读，按下去的控件会陷入底面。彩色在这里是稀缺资源：一屏只出现一个青色主操作、至多一个绿色成功点；出现大面积彩色块、渐变或玻璃模糊，触感隐喻立刻垮掉。

与库内相近风格的分工：`soft-pastel` 是低对比柔色但靠色块与描边分层，`neumorphism` 同色无描边、只靠双向投影；`tactile-3d` 是会随指针倾斜的浮起卡片，`neumorphism` 是静止在底面上、只由按压切换的凹陷；`liquid-glass` 是半透明工作台，`neumorphism` 完全不透明、不透视背景。

**Key Characteristics**

- 画布与控件同色 `{colors.canvas}` / `{colors.surface}`（#E7E5E4）——bergside 显式 surface 值，暖灰避开纯白，控件靠阴影浮起而非色差。
- 唯一主色 `{colors.primary}`（#006666，青）——bergside 显式 primary，只在主操作、链接与焦点环出现，对底 5.41:1。
- 状态绿 `{colors.accent}`（#0B7A32）——来源 #00A63D 调深，只做成功点与图标描边，4.35:1 满足非正文图形 ≥3:1。
- 一对双向阴影 `{elevation.e2}` / `{elevation.e3}`——凸起与凹陷只差 inset 方向与偏移正负，是全风格的材质语法。
- Inter 一族到底，六档字号 44/32/24/18/14/11px，中文正文 18px/1.7，字重只有 700 与 400。
- 圆角偏大：卡片 22px、按钮与标签 pill、面板 16px；不用尖角，直角会划破柔软感。
- 主分隔手段只有 shadow：没有边框线、没有色差分隔带。

## Colors

**Canvas & Surface**

- `{colors.canvas}` — #E7E5E4，页面底。bergside 的 `surface` 显式值；暖灰不是纯白，符合 The Floor 第 2 条，墨色在其上 11.70:1。
- `{colors.surface}` — #E7E5E4，按钮、卡片、面板的面，与画布同值。这是新拟态的定义：控件从底面浮起而不是贴一块异色板；层级交给 `{elevation.e2}`。
- `{colors.surface-alt}` — #DAD7D3，凹槽底（输入框、按下态、标签）。由画布向暗调一档的推断值，对底 1.14:1，只表达「陷进去」，不承载正文。

**Ink**

- `{colors.ink}` — #1E2938，标题与正文。bergside 显式 `text` 值，偏冷的深墨而非纯黑；对底 11.70:1、对凹槽底 10.04:1。
- `{colors.ink-muted}` — #4A515C，次要说明与标签。推断的中灰墨，对底 6.38:1。
- `{colors.ink-faint}` — #6B7280，最弱说明与禁用文字。推断值，对底 3.85:1，满足非正文 ≥3:1 的门槛。

**Accent**

- `{colors.primary}` — #006666，青色主操作、链接与焦点环。bergside 显式 `primary`；对底 5.41:1、对凹槽底 4.64:1。
- `{colors.on-primary}` — #F4F2EA，压在青底上的字。暖白而非纯白，对青底 6.06:1；青底本身 rarely 大面积出现，只做按钮态。
- `{colors.accent}` — #0B7A32，成功状态点与图标描边。由来源绿 #00A63D 调深而来——原值对底仅 2.56:1，调深后 4.35:1；只走 ≥14px 图形与非正文状态，不承载段落。
- `{colors.shadow-dark}` — #B9B6B3，右下暗影。由 neumorphism.io 底 #e0e0e0 配 #bebebe 的关系平移到本底 #E7E5E4 的推断值；对底 1.61:1，只走阴影。
- `{colors.shadow-light}` — #FFFFFF，左上高光。neumorphism.io 显式高光色；只走阴影变量，不作任何背景或文字色，避开 The Floor 第 2 条。

不设第二强调色：来源的 warning #FE9900、danger #FF2157 与多色语义态全部弃用，见 NOTES「弃」与 `Known Gaps`。

## Typography

字号六档：display 44px、heading 32px、subheading 24px、body 18px、label 14px、micro 11px。相邻比值 1.375 / 1.33 / 1.33 / 1.29 / 1.27，全部不低于 LAYERS 的 1.25。来源 stitchprompt 给标题 32px / 正文 16px / 标签 13px、bergside 给 h1 3rem / body 1rem / label 0.75rem；本库把正文从 16px 提到 18px 满足中文下限，44px 是来源 48px 向字阶靠拢的推断档，micro 11px 沿用来源 0.75rem 附近的小字。

字重只有两档：700 给 display / heading / subheading，400 给 body / label / micro。来源 bergside 声明 100–900 全档、stitchprompt 给粗体/常规/中等三档；本库按 §11 收敛到两档，避免中间字重在中文回退时丢失。字族一族到底：Inter → PingFang SC → Noto Sans SC → sans-serif，来源 stitchprompt 与 opendesigner 都用 Inter，不引入 Space Mono 当正文戏服；代码片段若出现才走系统的等宽栈。

11px 只给时间戳与状态刻度，不写中文句子；中文界面标签 14px/1.5，正文 18px/1.7。字距只有 display -0.02em、heading -0.01em 两档负值与 label/micro 0.02em 微正，body 与 subheading 全为 0——柔软界面不靠拉字距制造气质。

## Layout

- 页面最大宽 `{spacing.page}` 1080px，tool 模板的双栏工作台隐喻；两侧留 `{spacing.xl}` 24px。
- 两列：左侧 `{spacing.sidebar}` 侧栏导航，右侧主工作区；列间距 `{spacing.xl}` 24px。768px 以下折成单列。
- 间距阶 4 / 8 / 12 / 16 / 24 / 32 / 56px，基数 4px 来自 stitchprompt 的 8/12/24 与 bergside 的 4/8；卡片内边距 24px，凹槽区 16px。
- 卡片一排三格，间距 `{spacing.md}` 12px；每张卡片内部标题与正文之间留 `{spacing.sm}` 8px。
- 正文最大宽 `{spacing.measure}` 34em（18px × 34 ≈ 612px），不铺满整屏。
- 分隔只靠阴影：凸起卡片与凹槽面板之间不画线，靠 `{elevation.e2}` 与 `{elevation.e3}` 的明暗方向区分。

## Elevation & Depth

层级是这套风格的全部。`{elevation.lightSource}` 固定 top-left：任何凸起都是右下 `{colors.shadow-dark}` 暗影配左上 `{colors.shadow-light}` 高光，任何凹陷都把这一对翻进内侧。光源指认不出来，就不是新拟态而是普通灰卡片。

三级阶梯：`{elevation.e1}` 给小按钮、开关与胶囊标签（6px 偏移 / 12px 模糊）；`{elevation.e2}` 给卡片与面板（12px 偏移 / 24px 模糊）；`{elevation.e3}` 给凹槽、输入框与按下态（`inset`，5px 偏移 / 10px 模糊）。偏移与模糊的比例遵循 neumorphism.io 官方生成器默认「20px 偏移 / 60px 模糊」的 1:3 关系，本库按控件尺寸等比缩小到 1:2。

`{elevation.separator}` 只选 shadow：不用 border、不用色差带。没有 `0 0 Npx` 居中发光——所有投影都有右下或左上的明确偏移。

## Shapes

圆角策略是分层偏大：卡片 `{rounded.card}` 22px（opendesigner 显式默认 22px），按钮与标签 `{rounded.pill}` 全圆角，面板与凹槽 16px，小徽标 8px。不使用 0px 尖角——直角会划破塑料般的柔软感；也不混用 0px 与 pill 制造「一半硬一半软」的冲突。

形状以胶囊与圆角矩形为主：主操作按钮高度由 14px 字与 padding 撑到约 42px，宽度按内容走；开关是 44×24px 胶囊；标签是 pill 小片。图标走 1.8px 线性描边、24px 基准，与正文同色，不做彩色填充徽标。

## Material & Elevation

材质是一整块柔软的哑光塑料：画布、卡片、按钮同色，靠光从 top-left 单一方向照下来产生「浮起」与「陷下」。`{elevation.topHighlight}` 是左上那一条高光，右下收一条暗影；四处同时有光就是 slop。

面板层级不靠明度阶梯堆色，而靠投影是否 inset：凸起＝非 inset 的双向投影，凹陷＝inset 的双向投影，按下态就是把 `{elevation.e2}` 切成 `{elevation.e3}`，200ms 过渡。唯一允许的色差是 `{colors.surface-alt}` 对底 1.14:1 的凹槽底，它只说明「这里是坑」，不承担分层。出现彩色渐变、玻璃模糊、金属光泽或描边即破功。

## Mark & Media

标识：`{media.logoRule}`（`{media.logoType}`）；不搬任何硬件品牌徽标，只迁移排字规则。图片：比例 `{media.imageRatio}`、圆角 `{media.imageRadius}`、处理 `{media.imageTreatment}`；删除测试问的是「删掉这张图，读者是否失去操作入口或状态理解」，四问皆否就删掉。背景：`{media.background}`。图标：`{media.iconRule}`。空态：`{media.emptyState}`。

每张媒体都有静止帧：图片未加载时凹槽底与文字标签仍在，主任务可完成；`prefers-reduced-motion` 下按压切换为 1ms 静态终态，凸起/凹陷信息不丢失。文字、按钮、表单、数据标签一律真实 HTML/CSS 排版，不让生图模型画字。

## Motion & States

过渡曲线 `{motion.easing}`，快档 `{motion.durationFast}` 120ms、基准 `{motion.durationBase}` 200ms；来源是克制的触感界面，只有按压切换与 hover 微增一档阴影两处动效。hover：`{motion.hover}` 阴影微增、位移 0、不换色。焦点：`{motion.focusRing}` 2px 青色环画在双向阴影之外，offset 3px，不被阴影吞掉。展开：`{motion.openTransition}` 面板由凹陷切到凸起。按压：`{motion.pressUsesInset}` 为 true，active 时阴影翻成 inset，就是「按下去陷进去」。

交互组件逐项覆盖六态：default 为凸起 e2 与青色主操作；hover 阴影微增一档；focus-visible 加青色焦点环；active 切 inset e3、文字略微位移 0；disabled 用 `{colors.ink-faint}` 虚化文字、保留凸起轮廓、不靠降低透明度；error 用 `{colors.ink}` 一行说明配凹槽底，不新增警示色。

`prefers-reduced-motion` 时执行 `{motion.reducedMotion}`：过渡降到 1ms，凸起与凹陷保留静态终态。没有拖拽手势组件，按压是即时状态切换不是弹簧动画。

## Components

### button-primary

`{components.button-primary}` 是与底同色的胶囊按钮，青字 `{colors.primary}`、`{elevation.e1}` 双向阴影、pill 圆角、padding `12px 24px`、标签用 `{typography.label}`。hover 阴影微增，active 切成 `{elevation.e3}` inset，focus 加青色环；不做彩色填充、不做渐变。

### card

`{components.card}` 是 `{colors.surface}` 底、`{elevation.e2}` 凸起的圆角卡片，padding 24px、圆角 22px。卡片内部标题 `{typography.subheading}`、正文 `{typography.body}`；一屏最多三张并列，靠阴影而不是边框分区。

### tag

`{components.tag}` 用 `{colors.surface-alt}` 凹槽底、`{colors.ink-muted}` 字、pill 圆角、shadow `{elevation.e3}`，padding `6px 12px`。它是状态标记，不放在标题前宣布「下面是内容」；中文标签字距保持 0.02em。

### panel-inset

`{components.panel-inset}` 是凹槽面板，`{colors.surface-alt}` 底配 `{elevation.e3}`，圆角 16px、padding 16px，放输入框、开关组与「当前需要你决定」一类的确认区。它与凸起卡片是同一材质的一对反面，不叠加边框。

## Do's and Don'ts

### Do

- 画布与控件保持同色 `{colors.canvas}` / `{colors.surface}`，让层级只由双向投影表达。
- 光源固定在 top-left：凸起右下暗左上亮，凹陷把这一对翻进内侧。
- 一屏一个青色主操作、至多一个绿色成功点；其余全部中性灰墨。
- 中文正文 18px/1.7，界面标签 14px/1.5，11px 只给数字与时间戳。
- 按压动作用 inset 阴影切换，focus 环画在阴影之外。

### Don't

- 不要用彩色渐变、玻璃模糊、金属光泽——同色哑光塑料被取代，触感隐喻立刻消失。
- 不要用描边或色差带分隔——主分隔只有 shadow，加线会让「浮起」读成「框起来」。
- 不要用纯白背景或纯黑文字——来源纯白只走高光阴影、来源黑色换成深墨 `{colors.ink}`。
- 不要把 Space Mono / JetBrains Mono 当正文戏服；来源等宽字只适合代码片段。
- 不要用尖角混 pill、不要 0 0 Npx 居中发光、不要四处同时出现在阴影高光。
- 不要拿它做长文阅读、数据看板、密集表单与无障碍优先的长表单——低对比同色与凸起装饰会持续抢注意。

## Chinese Typography

- 中文正文行高 `{typography.body}` 的 1.7（18px × 1.7 = 30.6px），不低于 1.7 下限；界面标签 14px/1.5 不低于 1.5。
- 中西文之间留四分之一个空格：`24px 基准`、`用 Inter`；中文段落不首行缩进，启用避头尾，使用全角标点。
- 11px 只给时间戳与数字刻度，不写中文句子；中文标题降到 `{typography.heading}` 32px 仍用 700 粗体。
- Inter 不含中文，回退到 PingFang SC / Noto Sans SC；中文字重只有 400/700 两档可靠，不用 500/600。
- 负字距只给 display -0.02em 与 heading -0.01em，中文标题退回 0；拉大中文小标签字距会散开。
- 标题不用引号包整句；标签中文不超过 8 个字，避免 11px 小字压过正文。

## When to Use

**用**：智能家居与硬件伴侣 App、音频播放器与可调旋钮界面、趣味小工具与计算器、需要温柔触感隐喻的展示型页面、健康与睡眠类 calm 界面。

**别用**：信息密集后台与长表格、长文阅读与论文、需要精确扫读的数据看板、表单密集的办事流程、无障碍优先的长表单默认皮、高对比导向的金融医疗政务、打印为主的单栏文档。

## Iteration Guide

1. 一次只改一个组件，用 `{components.card}` 指代它；不要同时动阴影阶梯与色板。
2. 所有值走 `{token.refs}`，不写裸 hex；想加第二种强调色前，先确认青色是不是被误用成装饰。
3. 想加强触感时先把 `{elevation.e2}` 的偏移与模糊比调准，最后才考虑加图标——加描边或加渐变会直接破功。
4. 新增组件前先问：它能不能用同色 + 一对双向阴影表达；不能，再谈别的。
5. 改完必须重跑 `designlib check` 并重新截图；凸起/凹陷的读感与青绿对比只能靠真实渲染判断。

## Known Gaps

- bergside 与 stitchprompt 的底色不同（#E7E5E4 vs #F1F2F5），取 bergside 的 #E7E5E4 作画布；两者同为暖灰、都能承接双向阴影，冲突记入 NOTES「弃」。
- 来源 success #00A63D 对底仅 2.56:1，调深到 #0B7A32（4.35:1）；仍只做非正文图形，含表单的错误态需单独复核。
- 来源把 warning #FE9900 与 danger #FF2157 列为标准语义色，本库为守住三色族全部弃用；error 态借用墨色说明而非新增警示色。
- 来源字号 body 16px、label 13px，本库中文正文提到 18px/1.7、标签提到 14px/1.5；这是可访问性改造，不是原尺寸。
- 来源声明 100–900 九档字重，本库收敛到 700/400 两档；中文回退字体缺中间字重是原因。
- 来源的「按压陷入」依赖 3D 触控与设备振动反馈，Web 预览只有阴影切换，没有真实的力反馈。
- Web 预览里卡片与按钮都不响应指针倾斜；`tactile-3d` 才承担动效倾斜的职责，两者不要混用。
- 截图环境可能缺 Inter；中文回退到系统黑体后，柔软字腔会减弱，需在真机复核。
