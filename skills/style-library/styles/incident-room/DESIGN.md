---
version: alpha
name: Incident Room
description: >-
  面向进行中事故的协作控制台。暖黑画布、窄圆角、明确的严重度高亮和单一事故叙事：
  左侧证据与时间线，中间处置记录，右侧负责人、影响范围和 AI 调查建议；
  页面像值班房间的共享工作台，强调时间、决策和交接。
cues: 事故响应、故障处置、war room、值班交接、回滚决策、根因排查、AI 事故分析
avoid: 日常数据看板、营销落地页、长文阅读、公开状态页、多人社交聊天
surface: dark
register: operations

colors:
  canvas: "#11100F"
  surface: "#191816"
  surface-alt: "#23211E"
  surface-hover: "#2B2824"
  surface-input: "#0D0C0B"
  ink: "#F2EEE7"
  ink-muted: "#B8B1A7"
  ink-faint: "#857F77"
  hairline: "#37332E"
  hairline-strong: "#514A43"
  primary: "#F3B64D"
  primary-soft: "#332713"
  success: "#61C79C"
  warning: "#E4A83E"
  danger: "#FF7165"
  info: "#82B9FF"
typography:
  incident-title:
    fontFamily: "Inter, SF Pro Text, PingFang SC, system-ui, sans-serif"
    fontSize: 30px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.025em
  section-heading:
    fontFamily: "Inter, SF Pro Text, PingFang SC, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.01em
  entry-title:
    fontFamily: "Inter, SF Pro Text, PingFang SC, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.45
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, SF Pro Text, PingFang SC, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  label-md:
    fontFamily: "Inter, SF Pro Text, PingFang SC, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.01em
  machine-label:
    fontFamily: "Geist Mono, SF Mono, ui-monospace, monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  code-md:
    fontFamily: "Geist Mono, SF Mono, ui-monospace, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
rounded:
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  xxl: 32px
  section: 48px
  measure: 72ch
components:
  surface:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 16px
  timeline-entry:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
  action-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  action-danger:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  status-tag:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.label-md}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  evidence:
    backgroundColor: "{colors.surface-input}"
    textColor: "{colors.ink}"
    typography: "{typography.code-md}"
    rounded: "{rounded.sm}"
    padding: 12px
---

## Overview

Incident Room 是为“事故正在发生”设计的控制台风格。页面只有一个主角：当前事故。所有信息都回答值班团队此刻能否更快判断、采取动作或完成交接。它适合 P1/P2 级别的线上故障、回滚决策、共同诊断和事故时间线，不承担日常大盘的全部职责。

视觉上借用 Grafana 事故时间线的单线阅读、SigNoz 紧凑的数据层，以及 Kiali 拓扑节点把状态与流量合并呈现的做法。暖黑底降低长时间盯屏的冷感；窄圆角和清晰边框让界面更像操作台而不是卡片集合。强调色是琥珀，红色只属于当前故障，绿色只属于恢复和验证通过。

与 `signal-console` 的区别是注意力范围。Signal Console 面向广阔的信号空间和调查；Incident Room 面向一个事故的处置过程，固定显示负责人、影响范围、时间线与下一步动作。

**Key Characteristics**

- 一个页面只有一个事故标题 `{colors.ink}`；次级事故或相关告警放在附属列表。
- 画布 `{colors.canvas}` 与工作表面 `{colors.surface}` 只差一档亮度，形成连续工作区。
- 时间线和事件都使用统一时间轴；每条记录包含时间、执行者、动作、结果。
- AI 调查是证据面板，不是聊天气泡；建议和事实分层显示。
- 常规区域无阴影，只有确认弹层和交接抽屉使用阴影。
- 圆角 2 / 4 / 6 / 8px，提示条和状态标签不变成大药丸。

## Colors

### Canvas & Surface

- **Canvas** (`{colors.canvas}` — #11100F): 暖黑底，降低纯灰界面的冷感。
- **Surface** (`{colors.surface}` — #191816): 事故页主工作区。
- **Surface Alt** (`{colors.surface-alt}` — #23211E): 负责人卡、证据分组和次级行。
- **Surface Hover** (`{colors.surface-hover}` — #2B2824): 时间线悬停和当前步骤。
- **Surface Input** (`{colors.surface-input}` — #0D0C0B): 日志、命令和原始证据。

### Ink

- **Ink** (`{colors.ink}` — #F2EEE7): 事故标题、当前状态和关键动作。
- **Ink Muted** (`{colors.ink-muted}` — #B8B1A7): 时间线正文、说明与次级负责人。
- **Ink Faint** (`{colors.ink-faint}` — #857F77): 时间、ID、来源标签。

### Status

- **Primary** (`{colors.primary}` — #F3B64D): 当前阶段、需要确认的动作和当前选中时间点。
- **Warning** (`{colors.warning}` — #E4A83E): 风险、等待确认和不稳定指标。
- **Danger** (`{colors.danger}` — #FF7165): 故障主体、失败动作和不可逆风险。
- **Success** (`{colors.success}` — #61C79C): 已恢复、验证通过和回滚成功。
- **Info** (`{colors.info}` — #82B9FF): 查看证据、外部文档和一般链接。

## Typography

字号阶为 11 / 12 / 13 / 14 / 15 / 18 / 30px。

- **Incident Title** (`{typography.incident-title}` — 30px / 600): 只给当前事故。
- **Section Heading** (`{typography.section-heading}` — 18px / 600): 时间线、影响范围、AI 调查。
- **Entry Title** (`{typography.entry-title}` — 15px / 500): 时间线条目与动作名称。
- **Body** (`{typography.body-md}` — 14px / 400 / 1.6): 事故描述与交接。
- **Label** (`{typography.label-md}` — 12px / 500): 状态、负责人和筛选。
- **Machine Label** (`{typography.machine-label}` — 11px / 400): 时间、服务名和英文枚举。
- **Code** (`{typography.code-md}` — 13px / 400): 日志、命令和错误堆栈。

## Layout

固定骨架为顶部事故横幅、左中右三列和底部可停靠对话区。

- 顶部横幅 64–88px：事故标题、严重度、开始时间、负责人、当前状态。
- 左列 280–360px：影响范围、服务、告警与相关事故。
- 中列自适应：事故时间线、处置记录、AI 证据。
- 右列 300–380px：下一步、批准动作、回滚与交接。
- 底部对话区仅承载协作和 AI 追问，不复制主时间线。

4px 基础网格，间距 4 / 8 / 12 / 16 / 24 / 32 / 48px。时间线行高不低于 44px。

## Elevation & Depth

事故工作区没有卡片阴影。层级依靠：

1. 画布、工作表面和输入面三档底色。
2. 事件线的连续竖线 `{colors.hairline-strong}`。
3. 当前事件用左缘 2px `{colors.primary}`，不使用外扩光圈。

确认动作、交接抽屉和回滚弹窗使用 `0 14px 40px rgba(0,0,0,0.5)`。

## Shapes

圆角只用 2 / 4 / 6 / 8px。时间线和状态标签接近方形；只有严重度点、头像和筛选 chip 使用胶囊。

禁止大圆角卡片、玻璃模糊和渐变边框。事故状态需要像仪表和记录，不像消费产品通知。

## Components

### surface

`{components.surface}` 是事故页的主要分区，使用表面色、发丝线和 6px 圆角。

### timeline-entry

`{components.timeline-entry}` 沿同一竖轴排列。时间放第一列，动作放第二列，结果与证据放正文。不会把每条更新包成独立浮卡。

### action-primary / action-danger

`{components.action-primary}` 用于当前推荐且风险可控的动作。`{components.action-danger}` 用于回滚、删除或扩大故障范围的动作，必须写明影响对象和不可逆部分。

### status-tag

`{components.status-tag}` 同时显示文字与色点。状态词固定：调查中、已缓解、观察中、已恢复、待批准。

### evidence

`{components.evidence}` 放日志、查询、命令与截图引用。证据块必须有来源和时间范围。

## Do's and Don'ts

### Do

- 把事故开始时间、影响范围和是否仍在扩大放在首屏。
- 每条时间线记录写清时间、执行者、动作、结果。
- AI 建议先给证据，再给建议，再给风险与批准要求。
- 将人工操作、自动操作、只读调查和外部等待分开标记。
- 为交接保留固定摘要：现状、时间线、待决策、下一步、相关链接。
- 用文字、图标和颜色共同表达严重度。

### Don't

- 不要在事故页铺满无关 KPI 卡。
- 不要让 AI 对话占据页面中心；时间线与处置状态才是主线。
- 不要用红色表示普通删除按钮或装饰。
- 不要把同一事实同时写进顶部摘要、时间线和右侧建议三遍。
- 不要使用自动播放的拓扑动画模拟流量；只有真实流量数据才能动。
- 不要在事故期间加入需要理解的新视觉语言。

## Chinese Typography

- 中文正文行高不低于 1.6；时间线条目允许 1.45，但中文说明不得低于 12px。
- 中西文之间留 1/4 空格：`Pod 3 个`、`查询 P99 延迟`。
- 事故状态使用固定中文词；英文 `P1`、`HTTP 502`、`us-east-1` 作为机器字段保留。
- 时间统一显示 `HH:mm:ss`，跨日时补日期；时区只在顶部出现一次。
- 动作名称使用动词开头：确认回滚、暂停发布、扩大采样、恢复流量。
- 避免全大写中文标签、负字距和艺术化小数。

## Incident Flow

1. **识别**：事故标题、严重度、起始时间、影响范围。
2. **判断**：相关信号、拓扑节点、日志与最近变更。
3. **决策**：AI 建议、证据、风险、负责人批准。
4. **执行**：动作记录、执行者、开始与完成时间。
5. **验证**：错误率、延迟、流量和业务指标是否恢复。
6. **交接**：现状、未决问题、下一班负责人、审计链接。

## When to Use

**用**：线上事故响应、P1/P2 war room、回滚决策、故障时间线、值班交接、AI 事故调查。

**别用**：分钟级监控大盘、日常报表、公开状态页、事故复盘长文、跨团队项目管理。

## Iteration Guide

1. 先固定时间和责任链，再添加图表和装饰。
2. 每增加一块信息，问它属于识别、判断、决策、执行、验证还是交接。
3. 将 AI 文字放在证据旁，不新增独立聊天页。
4. 危险动作先检查影响对象、撤销方法和审批人。
5. 交接摘要变化时必须同步时间线和当前状态。

## Known Gaps

- 未定义多人实时协作光标、语音和外部会议集成。
- 未覆盖跨区域大规模拓扑的性能优化。
- 未定义公开状态页的对外语气。
- 生图只适合事故复盘背景和封面，不用于生成可操作的界面。
