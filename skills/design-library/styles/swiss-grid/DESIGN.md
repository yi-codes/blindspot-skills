---
version: alpha
name: Swiss Grid
description: >-
  理性的秩序感。纯白画布、无衬线一族到底、只留一个电蓝强调色，
  所有对齐都能追溯到一个 8px 的基线格。装饰即噪音，一律去掉。
# ---------------------------------------------------------------- 选择条件
# 这四项是 build-index.py 读的。没有它们，这个风格在索引里选不出来。
# 加字段时改 scripts/build-index.py 的 FIELDS 表即可，这里自由扩展。
family: professional
tier: core
sourceRefs: native
cues: 落地页、产品页、案例研究、数据看板、B 端界面、需要显得专业的页面
avoid: 长文阅读、需要情绪的场景、桌面应用外壳
surface: light
density: medium
register: professional

colors:
  canvas: "#FFFFFF"
  surface: "#FAFAFA"
  surface-alt: "#F2F2F2"
  ink: "#111111"
  ink-muted: "#6B6B6B"
  ink-faint: "#8F8F8F"
  hairline: "#E0E0E0"
  hairline-strong: "#111111"
  primary: "#2557D6"
  primary-soft: "#EAF0FD"
typography:
  headline-display:
    fontFamily: "Inter, Helvetica Neue, Noto Sans SC, PingFang SC, system-ui, sans-serif"
    fontSize: 49px
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: -0.022em
  headline-lg:
    fontFamily: "Inter, Helvetica Neue, Noto Sans SC, PingFang SC, system-ui, sans-serif"
    fontSize: 31px
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: -0.022em
  headline-md:
    fontFamily: "Inter, Helvetica Neue, Noto Sans SC, PingFang SC, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: -0.01em
  body-md:
    fontFamily: "Inter, Helvetica Neue, Noto Sans SC, PingFang SC, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: -0.006em
  body-sm:
    fontFamily: "Inter, Helvetica Neue, Noto Sans SC, PingFang SC, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: -0.004em
  label-caps:
    fontFamily: "Inter, Helvetica Neue, Noto Sans SC, PingFang SC, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.06em
  stat-numeral:
    fontFamily: "Inter, Helvetica Neue, Noto Sans SC, PingFang SC, system-ui, sans-serif"
    fontSize: 31px
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: -0.022em
    fontFeature: "tnum"
rounded:
  none: 0px
  sm: 2px
  pill: 9999px
spacing:
  base: 8px
  micro: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  xxxl: 72px
  section: 112px
  gutter: 24px
  measure: 38em
components:
  card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 24px
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
  button-primary-hover:
    backgroundColor: "{colors.primary}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline-strong}"
    rounded: "{rounded.sm}"
  tag:
    backgroundColor: "{colors.primary-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.sm}"
    padding: 4px 10px
  stat:
    borderColor: "{colors.hairline-strong}"
  stat-value:
    typography: "{typography.stat-numeral}"
    textColor: "{colors.ink}"
  stat-label:
    typography: "{typography.label-caps}"
    textColor: "{colors.ink-muted}"
  overlay-pop:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
---

## Overview

Swiss Grid 是这套库里唯一一个**为信息而生**的风格。原型是 1950 年代的国际主义平面设计：网格先于内容，字重先于颜色，对齐先于装饰。

它做出的两个约定让整个系统保持干净：**字体只有一族**（无衬线，靠字重分层），**彩色只有一个**（电蓝，只出现在可点击的东西上）。任何偏离这两条的改动，都会立刻让它从"专业"掉到"普通"。

**Key Characteristics**

- 画布是纯白 `{colors.canvas}`（#FFFFFF）。这个风格不怕纯白，因为它有网格和硬边撑着。
- 字体一族到底 `{typography.body-md}` / `{typography.headline-display}`，只有 400 和 600/700 两档字重。
- 间距全部是 8 的倍数，4px 只做微调（`{spacing.micro}`）。这一条比任何视觉规则都重要。
- 唯一彩色 `{colors.primary}`（电蓝 #2557D6），只用于链接、主按钮悬停、栏目名、标签。
- 圆角几乎为方 `{rounded.sm}` = 2px。不是 4，不是 8。
- 阴影只给浮层，且浅到几乎看不见。常规层级用 `{colors.hairline}` 的 1px 边框表达。
- 数字必须等宽 `tabular-nums`，否则表格和指标行对不齐。
- 大字字距收紧到 -0.022em，否则 49px 的标题会散。

## Colors

只有两类：灰阶（承担 95% 的界面）和一个电蓝。

### Neutral Scale

- **Canvas** (`{colors.canvas}` — #FFFFFF): 页面底。纯白，不心虚。
- **Surface** (`{colors.surface}` — #FAFAFA): 次级区块底，用于表格条纹、代码块外围。
- **Surface Alt** (`{colors.surface-alt}` — #F2F2F2): 悬停底、禁用底。
- **Ink** (`{colors.ink}` — #111111): 正文与标题。近黑，不是纯黑（纯黑会让细字重显得发毛）。
- **Ink Muted** (`{colors.ink-muted}` — #6B6B6B): 次要文字、说明、单位。
- **Ink Faint** (`{colors.ink-faint}` — #8F8F8F): 占位符、禁用文字。

### Line

- **Hairline** (`{colors.hairline}` — #E0E0E0): 常规分隔线、卡片边框。
- **Hairline Strong** (`{colors.hairline-strong}` — #111111): 强调分隔（表格顶线、指标卡顶线）。这一条经常被忽略——**网格风需要一条硬线来"压住"版面**。

### Accent

- **Primary** (`{colors.primary}` — #2557D6): 电蓝。只出现在可交互元素和栏目名上。它指路，不装饰。
- **Primary Soft** (`{colors.primary-soft}` — #EAF0FD): 标签底、选中态底。

状态色（成功/警告/错误）不设 token。真需要时用文字 + 图标表达，避免引入第三个色族。

## Typography

无衬线一族到底，靠字重和字号分层级。

- **Display** (`{typography.headline-display}` — 49px / 700 / 字距 -0.022em): 首屏主标题。负字距是必须的，大字号下正字距会显得松散无力。
- **Headline** (`{typography.headline-lg}` — 31px / 600): 区块标题。600 而不是 700，跟 display 拉开层次。
- **Body** (`{typography.body-md}` — 16px / 400 / 行高 1.6): 正文基准。1.6 是这个风格的下限，中文再紧就发闷。
- **Label** (`{typography.label-caps}` — 12px / 500 / 字距 0.06em / 全大写): 栏目名、单位、表头。
- **Stat** (`{typography.stat-numeral}` — 31px / 700 / `tnum`): 指标数字。必须等宽数字。

字号阶 12 / 13 / 16 / 20 / 25 / 31 / 39 / 49，比例 1.25。**只用两档字重：400 和 600/700。**

## Layout

12 列网格，8px 基线，桌面固定最大宽度 1200px。

- 间距阶 `{spacing.micro}` 4 / `{spacing.xs}` 8 / `{spacing.sm}` 12 / `{spacing.md}` 16 / `{spacing.lg}` 24 / `{spacing.xl}` 32 / `{spacing.xxl}` 48 / `{spacing.xxxl}` 72 / `{spacing.section}` 112。
- 栅格间距 `{spacing.gutter}` = 24px，全局统一。
- 卡片内边距 `{spacing.lg}`，卡片之间 `{spacing.lg}`。**同类元素间距必须一致**，一乱就露馅。
- 正文字宽 `{spacing.measure}` = 38em。

## Elevation & Depth

**基本没有高度。** 层级靠三件事：

1. **1px 边框** (`{colors.hairline}`)——卡片、分割、输入框。
2. **底色差**——canvas → surface → surface-alt。
3. **硬线** (`{colors.hairline-strong}`)——关键分隔处的 2px 墨线，用来"压住"版面。

阴影只允许出现在浮层（下拉、弹窗、tooltip）上，规格 `0 1px 2px rgba(0,0,0,.06), 0 8px 24px rgba(0,0,0,.04)`。**卡片不要阴影**——加了就变成 Bootstrap。

## Shapes

形状语言是**近乎方形**：`{rounded.sm}` = 2px。

- 按钮：2px。
- 卡片：2px。
- 输入框：2px。
- 标签：2px。
- 例外只有一种：状态圆点、头像、开关，用 `{rounded.pill}` / 50%。

不要在同一个页面里混用 2px 和 8px。**要么统一 2px，要么统一 pill，没有中间派。**

## Components

### card

白底 + 1px `{colors.hairline}` 边 + 2px 圆角 + 24px 内边距。无阴影。

卡片之间靠 `{spacing.lg}` 的间距和对齐呼吸，不靠浮起。

### button-primary

墨色实底 + 白字 + 2px 圆角，字距 0.06em。悬停时底色换成 `{colors.primary}`（电蓝）。

实心按钮一屏最多一个。两个就分不出主次。

### button-ghost

透明底 + 1px 墨色边 + 墨色字。用于次级操作，跟主按钮并排出现。

### tag

`{colors.primary-soft}` 底 + `{colors.primary}` 文字，12px，字距 0.06em，全大写。

### stat / stat-value / stat-label

指标块。顶部 2px 墨线 `{components.stat}`，数值 `{components.stat-value}`（31px / 700 / 等宽数字），标签 `{components.stat-label}`（12px / 全大写 / 灰色）。

这个组合是网格风里最能体现"专业"的组件——数字对齐、基线一致、顶线压边。

### overlay-pop

浮层唯一允许用阴影的地方。

## Do's and Don'ts

### Do

- 所有间距用 8 的倍数。4px 只做微调，不允许出现 10px、15px 这种数字。
- 字号从 12/13/16/20/25/31/39/49 里选。级差至少 1.25 倍。
- 字重只用 400 和 600/700。不要用 500——它会把前后两档的对比削平。
- 数字一律 `tabular-nums`。表格、指标、价格，全都要。
- 彩色只给 `{colors.primary}`。它出现在链接、主按钮悬停、栏目名、标签上，不出现大面积色块。
- 关键分隔处用 `{colors.hairline-strong}` 的 2px 墨线压边，让版面有"重力"。
- 大标题字距收紧到 -0.022em。

### Don't

- 不要加第二个强调色（成功绿、警告黄一起上）。这是网格风最大的破口。
- 不要用 8px 圆角。2px 是性格，8px 是默认值。
- 不要给卡片加阴影。加了立刻变"扁平化 Bootstrap"。
- 不要用字号 1.125 倍这种小跳跃。层级看不出来就等于没有层级。
- 不要在一个页面里混用 2px 和 pill 圆角。
- 不要用装饰性背景（渐变、纹理、插画铺底）。网格风的白底是资产，不是空白。
- 不要让文字左边参差——至少一条边必须是硬的，要么严格对齐栅格，要么两端对齐。

## Chinese Typography

> 这一节是 DESIGN.md 生态里普遍缺失的部分。

- **行高 1.6 是下限**：13px 及以下要放到 1.7。
- **中西文之间留 1/4 空格**：`12 列网格`、`用 Inter 字体`。
- **全大写 + 宽字距只用于栏目名、单位、表头**，不要用在正文。
- **两档字重**：中文 500 和 600 差别极小，实际只有 400 和 700 有效。规范里写 600，实际回退到 700 也没问题。
- **避头尾**：`line-break: strict`。
- **不首行缩进**：靠段落间距。

## When to Use

**用**：产品落地页、功能页、定价页、作品集、案例展示、数据看板、报表、B 端后台、产品静物图。

**别用**：讲情绪的品牌故事页（太冷）、长文阅读（留白节奏不像阅读器）、儿童/文创/餐饮这类需要温度的品类、深色主题需求。

## Iteration Guide

1. 一次改一个组件，用 `{components.xxx}` 指代。
2. 新组件的所有数值必须从 `{spacing.*}` / `{typography.*}` / `{colors.*}` 里取，不许内联。
3. 需要强调时的优先级：字号大一级 > 字重加一档 > 用 `{colors.hairline-strong}` 压边 > 最后一个才是加颜色。
4. 加任何新东西前，先检查它是否落在 8px 网格上。
5. 做完眯眼看一下：版面有没有"歪"的感觉。有，就是某个间距不是 8 的倍数。

## Known Gaps

- 没有定义表单控件（输入框、下拉、复选框）的完整状态。后台界面需要补 error/disabled/focus 三态。
- 没有定义图表配色。做数据可视化时建议只用电蓝的单色明度阶，不要引入图表库默认的多色。
- 深色模式未定义。这个风格是白底性格，硬做深色会变成 terminal-mono 的劣化版。
- 生图侧说明在 `prompt.md`。
