---version: alpha
name: Pixel Arcade｜像素街机
description: >-
  面向复古游戏与轻量互动 demo 的 8-bit 界面。4px 阶梯边框、8px 网格、
  离散状态切换和受限色板来自 NES.css；中文不强行像素化，正文保持系统无衬线与 1.75 行高。
cues: 复古游戏、浏览器小游戏、Game Jam、像素作品集、成就与徽章、轻量游戏化 demo、街机活动页
avoid: 长文阅读、企业后台、金融医疗政务、复杂表单、高密度数据、正式品牌官网、关键生产工具
surface: light
density: medium
register: story
family: retro
tier: variant
status: beta

colors:
  canvas: "#F8F8F0"
  surface: "#FCFCF4"
  ink: "#212529"
  ink-muted: "#4E555B"
  ink-faint: "#6C7278"
  hairline: "#ADAFBC"
  primary: "#108DE0"
  primary-soft: "#D4EBFA"
  highlight: "#F7D51D"
  on-primary: "#212529"
typography:
  display:
    fontFamily: "Press Start 2P, PingFang SC, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  headline:
    fontFamily: "Press Start 2P, PingFang SC, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body:
    fontFamily: "Press Start 2P, PingFang SC, Noto Sans SC, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.75
    letterSpacing: 0
  label:
    fontFamily: "Press Start 2P, PingFang SC, Noto Sans SC, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
rounded:
  none: 0px
spacing:
  base: 8px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  section: 48px
  measure: 36em
components:
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 16px
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: 12px 16px
  tag:
    backgroundColor: "{colors.highlight}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"

elevation:
  lightSource: top-left
  steps: 3
  e1: "0 1px 2px rgba(15,23,42,0.06)"
  e2: "0 4px 12px rgba(15,23,42,0.10)"
  e3: "0 12px 32px rgba(15,23,42,0.14)"
  topHighlight: "inset 0 1px 0 rgba(255,255,255,0.60)"
  borderLight: "{colors.hairline}"
  borderDark: "{colors.ink-faint}"
  separator: shadow
media:
  logoType: wordmark
  logoRule: "字标沿用显示字族，右侧留 0.5em；图形标只用单色 {colors.ink}，最小 24px"
  imageRadius: "{rounded.none}"
  imageRatio: "4:3"
  imageTreatment: "去饱和 6%，不加投影；与底色相接处用 1px 描边收口"
  background: "纯色 {colors.canvas}，无纹理、无氛围渐变"
  iconRule: "1.6px 描边，20px 基准，与正文同色，不使用彩色图标"
  emptyState: "淡底 + 一行说明文字，不放装饰插画和大号图标"
motion:
  easing: "cubic-bezier(0.2, 0.8, 0.2, 1)"
  durationFast: 120ms
  durationBase: 200ms
  hover: "背景升一档明度，位移 0；有阴影时抬高一级"
  focusRing: "3px solid {colors.primary}，offset 2px，不被圆角裁切"
  openTransition: "scaleY 0→1，transform-origin top，120ms"
  reducedMotion: "全部过渡降到 1ms，去掉位移"
  dragUsesSpring: false
---
## Overview

给复古游戏、Game Jam、像素作品集和轻量互动 demo 用。它借用的是早期游戏机的约束：有限色板、4px 边框、离散状态、清晰像素，而不是把普通后台套一层像素字体。

NES.css 提供 Press Start 2P、16px 基准、4px 边框和完整 NES 色板。本风格只取其中蓝、黄和中性色，避免把 54 色全部带进页面。中文没有对应点阵字形，因此关键正文必须回退到系统无衬线。

风格成立的标志是去掉像素装饰后交互仍然成立。游戏反馈可以有趣，但文字、按钮和错误提示不能为了怀旧变得难读。

**Key Characteristics**

- `{colors.canvas}` 与 `{colors.surface}` 来自 NES 高亮中性色的微调，避免纯白底。
- 4px 实线边框和 4px 硬投影，不用模糊或圆角模拟像素。
- 8px 布局网格；所有图标、图片与位移对齐 2px 或 4px。
- 蓝色 `{colors.primary}` 用于主操作，黄色 `{colors.highlight}` 用于奖励与分数。
- 英文短标签可用 Press Start 2P；中文正文使用 PingFang SC／Noto Sans SC。

## Colors

- `{colors.canvas}` — #F8F8F0，游戏纸面／屏幕底色。
- `{colors.surface}` — #FCFCF4，对话框和面板。
- `{colors.ink}` — #212529，NES.css 的主墨色。
- `{colors.ink-muted}` — #4E555B，说明和次要状态。
- `{colors.ink-faint}` — #6C7278，非关键编号。
- `{colors.hairline}` — #ADAFBC，NES.css 默认投影灰，也用于禁用态。
- `{colors.primary}` — #108DE0，主操作蓝。
- `{colors.primary-soft}` — #D4EBFA，选中项底色。
- `{colors.highlight}` — #F7D51D，奖励和分数；不用于小号正文。
- `{colors.on-primary}` — #212529，蓝底上的深字，避免白字对比不足。

## Typography

英文显示字号 32／20px，正文 16px，标签 12px；全部 400。Press Start 2P 本身已经足够醒目，不再加粗或拉开字距。

中文正文不能强行使用点阵字体。中文标题如需像素感，用系统字体配合像素边框与插图，而不是牺牲笔画识别。

## Layout

- 使用 8px 基础网格；对话框内距 16px，区间距 24／32／48px。
- 游戏页优先“舞台 + 状态条 + 主操作”，不要套用三列营销卡。
- 状态条数字使用 tabular nums；图标统一 16／24／32px，禁止不同像素密度混用。
- 正文最大 `{spacing.measure}`；长说明移到独立帮助页。
- 移动端保持 44px 最小触控高度，不能为了还原像素缩小按钮。

## Elevation & Depth

深度只有硬偏移：按钮和卡片使用 `0 4px 0` 的 `{colors.hairline}` 或 `{colors.ink}`。按下时元素下移 4px、投影归零。禁止 blur、发光、透明玻璃和柔和悬浮。

## Shapes

全部 `{rounded.none}`。像素阶梯应由 4px 边框与硬投影形成，不额外使用 clip-path 制造任意锯齿。图片设置 `image-rendering: pixelated`。

## Components

### card

`{components.card}` 是对话框／状态面板。4px 墨线、16px 内距、无圆角；一屏最多一个主对话框加少量状态条。

### button-primary

`{components.button-primary}` 蓝底深字，hover 使用 `{colors.primary-soft}`，active 下移 4px。过渡使用 100ms／steps(2)，不用弹簧回弹。

### tag

`{components.tag}` 只用于分数、关卡、奖励和状态事实。黄色标签不用于长句，也不能替代正文。

## Do's and Don'ts

### Do

- 对齐统一像素网格，并在高 DPI 屏幕检查清晰度。
- 用硬切换表达按下、选中和得分。
- 保留真实键盘焦点与 44px 触控目标。
- 中文长文本回退到清晰系统字体。

### Don't

- 不要把所有正文都设成 Press Start 2P。
- 不要使用平滑渐变、柔影、圆角和玻璃拟态。
- 不要混用 1px 细图标与 4px 像素图标。
- 不要用像素风掩盖空状态或错误信息的缺失。

## Chinese Typography

- 中文正文 16px／1.75，标签 12px／1.5；使用系统无衬线。
- 中西文之间留四分之一空格；分数、关卡和日期保持独立字段。
- 中文标题字距为 0，不伪造斜体或拉伸点阵字。
- 使用全角标点、避头尾、不首行缩进。
- 中文短按钮最多 6 字，超出时换更明确的短文案，不缩小字号。

## When to Use

**用**：复古游戏、Game Jam、像素作品集、互动小实验、成就徽章、街机活动页。

**别用**：正式企业产品、长文、支付医疗政务、数据后台、复杂生产工具、精密表单。

## Iteration Guide

1. 先验证游戏操作和状态，再加像素装饰。
2. 太吵时先减少黄色奖励和闪烁，不缩小文字。
3. 不清晰时先统一像素密度和边框，不增加更多颜色。
4. 修改 `{components.button-primary}` 后检查键盘、触屏和 active 位移。

## Known Gaps

- Press Start 2P 需另行加载且不含中文；离线环境会回退为系统字体。
- tokens.css 不包含 NES.css 的像素图标资源，只定义界面骨架。
- 尚未定义多人游戏、复杂库存和大型 RPG 菜单。
- 像素风在部分中文用户中可读性有限，必须用真实内容测试，不能只看英文预览。


## Material & Elevation

光从 `{elevation.lightSource}` 来，固定这一个方位。共 `{elevation.steps}` 级：
`{elevation.e1}` 贴面、`{elevation.e2}` 卡片、`{elevation.e3}` 浮层。
深色上层级靠明度与内描边，浅色上靠带偏移的阴影——不做居中发光。
主分隔手段是 `{elevation.separator}`，其余只做辅助。

## Mark & Media

标识：`{media.logoRule}`（`{media.logoType}`）。
图片：比例 `{media.imageRatio}`、圆角 `{media.imageRadius}`、处理 `{media.imageTreatment}`。
背景：`{media.background}`。图标：`{media.iconRule}`。空态：`{media.emptyState}`。
只写规则不写品牌资产；图片处理都是可复现参数。

## Motion & States

过渡曲线 `{motion.easing}`，快档 `{motion.durationFast}`、基准 `{motion.durationBase}`。
hover：`{motion.hover}`；焦点：`{motion.focusRing}`；展开：`{motion.openTransition}`。
交互组件逐项覆盖 default / hover / focus-visible / active / disabled / error 六态。
`prefers-reduced-motion` 时 `{motion.reducedMotion}`。
