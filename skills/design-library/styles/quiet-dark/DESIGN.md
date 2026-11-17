---
version: alpha
name: Quiet Dark
description: >-
  原生桌面应用的深色界面，附一套同源的浅色。纯灰阶、无彩色相，靠明度差和 8% 白的
  叠加边框分层，大圆角（16px 起）、系统无衬线字体、紧凑的行高。整个界面只有一处彩色：
  焦点环和信息蓝；代码差异（diff）是唯一被放行的第二处。
  适合需要长时间盯着、且不该抢内容风头的工具界面。
# ---------------------------------------------------------------- 选择条件
# 这四项是 build-index.py 读的。没有它们，这个风格在索引里选不出来。
# 加字段时改 scripts/build-index.py 的 FIELDS 表即可，这里自由扩展。
family: workbench
tier: variant
sourceRefs: openai-desktop-client-observed,chatgpt-ios
cues: 桌面应用、编辑器面板、内部后台、Agent 对话界面、需要长时间注视的工具
avoid: 营销落地页、长文阅读、品牌表达、打印
surface: dark
density: tight
register: tool

colors:
  # ---- 深色（从桌面客户端 app.asar 提取）----
  canvas: "#0d0d0d"
  surface: "#181818"
  surface-raised: "#212121"
  surface-hover: "#1c1c1c"
  surface-input: "#131313"
  ink: "#f7f7f7"
  ink-secondary: "#a6a6a6"
  ink-tertiary: "#767676"
  ink-faint: "#6b6b6b"
  hairline: "#2a2a2a"
  hairline-strong: "#3a3a3a"
  primary: "#3a83f7"
  primary-soft: "#16233a"
  focus-ring: "#339cff"
  success: "#3a843f"
  warning: "#c9a227"
  danger: "#d9534f"
  diff-add: "#4ea870"
  diff-del: "#cf6b6b"
  # ---- 浅色（从 ChatGPT iOS 拆解移植，部分值做过对比度修正）----
  light-canvas: "#FFFFFF"
  light-surface: "#F9F9F9"
  light-surface-hover: "#F0F0F0"
  light-surface-raised: "#ECECEC"
  light-surface-input: "#F7F7F7"
  light-ink: "#0D0D0D"
  light-ink-secondary: "#676767"
  light-ink-tertiary: "#6E6E6E"
  light-ink-faint: "#8E8E8E"
  light-hairline: "#E5E5E5"
  light-hairline-strong: "#D4D4D4"
  light-primary: "#0B62D6"
  light-primary-soft: "#E8F0FE"
  light-focus-ring: "#2A7FFF"
  light-success: "#0A7A5E"
  light-warning: "#B45309"
  light-danger: "#C53030"
  light-diff-add: "#1B7A4B"
  light-diff-del: "#B4322F"
  on-danger: "#FBF7F6"
typography:
  headline-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, SF Pro Text, PingFang SC, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.02em
  headline-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, SF Pro Text, PingFang SC, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.015em
  headline-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, SF Pro Text, PingFang SC, system-ui, sans-serif"
    fontSize: 17px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: -0.01em
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, SF Pro Text, PingFang SC, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, SF Pro Text, PingFang SC, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  label-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, SF Pro Text, PingFang SC, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.01em
  code-md:
    fontFamily: "ui-monospace, SFMono-Regular, SF Mono, Menlo, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
rounded:
  xs: 4px
  sm: 6px
  md: 10px
  lg: 16px
  xl: 20px
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  xxl: 32px
  section: 48px
  measure: 42em
components:
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.lg}"
    padding: 16px
  panel:
    backgroundColor: "{colors.surface-raised}"
    rounded: "{rounded.xl}"
    padding: 20px
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.label-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  input:
    backgroundColor: "{colors.surface-input}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 10px 14px
  tag:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.ink-secondary}"
    typography: "{typography.label-md}"
    rounded: "{rounded.sm}"
    padding: 2px 6px
  list-row:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: 10px 12px
  code-block:
    backgroundColor: "{colors.surface-input}"
    rounded: "{rounded.md}"
    padding: 14px
  field:
    backgroundColor: "{colors.surface-input}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 10px 14px
  icon-button:
    textColor: "{colors.ink-tertiary}"
    rounded: "{rounded.sm}"
    size: 32px
  nav-item:
    textColor: "{colors.ink-secondary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    height: 40px
  menu-item:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.ink-secondary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 10px
  dialog:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    width: 420px
    padding: 24px
  toast:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.ink-secondary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 12px
  segmented:
    backgroundColor: "{colors.surface-input}"
    textColor: "{colors.ink-tertiary}"
    typography: "{typography.label-md}"
    rounded: "{rounded.md}"
    padding: 2px
---

## Overview

Quiet Dark 是这套库里唯一一个**从真实产品反向工程出来**的风格。

色值不是凭感觉调的，是从 OpenAI 桌面客户端（ChatGPT / Codex）的 `app.asar` 里提取的 CSS 自定义属性。它的设计系统叫 "quiet" 名副其实：**整个界面没有彩色相**，只有一根 22 级的灰阶，加一个蓝色只在焦点环和信息提示上出现。

它和 `terminal-mono` 都是深色，但路子相反。Terminal 靠**荧光绿 + 等宽字体 + 1px 实线**营造"这就是终端"；Quiet Dark 靠**零彩色 + 大圆角 + 半透明叠加**营造"这是个做得好的原生 app"。前者有性格，后者没有性格——这是刻意的，工具界面不该有性格。

**Key Characteristics**

- 底色 `{colors.canvas}`（#0d0d0d）。中性纯黑系，不偏蓝不偏暖。这点和 terminal-mono 的 #0E1116 不同。
- **零彩色相**。整个界面只有灰。蓝色 `{colors.primary}`（#3a83f7）只出现在焦点环、链接、选中态，一屏不超过三处。
- **叠加式边框**：`rgba(255,255,255,0.08)`，不是实色灰。这样边框在任何底色上都是"提亮一档"，而不是画一条线。
- **大圆角**：卡片 16px `{rounded.lg}`，面板 20px `{rounded.xl}`，按钮全圆 `{rounded.full}`。比常见的 8px 大一倍。
- 字体是**系统无衬线**（SF Pro / PingFang SC），不加任何装饰性字体。等宽只留给代码和数值。
- 行高紧凑：正文 1.5，标题 1.25。桌面 app 的密度比网页高，因为屏幕就在眼前。
- **正文字重 350，不是 400**。深色底上的亮字视觉上更粗（光渗），浅色界面用 400 的地方这里要减 50。
- 层次全部靠**明度差**：canvas #0d0d0d → surface #181818 → raised #212121，三档每档差约 8-13 个亮度值。
- **深浅两套色板，一套结构**。字号、间距、圆角、动效、图标规格完全共用，只有颜色分两套——所以同一个组件在两种模式下形状一模一样。
- **表单有四个明确状态**（默认 / 聚焦 / 错误 / 禁用，另外只读是第五个），每个状态用不同手段表达，不混用。
- **动效是可枚举的**：五档时长、三种缓动，且只允许动 `transform` / `opacity` / `background` / `color` 四样。

## Colors

一根灰阶，一个蓝。**没有第二个色相。**

### Surfaces（从深到浅）

- **Canvas** (`{colors.canvas}` — #0d0d0d): 窗口底。中性黑，不用纯黑（纯黑会让圆角边缘和阴影糊成一团）。
- **Surface** (`{colors.surface}` — #181818): 卡片、侧栏、列表容器。
- **Surface Raised** (`{colors.surface-raised}` — #212121): 抬升面板、弹层、悬浮卡片。
- **Surface Hover** (`{colors.surface-hover}` — #1c1c1c): 悬停态。介于 canvas 和 surface 之间。
- **Surface Input** (`{colors.surface-input}` — #131313): 输入框、代码块。比 canvas 略亮一点点，形成"凹陷"错觉。

### Ink

- **Ink** (`{colors.ink}` — #f7f7f7): 主文字。不是纯白——纯白在深色屏幕上会晕。
- **Ink Secondary** (`{colors.ink-secondary}` — #a6a6a6): 次要文字、说明、时间戳。约等于 65% 白。
- **Ink Tertiary** (`{colors.ink-tertiary}` — #767676): 占位符、禁用、极弱信息。
- **Ink Faint** (`{colors.ink-faint}` — #6b6b6b): 分隔标签、行号。这是灰阶的底线，再暗就掉出 3:1 了（#5d5d5d 在 #0d0d0d 上只有 2.95:1，不能用于任何要读的字）。

### Line

- **Hairline** (`{colors.hairline}` — 实色折算 #2a2a2a，源码用 `rgba(255,255,255,0.08)`): 常规边框。**必须用半透明白**，这样它在 #0d0d0d 和 #212121 上都是"提亮一档"，视觉一致。
- **Hairline Strong** (`{colors.hairline-strong}` — #3a3a3a，源码 `rgba(255,255,255,0.16)`): 输入框、按钮描边、需要看清的边界。

### Accent

- **Primary** (`{colors.primary}` — #3a83f7): 信息蓝。焦点环、链接、选中。
- **Primary Soft** (`{colors.primary-soft}` — #16233a): 选中项的底。
- **Focus Ring** (`{colors.focus-ring}` — #339cff): 只有键盘焦点用。
- **Success / Warning / Danger**：极少量，只用于状态点，不做底色。

### Diff（唯一的例外）

`{colors.diff-add}`（#4ea870）/ `{colors.diff-del}`（#cf6b6b）。

这是整套风格里**唯一**被允许的第二种色相。理由不是"好看"，是**语义不可替代**：代码差异如果只用灰阶，加号和减号必须靠符号才能分辨，扫读速度会掉一半。这不是审美问题，是功能问题。

但有严格的三条边界：

1. **只在代码差异块内出现。** 任何卡片底色、按钮、标签、图表都不能用这两个色。
2. **只上文字和极淡的底纹。** 底纹用 `rgba(78,168,112,0.10)` / `rgba(207,107,107,0.10)`，不要用实色背景条。
3. **饱和度和明度都对半砍过。** 直接拿 GitHub 的 `#2ea043` / `#f85149` 会在这套灰阶里像贴了两块胶布。这里给的绿和红都被压到与 `ink-secondary` 同一明度档，所以它们"融"在灰阶里，只做区分不做强调。

反过来：**如果产出的界面里没有代码差异，就一个像素的这两个色都不要用。**

### Light（第二套色板）

浅色不是把深色反过来。它是一套独立的灰阶，只是共用同一组变量名。

**来源要说清楚**：深色的每一个值都从桌面客户端的 `app.asar` 里抠出来，可复现。桌面版没有可提取的浅色值，所以浅色这一套是从 **ChatGPT iOS 的拆解**移植的——同一个设计语言的另一个 surface。这意味着一部分值必须改：iOS 的浅色文字是给高环境光下的小屏幕调的，搬到白底桌面上过不了对比度。

| 位置 | iOS 源值 | 这里用 | 为什么改 |
|---|---|---|---|
| 三级文字 | `#8E8E8E` | `#6E6E6E` | 源值对白底只有 3.28:1，做不了标签文字 |
| 链接蓝 | `#2A7FFF` | `#0B62D6` | 源值 3.76:1，链接是文字，必须 ≥4.5 |
| 错误红 | `#E53E3E` | `#C53030` | 源值 4.13:1，同上 |
| 警告橙 | `#D97706` | `#B45309` | 源值 3.19:1，同上 |
| 成功绿 | `#10A37F` | `#0A7A5E` | 源值 3.20:1，同上 |

**一个方向反转，不是笔误。** 深色下侧栏 `#181818` 比画布 `#0d0d0d` **亮**；浅色下侧栏 `#F9F9F9` 比画布 `#FFFFFF` **暗**。深色的侧栏是嵌进画布里的凹槽，浅色的侧栏是从纸上推开的一层。两种都对，别试图统一。

**浅色下正文字重回到 400。** 深色用 350 是因为光渗让亮字显粗；浅色没有这个问题，减重反而显虚。

**浅色下投影可以回来一点。** 深色用阴影会变成灰雾，浅色不会。但只用一档：`0 4px 12px rgba(0,0,0,0.08)`。仍然不许两层叠加。

## Typography

系统字体，不加戏。

- **Headline** (`{typography.headline-lg}` — 28px / 600 / 字距 -0.02em): 页面主标题。桌面 app 的标题比网页小，因为窗口不大。
- **Body** (`{typography.body-md}` — 15px / 400 / 行高 1.5): 正文。15px 是桌面 app 的常见值（网页是 16）。
- **Label** (`{typography.label-md}` — 12px / 500): 按钮文字、字段名、tag。
- **Code** (`{typography.code-md}` — 13px 等宽): 代码、数值、路径。

字号阶 12 / 13 / 15 / 17 / 22 / 28。比例偏小偏密，这是 app 不是落地页。

## Layout

8px 基数，密度高。

- 间距 `{spacing.xs}` 4 / `{spacing.sm}` 8 / `{spacing.md}` 12 / `{spacing.lg}` 16 / `{spacing.xl}` 24 / `{spacing.xxl}` 32。
- 卡片内边距 16px `{spacing.lg}`，面板 20px。
- 列表行高 10px 上下内边距——**紧凑是特性**，不是缺点。
- 内容宽度 `{spacing.measure}` 42em。

## Elevation & Depth

**没有投影。** 深色界面上投影会变成灰雾。

层级靠三档底色 + 半透明边框：

1. canvas → surface → raised，每档亮度差 8-13。
2. `rgba(255,255,255,0.08)` 的边框，在任何一层上都等效"提亮一档"。
3. 弹层用 raised 底色 + strong 边框，不用阴影。

如果一定要投影（比如下拉菜单压住内容），用 `0 8px 24px rgba(0,0,0,0.55)`，但要极克制。

## Shapes

**大圆角是这套风格的签名。**

- 小控件（tag、徽标）`{rounded.sm}` 6px
- 卡片 `{rounded.lg}` 16px
- 面板、弹层 `{rounded.xl}` 20px
- 按钮 `{rounded.full}` 全圆
- 输入框 `{rounded.lg}` 16px

16px 比常见的 8px 大一半。这是"原生 macOS 感"和"网页卡片"的分界线——**看到 16px 圆角，就知道这不是一张网页截图**。

不要混：卡片 16、按钮 pill，这两个是固定搭配。中间档（10px）只给列表行和代码块。

## Motion

**动效的目的不是"好看"，是让人知道发生了什么。** 这套界面的目标性格是"安静"，所以动效只有一条原则：**东西从哪来、往哪去，一次说清，然后消失。**

### 时长

| 档位 | 值 | 用在哪 |
|---|---|---|
| instant | 120ms | 按下反馈、退出。**出去永远比进来快** |
| fast | 150ms | 交叉淡入、hover 底色、描边换色 |
| base | 200ms | 单元素淡出、颜色过渡 |
| slow | 250ms | 位移、弹层进入 |
| long | 400ms | 整屏转场。**一个界面最多出现一次** |

### 缓动

- `ease-out` `cubic-bezier(0.2, 0, 0, 1)` — 默认。进入、位移、几乎所有交互。
- `ease-in-out` `cubic-bezier(0.4, 0, 0.2, 1)` — 循环、呼吸、加载指示。
- `ease-spring` `cubic-bezier(0.34, 1.4, 0.64, 1)` — 阻尼约 0.8 的轻微过冲。只给"确认"类反馈（发送成功、勾选、收藏）。**不要给布局元素用，过冲会让相邻内容抖一下。**

`ease-in` 一次都不要用。它让东西"先慢后快"，在界面上读起来像卡了一下。

### 只许动这四样

`transform` / `opacity` / `background` / `color`。

**不许动** `width` `height` `top` `left` `filter` `backdrop-filter` `box-shadow` 的模糊半径。这些会触发重排或重绘整层，在长列表里直接掉帧——而且"糊一下再清楚"这个观感本身就是"不安静"。

### 三条具体规矩

1. **文字不做入场动画。** 流式输出就一个字符一个字符地追加，不要淡入、不要上浮。文字移动会让人以为内容在变。
2. **列表不做交错（stagger）入场。** 那是营销页的手法。工具界面里列表是"已经在那儿"的。
3. **超过 400ms 的动效等于没有动效**，用户已经去看别处了。要表达"正在处理"，用状态点或进度，不要用更长的动画。

## Icons

线性图标，1.5px 描边，**颜色永远是 `currentColor`**。

| 尺寸 | 用在哪 |
|---|---|
| 16px | 13px 文字旁边的行内图标 |
| 20px | 默认。按钮内、列表行内、菜单项内 |
| 24px | 顶栏动作、侧栏折叠按钮 |

- **不给图标单独设色。** 用 `currentColor`，让它自动跟随文字的四级灰阶。单独设色的图标一定会在某个状态下和旁边的字对不上。
- **可点区域最小 32×32。** 视觉尺寸可以只有 16，但热区必须撑到 32——这是手指和触控板的下限，不是审美。
- **不用实心彩色图标。** 全库唯一允许的填充色是主按钮里那个箭头/图标，因为它是反色的。
- **不用 emoji 当图标。** emoji 不受 `currentColor` 控制，在深色底上会自己发光。

## Components

### card

`{colors.surface}` 底 + 16px 圆角 + 16px 内边距，**无边框无阴影**。卡片靠底色从 canvas 上浮起来。

### panel

`{colors.surface-raised}` 底 + 20px 圆角 + 20px 内边距。用于弹层、悬浮面板。

### button-primary

`{colors.ink}` 实底 + `{colors.canvas}` 文字，全圆。这是唯一的"高明度"元素，用于主操作。

### button-secondary

`{colors.surface}` 底 + `ink` 文字 + 全圆 + 8% 白边框。次级操作。

### field

一个字段 = 标签 + 控件 + 提示，三者间距固定 6px。标签 12px `ink-secondary`，提示 12px `ink-tertiary`。**提示永远占位**：没有提示时留空，不要把控件上下间距压缩——那会让表单在报错时整体跳一下。

控件本身：`{colors.surface-input}` 底 + 16px 圆角 + `rgba(255,255,255,0.16)` 描边（用 `box-shadow: inset` 实现，不是 `border`，这样描边不占布局宽度）。

四个状态各有各的表达，**不许混用**：

| 状态 | 描边 | 外光 | 其它 |
|---|---|---|---|
| 默认 | `hairline-strong` | 无 | — |
| 聚焦 | `focus-ring` | `0 0 0 3px` 焦点色 34% | 只有 box-shadow 在动 |
| 错误 | `danger` | `0 0 0 3px` 红色 30% | 同时把提示文字换成 `ds-hint-error` |
| 禁用 | `hairline-strong` | 无 | 整体 `opacity: .4` |
| 只读 | 无 | 无 | 去掉底色，左右内边距归零 |

三条容易做错的地方：

1. **错误态不要加红底。** 红底 + 红字 + 红描边是三份强调，看起来像在骂人。只要描边和外光。
2. **禁用态不要改底色。** 改底色会让它看起来"还没填"，而不是"不能填"。降透明度是正确的语义。
3. **只读态要看起来像普通文字。** 它的意思是"能选中复制，但别改"，所以应该安静地融进版面，而不是变成一个灰盒子。

占位符用 `ink-faint`。占位符不是标签——**如果标签只能靠占位符表达，这个表单在填完后就是不可读的**。

### icon-button

32×32 热区 + 6px 圆角，透明底，图标色 `ink-tertiary`。悬停底色 `surface-hover`、图标转 `ink`。用于工具栏、列表行尾、弹层关闭。**不加边框，不加阴影。**

### nav-item

高度 40px，左右内边距 12px，10px 圆角，13px/500 文字。默认 `ink-secondary`，悬停 `surface-hover`，选中 `surface-raised` + `ink`。**选中态不加左侧色条**——那是一条用来"指示"的装饰，这套语言里没有装饰。

### menu

`surface-raised` 底 + 10px 圆角 + 4px 内边距 + `strong` 1px 内描边。菜单项 8/10 内边距、6px 圆角。危险项悬停时整行 `danger` 实底 + 白字——这是全库唯一允许的彩色实底，因为"删除"需要一次确认级别的红。

### dialog

420px 宽，20px 圆角，24px 内边距，`surface-raised` 底。背后 `rgba(0,0,0,0.5)` + `blur(2px)`。按钮在右下，间距 8px。**不加关闭按钮**——点遮罩或按 Esc 关，右上角那个 × 是网页的习惯。

### toast

胶囊形，8/12 内边距，`surface-raised` 底 + 内描边。13px `ink-secondary`。出现在底部居中，**2 秒后自己消失，不带关闭按钮**。超过 2 秒还没看完的提示，说明它不该是 toast。

### segmented

外层 `surface-input` 底 + 2px 内边距 + 10px 圆角，内层选中项 `surface-raised` + 6px 圆角。这是"三选一"的控件，不是标签页——标签页换的是内容区，分段切换的是同一个视图的参数。

### kbd

最小 18px 宽，`surface-raised` 底，4px 圆角，12px 等宽文字。**高度靠行高撑，不设固定高度**，否则和相邻文字的基线对不齐。

### avatar

32px 圆形，`surface-raised` 底，12px/600 文字。没有头像图时用姓名首字，不要用灰色人形剪影——那是个占位图标，看起来像加载失败。

### tag

`{colors.surface-raised}` 底 + `ink-secondary` 文字 + 6px 圆角 + 2px/6px 内边距。小而低调。

### list-row

10px/12px 内边距 + 10px 圆角，悬停时底色变 `{colors.surface-hover}`。**行与行之间不加分隔线**，靠圆角和间距区分。

### code-block

`{colors.surface-input}` 底 + 10px 圆角，比周围"暗一档"。加一条 `hairline` 内描边——代码块是唯一需要明确边界的容器，因为它和周围文字的密度差太大。

## Do's and Don'ts

### Do

- 整个界面只用灰阶。彩色只给焦点环、链接、状态点。
- 边框用 `rgba(255,255,255,0.08)`，不要用实色 #2a2a2a。叠加感是这套语言的根。
- 卡片 16px 圆角，按钮全圆。这两个是签名，别改。
- 层次靠三档底色（#0d0d0d / #181818 / #212121）。
- 正文 15px、行高 1.5。桌面 app 比网页紧一档。
- 主按钮用高明度实底（#f7f7f7 + 深字），这是全屏唯一的"亮点"。
- 图标用 1.5px 描边线性图标，不用实心彩色图标。
- 图标颜色一律 `currentColor`，让它跟着文字的四级灰阶走。
- 动画只动 `transform` / `opacity` / `background` / `color`。退出比进入快（120 vs 250）。
- 表单的四个状态用不同手段表达：聚焦换描边+外光，错误换红描边+红外光，禁用降透明度，只读去底去边。不许混着用。
- 浅色和深色共用同一套结构令牌（字号、间距、圆角、动效），只有颜色分两套。

### Don't

- 不要引入第二个色相。蓝之外任何彩色都会立刻破坏"安静"——代码差异色是唯一例外，且不准出差异块。
- 不要用 8px 圆角。16px 是这套风格的身份，改小了就变回普通网页。
- 不要用纯黑 #000 或纯白 #fff 做大面积。会显得廉价且刺眼。
- 不要给卡片加边框。卡片靠底色浮起，加边框就变成"盒子"。
- 不要用投影表达层级。浅色下可以回一点（`0 4px 12px rgba(0,0,0,0.08)`），深色下一律不许。
- 不要用衬线字体或装饰字体。
- 不要把间距放大到网页那种松度（24/32/48）。app 就该是密的。
- 不要用大面积彩色区块（长条 banner、彩色卡片底）。这里没有"品牌色铺底"这个概念。
- 不要给文字做入场动画，不要给列表做交错入场。文字动起来会被读成"内容在变"。
- 不要用 `ease-in`。它在界面上读起来像卡了一下。
- 不要给图标单独设色，也不要拿 emoji 当图标。
- 不要在错误态上加红底，不要在禁用态上改底色。

## Chinese Typography

- **行高 1.5 是这套风格的常态**，中文在这个行高下略紧但可接受——因为它是 app 界面，不是长文阅读。超过两段正文时要放宽到 1.6。
- **中西文之间留 1/4 空格**：`12 个文件`、`用 SF Pro 字体`。
- **系统字体优先**：PingFang SC 在 macOS 上就是最优解，不要为了"设计感"换思源。
- **界面标签不用全大写**：中文没有大小写，`text-transform: uppercase` 对中文无效，却会把拉丁字母拉宽。只在纯英文标签上用。
- **数字用 `tabular-nums`**：列表里的时间、大小、行数必须对齐。
- **12px 是中文的极限**：再小就糊。11px 只给拉丁字母。

## When to Use

**用**：桌面应用界面、开发者工具、编辑器配套面板、需要长时间注视的工具、内部后台、macOS 风格的原生感界面。

**别用**：营销落地页（太安静，没有说服力）、长文阅读（行高和密度不对）、需要品牌表达的场景、打印。

## Iteration Guide

1. 一次改一个组件，用 `{components.xxx}` 指代。
2. 加任何颜色前先问：能不能用灰阶 + 明度差解决？能就别加。
3. 圆角只有四个值：6 / 10 / 16 / 20 / full。不要发明 8、12、14。
4. 需要强调时：先用 `ink` 换掉 `ink-secondary`，再考虑加粗，最后才是加颜色。
5. 每加一个元素，检查它是否在 8px 网格上。

## Known Gaps

- **浅色是移植值，不是提取值。** 深色每一个十六进制都能从桌面客户端 `app.asar` 复现；浅色来自 ChatGPT iOS 的拆解，且有五个值因对比度不达标被改过。如果不接受这个来源差异，就只用深色。
- 没有定义空状态（empty state）的构图。目前只在 `showcase/codex.html` 里有一版示范，没抽成规则。
- 没有定义加载态：骨架屏（skeleton）和不确定进度条（indeterminate）。动效章节只覆盖了状态切换，没覆盖"持续等待"。
- 没有定义表格（table）。数据表格需要单独的密度、对齐、行悬停规则，目前建议直接用 `swiss-grid`。
- 没有定义多选、下拉选择器（select 的原生外观还没做过）的定制样式。
- 响应式只在"窗口缩放"这一个维度上成立。窄到 720px 以下时侧栏怎么收，没有规则。
- 生图侧说明在 `prompt.md`——但这套风格本质是"界面"，生图只适合做氛围图，不适合做 UI 效果图（UI 请直接用 tokens.css 渲染）。
