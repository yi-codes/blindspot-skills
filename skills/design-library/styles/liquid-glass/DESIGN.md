---version: beta
name: Liquid Glass
description: >-
  克制的半透明工作台。近中性纸面上浮着偏实的玻璃面板，只用一个沉静蓝指路；
  模糊负责区分工作层与信息层，不负责制造炫光。
family: operations
tier: variant
sourceRefs: ui-styles-liquid-glass
cues: 高频盯屏的控制台、任务指挥台、状态面板、需要保留环境上下文的工作界面、桌面与平板工具
avoid: 营销落地页、需要强烈视觉冲击的作品集、大量并排比较的长表格、打印
surface: mixed
density: tight
register: tool
status: stable

colors:
  canvas: "#F1F4F7"
  canvas-low: "#E4E9EF"
  surface: "#FAFBFD"
  surface-glass: "#D9E2EC"
  ink: "#283243"
  ink-muted: "#596579"
  ink-faint: "#7D8898"
  hairline: "#C9D1DB"
  accent: "#2F63B8"
  accent-strong: "#214B91"
  accent-soft: "#E5EDF9"
  ok: "#3E8064"
  warning: "#93678A"
  danger: "#A74C45"
  dark-canvas: "#192027"
  dark-surface: "#29343D"
  dark-ink: "#E9EEF2"
  dark-muted: "#B1BDC7"
  dark-line: "#46525C"
  dark-accent: "#8CB6ED"

typography:
  display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'PingFang SC', sans-serif"
    fontSize: 40px
    fontWeight: 650
    lineHeight: 1.12
    letterSpacing: -0.03em
  title:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'PingFang SC', sans-serif"
    fontSize: 26px
    fontWeight: 650
    lineHeight: 1.18
    letterSpacing: -0.02em
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'PingFang SC', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'PingFang SC', sans-serif"
    fontSize: 12px
    fontWeight: 550
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  control: 10px
  panel: 16px

spacing:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  section: 40px

components:
  panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.panel}"
    padding: 24px
  control:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.surface}"
    rounded: "{rounded.control}"
    padding: 10px 16px

elevation:
  lightSource: top-left
  steps: 3
  e1: "0 1px 2px rgba(15,23,42,0.06)"
  e2: "0 4px 12px rgba(15,23,42,0.10)"
  e3: "0 12px 32px rgba(15,23,42,0.14)"
  topHighlight: "inset 0 1px 0 rgba(255,255,255,0.60)"
  borderLight: "{colors.hairline}"
  borderDark: "{colors.ink-faint}"
  separator: border
media:
  logoType: combo
  logoRule: "字标沿用显示字族，右侧留 0.5em；图形标只用单色 {colors.ink}，最小 24px"
  imageRadius: "{rounded.panel}"
  imageRatio: "16:9"
  imageTreatment: "去饱和 6%，不加投影；与底色相接处用 1px 描边收口"
  background: "纯色 {colors.canvas}，无纹理、无氛围渐变"
  iconRule: "1.6px 描边，20px 基准，与正文同色，不使用彩色图标"
  emptyState: "淡底 + 一行说明文字，不放装饰插画和大号图标"
motion:
  easing: "cubic-bezier(0.2, 0.8, 0.2, 1)"
  durationFast: 120ms
  durationBase: 200ms
  hover: "背景升一档明度，位移 0；有阴影时抬高一级"
  focusRing: "3px solid {colors.accent}，offset 2px，不被圆角裁切"
  openTransition: "scaleY 0→1，transform-origin top，120ms"
  reducedMotion: "全部过渡降到 1ms，去掉位移"
  dragUsesSpring: true
---
## Overview

这是给高频工作的工具，不是给品牌发布会用的玻璃。背景只提供一层环境，当前工作面板必须比环境更实、更清楚。玻璃的半透明度、边缘高光和背景模糊共同回答“哪里是工作层”，而不是制造装饰。

**Key Characteristics**

- 画布 `{colors.canvas}` 是冷灰蓝纸，不使用纯白
- 面板以 `{colors.surface}` 为主，半透明只作为传统一层的办法
- 唯一强调色 `{colors.accent}` 只标记主操作、当前视图和焦点
- 正文 15px、行高 1.55，信息密集但保持可扫读
- 面板圆角 16px，控件 10px，不使用超大药丸

## Colors

- Canvas & Surface：`{colors.canvas}`、`{colors.canvas-low}`、`{colors.surface}` 提供三档底色
- Glass：`{colors.surface-glass}` 只用于透明层和背景关系
- Ink：`{colors.ink}`、`{colors.ink-muted}`、`{colors.ink-faint}` 形成三级文字
- Line：`{colors.hairline}` 是唯一常规分隔线
- Accent：`{colors.accent}` 与 `{colors.accent-strong}` 只用于操作和选中
- Status：`{colors.ok}`、`{colors.warning}`、`{colors.danger}` 只出现在状态文字或小面积标签

## Typography

系统无衬线负责全部层级。标题通过字号、字重和轻微负字距建立层级，不引入第二套展示字体。正文最小 15px，辅助信息 12px 起。数字、时间、ID 使用等宽字体。

## Layout

默认单列叙事加两级侧栏。顶部只放全局态势；主要工作区保持单列焦点。任务列表与详情可以并排，但详情永远拥有更稳定的阅读宽度。复杂页面使用 200 至 240px 的次级目录，移动端收起。

## Elevation & Depth

深度来自玻璃面板、背景模糊和一层极淡的内高光边。普通条目使用发丝线，浮层才允许带偏移的柔和阴影。不要给每个区块加阴影。

## Shapes

面板统一 16px，控件 10px，状态标签 4px。同一嵌套层级只使用一种圆角。禁止超大圆角药丸化整块区域。

## Components

- 面板：使用 `{components.panel}`，保持偏实背景
- 控件：使用 `{components.control}`，按下时只切换背景和 1px 位移
- 当前项：使用强调色内描边，不叠加发光
- 实时状态：用文字与时间说明，不用装饰性呼吸点作为唯一信号

## Do's and Don'ts

### Do

- 把当前最该处理的事项抬成唯一焦点
- 让筛选和状态标签低饱和、可扫读
- 在玻璃层后面保留清楚的信息结构

### Don't

- 不要用多色光斑、霓虹和高饱和渐变
- 不要让模糊导致正文穿透或对比度下降
- 不要把每个区块都做成悬浮玻璃卡

## Chinese Typography

界面密集区行高 1.55，长说明切换为 1.7。中英文之间留四分之一个空格。标签保持原样大小写，不拉字距。深色模式正文改用 350 字重。

## When to Use

**用**：

- Agent 指挥台、任务工作区、内部系统外壳
- 需要长期注视且要保持上下文的工具

**别用**：

- 对透明层没有语义的静态文章
- 需要紧密并排比较十个以上字段的宽表

## Iteration Guide

先确定焦点区，再决定哪些内容进入玻璃面板。每增加一个面板，先问它是否真的需要独立工作层。

## Known Gaps

不同浏览器对 `backdrop-filter` 的渲染略有差异；低性能设备应退回偏实底色。当前未覆盖打印。


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
