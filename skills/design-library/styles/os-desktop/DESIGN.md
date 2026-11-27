---
version: alpha
name: 桌面窗口｜OS Desktop
description: >-
  把浏览器当作一台电脑：青绿墙纸上浮着带标题栏、斜边和任务栏的窗口，每个区块是一个「应用」而不是一张卡片。
  显式参数取自 aesthetic.fyi 的 OS Desktop 风格页（青绿 #008080、标题栏灰渐变、系统字体栈、任务栏、图标网格、
  Good For / Not For）、IndexStyle 的 Windows 95 Interface 辞典（四色刻边、内外双线、4px 间隙、单一字号与粗体强调、
  按下明暗对调、禁圆角与柔影）、Win95 Web Designer 技能卡（11 色调色板、Tahoma 11px、28px 任务栏、
  32×32 图标、2px 4px 8px 间距阶与反模式）与 98.css 所引 Microsoft Windows User Experience（75×23px 按钮、
  焦点虚线内缩 4px、按下斜边反转）。为符合本库 The Floor，窗口内容用暖纸白而非纯白，标题栏浅蓝端调深到
  #0A5FA8 保证 11px 浅字 5.83:1，中文正文提到 18px/1.7，标为 beta/variant。
cues: 复古计算与数字博物馆展页、开发者个人站与作品集、怀旧活动与游戏化产品页、需要展示多窗口工作状态的实验界面、计算史教学页面
avoid: 企业 SaaS 与业务后台、移动优先的消费 App、电商与结算流程、极简品牌官网、长文新闻与文档、无障碍优先的长表单、需要精确扫读的数据表格
surface: mixed
density: medium
register: tool
family: retro
tier: variant
sourceRefs: os-desktop
status: beta

colors:
  canvas: "#F4F2EA"
  surface: "#DFDFDF"
  surface-alt: "#C0C0C0"
  desktop: "#008080"
  ink: "#1A1A1A"
  ink-muted: "#3D4A4A"
  ink-faint: "#5C6A6A"
  primary: "#000080"
  on-primary: "#F4F2EA"
  title-light: "#0A5FA8"
  title-inactive: "#808080"
  highlight: "#FFFFFF"
  shadow: "#808080"
  dark-shadow: "#000000"
typography:
  display:
    fontFamily: "Tahoma, 'Segoe UI', Arial, 'PingFang SC', 'Microsoft YaHei', sans-serif"
    fontSize: 44px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0
  heading-lg:
    fontFamily: "Tahoma, 'Segoe UI', Arial, 'PingFang SC', 'Microsoft YaHei', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  heading:
    fontFamily: "Tahoma, 'Segoe UI', Arial, 'PingFang SC', 'Microsoft YaHei', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  subheading:
    fontFamily: "Tahoma, 'Segoe UI', Arial, 'PingFang SC', 'Microsoft YaHei', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body:
    fontFamily: "Tahoma, 'Segoe UI', Arial, 'PingFang SC', 'Microsoft YaHei', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: 0
  label:
    fontFamily: "Tahoma, 'Segoe UI', Arial, 'PingFang SC', 'Microsoft YaHei', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  micro:
    fontFamily: "Tahoma, 'Segoe UI', Arial, 'PingFang SC', 'Microsoft YaHei', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0
rounded:
  none: 0px
  control: 0px
spacing:
  micro: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  xxl: 32px
  bar: 28px
  section: 56px
  sidebar: 224px
  page: 1080px
  measure: 34em
components:
  window:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 16px
    border: "2px 双色斜边：上左 {colors.highlight}、下右 {colors.dark-shadow}"
  button-primary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.control}"
    padding: "4px 12px"
    border: "2px 凸起斜边，按下时明暗对调"
  tag:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
  status-bar:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "8px 16px"
elevation:
  lightSource: top-left
  steps: 3
  e1: "inset -1px -1px 0 {colors.dark-shadow}, inset 1px 1px 0 {colors.highlight}, inset -2px -2px 0 {colors.shadow}, inset 2px 2px 0 {colors.surface} —— 凸起按钮与窗口外框"
  e2: "inset 1px 1px 0 {colors.shadow}, inset -1px -1px 0 {colors.highlight}, inset 2px 2px 0 {colors.dark-shadow}, inset -2px -2px 0 {colors.surface-alt} —— 内凹输入框与列表面板"
  e3: "2px 2px 0 {colors.dark-shadow} —— 窗口硬投影，无模糊无发光"
  topHighlight: "inset 1px 1px 0 {colors.highlight} —— 左上受光的一条白线"
  borderLight: "{colors.highlight}"
  borderDark: "{colors.dark-shadow}"
  separator: border
media:
  logoType: wordmark
  logoRule: "字标写成 Tahoma 11px 粗体短词，右侧留 0.5em；只迁移排字规则，不复制 Windows 旗标、开始按钮或任何厂商徽标"
  imageRadius: "{rounded.none}"
  imageRatio: "32:32（大图标）/ 16:16（小图标）"
  imageTreatment: "图标是 32×32 与 16×16 的直线方块画，1px 墨线、无抗锯齿、无柔化；照片不进窗口，需要配图时只用 1px 线稿"
  background: "{colors.desktop} 青绿墙纸实色铺满视口，无渐变无纹理；窗口以 2px 双色斜边浮在墙纸上"
  iconRule: "32px 大图标配 14px 标签，16px 小图标配 11px 标签；选中只换 {colors.primary} 底与 {colors.on-primary} 字，不加圆角不加光晕"
  emptyState: "{colors.surface-alt} 底 + 1px 内凹边框 + 一行 {colors.ink-muted} 说明，不放插画或空状态吉祥物"
motion:
  easing: linear
  durationFast: 0ms
  durationBase: 100ms
  hover: "按钮底色从 {colors.surface} 立即切到 {colors.surface-alt}，链接立即换 {colors.primary} 底；没有位移、没有缓动"
  focusRing: "1px dotted {colors.ink}，outline-offset -4px（98.css 显式：焦点虚线内缩 4px）"
  openTransition: "开始菜单与窗口即时出现，不做 scale 或淡入；推断给状态切换 100ms linear 只做色值切换"
  reducedMotion: "所有过渡降到 0ms，斜边、标题栏渐变与焦点虚线保留静态终态，信息零丢失"
  dragUsesSpring: false
---

## Overview

桌面窗口给复古计算展页、开发者个人站、怀旧活动页、计算史教学页，以及需要「一台机器里同时开着几个程序」叙事的实验界面用。它要确认的不是「这条信息被读到」，而是「你正坐在一台 1995 年的电脑前」。

性格来自五个可指认的选择。墙纸 `{colors.desktop}`（#008080）是 aesthetic.fyi 显式给出的青绿桌面，窗口覆盖在它之上；活动窗口标题栏用 `{colors.primary}`（#000080）到 `{colors.title-light}`（#0A5FA8）的 90° 蓝到蓝渐变，浅端由来源的 #1084D0 调深，让 11px 纸色标题达到 5.83:1；所有边界是 2px 外双线加 1px 内双线的斜边，靠明暗方向而不是阴影表达「能按」；字体只有一族系统无衬线，11px/14px 两档界面字阶与 18px 正文；任务栏固定在视口底部，`{spacing.bar}` 28px 高，符合来源显式值。实测对比：墨色对纸白 15.53:1、对按钮面 13.06:1、青绿对纸白 4.26:1；浅蓝端对纸色 5.83:1，深端 14.28:1。

读者先看到青绿桌面上的窗口轮廓与蓝色标题栏，再按「左侧程序列表 → 主窗口标题 → 三格列表视图 → 底部状态栏」的顺序读，最后才注意到底部任务栏。圆角、柔影、玻璃和彩色插画一律不出现——IndexStyle 明确说，只抄灰色和两道线却添圆角或柔影，刻痕的方向就读不出来。

与库内相近风格的分工：`pixel-arcade` 是 8-bit 游戏的像素网格，`os-desktop` 是 GUI 的窗口与任务栏；`terminal-mono` 只有一层文本流，`os-desktop` 靠层叠窗口和焦点表达多任务；`quiet-dark` 与 `codex-workbench` 是现代工作台的克制面板，`os-desktop` 把控件装饰当作主角。

**Key Characteristics**

- 青绿墙纸 `{colors.desktop}`（#008080）上浮 `{colors.canvas}`（#F4F2EA）纸白窗口；纸白是来源纯白的暖化，不是新增色相。
- 活动标题栏的蓝到蓝渐变 `{colors.primary}` → `{colors.title-light}`，非活动标题栏退回 `{colors.title-inactive}` 灰。
- 2px 外双线 + 1px 内双线斜边：凸起、内凹、按下三态只翻转明暗方向，不用投影表达按压。
- Tahoma 一族到底；界面 11/14px，中文正文 18px/1.7，字重只有 400 与 700。
- 4px 间距基数、2/4/8/12/16/24/28/32px 阶；窗口最大宽 `{spacing.page}` 1080px。
- 全部圆角为 `{rounded.none}` 0px；唯一的阴影是 `{elevation.e3}` 2px 无模糊硬投影。

## Colors

**Canvas & Surface**

- `{colors.canvas}` — #F4F2EA，窗口内容底。来源给的是 #FFFFFF，本库按 The Floor 第 2 条暖化为偏灰的纸白；墨色在其上 15.53:1。
- `{colors.surface}` — #DFDFDF，按钮面与斜边亮阶。技能卡显式 `Button Face #dfdfdf`；墨色在其上 13.06:1。
- `{colors.surface-alt}` — #C0C0C0，系统灰、任务栏与状态栏底。技能卡显式 `System Gray #c0c0c0`；墨色在其上 9.57:1。
- `{colors.desktop}` — #008080，墙纸。aesthetic.fyi 与技能卡双源显式；对纸白 4.26:1，只承载图形与窗口间隙，不放正文。

**Ink**

- `{colors.ink}` — #1A1A1A，标题与正文。由来源黑色（#000000 深影）向主色偏一档得到，避免裸纯黑；对纸白 15.53:1。
- `{colors.ink-muted}` — #3D4A4A，状态栏与次要说明。推断的青灰，对纸白 8.23:1；来源没有独立次要色。
- `{colors.ink-faint}` — #5C6A6A，禁用文字与最弱标签。推断值，对纸白 5.03:1，满足 ≥3:1 的非正文门槛。

**Line & Accent**

- `{colors.primary}` — #000080，活动标题栏起点、选中项底与链接强调。技能卡显式 `Title Blue (Dark)`；对纸白 14.28:1。
- `{colors.on-primary}` — #F4F2EA，标题栏与选中项上的字；对深蓝 14.28:1。
- `{colors.title-light}` — #0A5FA8，活动标题栏浅端。由技能卡显式 #1084D0 调深的推断值：原值对纸白仅 3.58:1，调深后 5.83:1；仍在同一蓝色相内。
- `{colors.title-inactive}` — #808080，非活动窗口标题栏。aesthetic.fyi 显式「非活动窗口保持灰色」。
- `{colors.highlight}` — #FFFFFF，只走 1px 上/左斜边，不作背景；与 `{colors.shadow}` 同值族构成外内双线。
- `{colors.shadow}` — #808080，下/右中灰斜边，来源显式 `Button Shadow`。
- `{colors.dark-shadow}` — #000000，只走 1px 外缘与 2px 硬投影，来源显式 `Button Dark Shadow`；不作大面积底。

不设第二强调色：黄/红状态色与 Plus! 主题全部弃用，详见 NOTES「弃」与 `Known Gaps`。

## Typography

字号七档：display 44px、heading-lg 32px、heading 24px、subheading 18px、body 18px、label 14px、micro 11px。相邻比值 1.375、1.33、1.33、1.29、1.29、1.27，全部不低于 LAYERS 的 1.25。11px 与 14px 是技能卡显式界面字号，18px 正文是本库为满足中文 ≥18px/1.7 从来源 11px 上提的档位，44/32/24px 是为网页标题补足的推断档。

字重只有两档：700 给 display / heading-lg / heading / subheading / micro，400 给 body / label；与 IndexStyle「字号只留一种，强调只用粗体」的精神一致，只是本库按网页层级扩展了字号。字族一族到底：Tahoma → Segoe UI → Arial → PingFang SC → Microsoft YaHei → sans-serif；来源的系统字体栈只取「无装饰、功能字」这条规则，不引入 Fixedsys 等专属字形资产。

11px 只给窗口控制符与状态栏刻度，不承载中文段落；中文界面标签用 14px/1.5，中文正文 18px/1.7。全部档位字距为 0——Win95 的点阵字靠字形本身，不靠拉字距制造气质。

## Layout

- 页面最大宽 `{spacing.page}` 1080px，来自风格卡与技能卡的桌面隐喻；两侧留 `{spacing.xl}` 24px。
- 桌面分两层：底部 `{spacing.bar}` 28px 任务栏常驻，其余是窗口工作区；来源显式「画面分成下端的带子和工作区两层」。
- 工作区两列：左侧 `{spacing.sidebar}` 224px 程序窗口，右侧主窗口；列间距 `{spacing.xl}` 24px。768px 以下折成单列。
- 间距阶 2 / 4 / 8 / 12 / 16 / 24 / 28 / 32px，基数 4px 来自技能卡；部件间隙压到 4px 上下，来自 IndexStyle。
- 主窗口内部：标题栏高 28px，内容区上下留 `{spacing.lg}` 16px，列表视图三格并列、格间距 `{spacing.sm}` 8px。
- 桌面图标固定在左上 `{spacing.md}` 12px 处，32px 方块按 2 列排布；不产生横向溢出。
- 正文最大宽 `{spacing.measure}` 34em（18px × 34 ≈ 612px）；虽然窗口很宽，正文仍不全宽铺开。
- 主分隔手段只有 `border`：2px 刻边与 1px 内线，投影只说明「窗口浮在墙纸上」。

## Elevation & Depth

层级不靠柔影，靠斜边明暗方向。`{elevation.lightSource}` 固定 top-left：上左总是 `{colors.highlight}`，下右总是 `{colors.dark-shadow}`；按下时两者对调，这就是 IndexStyle 说的「按下的瞬间明暗对调」。

三级阶梯：`{elevation.e1}` 是凸起按钮与窗口外框的四层 inset 斜边；`{elevation.e2}` 是内凹输入框、列表面板与状态栏的反向 inset；`{elevation.e3}` 是窗口右下 2px 无模糊硬投影，来源技能卡明确 `box-shadow: 2px 2px 0 #000000`。没有 `0 0 Npx` 发光，没有半透明高斯模糊。

`{elevation.separator}` 只选 border：斜边是主分隔器，墙纸与纸白的色差是辅助；投影不承担分栏。

## Shapes

圆角策略是「没有圆角」：窗口、按钮、标签、输入框、图标一律 `{rounded.none}` 0px / `{rounded.control}` 0px。IndexStyle 直接点名「添上圆角或柔和的阴影，刻痕的方向就读不出来」。禁止 pill 按钮、圆角卡片、圆形头像和任意 >0 的 border-radius。

形状只有矩形与 2px 斜边：控制按钮 16×16px 方块，标准按钮最小 75×23px（98.css 引 Microsoft 显式值，本库宽度用 75px、高度由 14px 字与 padding 推出 23px），桌面图标 32×32px。三个窗口控件并排右上，间距 2px；不做圆点式 macOS 控件。

## Material & Elevation

材质是喷绘点阵屏上的灰色金属面板：青绿墙纸是印刷色，窗口是灰白塑料，标题栏是一条蓝漆。光从左上单一方向来：`{elevation.topHighlight}` 是 1px 白线上沿，右下收 1px 黑线与 2px 硬投影，四个方向不会同时有光。

面板的层级靠明度阶梯表达：`{colors.surface}` → `{colors.surface-alt}` → `{colors.shadow}` → `{colors.dark-shadow}`。标题栏渐变限定在活动窗口，来源反模式明确「只有标题栏有渐变，其他所有地方都是纯色」。出现玻璃模糊、柔影、霓虹或圆角即破功。

## Mark & Media

标识：`{media.logoRule}`（`{media.logoType}`）；不搬 Windows 徽标、开始按钮图标或任何厂商字标，只迁移排字规则。图片：比例 `{media.imageRatio}`、圆角 `{media.imageRadius}`、处理 `{media.imageTreatment}`；删除测试问的是「删掉这个 32px 图标，读者是否失去程序身份或选中状态」，四问皆否就删掉。背景：`{media.background}`。图标：`{media.iconRule}`。空态：`{media.emptyState}`。

每张媒体都有静止帧：图标未加载时 32px 方框与 1px 墨线仍在，文字标签照常可读；`prefers-reduced-motion` 下所有色值切换为 0ms，状态不丢失。文字、按钮、表单、数据标签一律真实 HTML/CSS 排版，不让生图模型画字。

## Motion & States

过渡曲线 `{motion.easing}`，快档 `{motion.durationFast}` 0ms、基准 `{motion.durationBase}` 100ms；来源本质是即时重绘，100ms 只用于状态色切换的推断。hover：`{motion.hover}` 按钮底色立即换一档、链接立即翻深蓝底，没有位移。焦点：`{motion.focusRing}` 1px 虚线内缩 4px，98.css 显式要求，不用外扩光环。展开：`{motion.openTransition}` 开始菜单与窗口即时出现，不做 scale 或淡入。

交互组件逐项覆盖六态：default 为凸起斜边与按钮面；hover 底色换系统灰，斜边不动；focus-visible 加内缩虚线；active 斜边明暗对调、底色更深；disabled 用 `{colors.ink-faint}` 虚化文字、保留凸起斜边，不靠降低透明度；error 用 `{colors.primary}` 1px 边框加一行 `{colors.ink}` 说明，不新增警示色。下拉/开始菜单另有 open 态：即时显示、选中行翻深蓝底。

`prefers-reduced-motion` 时执行 `{motion.reducedMotion}`：过渡降到 0ms，所有斜边、标题栏渐变与焦点虚线保留静态终态。没有拖拽手势组件，`motion.dragUsesSpring` 为 false。

## Components

### window

`{components.window}` 是 `{colors.canvas}` 底、2px 外双线斜边、1px 内线的矩形窗口；标题栏走蓝渐变、纸色 14px 粗体字，右上角三个 16×16px 控制方块。右下角 `{elevation.e3}` 2px 硬投影说明它浮在墙纸上。非活动窗口标题栏退 `{colors.title-inactive}` 灰。

### button-primary

`{components.button-primary}` 是 `{colors.surface}` 底、`{colors.ink}` 字、2px 凸起斜边、最小 75×23px 的方块按钮，padding `4px 12px`，标签用 `{typography.label}`。hover 底色翻系统灰，active 斜边明暗对调，focus 内缩 1px 虚线；不做圆角、不做阴影位移。

### tag

`{components.tag}` 用 `{colors.surface-alt}` 底、`{colors.ink}` 字、0px 圆角、1px 内凹线，padding `2px 8px`。它是状态栏标记或文件类型标签，不放在标题前宣布「下面是内容」；中文标签把字距保持为 0。

### status-bar

`{components.status-bar}` 是窗口底部 `{colors.surface-alt}` 灰带、1px 上内线、padding `8px 16px`，放当前窗口数与提示。信息密度按 14px/1.5 控制，不塞第二段说明。

## Do's and Don'ts

### Do

- 墙纸用 `{colors.desktop}` 青绿实色，窗口用 `{colors.canvas}` 暖纸白；两色都不走渐变。
- 活动标题栏才走蓝渐变；渐变只在窗框上沿出现，浅端用调深后的 `{colors.title-light}`。
- 每条边界用 2px 外双线 + 1px 内双线，左上角亮、右下角暗，按下时对调。
- 文字只用 Tahoma 一族；11px 给控制符与刻度，14px 给界面标签，18px/1.7 给中文正文。
- 交互即时重绘，焦点是内缩 4px 的 1px 虚线，投影只留 2px 硬边。

### Don't

- 不要圆角、柔影、玻璃模糊、霓虹与渐变墙纸——IndexStyle 说这会抹掉刻痕方向，风格立刻垮掉。
- 不要用汉堡菜单、悬浮操作按钮或圆角卡片布局——技能卡列为三大反模式；用开始按钮、工具栏按钮与窗口列表。
- 不要把标题栏渐变铺到其他组件——来源反模式明确「只有标题栏有渐变」。
- 不要用纯白窗口背景或裸黑大面积底；本库用暖纸白与墨色，来源纯白/纯黑只剩 1px 斜边。
- 不要搬真实 Windows 徽标、开始按钮图标、厂商字标或 Plus! 主题包；只迁移可复现的排字、色值与斜边规则。
- 不要拿它做长文阅读、企业后台、电商结算和无障碍优先的长表单——窗口装饰与固定任务栏会持续抢注意。

## Chinese Typography

- 中文正文行高 `{typography.body}` 的 1.7（18px × 1.7 = 30.6px），高于 1.7 下限；界面标签 14px/1.5 不低于 1.5。
- 中西文之间留四分之一个空格：`32px 图标`、`用 Tahoma`；中文段落不首行缩进，启用避头尾，使用全角标点。
- 11px 只给窗口控制符与数字刻度，不写中文句子；中文标题降到 `{typography.heading}` 24px，仍用 700 粗体。
- Tahoma 不含中文，回退到 PingFang SC / Microsoft YaHei；字重只有 400/700 两档可靠，不用 500/600。
- 全部字号字距为 0；来源点阵字靠字形本身，拉字距会让中文小标签散开。
- 标题不用引号包整句；状态栏中文不超过 12 个字，避免 14px 灰底小字压过正文。

## When to Use

**用**：复古计算与数字博物馆展页、开发者个人站与作品集、怀旧活动与游戏化产品页、需要展示多窗口工作状态的实验界面、计算史教学页面。

**别用**：企业 SaaS 与业务后台、移动优先的消费 App、电商与结算流程、极简品牌官网、长文新闻与文档、无障碍优先的长表单、需要精确扫读的数据表格。

## Iteration Guide

1. 一次只改一个组件，用 `{components.window}` 指代它；不要同时动墙纸、标题栏渐变与斜边。
2. 所有值走 token，不写裸 hex；想加第二种强调色前，先确认深蓝是不是被误用成了装饰。
3. 想加强风格时先把 2px 斜边的明暗方向调准，最后才考虑加图标——加圆角或加柔影会直接破功。
4. 新增窗口或图标前先跑删除测试：删掉它读者会不会失去程序身份、层级或状态；不会就删掉。
5. 改完必须重跑 `designlib check` 并重新截图；标题栏浅字对比与 2px 硬边只能靠真实渲染判断。

## Known Gaps

- 四份来源的标题栏浅端不同：aesthetic.fyi 给灰渐变 #DFDFDF→#C0C0C0，技能卡给蓝渐变 #000080→#1084D0，IndexStyle 强调深蓝纯色。取技能卡蓝渐变，并把浅端调深到 #0A5FA8；#1084D0 对纸白仅 3.58:1，不达 11px 正文门槛。
- 来源窗口内容 #FFFFFF 与深影 #000000 触犯 The Floor 第 2 条；本库把内容暖化为 #F4F2EA、墨色收成 #1A1A1A，纯白与纯黑只保留在 1px 斜边 token 中。
- 来源正文与界面字都是 11px，本库中文正文提到 18px/1.7、界面标签提到 14px/1.5；这是可访问性改造，不是 Win95 原尺寸。
- 技能卡的 28px 任务栏在 14px 中文标签下偏紧；沿用显式值，但任务栏只放短词与数字，不写长句。
- 来源没有给出错误态、空态与弹窗的明确文案；`Motion & States` 的 disabled / error / open 三态按本库六态要求推断，不是来源显式值。
- 没有引入可拖拽的真实窗口 JS；当前预览用固定双栏与 `:focus-within` 表达层级，拖拽、层叠顺序与最小化动画仍需单独实现。
- 黄色记事本、Clippy 助手、Plus! 暗色主题与开始菜单侧栏属于延伸资产，本轮只迁移桌面、窗口、任务栏与图标网格四条主干。
- 截图环境可能缺 Tahoma；中文回退到系统黑体后，点阵字的「无抗锯齿」气质会减弱，需在真机复核。
