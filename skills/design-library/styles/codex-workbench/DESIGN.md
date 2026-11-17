---
version: beta
name: Codex Workbench
description: >-
  暖中性纸面上的安静工作台。大标题负责建立叙事，正文保持连续可读，
  状态与操作只用少量低饱和绿色。不是缩小字号的仪表盘，也不是卡片拼贴。
family: workbench
tier: core
sourceRefs: openai-codex-observed
cues: Agent 任务工作台、产品方案页、设置页、插件面板、需要连续阅读和反复操作的工具页
avoid: 营销落地页、强视觉叙事作品、数据密集型分析大屏、需要高密度多维图表的事故台
surface: mixed
density: medium
register: tool
status: stable

colors:
  canvas: "#F7F5F0"
  surface: "#FCFAF5"
  surface-soft: "#EFECE5"
  ink: "#2A322D"
  ink-muted: "#66706A"
  ink-faint: "#838A85"
  hairline: "#DEDAD1"
  hairline-strong: "#C4C0B6"
  accent: "#2D7557"
  accent-soft: "#DDEADF"
  warning: "#946A2D"
  danger: "#A4483E"
  dark-canvas: "#1D211F"
  dark-surface: "#262C28"
  dark-surface-soft: "#303732"
  dark-ink: "#E9EAE5"
  dark-muted: "#ABB2AC"
  dark-line: "#3B433E"
  dark-accent: "#8DC5A8"

typography:
  display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'PingFang SC', sans-serif"
    fontSize: 42px
    fontWeight: 650
    lineHeight: 1.14
    letterSpacing: -0.035em
  title:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'PingFang SC', sans-serif"
    fontSize: 28px
    fontWeight: 650
    lineHeight: 1.18
    letterSpacing: -0.02em
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'PingFang SC', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.72
    letterSpacing: 0
  label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'SF Pro Text', 'PingFang SC', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  control: 9px
  panel: 14px

spacing:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  section: 48px

components:
  surface:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.panel}"
    padding: 24px
  action:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.surface}"
    rounded: "{rounded.control}"
    padding: 10px 16px
---

## Overview

它追求“像原生工具一样安静、直接、可扫描”。暖中性底面降低长时间阅读的冷硬感，标题负责叙事，正文负责解释，只有真正需要注意的状态才出现颜色。卡片只承载并列信息，长文留在正文里。

**Key Characteristics**

- 画布 `{colors.canvas}` 是暖灰纸，面板 `{colors.surface}` 只亮一档
- 强调色 `{colors.accent}` 是低饱和绿色，只标记确认、成功和当前状态
- 正文 16px、行高 1.72，连续阅读优先
- 圆角 14px 和 9px，边界主要靠发丝线
- 一屏只有一个主问题和一组主行动

## Colors

- Canvas & Surface：`{colors.canvas}`、`{colors.surface}`、`{colors.surface-soft}`
- Ink：`{colors.ink}`、`{colors.ink-muted}`、`{colors.ink-faint}`
- Line：`{colors.hairline}` 与 `{colors.hairline-strong}`
- Accent：`{colors.accent}` 与 `{colors.accent-soft}`
- Semantic：`{colors.warning}`、`{colors.danger}` 只用于风险和错误

## Typography

标题与正文使用同族系统字体。显示标题 42px，章节标题 28px，正文 16px。辅助标签 12px。数字、时间、ID、命令使用等宽字体。不使用连续三个相近字号制造假层级。

## Layout

产品文档使用顶部产品名、单句状态、核心变化、关键结论、决策章节和下一步。工具工作台保留产品级顶部导航；设置页使用窄二级导航；详情进入抽屉或独立阅读栏，不把细节塞进任务卡。

## Elevation & Depth

普通区域使用间距和发丝线。只有抽屉、菜单和对话框允许一层柔和阴影。卡片不使用阴影做常规层级。

## Shapes

面板 14px，控件 9px，标签 4px。同一嵌套层级只使用一种圆角。按钮不使用药丸形状。

## Components

- 表面：使用 `{components.surface}`，不加普通阴影
- 主操作：使用 `{components.action}`，一屏最多一个
- 章节标题：一句结论在上，解释和证据在下
- 状态标签：文字先说明状态，颜色只辅助

## Do's and Don'ts

### Do

- 让正文保持 60 至 72ch 的阅读宽度
- 每个章节先给结论，再给解释和证据
- 把技术约束放进可折叠细节

### Don't

- 不要每段都包卡片
- 不要在正文里再嵌套第二层卡片
- 不要用过小字号和 GPT 式假窗口装饰冒充 Codex

## Chinese Typography

正文行高 1.72。中英文之间留四分之一个空格。正文 400，强调 650；不使用无效的 500 与 600 连续堆叠。深色模式正文改为 350。

## When to Use

**用**：

- 产品方案、任务工作台、设置页、Agent 插件面板
- 需要连续阅读同时反复操作的界面

**别用**：

- 高密度多维图表的大屏
- 需要强烈视觉冲击的品牌页

## Iteration Guide

先问这一屏唯一要回答的问题，再决定容器。能用段落说清就不要做卡；能用一个主行动就不要并排放三个。

## Known Gaps

未覆盖复杂表格和实时拓扑；这两类应该使用 `quiet-dark`、`signal-console` 或 `incident-room`。

