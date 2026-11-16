---
version: alpha
name: Quiet Dark
description: >-
  原生桌面应用的深色界面。纯灰阶、无彩色相，靠明度差和 8% 白的叠加边框分层，
  大圆角（16px 起）、系统无衬线字体、紧凑的行高。整个界面只有一处彩色：
  焦点环和信息蓝；代码差异（diff）是唯一被放行的第二处。
  适合需要长时间盯着、且不该抢内容风头的工具界面。
# ---------------------------------------------------------------- 选择条件
# 这四项是 build-index.py 读的。没有它们，这个风格在索引里选不出来。
# 加字段时改 scripts/build-index.py 的 FIELDS 表即可，这里自由扩展。
cues: 桌面应用、编辑器面板、内部后台、Agent 对话界面、需要长时间注视的工具
avoid: 营销落地页、长文阅读、品牌表达、打印
surface: dark
register: tool

colors:
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

## Components

### card

`{colors.surface}` 底 + 16px 圆角 + 16px 内边距，**无边框无阴影**。卡片靠底色从 canvas 上浮起来。

### panel

`{colors.surface-raised}` 底 + 20px 圆角 + 20px 内边距。用于弹层、悬浮面板。

### button-primary

`{colors.ink}` 实底 + `{colors.canvas}` 文字，全圆。这是唯一的"高明度"元素，用于主操作。

### button-secondary

`{colors.surface}` 底 + `ink` 文字 + 全圆 + 8% 白边框。次级操作。

### input

`{colors.surface-input}` 底 + 16px 圆角 + `rgba(255,255,255,0.16)` 边框。聚焦时换成 `{colors.focus-ring}`。

### tag

`{colors.surface-raised}` 底 + `ink-secondary` 文字 + 6px 圆角 + 2px/6px 内边距。小而低调。

### list-row

10px/12px 内边距 + 10px 圆角，悬停时底色变 `{colors.surface-hover}`。**行与行之间不加分隔线**，靠圆角和间距区分。

### code-block

`{colors.surface-input}` 底 + 10px 圆角，比周围"暗一档"。

## Do's and Don'ts

### Do

- 整个界面只用灰阶。彩色只给焦点环、链接、状态点。
- 边框用 `rgba(255,255,255,0.08)`，不要用实色 #2a2a2a。叠加感是这套语言的根。
- 卡片 16px 圆角，按钮全圆。这两个是签名，别改。
- 层次靠三档底色（#0d0d0d / #181818 / #212121）。
- 正文 15px、行高 1.5。桌面 app 比网页紧一档。
- 主按钮用高明度实底（#f7f7f7 + 深字），这是全屏唯一的"亮点"。
- 图标用 1.5px 描边线性图标，不用实心彩色图标。

### Don't

- 不要引入第二个色相。蓝之外任何彩色都会立刻破坏"安静"——代码差异色是唯一例外，且不准出差异块。
- 不要用 8px 圆角。16px 是这套风格的身份，改小了就变回普通网页。
- 不要用纯黑 #000 或纯白 #fff 做大面积。会显得廉价且刺眼。
- 不要给卡片加边框。卡片靠底色浮起，加边框就变成"盒子"。
- 不要用投影表达层级。
- 不要用衬线字体或装饰字体。
- 不要把间距放大到网页那种松度（24/32/48）。app 就该是密的。
- 不要用大面积彩色区块（长条 banner、彩色卡片底）。这里没有"品牌色铺底"这个概念。

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

- 只定义了深色。浅色版本需要另一套灰阶（#fcfcfc 到 #0d0d0d 反向），本文件不覆盖。
- 没有定义完整的表单状态（error / disabled / readonly 的边框与底色组合）。
- 没有定义图标规格。建议 1.5px 描边、16/20px 两档，但未固化。
- 动画时长未定义。参考值是 120-160ms，缓动用 ease-out。
- 生图侧说明在 `prompt.md`——但这套风格本质是"界面"，生图只适合做氛围图，不适合做 UI 效果图（UI 请直接用 tokens.css 渲染）。
