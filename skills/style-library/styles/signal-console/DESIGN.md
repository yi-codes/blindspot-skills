---
version: alpha
name: Signal Console
description: >-
  面向 AI 运维控制台的高密度界面。中性石墨底、蓝色运行信号与低饱和状态色，
  信息按“发生了什么、证据是什么、AI 建议做什么、批准后留下什么回执”组织；
  卡片像网络和日志工作区一样扁平，浮层才使用阴影。
cues: 运维控制台、告警分诊、可观测性、日志指标追踪、服务拓扑、AI SRE 助手、长期值守
avoid: 营销落地页、长文阅读、消费级应用、公开状态页、创意作品集
surface: mixed
register: operations

colors:
  canvas: "#0B0F14"
  surface: "#141A21"
  surface-alt: "#1B2430"
  surface-hover: "#202936"
  surface-input: "#0F141A"
  ink: "#E6EDF5"
  ink-muted: "#A7B4C2"
  ink-faint: "#7E8B98"
  hairline: "#293440"
  hairline-strong: "#405061"
  primary: "#5AA7FF"
  primary-soft: "#132B45"
  success: "#57C98D"
  warning: "#E6AA45"
  danger: "#F06A6A"
  info: "#5EC8E5"
  series-1: "#5AA7FF"
  series-2: "#57C98D"
  series-3: "#E6AA45"
  series-4: "#B99AF5"
  series-5: "#5EC8E5"
  light-canvas: "#F5F7F9"
  light-surface: "#FFFFFF"
  light-surface-alt: "#E9EEF3"
  light-surface-hover: "#E2E8EE"
  light-surface-input: "#EEF2F5"
  light-ink: "#18212B"
  light-ink-muted: "#566574"
  light-ink-faint: "#7C8996"
  light-hairline: "#D7DEE5"
  light-hairline-strong: "#BBC6D1"
  light-primary: "#0B6FD8"
  light-primary-soft: "#E5F0FD"
  light-success: "#167A57"
  light-warning: "#9A6400"
  light-danger: "#BE3947"
  light-info: "#087D96"
  light-series-1: "#0B6FD8"
  light-series-2: "#167A57"
  light-series-3: "#8A5A00"
  light-series-4: "#6E4CC2"
  light-series-5: "#087D96"
typography:
  console-title:
    fontFamily: "Inter, SF Pro Text, PingFang SC, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.02em
  section-heading:
    fontFamily: "Inter, SF Pro Text, PingFang SC, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.01em
  row-title:
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
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
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
  measure: 74ch
components:
  panel:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 16px
  metric:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 12px
  signal-row:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  action-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  action-secondary:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.ink}"
    typography: "{typography.label-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  status-tag:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.label-md}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  code-block:
    backgroundColor: "{colors.surface-input}"
    textColor: "{colors.ink}"
    typography: "{typography.code-md}"
    rounded: "{rounded.sm}"
    padding: 12px
---

## Overview

Signal Console 面向长期盯屏的运维与 SRE 控制台。它把“系统当前是否健康、哪个信号变了、AI 为什么这样判断、下一步动作是否安全”放在同一视线里。页面首先服务诊断和处置，阅读舒适度服从于扫读与证据核对。

风格沿用成熟可观测性产品的密度，而不照搬它们的皮肤：Grafana 的 14px 正文、扁平卡片、显式表面层级和仅用于叠层的阴影；SigNoz 的 13px 日志行、紧凑表格、状态标签和清晰的明暗主题 token。再叠加 Kiali 的拓扑优先和“节点状态与流量标签一起出现”原则，形成面向 AI 运维控制台的结构。

它与 `quiet-dark` 的区别是密度和目标。`quiet-dark` 适合低频决定和 Agent 对话；Signal Console 允许更多列、更多数字、更多实时行，并要求图表、日志和 AI 建议始终共享时间范围和来源。

**Key Characteristics**

- 默认深色画布 `{colors.canvas}`，卡片只上浮一档到 `{colors.surface}`；浅色模式使用 `{colors.light-canvas}` 和白色工作表面。
- 蓝色 `{colors.primary}` 只表示可操作、被选中或系统正在运行。警告和故障只用 `{colors.warning}`、`{colors.danger}`。
- 正文 14px，机器标签 11px，数据行 13px 等宽。高密度来自布局和行距，不靠继续缩字号。
- 常规面板没有投影，使用 1px 发丝线和表面明度分层。只有命令面板、抽屉和确认弹层允许阴影。
- 圆角集中在 4 / 6 / 8 / 12px。拓扑节点、表格和日志工作区优先接近方形。
- 同一屏必须保留统一时间范围；图表、日志、事件和建议的时区与窗口必须一致。

## Colors

### Canvas & Surface

- **Canvas** (`{colors.canvas}` — #0B0F14): 深色模式窗口底。给图表和网格留出稳定压低层，不使用纯黑。
- **Surface** (`{colors.surface}` — #141A21): 主要工作表面、事件行和面板。
- **Surface Alt** (`{colors.surface-alt}` — #1B2430): 次级块、选中行底色和指标单元。
- **Surface Hover** (`{colors.surface-hover}` — #202936): 行和节点的悬停态。
- **Surface Input** (`{colors.surface-input}` — #0F141A): 查询编辑器、日志和命令输出。
- **Light Canvas / Surface** 由 `light-*` 前缀的 token 定义；切换主题只替换颜色和阴影，不改尺寸与布局。

### Ink

- **Ink** (`{colors.ink}` — #E6EDF5): 标题、关键数值和主要操作。
- **Ink Muted** (`{colors.ink-muted}` — #A7B4C2): 说明、标签、次级值。
- **Ink Faint** (`{colors.ink-faint}` — #7E8B98): 时间、ID、网格注释。中文正文不得低于 12px。

### Semantic & Series

- **Primary** (`{colors.primary}` — #5AA7FF): 当前操作、已选节点、AI 正在引用或新增的信号。
- **Success** (`{colors.success}` — #57C98D): 健康、恢复、验证通过。
- **Warning** (`{colors.warning}` — #E6AA45): 性能退化、阈值接近、等待批准。
- **Danger** (`{colors.danger}` — #F06A6A): 故障、拒绝、失败和高风险动作。
- **Info** (`{colors.info}` — #5EC8E5): 非主操作链路的信息和拓扑边。
- **Series 1–5**：仅用于同时出现的多条指标曲线。必须直接标注系列名，不能只靠颜色。

## Typography

字号阶为 11 / 12 / 13 / 14 / 15 / 18 / 28px。11px 只用于机器标签、端口、路径和英文代码；中文最小 12px。

- **Console Title** (`{typography.console-title}` — 28px / 600): 页面级标题或正在处理的事故名称。
- **Section Heading** (`{typography.section-heading}` — 18px / 600): 面板和诊断分区标题。
- **Row Title** (`{typography.row-title}` — 15px / 500): 事件、服务和告警行标题。
- **Body** (`{typography.body-md}` — 14px / 400 / 1.6): 说明和操作正文。
- **Label** (`{typography.label-md}` — 12px / 500): 状态、过滤器和表格表头。
- **Code** (`{typography.code-md}` — 13px / 400): 日志、命令、查询和堆栈。

常规界面只用 400 / 500 / 600 三档。排序、表格和指标使用 `tabular-nums`。

## Layout

4px 基础网格，常用间距为 4 / 8 / 12 / 16 / 24 / 32px。主框架建议三档：

1. 左侧 216–248px：服务、环境和保存视图。
2. 中间自适应：时间轴、指标、日志或拓扑。
3. 右侧 320–420px：AI 诊断、证据和操作确认。

顶部工具栏 48px，筛选行 40px，表格行 36–44px，日志行 24–28px。正文阅读宽度 `{spacing.measure}` 只用于 AI 解释，不限制表格和图表。

窗口小于 900px 时先收右侧 AI 面板为抽屉；小于 640px 时再收起左侧导航，保留时间范围和告警严重度。

## Elevation & Depth

普通查询区、指标面板、表格和拓扑没有阴影。层级由三件事表达：

1. 画布、面板、抬升面板三档底色。
2. 1px `{colors.hairline}`；输入与激活边界使用 `{colors.hairline-strong}`。
3. 选择态用左缘 2px 强调线或 `{colors.primary-soft}` 底，不上浮卡片。

只有命令面板、详情抽屉、确认弹层和悬浮 AI 引用使用 `0 18px 48px rgba(0,0,0,0.42)`。浅色模式使用更短的 `0 10px 28px rgba(18,24,32,0.14)`。

## Shapes

圆角分四档：4 / 6 / 8 / 12px，胶囊只用于严重度和过滤 token。

- 输入、按钮、事件行：6px。
- 面板、图表容器：8px。
- 抽屉和模态：12px。
- 拓扑节点与表格：4px，保持可连接和可对齐。

不要用 16–20px 的大圆角，也不要在同一区域混用胶囊与直角卡片。

## Components

### panel

`{components.panel}` 是基本工作表面：表面底色 + 1px 发丝线 + 8px 圆角，无阴影。面板标题与内容之间保留 12px 间距。

### metric

`{components.metric}` 只放一个值、一个标签和一个变化方向。变化必须带时间窗口；没有基线时只显示当前值。

### signal-row

`{components.signal-row}` 用于告警、日志摘要和事件。左侧列固定放严重度，右侧放时间、来源和对象，正文只写一个事实。

### action-primary / action-secondary

`{components.action-primary}` 只给当前最重要的处置或确认。`{components.action-secondary}` 用于查看证据、复制查询和暂缓。高风险动作必须和影响范围一起出现。

### status-tag

`{components.status-tag}` 同时显示文字和色点。禁止只用颜色区分严重度；色彩之外要保留文字、图标或行位置。

### code-block

`{components.code-block}` 用于命令、标签集、查询和日志证据。允许横向滚动，不自动折行。

## Do's and Don'ts

### Do

- 先显示当前最异常或最值得处理的信号，再显示全局统计。
- 把时间范围、环境、服务范围和采样窗口放在图表附近。
- 让 AI 结论紧邻证据；每条建议都能打开原始指标、日志、拓扑或事件。
- 用直接标签代替长图例；系列超过五条时合并或提供筛选。
- 表格数字右对齐并使用等宽数字。
- 视觉变化优先使用边框、底色、位置和文字，颜色只承担语义。
- 主题切换只替换颜色、阴影和图表色板，不改布局。

### Don't

- 不要把所有内容都塞进卡片；表格、日志和拓扑本身不需要再次套卡片。
- 不要用渐变、光晕、玻璃模糊或呼吸光表示“智能”。
- 不要使用红色装饰；红色只代表故障、拒绝或高危动作。
- 不要在上方铺 KPI 大卡而把异常藏在下面。
- 不要写没有时间窗口的“上升 18%”或没有来源的 AI 结论。
- 不要把 AI 建议与系统事实混在同一列表；两者必须可区分。

## Chinese Typography

- 中文正文行高不低于 1.6；日志与机器标签可以紧凑，但中文注释不得小于 12px。
- 中西文之间留 1/4 空格：`Pod 12 个`、`查询 P95 延迟`。
- 状态标签优先使用“严重 / 警告 / 恢复”等中文词，英文枚举 `critical / warning / healthy` 只放在机器字段。
- 时间、资源量和 ID 使用等宽数字；单位与数值之间留一个半角空格。
- 中文标题不追加大字距；全大写仅用于真实英文环境变量和协议名。
- 使用全角中文标点，`line-break: strict`，不首行缩进。

## Operations Layout

- 首屏先给“最近 30 分钟”或“当前事故”单一焦点，不做无上下文的九宫格。
- 监控、排查和处置共用当前时间范围。跨视图跳转时继承服务、环境和时间窗口。
- 顶部固定显示环境、数据新鲜度、时间范围与自动刷新状态。
- AI 面板回答四个问题：发生了什么、证据是什么、最可能原因、建议动作；不要输出泛泛的“持续关注”。
- 手动动作、自动动作、回滚和只读查询必须使用不同标签。
- 动作完成后显示结果、时间、执行者和可回放的审计记录。

## When to Use

**用**：可观测性平台、AI SRE 助手、告警中心、服务拓扑、日志与追踪工作台、值班控制台。

**别用**：营销页面、长文报告、对外状态页、低密度任务待办、仅展示概念的演示首页。

## Iteration Guide

1. 先用 `{components.panel}` 建立工作表面，再增加指标、日志或拓扑。
2. 新增一个颜色前先检查它是否承担状态语义。
3. 新信息必须绑定对象、时间和来源；缺一项就不进入主视图。
4. 需要更强层级时，先调整位置和尺寸，再使用边框，最后才使用强调色。
5. 每次主题切换后重新检查对比度、图表系列识别和网格线可见度。

## Known Gaps

- 未定义具体图表渲染库；实现时应把主题颜色解析成实际色值。
- 浅色模式下高密度日志需要额外验证，12px 只是下限。
- 拓扑自动布局、边标签碰撞和大规模给性能策略不在本规范内。
- 未定义告警抑制、SLO 和值班排班等业务流程。
- 生图只适合控制室氛围图，不适合直接生成可读 UI。
