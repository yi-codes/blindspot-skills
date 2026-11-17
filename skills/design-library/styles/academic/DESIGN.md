---
version: alpha
name: Academic
description: >-
  论文体。两端对齐、首行缩进、段间不留空行、标题自动编号、定理带计数器、
  边注挂在版心外面。衬线字体、1.8 行高、80 字符版心。
  目标不是"看起来专业"，是"看起来像一篇排版正确的文章"。
# ---------------------------------------------------------------- 选择条件
family: reading
tier: core
sourceRefs: latex-css
cues: 论文、技术报告、规范文档、白皮书、有定理和证明的内容、需要打印的文档
avoid: 产品落地页、工具界面、营销页、需要快速扫读的列表
surface: mixed
density: roomy
register: technical

colors:
  # ---- 浅色 ----
  canvas: "#F9FAFB"
  ink: "#1B1818"
  ink-muted: "#636363"
  rule: "#000000"
  surface-code: "#E8EDF2"
  surface-kbd: "#FFFFFF"
  border-kbd: "#AFB2B6"
  link: "#1660F3"
  link-visited: "#A80000"
  mark: "#F1EED0"
  # ---- 深色 ----
  dark-canvas: "#292929"
  dark-ink: "#DBDBDB"
  dark-ink-muted: "#979797"
  dark-rule: "#FFFFFF"
  dark-surface-code: "#403F3F"
  dark-link: "#8FB3E6"
  dark-link-visited: "#95DAF3"
  dark-mark: "#514D1F"

typography:
  headline-h1:
    fontFamily: "Latin Modern Roman, Libertinus Serif, Songti SC, Georgia, serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  headline-h2:
    fontFamily: "Latin Modern Roman, Libertinus Serif, Songti SC, Georgia, serif"
    fontSize: 27px
    fontWeight: 700
    lineHeight: 1.176
    letterSpacing: 0
  headline-h3:
    fontFamily: "Latin Modern Roman, Libertinus Serif, Songti SC, Georgia, serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  headline-h4:
    fontFamily: "Latin Modern Roman, Libertinus Serif, Songti SC, Georgia, serif"
    fontSize: 19px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Latin Modern Roman, Libertinus Serif, Songti SC, Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.8
    letterSpacing: 0
  caption-sm:
    fontFamily: "Latin Modern Roman, Libertinus Serif, Songti SC, Georgia, serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  code-md:
    fontFamily: "Menlo, Monaco, Consolas, Liberation Mono, Courier New, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  none: 0

spacing:
  base: 8px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 32px
  xl: 40px
  xxl: 48px
  section: 64px
  measure: 80ch

components:
  table:
    textColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
    padding: 8px
  code-block:
    backgroundColor: "{colors.surface-code}"
    textColor: "{colors.ink}"
    typography: "{typography.code-md}"
    rounded: "{rounded.none}"
    padding: 16px
  button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 4px 12px
  sidenote:
    textColor: "{colors.ink-muted}"
    typography: "{typography.caption-sm}"
    width: 30%
---

## Overview

Academic 是这套库里**唯一一个不把网页当网页**的风格。

它的前提是：屏幕上的文章应该遵守纸上的排版传统，因为那套传统是五百年校对出来的，不是为了省事。所以它做三件所有现代网页框架都不做的事：

1. **首行缩进，段间不留空行。** 现代网页是反过来的。LaTeX 的做法是缩进（`\parindent`），段落之间不空行——因为空行会打断阅读的连续感。
2. **两端对齐 + 自动断字。** 中文天然对齐，拉丁需要 `hyphens: auto`。右边缘参差是"网页"，右边缘齐平是"印刷"。
3. **标题自动编号。** 用 CSS counter，不是手写数字。手写的 1.2.3 一改就错。

这套风格的原始素材是 `latex-css`（785 行 CSS，把 LaTeX 的观感搬到网页）。我做的事情是提取它的数值和那几条"反网页"的规则，然后补上它没有的部分（组件、深浅两套、中文适配）。

**Key Characteristics**

- 正文 16px、**行高 1.8** `{typography.body-md}`。中文接近 1.8 刚好，1.5 会发闷。
- **版心 80ch** `{spacing.measure}`。不是 em——ch 跟字号无关，换字号版心不变，这才是正确的度量。
- 衬线到底：正文、标题、题注、按钮全部 `{typography.body-md}` 那支字体栈。**没有一处无衬线**（除了代码和 kbd）。
- 段落缩进 `1.463rem`。这个数不是拍的：LaTeX 的 `\parindent = 17.625pt`，按 `1pt[LaTeX] = (72/72.27)pt[HTML]`、`12pt = 1rem` 折算是 1.463rem。
- 线宽是**分数像素**：1.36px 细线、2.27px 粗线。因为它从 pt 折算过来，取整反而不准。
- 表格走 booktabs 风格：**只有顶线、中线、底线三条**，没有竖线，表头斜体不加粗。
- 深色版是原项目自带的（`.latex-dark`），不是反推的。

## Colors

这套颜色几乎不值得讨论——**论文体的颜色越少越好**。一页纸上只有墨、纸、和"这条链接点过了"。

### Canvas & Ink

- **Canvas** (`{colors.canvas}` — #F9FAFB): 冷近白。来源是 `hsl(210 20% 98%)`——它**不是**米黄纸色。这一点很容易搞错：论文体不等于复古米黄，LaTeX 的默认底色就是接近白。
- **Ink** (`{colors.ink}` — #1B1818): 带一点暖的近黑。来源 `hsl(0 5% 10%)`。5% 的饱和度刚好让它在屏幕上不显得"塑料黑"。
- **Ink Muted** (`{colors.ink-muted}` — #636363): 边注、脚注、题注。5.75:1。

### Rule

- **Rule** (`{colors.rule}` — #000000): 表格线的原值就是纯黑，源码里写的就是 `black`。这里不改成"近黑"——印刷的表格线就该是实的，虚一点都不像。

### Accent

只有两个颜色，都是链接状态：

- **Link** (`{colors.link}` — #1660F3): `hsl(220 90% 52%)`。**这个值原本是源码里的焦点描边色**，我把它借来做链接色——因为原项目没定义未访问链接的颜色（沿用浏览器默认蓝），而浏览器默认蓝在 2026 年已经不合适了。这是本文件对源值的一处主动偏离，记录在此。
- **Link Visited** (`{colors.link-visited}` — #A80000): `hsl(0 100% 33%)`。源码明写。

### Mark

- **Mark** (`{colors.mark}` — #F1EED0): 荧光笔。色相取自源码里那个黄色（`hsl(55 55% 70%)`，本来是边注标记框的颜色），提到 88% 亮度后当高亮底。

### 深色

`{colors.dark-canvas}`（#292929）配 `{colors.dark-ink}`（#DBDBDB），10.51:1。深色版是项目自带的 `.latex-dark` 类，值全部原样搬过来。**注意深色下表格线变成白色**——这是源码的做法，因为黑线在深底上看不见。

## Typography

**只有一支字体栈**：`Latin Modern Roman → Libertinus Serif → Computer Modern → Songti SC → Georgia`。

前三个都是 LaTeX 的血统字体（Computer Modern 是 Knuth 原版）。中文退到**宋体**——宋体就是中文的衬线，这个对应关系成立。**不要用黑体**：黑体是无衬线，会立刻把观感推回"网页"。

字号阶直接对应源码的 rem 值，一档不发明：

| 位置 | 字号 | 行高 |
|---|---|---|
| h1 | 40px (2.5rem) | 1.3 |
| h2 | 27px (1.7rem) | 1.176 |
| h3 | 22px (1.4rem) | 1.4 |
| h4 | 19px (1.2rem) | 1.4 |
| 正文 | 16px (1rem) | **1.8** |
| 题注 | 15px (0.923rem) | 1.5 |
| 代码 | 14px (0.85rem) | 1.4 |

注意 h2 的行高 1.176 —— 比正文紧得多。这是 LaTeX 的特点：标题靠字号建立层级，不靠行距。

`font-variant-numeric: oldstyle-nums` —— 数字用旧式（上下伸出的），这是书籍排版的默认，不是装饰。

## Layout

- 版心 `{spacing.measure}` 80ch，居中。
- **段落首行缩进 `1.463rem`，段间 `margin: 0`。** 这是最反网页的一条规则，也是最重要的一条。
- 标题前的空间远大于标题后的空间：h2 上 48px、下 16px。这样标题和它下面的正文是一组。
- 边注挂在版心右侧外面（负外边距 64px），宽度 30%。

## Elevation & Depth

**没有。** 论文是平面的。没有卡片、没有阴影、没有浮层。

唯一的"层级"是**字号 + 缩进 + 编号**：一个 h2 之所以是 h2，因为它更大、有编号、上面有 48px 空白。这三件事一起工作，不需要任何装饰。

## Shapes

**零圆角，一个值。** 表格、代码块、按钮、kbd 全部直角。

线宽只有两个值，且都是分数：

- `1.36px` 细线（表格中线、脚注分隔）
- `2.27px` 粗线（表格顶线、底线）

这两个数来自 `0.4pt` 和 `0.8pt` 的 pt→px 折算。**不要取整成 1px 和 2px**——在大字号下能看出区别，而"看着像印的"正是这套风格要的。

代码块里 kbd 的圆角是 2px，这是唯一的例外（kbd 本来就是个按键的样子）。

## Components

### table

Booktabs 风格：顶线 2.27px、表头下中线 1.36px、底线 2.27px，**没有竖线**。表头用**斜体不加粗**（不是加粗）——这是 booktabs 的规矩，因为它要和正文区分，而不是和正文竞争。

`caption` 在表格**上方**，编号由 counter 生成（"表 1"）。

### code-block

`{colors.surface-code}` 底、零圆角、16px 内边距、`text-align: left`（正文是 justify，代码必须左对齐，否则会拉开字距）。

### theorem / proof

定理：加粗的"定理 N．"标签 + 正文，**无框、无底色、无左边线**。证明：斜体"证明．"开头，末尾右浮一个 □（QED 方块）。

这是 amsthm 的 plain 样式。不要加框——加了就变成"卡片"，论文里没有卡片。

### sidenote

右浮动、宽 30%、负外边距 64px 挂到版心外面。字号 15px、左对齐、不缩进、次要色。

边注是论文体最重要的"高级感"来源，也是最容易被做错的地方：**它必须真的在版心外面**，否则就只是一个"旁白段落"。

### button

论文里没有按钮。但网页需要，所以做成"参考文献条目"的样子：透明底、1px 直角边框、悬停时反色。**不加圆角、不加阴影、不填色块**。

## Do's and Don'ts

### Do

- 段落首行缩进，段间不留空行。
- 正文 1.8 行高。觉得松是错觉，1.5 在中文里会发闷。
- 标题一律自动编号（CSS counter）。
- 表格只用三条横线，没有竖线。
- 边注挂到版心外面，不要塞进正文里。
- 全文一支衬线字体栈。中文用宋体。
- 数字用 oldstyle-nums。
- 代码块左对齐，正文两端对齐。

### Don't

- 不要用黑体做标题。一用就变网页。
- 不要加卡片、边框、阴影来表达层级。用字号和空白。
- 不要用米黄纸色。LaTeX 的底色是接近白的。
- 不要在段落之间加空行。那是网页的做法。
- 不要给定理加框。
- 不要用圆角。
- 不要把表格做成斑马纹。booktabs 没有斑马纹。
- 不要用无衬线的按钮和标签。

## Chinese Typography

- **中文的"衬线"是宋体。** 标题也用宋体加粗，不要换成黑体——一旦换，整套拉丁衬线的气质就断了。
- **中文不需要 `hyphens: auto`**，但需要 `text-align: justify` 配合 `line-break: strict`（避头尾）。中文两端对齐的效果远好于拉丁，因为汉字是方块。
- **首行缩进对中文是天然的**：中文出版一直是两字符缩进（32px），比 `1.463rem`（23.4px）宽。中文场景建议改成 `2em`。
- **行高 1.8 对中文刚好**。拉丁 1.8 偏松，中文 1.8 正常。
- **中西文之间留 1/4 空格**：`见第 3 节`、`使用 LSTM 模型`。
- **不要用全角标点混半角**：中文用「，。」，括号里的英文用半角。
- **定理、证明、图、表的编号词要改成中文**：本文件用的是"定理 N．""证明．""图 N""表 N"，源码里是英文的 "Theorem 1."。这是本地化，不是偏离。
- **公式用 MathML 或 KaTeX**，不要截图。截图在深色模式下会变成一个白方块。

## When to Use

**用**：论文与预印本、技术报告、RFC 式的规范文档、白皮书、教材、任何有定理/证明/编号章节的内容、需要打印或导出 PDF 的页面。

**别用**：产品落地页（太慢）、工具界面（密度不对）、营销页（没有说服力）、需要快速扫读的列表页（缩进会妨碍扫读）。

## Iteration Guide

1. 加任何视觉元素之前先问：LaTeX 里有这个东西吗？没有就先别加。
2. 编号一律用 counter，不要手写。
3. 线宽只有 1.36 / 2.27 两个值。
4. 需要强调时：用斜体，不用加粗，不用颜色。斜体是学术写作的强调手段。
5. 每加一个组件都要检查它是不是破坏了两端对齐（比如代码、表格、按钮必须 `text-align: left`）。

## Known Gaps

- **拉丁字体拿不到。** Latin Modern / Libertinus 需要自托管 woff2，现在退到 Georgia，观感差距明显（Georgia 的 x-height 更大，行高 1.8 会显得空）。
- 没有定义公式排版。MathML 的样式需要在 `tokens.css` 之外单独处理。
- 没有定义参考文献列表（bibliography）的悬挂缩进样式。
- 没有定义多栏排版（twocolumn）。学术论文常见双栏，这里只做了单栏。
- 边注在窄屏（<1024px）会跑到屏幕外。需要一套"边注降级为脚注"的规则，暂未做。
- 深色版的 `mark` 颜色是我按色相推的，不是源码值。
- 生图侧说明在 `prompt.md`——但这套风格的配图应该是图表，不是照片。
