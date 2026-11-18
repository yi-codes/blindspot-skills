---version: beta
name: Signal Console
description: >-
  日常运维信号台。先回答哪里不对劲、证据是什么、下一步是否安全，
  再把 AI 诊断放在证据旁边。高密度来自信息关系，不来自堆 KPI。
family: operations
tier: core
sourceRefs: ui-styles-ops-console
cues: AI SRE 助手、告警分诊、日志指标追踪、服务拓扑、值班交接、日常可观测性控制台
avoid: 营销页、长文报告、公开状态页、低频任务列表、正在发生重大事故时的统一事故时间线
surface: dark
density: tight
register: tool
status: stable

colors:
  canvas: "#111820"
  surface: "#172129"
  raised: "#1D2832"
  input: "#131C24"
  ink: "#E7EDF0"
  ink-muted: "#A1ADB5"
  ink-faint: "#75828C"
  line: "#2B3742"
  line-strong: "#40505E"
  accent: "#6BA7E6"
  accent-soft: "#233B57"
  ok: "#65B58D"
  warning: "#D5A44F"
  danger: "#E06B63"
  series-4: "#9B8FD1"
  series-5: "#62B2BD"

typography:
  title:
    fontFamily: "Avenir Next, 'Segoe UI Variable', 'PingFang SC', sans-serif"
    fontSize: 27px
    fontWeight: 620
    lineHeight: 1.18
    letterSpacing: -0.02em
  section:
    fontFamily: "Avenir Next, 'Segoe UI Variable', 'PingFang SC', sans-serif"
    fontSize: 21px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.01em
  body:
    fontFamily: "Avenir Next, 'Segoe UI Variable', 'PingFang SC', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  label:
    fontFamily: "Avenir Next, 'Segoe UI Variable', 'PingFang SC', sans-serif"
    fontSize: 12px
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

信号台只围绕一个当前信号展开。页面顶部锁定环境、服务范围、时间窗和数据新鲜度；中间是信号与证据；右侧是 AI 诊断，结构固定为事实、证据、建议、风险、待批准动作。AI 不另开聊天入口，也不与系统事实混排。

**Key Characteristics**

- 深色画布 `{colors.canvas}`，表面只提升数个百分点
- 唯一强强调 `{colors.accent}` 标记当前选择和主操作
- 红色只表示故障、拒绝或高危，绿色只表示健康与验证通过
- 正文 15px、行高 1.55，密集但可扫读
- 常规面板无阴影，表格与日志优先接近方形

## Colors

- Canvas & Surface：`{colors.canvas}`、`{colors.surface}`、`{colors.raised}`、`{colors.input}`
- Ink：`{colors.ink}`、`{colors.ink-muted}`、`{colors.ink-faint}`
- Line：`{colors.line}` 与 `{colors.line-strong}`
- Accent：`{colors.accent}` 与 `{colors.accent-soft}`
- Semantic：`{colors.ok}`、`{colors.warning}`、`{colors.danger}`
- Series：`{colors.series-4}`、`{colors.series-5}` 只用于图表系列且必须直接标注

## Typography

界面使用一族无衬线。标题 27px，章节 21px，正文 15px，标签 12px。日志、时间戳、指标和 ID 使用等宽字体。表格头保持句首大写，不使用大写与宽字距伪装标签。

## Layout

顶栏放环境、服务范围、时间窗口、刷新状态。左栏是服务和严重度过滤。主区只显示当前信号或事故，以及统一的指标、日志、拓扑证据。右栏承载 AI 诊断与待批准动作。小屏依次折叠过滤、证据与诊断，不压缩宽表。

## Elevation & Depth

层级主要靠明度与 1px 内描边。抽屉、命令面板和批准弹层才使用带偏移的阴影。不要使用发光描边。

## Shapes

圆角 4 / 6 / 8px。表格、日志、拓扑优先接近方形。同一嵌套层级只使用一档圆角。

## Components

- 面板：使用 `{components.panel}`
- 主操作：使用 `{components.action}`，一屏最多一个
- 状态：文字、位置和颜色同时表达，不只用颜色
- 图表：系列直接标注名称；没有基线时只显示当前值

## Do's and Don'ts

### Do

- 所有数字带时间窗口和单位
- 把 AI 建议与系统事实分开
- 让批准动作与证据保持相邻

### Don't

- 不要做 KPI 卡片墙
- 不要使用霓虹、全屏渐变和装饰性拓扑动画
- 不要把 AI 聊天常驻在屏幕中心

## Chinese Typography

正文行高 1.55，长解释 1.7。中英文之间留四分之一个空格。正文 350，强调 600。日志与指标使用等宽数字。

## When to Use

**用**：

- 告警分诊、可观测性、服务拓扑
- AI 排障与值班交接

**别用**：

- 正在发生重大事故且需要统一事件叙事
- 公开状态页与营销页面

## Iteration Guide

先确定当前信号，再选支撑它的三组证据。任何不服务于当前判断的图表都应移到次级视图。

## Known Gaps

未覆盖三屏以上的大型数据墙与打印。复杂拓扑需要独立的交互与标签避让策略。


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
