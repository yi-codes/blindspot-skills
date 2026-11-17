# 风格索引

> 这个文件是脚本生成的，不要手改。改风格选择条件，去改该风格 `DESIGN.md` 的 front matter。
>
> 重建：`python3 scripts/designlib.py build`

当前 **14** 个风格。

## 决定表

先定**这篇东西要让读者确认什么**，再在那一组里挑。

| 读者要确认的 | 职守 | 风格 |
|---|---|---|
| 「这东西有品 / 值得读」 | 讲故事 | `editorial-serif`、`neobrutalist`、`nocturne`、`tactile-3d` |
| 「这东西专业 / 可以信任」 | 讲专业 | `civic`、`swiss-grid` |
| 「这人懂技术 / 内容可信」 | 讲技术 | `academic`、`terminal-mono` |
| 「这是给高频工作的人做的」 | 讲工具 | `codex-workbench`、`incident-room`、`liquid-glass`、`quiet-dark`、`signal-console`、`soft-pastel` |

## 交叉表（职守 × 密度）

**密度是「这一屏要塞多少东西」，不是「留白多少」**。紧表示信息密度优先，松表示阅读节奏优先。

| 职守 | 紧 | 中 | 松 |
|---|---|---|---|
| 讲故事 | — | `neobrutalist`、`nocturne` | `editorial-serif`、`tactile-3d` |
| 讲专业 | — | `civic`、`swiss-grid` | — |
| 讲技术 | `terminal-mono` | — | `academic` |
| 讲工具 | `incident-room`、`liquid-glass`、`quiet-dark`、`signal-console` | `codex-workbench` | `soft-pastel` |

## 全表

| 风格 | 状态 | 职守 | 明暗 | 密度 | 什么时候用 | 什么时候别用 | 画布 |
|---|---|---|---|---|---|---|---|
| **Academic** `academic` | stable | 讲技术 | 双模 | 松 | 论文、技术报告、规范文档、白皮书、有定理和证明的内容、需要打印的文档 | 产品落地页、工具界面、营销页、需要快速扫读的列表 | `#F9FAFB` |
| **Civic** `civic` | stable | 讲专业 | 浅色 | 中 | 政务/公共服务、表单密集的办事流程、需要无障碍合规、给不确定人群看的说明页、政策文件 | 品牌营销、需要"高级感"的官网、创意作品集、需要视觉冲击的页面 | `#FFFFFF` |
| **Codex Workbench** `codex-workbench` | stable | 讲工具 | 双模 | 中 | Agent 任务工作台、产品方案页、设置页、插件面板、需要连续阅读和反复操作的工具页 | 营销落地页、强视觉叙事作品、数据密集型分析大屏、需要高密度多维图表的事故台 | `#F7F5F0` |
| **Editorial Serif** `editorial-serif` | stable | 讲故事 | 浅色 | 松 | 长文、博客、白皮书、品牌故事、需要慢慢读的页面、杂志式栏目 | 工具界面、高密度数据、桌面应用、需要速度感的场景 | `#F2F3F0` |
| **Incident Room** `incident-room` | stable | 讲工具 | 深色 | 紧 | 正在发生的事故、事故响应、值班交接、故障复盘、重大变更回滚、需要统一事件叙事的跨团队协作 | 日常低风险监控、营销页、长期产品文档、需要同时比较多个无关信号的普通控制台 | `#1A1714` |
| **Liquid Glass** `liquid-glass` | stable | 讲工具 | 双模 | 紧 | 高频盯屏的控制台、任务指挥台、状态面板、需要保留环境上下文的工作界面、桌面与平板工具 | 营销落地页、需要强烈视觉冲击的作品集、大量并排比较的长表格、打印 | `#F1F4F7` |
| **Neobrutalist** `neobrutalist` | stable | 讲故事 | 浅色 | 中 | 作品集、活动页、创意工具、需要"有态度"的产品官网、年轻用户、独立产品 | 金融/医疗/政务、长文阅读、需要效率感的工具界面、企业后台 | `#DCEBFE` |
| **夜色舞台** `nocturne` | stable | 讲故事 | 深色 | 中 | 桌游/剧本杀的产品页与发行页、活动与票务、沉浸式叙事产品、需要悬念的落地页、夜间模式的展示型界面 | 白天阅读的长文、后台与表单、数据密集型列表、需要平等比较多个选项的界面、打印 | `#0B0A09` |
| **Quiet Dark** `quiet-dark` | stable | 讲工具 | 深色 | 紧 | 桌面应用、编辑器面板、内部后台、Agent 对话界面、需要长时间注视的工具 | 营销落地页、长文阅读、品牌表达、打印 | `#0d0d0d` |
| **Signal Console** `signal-console` | stable | 讲工具 | 深色 | 紧 | AI SRE 助手、告警分诊、日志指标追踪、服务拓扑、值班交接、日常可观测性控制台 | 营销页、长文报告、公开状态页、低频任务列表、正在发生重大事故时的统一事故时间线 | `#111820` |
| **Soft Pastel** `soft-pastel` | stable | 讲工具 | 双模 | 松 | 消费级 app、陪伴型产品、笔记与阅读工具、社区、需要"温和不催促"的界面 | 数据看板、高密度后台、需要紧迫感的场景、对色觉障碍要求严格的场景 | `#EFF1F5` |
| **Swiss Grid** `swiss-grid` | stable | 讲专业 | 浅色 | 中 | 落地页、产品页、案例研究、数据看板、B 端界面、需要显得专业的页面 | 长文阅读、需要情绪的场景、桌面应用外壳 | `#FFFFFF` |
| **Tactile 3D** `tactile-3d` | stable | 讲故事 | 深色 | 松 | 游戏/影视产品页、硬件开箱、作品集、发布会主视觉、可拖拽的选择器、需要"手感"的展示型界面 | 长文阅读、表单、后台管理、需要快速扫读的列表、打印、任何以读字为主的地方 | `#0A0A0B` |
| **Terminal Mono** `terminal-mono` | stable | 讲技术 | 深色 | 紧 | 技术文档、开发者工具、CLI 配套界面、以日志和代码为主体的页面 | 消费级产品、品牌表达、需要温度的场景 | `#0E1116` |

## 用法速查

```html
<link rel="stylesheet" href="styles/<slug>/tokens.css">
<div class="ds-<slug>">…</div>
```

更快的入口：

```bash
python3 scripts/designlib.py recommend "<你要做什么>"
python3 scripts/designlib.py show <slug>
```

## 排他说明

`avoid` 不是「不太推荐」，是「别用」。命中排他条件的风格，通常没有为那个场景建立必要的约束。
