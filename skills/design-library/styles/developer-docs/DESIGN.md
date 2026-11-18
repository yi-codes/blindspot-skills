---version: beta
name: Developer Docs
description: >-
  现代产品文档的清晰工作区。浅色正文、稳定的侧栏、可直接执行的代码块和明确的版本状态，
  让读者从概念走到运行结果；不把等宽字体当成技术感的戏服。
family: developer
tier: core
sourceRefs: primer,geist,radix
cues: 产品文档、API 参考、SDK 指南、开发者入门、版本迁移、代码示例密集的页面
avoid: 终端模拟器、营销落地页、事故指挥台、纯打印论文、需要强情绪表达的页面
surface: mixed
density: medium
register: technical
status: stable
previewVariant: docs

colors:
  canvas: "#F4F6F4"
  surface: "#FBFCFA"
  surface-soft: "#EBEFEB"
  sunk: "#E1E7E2"
  ink: "#222A2A"
  ink-muted: "#586462"
  ink-faint: "#677270"
  line: "#D3DAD5"
  line-strong: "#AEB9B2"
  accent: "#1E6F67"
  accent-strong: "#15534E"
  accent-soft: "#DEEEEA"
  warning: "#8B6626"
  danger: "#A6423B"
  code: "#EDF1ED"
  dark-canvas: "#171C1B"
  dark-surface: "#202725"
  dark-soft: "#29312E"
  dark-ink: "#E8ECE8"
  dark-muted: "#A3AEA8"
  dark-line: "#3B4641"
  dark-accent: "#83C6BD"

typography:
  display:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif"
    fontSize: 44px
    fontWeight: 650
    lineHeight: 1.12
    letterSpacing: -0.035em
  title:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif"
    fontSize: 28px
    fontWeight: 620
    lineHeight: 1.2
    letterSpacing: -0.02em
  body:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.72
    letterSpacing: 0
  label:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif"
    fontSize: 13px
    fontWeight: 550
    lineHeight: 1.4
    letterSpacing: 0
  code:
    fontFamily: "'Geist Mono', 'SF Mono', ui-monospace, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0

rounded:
  sm: 4px
  control: 6px
  panel: 10px

spacing:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  section: 40px
  page: 64px

components:
  panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.panel}"
    padding: 24px
  action:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.surface}"
    rounded: "{rounded.control}"
    padding: 9px 14px

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
  logoType: wordmark
  logoRule: "字标沿用显示字族，右侧留 0.5em；图形标只用单色 {colors.ink}，最小 24px"
  imageRadius: "{rounded.panel}"
  imageRatio: "16:10"
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
  dragUsesSpring: false
---
## Overview

面向开发者的文档首先是一套可导航的阅读系统，不是终端外观。页面必须让读者快速判断“这是哪个版本、这个概念解决什么问题、命令能否直接运行、失败时下一步看哪里”。代码和数据使用等宽字体，说明、导航与标签仍使用正文体系。

**Key Characteristics**

- 画布 `{colors.canvas}` 与内容面 `{colors.surface}` 只拉开一档，适合长时间阅读
- 唯一强调色 `{colors.accent}` 标记链接、当前目录和主操作
- 正文 17px、行高 1.72；代码 14px、行高 1.6
- 侧栏、正文和右侧目录形成稳定的三列阅读结构
- 所有代码块都有语言、复制状态和版本上下文

## Colors

- Canvas & Surface：`{colors.canvas}`、`{colors.surface}`、`{colors.surface-soft}`、`{colors.sunk}`
- Ink：`{colors.ink}`、`{colors.ink-muted}`、`{colors.ink-faint}`
- Line：`{colors.line}`、`{colors.line-strong}`
- Accent：`{colors.accent}`、`{colors.accent-strong}`、`{colors.accent-soft}`
- Code：`{colors.code}` 只用于代码块和行内代码
- Semantic：`{colors.warning}`、`{colors.danger}`

## Typography

正文与界面使用一个无衬线家族，代码和命令使用等宽字体。标题 44 / 28px，正文 17px，标签 13px，代码 14px。避免把导航、按钮和普通标签改成等宽字体。

## Layout

桌面为三栏：240px 文档导航、主内容、200px 页内目录。主内容正文不超过 72ch，代码和表格允许更宽。移动端把导航收进页面顶部的目录按钮，页内目录放到文末，不横向压缩代码。

## Elevation & Depth

页面不使用悬浮卡片。侧栏通过表面色区分，抽屉与搜索浮层允许一层带偏移阴影。代码块用背景和发丝线建立边界，不使用阴影。

## Shapes

控件 6px，代码块和提示块 10px，标签 4px。正文区域不加圆角容器；只有可独立操作的代码、搜索和浮层使用圆角。

## Components

- 代码块：语言、文件名、复制、执行状态使用 `{components.panel}`
- 主操作：使用 `{components.action}`，一页只保留一个主要行动
- 导航：当前项用文字加粗与强调色，不只用背景色
- 版本：版本号始终靠近标题或代码示例
- 警告：先说影响，再给恢复命令

## Do's and Don'ts

### Do

- 让概念页、任务页和 API 参考共享同一套导航
- 示例代码先可运行，再解释可选参数
- 在版本切换处说明差异和不兼容项

### Don't

- 不要把整个文档做成深色终端
- 不要用等宽字体装饰所有标签
- 不要用无来源的“最佳实践”代替明确约束

## Chinese Typography

正文行高 1.72，代码行高 1.6。中英文之间留四分之一个空格。路径、命令、API 名保持原样大小写；中文说明不使用大写或宽字距伪装层级。

## When to Use

**用**：

- API、SDK、产品使用手册和开发者入门
- 需要搜索、版本切换和大量代码示例的站点

**别用**：

- 事故指挥与实时监控
- 纯展示型品牌页

## Iteration Guide

先修阅读路径和代码可执行性，再调整表面。新增组件前先检查能否用标题、列表、代码块和提示块表达。

## Known Gaps

未覆盖多语言 API 文档生成器与跨版本自动迁移。搜索需要接入实际索引服务，静态预览不验证结果相关性。


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
