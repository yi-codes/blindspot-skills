---version: beta
name: Incident Room
description: >-
  重大事故响应台。用一条连续时间线把发现、判断、动作、验证和回执串起来，
  让接班者不读整段聊天也能恢复现场。高密度但不制造警报噪音。
family: operations
tier: core
sourceRefs: ui-styles-ops-console
cues: 正在发生的事故、事故响应、值班交接、故障复盘、重大变更回滚、需要统一事件叙事的跨团队协作
avoid: 日常低风险监控、营销页、长期产品文档、需要同时比较多个无关信号的普通控制台
surface: dark
density: tight
register: tool
status: stable

colors:
  canvas: "#1A1714"
  surface: "#221E1A"
  raised: "#2B2520"
  input: "#171411"
  ink: "#F0E8DE"
  ink-muted: "#B4A89C"
  ink-faint: "#7F746A"
  line: "#3A332C"
  line-strong: "#574B40"
  accent: "#E0A458"
  accent-soft: "#49351F"
  ok: "#7BBE9A"
  warning: "#E0A458"
  danger: "#D76E66"

typography:
  title:
    fontFamily: "Avenir Next, 'Segoe UI Variable', 'PingFang SC', sans-serif"
    fontSize: 34px
    fontWeight: 650
    lineHeight: 1.12
    letterSpacing: -0.025em
  section:
    fontFamily: "Avenir Next, 'Segoe UI Variable', 'PingFang SC', sans-serif"
    fontSize: 26px
    fontWeight: 620
    lineHeight: 1.2
    letterSpacing: -0.015em
  body:
    fontFamily: "Avenir Next, 'Segoe UI Variable', 'PingFang SC', sans-serif"
    fontSize: 16px
    fontWeight: 380
    lineHeight: 1.62
    letterSpacing: 0
  label:
    fontFamily: "Avenir Next, 'Segoe UI Variable', 'PingFang SC', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  sm: 4px
  control: 6px
  panel: 8px

spacing:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  section: 32px

components:
  panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.panel}"
    padding: 16px
  action:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.control}"
    padding: 8px 12px

elevation:
  lightSource: top-left
  steps: 3
  e1: "inset 0 0 0 1px {colors.line}"
  e2: "inset 0 0 0 1px {colors.line}, 0 1px 0 rgba(255,255,255,0.04)"
  e3: "inset 0 0 0 1px {colors.line-strong}, 0 8px 24px rgba(0,0,0,0.32)"
  topHighlight: "inset 0 1px 0 rgba(255,255,255,0.06)"
  borderLight: "{colors.line}"
  borderDark: "{colors.line-strong}"
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

事故台的核心对象不是图表，而是一条可审计的时间线。顶部固定事故级别、影响范围、开始时间、当前负责人和下一次更新。主区以时间为轴显示事实、假设、动作和验证，右栏只保留当前决定与待批准操作。所有结论都带来源与时间。

**Key Characteristics**

- 画布 `{colors.canvas}` 是暖黑石墨，避免冷蓝控制台的常规感
- 强调 `{colors.accent}` 是琥珀色，用于当前步骤与需要决定的事项
- 红色只保留给故障和危险操作，绿色只表示验证通过
- 正文 16px、行高 1.62，重要信息可连续阅读
- 圆角 4 / 6 / 8px，时间线使用连续细线而非卡片墙

## Colors

- Canvas & Surface：`{colors.canvas}`、`{colors.surface}`、`{colors.raised}`
- Ink：`{colors.ink}`、`{colors.ink-muted}`、`{colors.ink-faint}`
- Line：`{colors.line}` 与 `{colors.line-strong}`
- Accent：`{colors.accent}` 与 `{colors.accent-soft}`
- Semantic：`{colors.ok}`、`{colors.warning}`、`{colors.danger}`

## Typography

标题 34px，章节 26px，正文 16px，标签 13px。时间、命令、回执 ID 使用等宽字体。正文 380 字重，强调 620。事件标题与前一步的结论必须能单独扫读。

## Layout

顶部固定事故元信息。主区三分：时间线、当前证据、决定与待批准动作。移动端先显示元信息与当前决定，再展开时间线。时间线不隐藏历史，长事件按阶段折叠。

## Elevation & Depth

使用背景明度与分隔线表达层级。只有命令面板、批准弹层和证据抽屉使用带偏移阴影。禁止用红色边框贯穿整页制造持续恐慌。

## Shapes

面板 8px，控件 6px，标签 4px。时间点保持小尺寸圆形或方形，不使用发光点。

## Components

- 事件：时间、类型、事实、来源、执行者、回执
- 当前步骤：使用 `{colors.accent}` 强调，不闪烁
- 决定：结论、依据、风险、批准人、时间
- 验证：结果、时间窗、验证人

## Do's and Don'ts

### Do

- 每条事实带时间和来源
- 把假设明确标成假设
- 把执行动作与回执相邻
- 让接班者从顶部恢复现场

### Don't

- 不要用装饰动画模拟“紧张感”
- 不要把事实和 AI 推测混在同一列表
- 不要每天低频监控也套用事故模式

## Chinese Typography

正文行高 1.62，长说明 1.75。中英文之间留四分之一个空格。正文 380，关键结论 620。时间与单位之间使用不换行空格。

## When to Use

**用**：

- 正在发生的事故与跨团队响应
- 值班交接、故障复盘和回滚验证

**别用**：

- 日常低风险告警
- 需要同时自由探索多个无关信号的控制台

## Iteration Guide

先写清楚事故当前状态和下一步，再倒推时间线。任何不帮助接班者判断的图表都移到证据抽屉。

## Known Gaps

未覆盖公开状态页、事后长文报告和跨月多事故归档。多事故并行时需要独立的优先级视图。


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
