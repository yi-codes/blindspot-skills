---
version: alpha
name: Terminal Mono
description: >-
  把命令行搬进正文。深灰蓝画布、等宽为骨架、语义四色只用来标记状态。
  标题和代码走等宽，长段落退回无衬线——满屏等宽中文是读不下去的。
# ---------------------------------------------------------------- 选择条件
# 这四项是 build-index.py 读的。没有它们，这个风格在索引里选不出来。
# 加字段时改 scripts/build-index.py 的 FIELDS 表即可，这里自由扩展。
cues: 技术文档、开发者工具、CLI 配套界面、以日志和代码为主体的页面
avoid: 消费级产品、品牌表达、需要温度的场景
surface: dark
register: technical

colors:
  canvas: "#0E1116"
  surface: "#161B22"
  surface-alt: "#1F262E"
  ink: "#C9D1D9"
  ink-strong: "#F0F6FC"
  ink-muted: "#7D8590"
  ink-faint: "#5C646E"
  hairline: "#30363D"
  hairline-strong: "#444C56"
  primary: "#3FB950"
  primary-soft: "#12261A"
  warning: "#D29922"
  danger: "#F85149"
  info: "#58A6FF"
  code-bg: "#0A0D12"
typography:
  headline-lg:
    fontFamily: "JetBrains Mono, SF Mono, Cascadia Code, Sarasa Mono SC, monospace"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.02em
  headline-md:
    fontFamily: "JetBrains Mono, SF Mono, Cascadia Code, Sarasa Mono SC, monospace"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.02em
  headline-sm:
    fontFamily: "JetBrains Mono, SF Mono, Cascadia Code, Sarasa Mono SC, monospace"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0.02em
  body-md:
    fontFamily: "Inter, Noto Sans SC, PingFang SC, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.75
    letterSpacing: 0
  code-md:
    fontFamily: "JetBrains Mono, SF Mono, Cascadia Code, Sarasa Mono SC, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.02em
    fontFeature: "calt 0, liga 0"
  label-caps:
    fontFamily: "JetBrains Mono, SF Mono, Cascadia Code, Sarasa Mono SC, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.08em
rounded:
  sm: 4px
spacing:
  base: 8px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 32px
  xl: 48px
  xxl: 64px
  measure: 40em
components:
  card:
    backgroundColor: "{colors.surface}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 24px
  button-primary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline-strong}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.sm}"
    padding: 10px 18px
  button-primary-hover:
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
  tag-default:
    backgroundColor: "{colors.primary-soft}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.sm}"
    padding: 3px 8px
  tag-warning:
    textColor: "{colors.warning}"
    borderColor: "{colors.warning}"
  tag-danger:
    textColor: "{colors.danger}"
    borderColor: "{colors.danger}"
  code-block:
    backgroundColor: "{colors.code-bg}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 16px
  prompt-marker:
    textColor: "{colors.primary}"
    typography: "{typography.code-md}"
  stat-label:
    typography: "{typography.label-caps}"
    textColor: "{colors.ink-muted}"
---

## Overview

Terminal Mono 是这套库里唯一一个**为技术而生**的风格。它不试图讨好任何人，只传递一个信号：这东西是工程师做的。

它的可信度来自四个具体的细节，不是"赛博朋克"这种形容词：**深灰蓝而不是纯黑的画布**、**带一点灰的文字而不是纯白**、**1px 实线边框而不是阴影**、**关掉连字的等宽字体**。少任何一个，它就从"终端"掉到"游戏论坛签名档"。

**Key Characteristics**

- 画布是 `{colors.canvas}`（#0E1116）。深灰蓝，不是纯黑——纯黑会让 1px 边框消失，整个界面塌掉。
- 文字是 `{colors.ink}`（#C9D1D9）。带灰，不是纯白——纯白在深底上过曝，且显得廉价。
- 标题、代码、数据走等宽 `{typography.headline-lg}`；**长段落退回无衬线** `{typography.body-md}`。这是最容易做错、也最致命的一条。
- 语义四色：绿 `{colors.primary}` 可执行/成功、琥珀 `{colors.warning}` 警告、红 `{colors.danger}` 错误、蓝 `{colors.info}` 链接。
- 圆角 4px `{rounded.sm}`，装饰主要是 1px 实线 `{colors.hairline}`。
- 光效用**内发光**（`0 0 0 1px` + 微弱扩散），不用投影。投影在深底上会形成难看的灰雾。
- 等宽字体**关闭连字**（`calt 0, liga 0`），避免 `!=`、`=>` 这类字符歧义。

## Colors

深底上一个四级灰阶，加四个语义色。**语义色只标记状态，不做装饰。**

### Surface

- **Canvas** (`{colors.canvas}` — #0E1116): 页面底。带蓝调的深灰，比 #000000 柔和，也让边框可见。
- **Surface** (`{colors.surface}` — #161B22): 面板、卡片、按钮底。
- **Surface Alt** (`{colors.surface-alt}` — #1F262E): 悬停态、表头、代码行高亮。
- **Code Bg** (`{colors.code-bg}` — #0A0D12): 代码块底。比 canvas 更深，形成"凹陷"感。

### Ink

- **Ink** (`{colors.ink}` — #C9D1D9): 正文默认色。
- **Ink Strong** (`{colors.ink-strong}` — #F0F6FC): 标题、代码文字。接近白，但仍带一点点蓝。
- **Ink Muted** (`{colors.ink-muted}` — #7D8590): 注释、meta、次要说明。
- **Ink Faint** (`{colors.ink-faint}` — #5C646E): 行号、极弱提示。

### Line

- **Hairline** (`{colors.hairline}` — #30363D): 常规边框、分割线。这是深色界面的主要装饰。
- **Hairline Strong** (`{colors.hairline-strong}` — #444C56): 按钮边框、面板顶边。

### Semantic

- **Primary / 绿** (`{colors.primary}` — #3FB950): 成功状态、可执行操作、提示符 `$`。**这是本风格的主色**。
- **Primary Soft** (`{colors.primary-soft}` — #12261A): 绿标签的底。
- **Warning / 琥珀** (`{colors.warning}` — #D29922): 警告、beta 标记、需要注意的参数。
- **Danger / 红** (`{colors.danger}` — #F85149): 错误、dangerous 操作。
- **Info / 蓝** (`{colors.info}` — #58A6FF): 链接、可点击引用。

四种语义色的**总面积不应超过屏幕的 5%**。超过就变成海报，不是界面。

## Typography

双字体系统：等宽承担"被当作数据看"的一切，无衬线承担"要被读进去"的一切。

- **Headline** (`{typography.headline-lg}` — JetBrains Mono 700，28px，字距 0.02em): 等宽标题。字距略放是因为等宽字形本身偏紧。
- **Body** (`{typography.body-md}` — Inter / Noto Sans SC 400，15px，行高 1.75): 长段落。**这里必须是比例字体**，用等宽读三屏中文会让人放弃。
- **Code** (`{typography.code-md}` — 等宽 14px，关闭连字): 代码块、行内代码、命令。
- **Label** (`{typography.label-caps}` — 等宽 12px，字距 0.08em): 状态标签、字段名、单位。

基准字号 15px 而非 16px：等宽字形偏宽，15px 的视觉体量约等于比例字体的 16px。

## Layout

8 的倍数，规整优先。

- 间距阶 `{spacing.xs}` 8 / `{spacing.sm}` 16 / `{spacing.md}` 24 / `{spacing.lg}` 32 / `{spacing.xl}` 48 / `{spacing.xxl}` 64。
- 面板内边距 `{spacing.md}` = 24px，面板间距 `{spacing.md}`。
- 正文字宽 `{spacing.measure}` = 40em。
- 代码块允许横向滚动，不要自动折行——折行会破坏对齐，比滚动更难读。

## Elevation & Depth

**不用投影。** 深色底上的投影会形成一圈灰雾，非常廉价。

层级用三件事：

1. **边框** (`{colors.hairline}`)——面板、代码块、分割。
2. **底色差**——canvas → surface → surface-alt，三档明度。
3. **内发光**——焦点态和悬停态用 `0 0 0 1px <色>, 0 0 16px <色>/12%`，让元素像被"点亮"而不是"浮起"。

面板阴影 `0 8px 32px rgba(0,0,0,.45)` 只在浮层里用。

## Shapes

形状语言是**小圆角 + 实线**：`{rounded.sm}` = 4px。

- 按钮 4px，面板 4px，标签 4px，代码块 4px。
- 统一的 1px 边框是这个风格的"装饰"。加粗到 2px 会变成复古终端，减到 0 会失去结构。
- **不要用扫描线、CRT 曲率、噪点贴图**。那些是"复古变体"的装饰，会限制使用场景。

## Components

### card

`{colors.surface}` 底 + 1px `{colors.hairline}` 边 + 4px 圆角 + 24px 内边距。像一块终端窗口。

### button-primary

`{colors.surface}` 底 + `{colors.hairline-strong}` 边 + 等宽小字。悬停时边框和文字变绿 `{colors.primary}`，并带一圈内发光。

按钮的文字建议写成可执行的语气（`$ npm run build`、`RUN`），而不是 `提交`。

### tag-default / -warning / -danger

描边标签，等宽 12px，全大写。

- `{components.tag-default}`：绿框 + `{colors.primary-soft}` 底，用于 stable、ok、ready。
- `{components.tag-warning}`：琥珀描边，透明底，用于 beta、deprecated。
- `{components.tag-danger}`：红描边，透明底，用于 breaking、error。

### code-block

`{colors.code-bg}` 底 + 1px 边框，比周围"凹"一档。关闭连字。允许横向滚动。

### prompt-marker

正文里的 `$ ` 提示符，绿色等宽。用 `::before` 加，不写进文本内容里。

### stat-label

小写等宽灰字，用于 `build_time`、`0 errors` 这类键值对的键。

## Do's and Don'ts

### Do

- 画布用 `{colors.canvas}`（#0E1116）。带蓝调的深灰，不是纯黑。
- 文字用 `{colors.ink}`（#C9D1D9）。带灰，不是纯白。
- 标题/代码/数据用等宽，**长段落必须用无衬线** `{typography.body-md}`。
- 语义色只标记状态。绿 = 可执行/成功，琥珀 = 警告，红 = 错误，蓝 = 链接。
- 分隔和装饰用 1px `{colors.hairline}` 实线。
- 焦点/悬停用内发光（`0 0 0 1px` + 微弱扩散）。
- 等宽字体关闭连字：`font-variant-ligatures: none`。

### Don't

- 不要整段用等宽。这是这个风格最容易犯、也最致命的错。
- 不要用纯黑 `#000000` + 纯白 `#FFFFFF`。一眼廉价。
- 不要让荧光色铺满屏幕。四色总面积控制在 5% 以内。
- 不要加扫描线、CRT 曲率、噪点。要就单独开一个变体。
- 不要混用两套等宽字体。标题 JetBrains、代码 SF Mono，字面宽度对不上。
- 不要用投影表达层级。深底上的投影是灰雾。
- 不要把代码块自动折行。宁可横向滚动。

## Chinese Typography

> 这一节是 DESIGN.md 生态里普遍缺失的部分。深色 + 等宽 + 中文，是最容易崩的三重叠加。

- **中文配等宽字体很容易变丑**：优先 `Sarasa Mono SC`（更纱黑体等距版），退而求其次是系统黑体 + 单独控制字距。不要用未做等距处理的中文字体配英文等宽。
- **代码块里的中文注释要和代码列宽对齐**：做不到就换行，不要硬挤成一个字符宽。
- **正文用无衬线**（`{typography.body-md}`）。这一条重复三遍都不算多。
- **行高 1.75**：深底会让字显小，行距不够会更累。
- **中西文之间留 1/4 空格**：`运行 npm install`。
- **全大写 + 0.08em 字距只用于状态标签和字段名**，不要用在正文。

## When to Use

**用**：技术文档、API 说明、开发者工具界面、CLI 配套页面、个人技术博客的"硬核"部分、技术主题配图、暗调氛围图。

**别用**：面向大众消费者的产品页（会劝退）、长文阅读（等宽+深底双重疲劳）、打印场景、需要高对比度无障碍的场景。

## Iteration Guide

1. 一次改一个组件，用 `{components.xxx}` 指代。
2. 所有值走 `{token.refs}`，不要内联十六进制。
3. 加新元素前先问：它是"数据"还是"内容"？数据走等宽，内容走无衬线。
4. 需要更强调时：先加边框亮度，再加内发光，最后才考虑加一个新色。
5. 每加一处彩色，检查全屏彩色面积是否还在 5% 以内。

## Known Gaps

- 没有定义表格样式。技术文档常有参数表，需要补 zebra + hover 行。
- 没有定义滚动条样式。深色页面里默认滚动条非常突兀，生产环境需补。
- `Sarasa Mono SC` 需要用户自行安装，未安装时会退化到系统黑体，中英文混排的列宽会对不齐。
- 打印样式完全缺失。这个风格不适合打印，不要尝试适配。
- 生图侧说明在 `prompt.md`。
