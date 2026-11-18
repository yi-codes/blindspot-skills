---version: beta
name: Adaptive Companion
description: >-
  跨手机、平板和桌面的陪伴型工作界面。触控目标优先，信息按使用节奏渐进展开，
  同一任务在不同窗口尺寸保持相同层次；不是把桌面后台缩成手机卡片。
family: companion
tier: core
sourceRefs: material-3,fluent-2
cues: 移动端 app、跨设备助理、陪伴型工具、个人日程、触控操作、渐进式引导、响应式产品
avoid: 高密度管理后台、宽表格、事故指挥台、营销落地页、以打印为主的文档
surface: mixed
density: roomy
register: tool
status: stable
previewVariant: adaptive

colors:
  canvas: "#F1F3F4"
  surface: "#FAFBFA"
  surface-soft: "#E9EDEB"
  raised: "#FDFDFB"
  ink: "#25302F"
  ink-muted: "#5E6865"
  ink-faint: "#737D79"
  line: "#D8DDD7"
  line-strong: "#B6C0BA"
  accent: "#356D87"
  accent-strong: "#28566C"
  accent-soft: "#DCEAF0"
  ok: "#3F8068"
  warning: "#9A6B2A"
  danger: "#A64C47"
  dark-canvas: "#171D21"
  dark-surface: "#20282C"
  dark-soft: "#293338"
  dark-ink: "#E8ECEC"
  dark-muted: "#A7B1AF"
  dark-line: "#3D484D"
  dark-accent: "#8EC1D5"

typography:
  display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'PingFang SC', sans-serif"
    fontSize: 32px
    fontWeight: 650
    lineHeight: 1.18
    letterSpacing: -0.03em
  title:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'PingFang SC', sans-serif"
    fontSize: 24px
    fontWeight: 620
    lineHeight: 1.25
    letterSpacing: -0.02em
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'PingFang SC', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.62
    letterSpacing: 0
  label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'PingFang SC', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  nav:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'PingFang SC', sans-serif"
    fontSize: 12px
    fontWeight: 550
    lineHeight: 1.3
    letterSpacing: 0

rounded:
  sm: 4px
  control: 10px
  panel: 20px
  pill: 9999px

spacing:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  section: 32px
  page: 48px

components:
  panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.panel}"
    padding: 20px
  action:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.surface}"
    rounded: "{rounded.control}"
    padding: 11px 16px

elevation:
  lightSource: top-left
  steps: 3
  e1: "0 1px 2px rgba(15,23,42,0.06)"
  e2: "0 4px 12px rgba(15,23,42,0.10)"
  e3: "0 12px 32px rgba(15,23,42,0.14)"
  topHighlight: "inset 0 1px 0 rgba(255,255,255,0.60)"
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

这是一套随上下文改变结构、但不改变身份的工具型界面。手机上一屏只回答一个问题，平板允许并列信息，桌面可展开更多历史；导航、主操作和状态始终留在用户熟悉的位置。触控不是给按钮增大内边距，而是让整个页面按手势与单手操作重新编排。

**Key Characteristics**

- 画布 `{colors.canvas}` 和表面 `{colors.surface}` 保持柔和但清楚的亮度差
- 强调色 `{colors.accent}` 只标记主操作、当前页和选中状态
- 正文 16px，行高 1.62；导航与标签 12–13px
- 触控目标至少 44px，面板圆角 20px
- 手机、平板和桌面使用同一组信息角色

## Colors

- Canvas & Surface：`{colors.canvas}`、`{colors.surface}`、`{colors.surface-soft}`、`{colors.raised}`
- Ink：`{colors.ink}`、`{colors.ink-muted}`、`{colors.ink-faint}`
- Line：`{colors.line}`、`{colors.line-strong}`
- Accent：`{colors.accent}`、`{colors.accent-strong}`、`{colors.accent-soft}`
- Semantic：`{colors.ok}`、`{colors.warning}`、`{colors.danger}`

## Typography

系统无衬线负责全部界面。手机标题 32px，章节 24px，正文 16px；导航标签 12px，普通标签 13px。数字和计时器使用 tabular numerals，不用展示字体。

## Layout

手机单列，主操作固定在拇指可达区；平板使用 8 列网格；桌面最多 12 列。导航在手机上使用底部栏或抽屉，在桌面上才升级为侧栏。任何桌面宽表在手机上都要变成记录列表和详情，不横向压缩。

## Elevation & Depth

普通内容使用表面色和间距。底部操作条、抽屉和浮层允许一层柔和阴影。浮层不得遮住当前主任务的标题和主操作。

## Shapes

面板 20px、控件 10px、标签 4px，药丸只用于导航状态和极短标签。同一嵌套层级只使用一种圆角。

## Components

- 主面板：使用 `{components.panel}`
- 主操作：使用 `{components.action}`，触控高度至少 44px
- 底部栏：3–5 个目的地，当前项使用文字和形状双重状态
- 底部抽屉：先显示摘要和一个主操作，详细设置渐进展开
- 空态：说明下一步能做什么，不给装饰性插图

## Do's and Don'ts

### Do

- 保持跨设备一致的术语和操作顺序
- 让主操作在单手可达区域
- 为离线、加载、错误和空状态分别设计

### Don't

- 不要把桌面表格直接缩小
- 不要用底部导航承载超过五个目的地
- 不要用装饰性动效掩盖状态延迟

## Chinese Typography

正文行高 1.62，长说明 1.75。中英文之间留四分之一个空格。手机正文不因窄屏缩小到 16px 以下。导航标签保持原样大小写，不拉字距。

## When to Use

**用**：

- 移动助理、个人任务、跨设备笔记和轻量工作流
- 需要触控、渐进披露和多窗口适配的产品

**别用**：

- 高密度宽表与批量管理
- 以打印和长文为主的页面

## Iteration Guide

先画手机上的唯一主任务，再扩展到平板和桌面。每增加一处并列内容，都要回答它在手机上如何收起。

## Known Gaps

未覆盖原生手势冲突、平板分屏的手写笔输入和复杂离线同步。桌面端仍需使用同一 token，不另造一套主题。


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
