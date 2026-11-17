---
version: alpha
name: Editorial Serif
description: >-
  冷灰白纸上的编辑体。标题走衬线、正文走黑体，全系统只有一个赭红强调色，
  所有装饰让位给文字。目标是让人愿意把一篇长文读完，而不是被界面惊艳一下。
# ---------------------------------------------------------------- 选择条件
# 这四项是 build-index.py 读的。没有它们，这个风格在索引里选不出来。
# 加字段时改 scripts/build-index.py 的 FIELDS 表即可，这里自由扩展。
cues: 长文、博客、白皮书、品牌故事、需要慢慢读的页面、杂志式栏目
avoid: 工具界面、高密度数据、桌面应用、需要速度感的场景
surface: light
density: roomy
register: story

colors:
  canvas: "#F2F3F0"
  surface: "#FAFBF9"
  surface-alt: "#E9EBE7"
  ink: "#191A18"
  ink-muted: "#545851"
  ink-faint: "#7D8278"
  hairline: "#DCDFD8"
  primary: "#A63D2F"
  primary-active: "#7A2A1F"
  primary-soft: "#F1E4DE"
typography:
  headline-display:
    fontFamily: "Noto Serif SC, Source Han Serif SC, Songti SC, Georgia, serif"
    fontSize: 54px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: "Noto Serif SC, Source Han Serif SC, Songti SC, Georgia, serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.01em
  headline-md:
    fontFamily: "Noto Serif SC, Source Han Serif SC, Songti SC, Georgia, serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: "Noto Serif SC, Source Han Serif SC, Songti SC, Georgia, serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Noto Sans SC, PingFang SC, Hiragino Sans GB, system-ui, sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.85
    letterSpacing: 0.005em
  body-sm:
    fontFamily: "Noto Sans SC, PingFang SC, Hiragino Sans GB, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.75
    letterSpacing: 0.005em
  label-caps:
    fontFamily: "Noto Sans SC, PingFang SC, Hiragino Sans GB, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.18em
  figure-numeral:
    fontFamily: "Noto Serif SC, Source Han Serif SC, Songti SC, Georgia, serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
    fontFeature: "oldstyle-nums"
rounded:
  none: 0px
spacing:
  base: 16px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  xxl: 64px
  section: 104px
  measure: 34em
components:
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.none}"
    padding: 24px
  card-divider:
    backgroundColor: "{colors.ink}"
    height: 2px
  button-primary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 12px 28px
  button-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
  eyebrow:
    textColor: "{colors.primary}"
    typography: "{typography.label-caps}"
  tag:
    backgroundColor: "{colors.primary-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  figure:
    textColor: "{colors.ink}"
    typography: "{typography.figure-numeral}"
---

## Overview

Editorial Serif 是这套库里唯一一个**为阅读而生**的风格。它的原型不是 SaaS 落地页，是一本做得讲究的纸质杂志：冷灰白的画布、墨黑而非纯黑的正文、一个赭红只出现在栏目名和链接上。

它的性格来自三个"不够纯"的选择：背景不用 `#FFFFFF` 也不用米色，而用带一点绿倾向的 `{colors.canvas}`；文字不用 `#000000` 而用带一点冷调的 `{colors.ink}`；强调色不用蓝、不用黑，用一枚会让人想起铁锈和陶土的 `{colors.primary}`。纯白和纯黑是最省事的选择，也最没有记忆点。

**关于纸色的一段记录**：这个风格原来用的是暖米纸 `#FBF8F3`。它被换掉，不是因为不好看，是因为**米色纸本身就是"AI 生成的博客模板"的第一识别特征**——hallmark 的门禁表把"米色背景 + 高对比衬线 + 陶土红"整组列为一眼认得出的长相。做完五轴对照（只换纸 / 只换点缀色 / 只换字体搭配）后才看清：点缀色在这套版式里占不到 1% 的面积，换成墨青肉眼几乎分不出；真正背锅的是那层米色。所以只动了一个轴——纸冷了，赭红一点没动，编辑感还在。

**Key Characteristics**

- 画布是冷灰白 `{colors.canvas}`（#F2F3F0），微绿倾向，不是纯白也不是米色。这是这个风格的第一识别点。
- 全站只有一处温差：冷纸上的赭红 `{colors.primary}`。纸越冷，那点红越像一枚印章。
- 标题走衬线 `{typography.headline-display}`，正文走黑体 `{typography.body-md}`。中文排版里最稳的一组搭配，衬线给重量，黑体给清晰。
- 正文行高 1.85，比常规的 1.5–1.6 松得多。中文汉字是满方块，行距不够会立刻发闷，这是不可协商的。
- 正文字宽收到 34em（约 34 个汉字）`{spacing.measure}`，超出的部分用留白。
- 圆角恒为 0 `{rounded.none}`，全系统没有一处阴影，层级只用 `{colors.hairline}` 的 1px 细线表达。
- 只有一枚彩色 `{colors.primary}`（赭红 #A63D2F）。它出现在栏目名、链接、标签底，不出现大面积色块。
- 字号跳跃遵循 1.333 律（大三度），中间状态一律不设。

## Colors

颜色收敛到"冷纸 / 墨 / 一点赭红"三件事。多一个颜色，这个风格就变成网店。

### Canvas & Surface

- **Canvas** (`{colors.canvas}` — #F2F3F0): 页面底色。冷灰白，接近未涂布的纸，不是米黄。全站唯一的大面积底色。
- **Surface** (`{colors.surface}` — #FAFBF9): 卡片表面。比 canvas 亮一档但仍是暖白偏冷，让卡片"浮"出来一点点——是唯一的例外。
- **Surface Alt** (`{colors.surface-alt}` — #E9EBE7): 次级区块底，比 canvas 再沉一档，用于引文、注释、边栏。

### Ink

- **Ink** (`{colors.ink}` — #191A18): 正文与标题。带一点冷绿的近黑，比纯黑柔和，接近真实油墨。
- **Ink Muted** (`{colors.ink-muted}` — #545851): 次要文字、图注、meta 信息。
- **Ink Faint** (`{colors.ink-faint}` — #7D8278): 最弱一级，用于页脚、时间戳、占位。对 canvas 3.5:1、对 surface-alt 3.3:1，刚好守住 3:1 的可读下限。

### Line & Accent

- **Hairline** (`{colors.hairline}` — #DCDFD8): 唯一的分隔手段。所有"线"都用它。
- **Primary** (`{colors.primary}` — #A63D2F): 赭红。栏目名、链接、强调数字。**全站唯一的暖色**，不要在它之外再加任何暖调。
- **Primary Active** (`{colors.primary-active}` — #7A2A1F): 链接按下态、标签文字色。
- **Primary Soft** (`{colors.primary-soft}` — #F1E4DE): 标签底、引用块底。唯一的浅色强调——它在冷纸上是一小块暖斑，这是有意的，不是失误。

## Typography

一套衬线 + 一套黑体，各司其职，不混用。

- **Display / Headlines** (`{typography.headline-display}` — Noto Serif SC 700，54px，字距 -0.01em): 衬线标题承载"这是个正经东西"的信号。权重只到 700，不到 900——中文衬线再加粗会糊成一团墨。
- **Body** (`{typography.body-md}` — Noto Sans SC 400，17px，行高 1.85): 17px 而非 16px，因为中文字形在 16px 下笔画会挤；行高 1.85 是长文可读性的下限。
- **Label** (`{typography.label-caps}` — 12px，字距 0.18em，全大写): 只用于栏目名（"CASE STUDY"、"案例"）。宽字距是为了让这几个字从小字号里"做出来"，而不是靠加粗。
- **Figure** (`{typography.figure-numeral}` — 衬线，oldstyle-nums): 数字用衬线老式数字，会随文本基线起伏，比等高的现代数字更有印刷感。

字号阶：12 / 14 / 17 / 22 / 30 / 40 / 54，比例约 1.333。**不设 15、18、19 这类中间档**。

## Layout

单栏为主，正文宽 `{spacing.measure}`（34em）。

- 间距阶 `{spacing.xs}` 4 / `{spacing.sm}` 8 / `{spacing.md}` 16 / `{spacing.lg}` 24 / `{spacing.xl}` 40 / `{spacing.xxl}` 64 / `{spacing.section}` 104。
- 段落间距用 `{spacing.md}`，区块间距用 `{spacing.xl}`，章节间距用 `{spacing.section}`。三级固定，不临时发挥。
- 页边距宁可大：窄屏留 24px，宽屏留到内容宽度的 8% 以上。
- 两栏只在一种情况下允许：正文 + 边注（注释、术语解释）。不要做"左文右图"的营销版式。

## Elevation & Depth

**这个风格没有高度概念。** 全系统不使用 `box-shadow`。

层级靠三件事表达：

1. **1px 细线** (`{colors.hairline}`)——卡片顶线、引用左边线、表格横线。
2. **底色差**——canvas → surface-alt → surface 三档，靠明度差而不是投影。
3. **字重和字号**——最重要的一段话，把字号提一级，而不是加个框。

任何一处阴影都会让"纸"变成"卡片 UI"，是这个风格最快破功的方式。

## Shapes

形状语言是**利落**：所有矩形都是直角，`{rounded.none}` = 0px。

- 按钮：直角描边，1px 实线 `{colors.ink}`。
- 卡片：直角，靠 2px 顶部实线（`{components.card-divider}`）与上方内容分隔。
- 标签：直角，`{colors.primary-soft}` 底。
- 图片：直角，不加边框，不加圆角。宁可裁切，不要圆角。

`border-radius` 在这个风格里是禁用属性。需要"软化"的时候，用留白，不用圆角。

## Components

### card

纸白色底、直角、24px 内边距，顶部一条 2px 墨线 `{components.card-divider}`。

卡片之间**不用阴影区分**，用间距（`{spacing.lg}` = 24px）和顶线。

### button-primary

描边按钮：透明底 + `{colors.ink}` 1px 边 + 墨色文字，字距 0.08em（小字加宽字距，显得郑重）。

悬停时**反色**：墨色底 + 纸色文字。不做位移、不做缩放、不做阴影。

### eyebrow

栏目名。`{typography.label-caps}` + `{colors.primary}`。放在标题上方，用于标记文章所属栏目。

每个可见区块最多出现一次，多了就成了装饰。

### tag

`{colors.primary-soft}` 底 + `{colors.primary-active}` 文字，直角，12px，字距 0.1em。用于日期、分类、状态。

### figure

数字大字。衬线 + `oldstyle-nums`。用于"12 分钟""3,400 字"这类需要被读到的数字。

## Do's and Don'ts

### Do

- 全站锚定在冷灰白 `{colors.canvas}` 上。纯白会让它退化成"又一个博客模板"，米色会让它退化成"又一个 AI 生成的博客模板"——两头都不能去。
- 标题一律用衬线 `{typography.headline-display}`，正文一律用黑体 `{typography.body-md}`。这个分工不要跨。
- 正文行高保持 1.85。觉得"太空"是错觉，中文 1.6 才是真挤。
- 强调只用一枚赭红 `{colors.primary}`。要更强调就加大字号、加深颜色，不要引入第二个色相。
- 分隔一律用 `{colors.hairline}` 的 1px 线或留白。
- 数字用衬线 `{typography.figure-numeral}`，让它有印刷感。
- 每 3–4 段插入一个一到两行的短段，制造呼吸停顿。

### Don't

- 不要在任何地方加 `border-radius`。圆角一处，纸感全失。
- 不要用 `box-shadow`。零容忍。
- 不要加第二个彩色（成功绿、警告黄都不行）。需要状态提示时用文字，不用色块。
- 不要用 900 字重的衬线标题。700 已经是上限，再重会糊。
- 不要用字号 15/18/19 这类中间档。要么同级，要么跳一大截。
- 不要把正文拉满全宽。超过 34em 就断开，多出来的给留白。
- 不要做"左文右图"的两栏营销版式。
- 不要用图标代替文字。这个风格里图标是噪音。

## Chinese Typography

> 这一节是 DESIGN.md 生态里普遍缺失的部分。84 个西方品牌样本的排版规则，大多建立在拉丁字母的字形假设上，直接套到中文会出问题。

- **行高不能照搬**：西文 1.5 舒服，中文 1.5 发闷。正文下限 1.7，长文 1.85。
- **中西文之间留 1/4 空格**：`2026 年`、`用 A7C2 拍`、`Noto Sans SC 字体`。挤在一起是中文排版最常见的粗糙感来源。
- **标点占一个汉字宽**：中文逗号、句号、书名号都是全角，不要用半角标点混排。
- **避头尾**：句号、逗号、右括号不能出现在行首（`line-break: strict`）。
- **不首行缩进**：网页用段落间距分隔，缩进是印刷时代纸张成本的产物，屏幕上只会让左边不齐。
- **字重别乱加**：中文字体 500 和 600 的区别极小，用了等于没用。要么 400，要么直接 700。
- **引号用 「」或 ""**：与正文同字号，不要用英文弯引号配中文。
- **标题不用 letter-spacing 负值太多**：中文字形是满方块，-0.02em 已经开始压笔画，-0.01em 是安全线。

## When to Use

**用**：长文阅读、博客正文、白皮书、行业分析、品牌故事页、关于我们、知识库对外呈现、读书笔记。

**别用**：数据看板（密度不够）、需要"锋利科技感"的产品落地页、深色主题场景（这套是冷白纸感，硬改深色会失去性格）。

## Iteration Guide

1. 一次只改一个组件，用 `{components.xxx}` 指代它。
2. 所有颜色、字号、间距都走 `{token.refs}`，不要内联十六进制。
3. 需要更强调时，先考虑"字号大一级"，最后才考虑"加一个新颜色"——后者基本等于破功。
4. 新增组件时，先问"它能不能用现成的 hairline + 留白表达"。不能，再谈别的。
5. 中文排版的六条规则是硬约束，任何新组件都要过一遍。

## Known Gaps

- 衬线字体在部分安卓设备上没有 Noto Serif SC，会退化到系统默认衬线（可能很难看）。生产环境建议自托管字体子集。
- 这个风格没有定义表单控件（输入框、下拉、复选）的样式。用于纯阅读页面足够，用于后台界面需要补。
- 没有定义表格样式。数据表格建议直接用 `swiss-grid`。
- 生图侧的对应说明在 `prompt.md`，不在本文件内——DESIGN.md 规范只覆盖 UI，不覆盖摄影/插画方向。
