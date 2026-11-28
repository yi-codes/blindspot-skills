# 构图骨架索引

> 骨架决定信息怎么站队，风格决定它长什么样。**先选骨架，再选风格。**
> 每个骨架都锚定 `preview/_frame.css` 里真实存在的结构类，并有活样例页。
> 规范与入库门槛见 [`README.md`](README.md)。

| 骨架 | 中文名 | 主角 | 密度 | 典型任务 | 活样例 |
|---|---|---|---|---|---|
| [`editorial-lede`](editorial-lede.md) | 叙事引导型 | H1 主张 | sparse | 作品集 / 发布页 / 长文封面 | [`bauhaus`](../preview/bauhaus.html) |
| [`split-manifesto`](split-manifesto.md) | 分屏对照型 | 左栏断言 | sparse | 机构介绍 / 年报摘要 / 关于我们 | [`civic`](../preview/civic.html) |
| [`workbench-rail`](workbench-rail.md) | 工作台侧栏型 | 当前任务标题 | medium | Agent 控制台 / 运维台 / 后台 | [`codex-workbench`](../preview/codex-workbench.html) |
| [`docs-three-column`](docs-three-column.md) | 文档三栏型 | 正文 | medium | API 文档 / 规范手册 / 知识库 | [`developer-docs`](../preview/developer-docs.html) |
| [`mobile-companion`](mobile-companion.md) | 移动伴侣型 | 当前状态 | medium | 硬件伴侣 / 健康记录 / 播放器 | [`adaptive-companion`](../preview/adaptive-companion.html) |
| [`data-shell`](data-shell.md) | 数据外壳型 | 数据表 | dense | 报表 / 告警列表 / 管理后台 | [`enterprise-data`](../preview/enterprise-data.html) |

## 怎么选

按用户要完成什么，不要按审美偏好：

| 用户要… | 用 |
|---|---|
| 判断"值不值得继续看" | `editorial-lede` |
| 看一句立场配一组事实 | `split-manifesto` |
| 盯着状态并动手操作 | `workbench-rail` |
| 在长文里定位某一段 | `docs-three-column` |
| 抬手一眼看状态、单手操作 | `mobile-companion` |
| 扫读筛选大量行 | `data-shell` |

选定后读该骨架文件的「禁用项」，确认任务不在里面；再去 `styles/` 选风格。

## 结构类与职守分化

`preview/_frame.css` 按骨架职守给分隔手段定了性，选骨架时一并继承：

- 叙事（`frame-story`）：`--frame-sep: none`，靠留白
- 专业 / 数据（`frame-professional`、`frame-task`）：实线描边
- 技术 / 文档（`frame-technical`）：虚线描边
- 筛选条（`frame-filterbar`）：上下双实线

**一个主分隔手段只选一个**，其余退到辅助位——见 `LAYERS.md` 第 4 层合格线。

## 当前覆盖与缺口

已覆盖 6 类页面职责：叙事、对照、工具、文档、移动、数据。

尚未沉淀（下一轮优先）：
- 画廊/网格墙型（作品矩阵、图片优先）
- 时间轴/流程推进型（状态流转、订单进度）
- 对话/消息流型（IM、评论、Agent 对话）
- 空态与首次使用引导型（onboarding）
