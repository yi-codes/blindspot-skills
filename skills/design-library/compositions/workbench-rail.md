---
name: 工作台侧栏型
slug: workbench-rail
version: 1
status: beta
density: medium
register: tool
frame: [frame-app, frame-side, frame-workspace, frame-toolbar, frame-task, frame-grid]
sample: ../preview/codex-workbench.html
---

# 工作台侧栏型 · workbench-rail

## 适用任务

用户带着任务来、要盯着状态并动手：Agent 控制台、运维值班台、IDE 类工作台、
内容管理后台。导航长期可见，主区是"当前任务 + 待办/结果"，不是宣传页。

## 主角与视线

唯一主角是 **`frame-toolbar` 里的当前任务标题**，它必须就是用户此行最该处理的事。
视线路径：`侧栏当前项 → toolbar H1 → 主操作 → frame-task 列表`。
侧栏是"我在哪"，不是主角；把它做重会抢走主区注意力。

## 网格与密度

- 密度 `medium`：`frame-app` 为 `minmax(10rem,14rem) : minmax(0,1fr)`，侧栏窄且固定。
- 主区 `frame-workspace` 必须 `min-width: 0`，否则长表格/代码块会撑破 grid。
- `frame-toolbar` 用 `1fr : auto` 把标题与操作分开；`frame-task` 同样 `1fr : auto`，
  右侧挂状态与动作，密度压在行内而不是堆卡片。
- 48rem 以下侧栏塌成顶部横向 nav（3 列），`frame-task` 塌成单栏。

## 挂载点

| 结构类 | 挂什么 | 状态要求 |
|---|---|---|
| `frame-side` | 导航 + 底部状态说明 | `aria-current`、键盘可达 |
| `frame-toolbar` | H1 + 主操作按钮 | 加载态/禁用态可见 |
| `frame-grid` | 概览卡片（2–3 块） | 空态、错误态 |
| `frame-task` | 待办行/结果行 | 运行中、失败、已确认三态 |
| `frame-muted` | 次要说明 | 对比度仍需达 AA |

工具界面靠描边分段（`--frame-sep: 1px solid currentColor`），与叙事骨架的留白相反。

## 与风格的咬合

适合 `register: tool` 或 `family` 为 industrial / technical / companion 的风格。
低对比、强浮雕的风格（如 neumorphism）套这个骨架时，密集 `frame-task` 行会糊成一片，
`avoid` 里已写明"信息密集后台"，遵守它。暗色风格注意侧栏与主区靠明度差而非投影分层。

## 禁用项

- 只有一个阅读目标、没有并行任务：侧栏会变成纯装饰，换叙事引导型。
- 需要横向扫读的宽表：14rem 侧栏 + 窄主区会逼出横向滚动，换数据外壳型。
- 移动端为主且无桌面版：这个骨架的降级只是"能看"，不是好用，换伴侣型。
