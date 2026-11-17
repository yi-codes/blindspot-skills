---
version: beta
name: Enterprise Data
description: >-
  面向真实业务操作的数据界面。表格、筛选、批量动作、权限与审计信息共用一套稳定尺度，
  让熟练用户在一屏内完成判断和修改；不把后台做成 KPI 卡片墙。
family: enterprise-data
tier: core
sourceRefs: carbon,radix
cues: 企业管理后台、数据表格、批量操作、权限与审计、订单账单、客户运营、B 端管理工作流
avoid: 品牌营销页、长文阅读、移动优先消费产品、事故时间线、沉浸式展示
surface: mixed
density: tight
register: professional
status: stable
previewVariant: table

colors:
  canvas: "#EEF1F2"
  surface: "#F8FAFA"
  surface-alt: "#E7ECEE"
  sunk: "#E1E7E9"
  ink: "#20282E"
  ink-muted: "#56656D"
  ink-faint: "#6E7D84"
  line: "#D1D9DE"
  line-strong: "#AEBAC2"
  accent: "#2E6D58"
  accent-strong: "#225542"
  accent-soft: "#DDECE5"
  info: "#356B9D"
  warning: "#92671F"
  danger: "#A7433D"
  dark-canvas: "#151B1F"
  dark-surface: "#1D252A"
  dark-raised: "#263037"
  dark-ink: "#E7EDF0"
  dark-muted: "#A3AFB6"
  dark-line: "#39464F"
  dark-accent: "#79BCA2"

typography:
  title:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif"
    fontSize: 28px
    fontWeight: 620
    lineHeight: 1.18
    letterSpacing: -0.02em
  section:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.28
    letterSpacing: -0.01em
  body:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  label:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  data:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif"
    fontSize: 13px
    fontWeight: 420
    lineHeight: 1.45
    letterSpacing: 0

rounded:
  sm: 2px
  control: 4px
  panel: 6px

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
    textColor: "{colors.surface}"
    rounded: "{rounded.control}"
    padding: 7px 12px
---

## Overview

企业数据界面不靠卡片表达业务，而靠可比较的行、可复用的列和始终可见的动作。用户多数已经在工作中，目标不是被吸引，而是快速找到记录、判断状态、批量修改并留下审计证据。

**Key Characteristics**

- 画布 `{colors.canvas}`、内容面 `{colors.surface}` 和表头 `{colors.surface-alt}` 形成三级工作表面
- 唯一主动作色 `{colors.accent}` 用于选中、提交和确认
- 正文 15px，表格数据 13px，所有数字等宽对齐
- 圆角 2 / 4 / 6px，表格和筛选区接近方形
- 表格优先，卡片只用于独立详情

## Colors

- Canvas & Surface：`{colors.canvas}`、`{colors.surface}`、`{colors.surface-alt}`、`{colors.sunk}`
- Ink：`{colors.ink}`、`{colors.ink-muted}`、`{colors.ink-faint}`
- Line：`{colors.line}`、`{colors.line-strong}`
- Accent：`{colors.accent}`、`{colors.accent-strong}`、`{colors.accent-soft}`
- Semantic：`{colors.info}`、`{colors.warning}`、`{colors.danger}`

## Typography

标题 28px，章节 20px，正文 15px，表格与筛选标签 13px，辅助元信息 12px。数字、金额、ID、时间和计数启用 tabular numerals。标签不通过全大写和宽字距制造层级。

## Layout

顶栏放组织、环境和全局搜索；左栏放业务域与保存视图；主区是全宽表格或列表；详情使用右侧抽屉，不把每一行变成卡。移动端保留主键列和主操作，其他列进入行详情。

## Elevation & Depth

常规区域只使用表面色与边界。批量操作栏固定时使用底边分界；抽屉、筛选浮层和命令菜单使用带偏移阴影。禁止给每一行加阴影。

## Shapes

表格与筛选区接近方形；控件 4px，面板 6px。状态标签 2px。不要在表格里混用大量药丸和圆形按钮。

## Components

- 数据表：固定表头、可排序、可调整列宽；使用 `{components.panel}`
- 主操作：使用 `{components.action}`，批量动作必须显示作用数量
- 筛选：当前条件有可见摘要，并提供一键清除
- 详情：抽屉展示完整记录、权限和审计
- 空态：解释为何为空，并给唯一补数动作

## Do's and Don'ts

### Do

- 让主键列和行操作保持稳定位置
- 批量操作前明确影响范围和不可逆性
- 把审计信息放在记录详情内

### Don't

- 不要用 KPI 卡片墙代替数据关系
- 不要让每个单元格都成为可点击卡片
- 不要只用颜色表示状态

## Chinese Typography

界面行高 1.5，长说明可提升到 1.7。中英文之间留四分之一个空格。表格标签 13px 起，关键标签不低于 12px。数字与单位之间保持不换行。

## When to Use

**用**：

- 客户、订单、账单、权限、审计与运营管理
- 需要筛选、批量修改和记录追踪的 B 端工作流

**别用**：

- 面向消费者的轻量 app
- 品牌叙事和长文阅读

## Iteration Guide

先设计一条真实记录从发现到修改的路径，再决定列和筛选。能用一个表格表达的关系，不要拆成卡片网格。

## Known Gaps

未覆盖超宽 50 列以上表格的冻结策略与虚拟滚动。复杂权限矩阵需要独立交互验证。

