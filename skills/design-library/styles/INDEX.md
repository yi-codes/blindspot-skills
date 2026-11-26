# 风格索引

> 这个文件是脚本生成的，不要手改。改风格选择条件，去改该风格 `DESIGN.md` 的 front matter。
>
> 重建：`python3 scripts/designlib.py build`

当前 **31** 个风格。

## 决定表

先定**这篇东西要让读者确认什么**，再在核心风格里挑。变体和技法仍完整保留，见后文。

| 读者要确认的 | 职守 | 风格 |
|---|---|---|
| 「这东西有品 / 值得读」 | 讲故事 | `editorial-serif`、`neobrutalist` |
| 「这东西专业 / 可以信任」 | 讲专业 | `civic`、`enterprise-data`、`swiss-grid` |
| 「这人懂技术 / 内容可信」 | 讲技术 | `academic`、`developer-docs` |
| 「这是给高频工作的人做的」 | 讲工具 | `adaptive-companion`、`codex-workbench`、`incident-room`、`signal-console` |

## 交叉表（职守 × 密度）

**密度是「这一屏要塞多少东西」，不是「留白多少」**。紧表示信息密度优先，松表示阅读节奏优先。

| 职守 | 紧 | 中 | 松 |
|---|---|---|---|
| 讲故事 | — | `neobrutalist` | `editorial-serif` |
| 讲专业 | `enterprise-data` | `civic`、`swiss-grid` | — |
| 讲技术 | — | `developer-docs` | `academic` |
| 讲工具 | `incident-room`、`signal-console` | `codex-workbench` | `adaptive-companion` |

## 变体与技法

这些不是低质量项，而是需要附着在核心风格或具体组件上的明暗、材料与动效变体。

| 风格 | 层级 | 家族 | 来源 | 一句话 |
|---|---|---|---|---|
| **Art Nouveau｜新艺术曲线** `art-nouveau` | 变体 | expressive | art-nouveau | 把 1890–1910 年新艺术运动的海报语法搬进网页：奶油纸底上的鞭状曲线、拱形画框、 1px 烫金描边与高对比衬线标题，深绿负责正文和主行动，酒红只留在印章级强调。 |
| **Bauhaus Grid｜包豪斯几何** `bauhaus` | 变体 | expressive | bauhaus | 用三原色、圆方三角与不对称网格做构图的海报式页面。 |
| **Bento Grid｜便当格** `bento-grid` | 变体 | expressive | bento-grid | 用大小不等、圆角一致的卡片紧密拼成一屏，每格只装一个信息点，卡片跨度代表信息优先级。 |
| **Blueprint｜工程蓝图** `blueprint` | 变体 | developer | blueprint | 把氰版晒图的工程图纸语法搬进网页：蓝晒蓝 #0B3D91 底上铺 20px 白线网格， 1px 图纸白线框把区块连成一张图，尺寸虚线、十字准星和 FIG. 编号说明每块是什么， 标注黄 #FFD36A 只给关键数字与主行动。 |
| **Constructivism｜构成主义海报** `constructivism` | 变体 | expressive | constructivism | 把 1910–30 年代构成主义海报的视觉语法做成展示型网页： 泛黄纸底 #F2E8D5、革命红 #CC0000 与暖墨 #1A1A1A 三色硬边， -2° 倾斜的号令式大标题、-12° 斜切红楔与 4px 墨线， 按钮用「色块侵入」横扫与红黑反转制造机械感。 |
| **Deco Ceremony｜装饰艺术典礼** `deco-ceremony` | 变体 | ceremonial | — | 给精品酒店、晚宴、珠宝与颁奖典礼用的 Art Deco 页面。 |
| **Frutiger Aero｜晴空拟物** `frutiger-aero` | 变体 | retro | frutiger-aero | 把 2004–2013 年"科技与自然和谐相处"的乐观想象做成一套可直接用的界面语言： 天蓝到草绿的通透渐变、带高光条的玻璃按钮、气泡与水滴、人文无衬线字。 |
| **Gallery Wall｜展陈画廊** `gallery-wall` | 变体 | gallery | — | 让作品而不是界面成为主角的展陈系统。 |
| **Liquid Glass** `liquid-glass` | 变体 | operations | ui-styles-liquid-glass | 克制的半透明工作台。 |
| **Memphis｜孟菲斯海报** `memphis` | 变体 | expressive | memphis | 把 1981 年米兰 Memphis Group 的后现代装饰语言做成一套可直接用的展示型界面： 奶白底、玫红/柠檬黄/薄荷/靛蓝四色撞色、3px 墨黑描边、6px 无模糊硬投影， 波点与 45° 斜纹只待在角落，圆/方/三角/波浪线故意错落。 |
| **Newsprint Grid｜新闻纸网格** `newsprint-grid` | 变体 | editorial | — | 给真正拥有多条新闻的编辑首页：12 列、细线分栏、衬线标题与无衬线元信息， 首屏直接进入故事网格而非营销 Hero。 |
| **夜色舞台** `nocturne` | 变体 | expressive | native | 一盏灯，一圈黑。 |
| **Pixel Arcade｜像素街机** `pixel-arcade` | 变体 | retro | — | 面向复古游戏与轻量互动 demo 的 8-bit 界面。 |
| **Quiet Dark** `quiet-dark` | 变体 | workbench | openai-desktop-client-observed、chatgpt-ios | 原生桌面应用的深色界面，附一套同源的浅色。 |
| **Riso Zine｜孔版独立志** `riso-zine` | 变体 | zine | — | 用两种专色、1–3px 套印错位和可见纸纹做独立出版物。 |
| **Sketch Notes｜手绘笔记** `sketch-notes` | 变体 | illustration | — | 面向解释、教学和工作坊的纸上草图风格。 |
| **Soft Pastel** `soft-pastel` | 变体 | companion | catppuccin | 低对比柔色界面。 |
| **Tactile 3D** `tactile-3d` | 技法 | expressive | atropos、react-bits | 会动的卡片。 |
| **Terminal Mono** `terminal-mono` | 变体 | developer | native | 把命令行搬进正文。 |
| **Vaporwave｜蒸汽波** `vaporwave` | 变体 | retro | vaporwave | 把 1980–90 年代消费电子与早期互联网的记忆做成一场慢速霓虹梦：深紫黑底上粉与青两束霓虹、 退向地平线的透视网格、条纹落日与轻微色差 glitch。 |

## 全表

| 风格 | 状态 | 家族 | 层级 | 来源 | 职守 | 明暗 | 密度 | 什么时候用 | 什么时候别用 | 画布 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Academic** `academic` | stable | reading | 核心 | latex-css | 讲技术 | 双模 | 松 | 论文、技术报告、规范文档、白皮书、有定理和证明的内容、需要打印的文档 | 产品落地页、工具界面、营销页、需要快速扫读的列表 | `#F9FAFB` |
| **Adaptive Companion** `adaptive-companion` | stable | companion | 核心 | material-3、fluent-2 | 讲工具 | 双模 | 松 | 移动端 app、跨设备助理、陪伴型工具、个人日程、触控操作、渐进式引导、响应式产品 | 高密度管理后台、宽表格、事故指挥台、营销落地页、以打印为主的文档 | `#F1F3F4` |
| **Art Nouveau｜新艺术曲线** `art-nouveau` | beta | expressive | 变体 | art-nouveau | 讲故事 | 浅色 | 中 | 美术馆与画廊展览页、精品酒店与珠宝腕表品牌页、剧院演出与婚礼请柬、插画师作品集与主视觉、需要手工装饰感的品牌发布页 | 开发者工具与技术文档、数据看板与密集表格、高频交易与监控台、移动优先的工具型 App、快速新闻流、无障碍优先的长表单默认皮、打印为主的单栏正文 | `#F5EFE0` |
| **Bauhaus Grid｜包豪斯几何** `bauhaus` | beta | expressive | 变体 | bauhaus | 讲故事 | 浅色 | 松 | 设计工作室与建筑事务所作品集、文化机构与美术馆页面、字体展示与设计教育、品牌发布与主视觉页、需要强烈设计主张的落地页 | 大目录电商、内容密集型新闻与博客、高密度后台与表单、需要温暖亲和的消费产品、金融医疗与政务、多人协作的复杂工具界面 | `#F4F0E6` |
| **Bento Grid｜便当格** `bento-grid` | beta | expressive | 变体 | bento-grid | 讲故事 | 浅色 | 中 | 产品功能总览与发布会规格墙、SaaS 营销落地页与作品集首屏、App 仪表盘首页与设置总览、需要一屏并列展示多个同级能力 | 长表单与密集数据表格、必须从上到下线性阅读的流程、少于五格的内容、长篇散文与论文、需要严肃权威气质的金融医疗政务、打印为主的单栏文档 | `#F4F4F5` |
| **Blueprint｜工程蓝图** `blueprint` | beta | developer | 变体 | blueprint | 讲技术 | 深色 | 中 | 建筑与硬件项目页、开发者大会与黑客松活动页、众筹产品结构展示专题、技术方案与规格说明页、需要展示「未建成图纸」感的作品集 | 温馨消费品牌主站、长篇散文与小说阅读、需要柔和亲和插画的消费 App、无障碍要求下的长表单默认皮、金融医疗政务等需要权威稳重的页面、打印为主的单栏文档 | `#0B3D91` |
| **Civic** `civic` | stable | trusted-service | 核心 | govuk、uswds | 讲专业 | 浅色 | 中 | 政务/公共服务、表单密集的办事流程、需要无障碍合规、给不确定人群看的说明页、政策文件 | 品牌营销、需要"高级感"的官网、创意作品集、需要视觉冲击的页面 | `#FFFFFF` |
| **Codex Workbench** `codex-workbench` | stable | workbench | 核心 | openai-codex-observed | 讲工具 | 双模 | 中 | Agent 任务工作台、产品方案页、设置页、插件面板、需要连续阅读和反复操作的工具页 | 营销落地页、强视觉叙事作品、数据密集型分析大屏、需要高密度多维图表的事故台 | `#F7F5F0` |
| **Constructivism｜构成主义海报** `constructivism` | beta | expressive | 变体 | constructivism | 讲故事 | 浅色 | 中 | 文化活动与展览活动页、产品/影片/演出发布页、主张鲜明的宣言式落地页、体育与音乐赛事宣传页、需要一屏建立强烈态度的作品集首屏 | 长文阅读与论文、产品文档与帮助中心、高密度后台与数据表格、表单密集的办事流程、金融医疗法律等需要克制可信的场景、政务与官方公告、需要平等比较多个选项的页面 | `#F2E8D5` |
| **Deco Ceremony｜装饰艺术典礼** `deco-ceremony` | beta | ceremonial | 变体 | — | 讲故事 | 深色 | 松 | 精品酒店、高级餐厅、珠宝与腕表、晚宴与典礼、电影节、会员制俱乐部、历史建筑与品牌纪念页 | 日常工具、数据后台、儿童产品、折扣电商、开发文档、密集表单、轻松亲民的消费 App | `#1A1A1A` |
| **Developer Docs** `developer-docs` | stable | developer | 核心 | primer、geist、radix | 讲技术 | 双模 | 中 | 产品文档、API 参考、SDK 指南、开发者入门、版本迁移、代码示例密集的页面 | 终端模拟器、营销落地页、事故指挥台、纯打印论文、需要强情绪表达的页面 | `#F4F6F4` |
| **Editorial Serif** `editorial-serif` | stable | reading | 核心 | native | 讲故事 | 浅色 | 松 | 长文、博客、白皮书、品牌故事、需要慢慢读的页面、杂志式栏目 | 工具界面、高密度数据、桌面应用、需要速度感的场景 | `#F2F3F0` |
| **Enterprise Data** `enterprise-data` | stable | enterprise-data | 核心 | carbon、radix | 讲专业 | 双模 | 紧 | 企业管理后台、数据表格、批量操作、权限与审计、订单账单、客户运营、B 端管理工作流 | 品牌营销页、长文阅读、移动优先消费产品、事故时间线、沉浸式展示 | `#EEF1F2` |
| **Frutiger Aero｜晴空拟物** `frutiger-aero` | beta | retro | 变体 | frutiger-aero | 讲故事 | 浅色 | 中 | 怀旧科技与 Y2K 品牌活动页、消费电子与饮品官网、音乐与媒体播放器、健康与天气类工具 App、游戏启动器、需要乐观亲和气的展示型界面 | 数据密集型后台与大表格、扁平/极简/单色品牌、需要严肃权威的金融医疗政务、长文与论文阅读、表单密集的办事流程、以打印为主的文档 | `#EAF6FF` |
| **Gallery Wall｜展陈画廊** `gallery-wall` | beta | gallery | 变体 | — | 讲故事 | 浅色 | 松 | 艺术展览、博物馆与画廊、摄影作品集、艺术家档案、拍卖目录、文化机构官网、图片主导的作品展示 | 高密度后台、长文正文、复杂表单、促销电商、数据看板、以操作为主的工具界面 | `#F3F3F0` |
| **Incident Room** `incident-room` | stable | operations | 核心 | ui-styles-ops-console | 讲工具 | 深色 | 紧 | 正在发生的事故、事故响应、值班交接、故障复盘、重大变更回滚、需要统一事件叙事的跨团队协作 | 日常低风险监控、营销页、长期产品文档、需要同时比较多个无关信号的普通控制台 | `#1A1714` |
| **Liquid Glass** `liquid-glass` | stable | operations | 变体 | ui-styles-liquid-glass | 讲工具 | 双模 | 紧 | 高频盯屏的控制台、任务指挥台、状态面板、需要保留环境上下文的工作界面、桌面与平板工具 | 营销落地页、需要强烈视觉冲击的作品集、大量并排比较的长表格、打印 | `#F1F4F7` |
| **Memphis｜孟菲斯海报** `memphis` | beta | expressive | 变体 | memphis | 讲故事 | 浅色 | 中 | 儿童教育与玩具文具品牌站、展览与创意市集活动页、音乐与时尚编辑页面、社交媒体封面与包装插画、需要强烈 80 年代后现代态度的展示型落地页 | 金融法律医疗等严肃场景、长文阅读与产品文档、需要极简克制品牌气质的产品、高密度后台与长表单、需要精确扫读的数据页、政务与公共服务 | `#FFF8EC` |
| **Neobrutalist** `neobrutalist` | stable | expressive | 核心 | neobrutalism | 讲故事 | 浅色 | 中 | 作品集、活动页、创意工具、需要"有态度"的产品官网、年轻用户、独立产品 | 金融/医疗/政务、长文阅读、需要效率感的工具界面、企业后台 | `#DCEBFE` |
| **Newsprint Grid｜新闻纸网格** `newsprint-grid` | beta | editorial | 变体 | — | 讲故事 | 浅色 | 紧 | 新闻首页、科技杂志、每日简报、专题聚合、多栏目编辑页、需要快速扫读标题的内容流 | 单一产品营销页、作品集、工具后台、复杂表单、内容不足三条的页面、沉浸式品牌叙事 | `#F7F6F2` |
| **夜色舞台** `nocturne` | stable | expressive | 变体 | native | 讲故事 | 深色 | 中 | 桌游/剧本杀的产品页与发行页、活动与票务、沉浸式叙事产品、需要悬念的落地页、夜间模式的展示型界面 | 白天阅读的长文、后台与表单、数据密集型列表、需要平等比较多个选项的界面、打印 | `#0B0A09` |
| **Pixel Arcade｜像素街机** `pixel-arcade` | beta | retro | 变体 | — | 讲故事 | 浅色 | 中 | 复古游戏、浏览器小游戏、Game Jam、像素作品集、成就与徽章、轻量游戏化 demo、街机活动页 | 长文阅读、企业后台、金融医疗政务、复杂表单、高密度数据、正式品牌官网、关键生产工具 | `#F8F8F0` |
| **Quiet Dark** `quiet-dark` | stable | workbench | 变体 | openai-desktop-client-observed、chatgpt-ios | 讲工具 | 深色 | 紧 | 桌面应用、编辑器面板、内部后台、Agent 对话界面、需要长时间注视的工具 | 营销落地页、长文阅读、品牌表达、打印 | `#0d0d0d` |
| **Riso Zine｜孔版独立志** `riso-zine` | beta | zine | 变体 | — | 讲故事 | 浅色 | 中 | 独立杂志、音乐节与演出海报、独立出版、诗歌与小册子、艺术活动页、乐队与唱片、创意工作坊 | 企业年报、金融医疗政务、密集表单、数据看板、长文阅读、需要严肃可信的公共服务 | `#FDFBF6` |
| **Signal Console** `signal-console` | stable | operations | 核心 | ui-styles-ops-console | 讲工具 | 深色 | 紧 | AI SRE 助手、告警分诊、日志指标追踪、服务拓扑、值班交接、日常可观测性控制台 | 营销页、长文报告、公开状态页、低频任务列表、正在发生重大事故时的统一事故时间线 | `#111820` |
| **Sketch Notes｜手绘笔记** `sketch-notes` | beta | illustration | 变体 | — | 讲技术 | 浅色 | 中 | 教学解释、工作坊、知识卡片、概念图解、儿童教育、轻量 onboarding、创意原型、个人学习笔记 | 法律与合同、金融医疗、正式企业后台、精密数据表、长文出版、需要严肃权威的安全流程 | `#F7F3E8` |
| **Soft Pastel** `soft-pastel` | stable | companion | 变体 | catppuccin | 讲工具 | 双模 | 松 | 消费级 app、陪伴型产品、笔记与阅读工具、社区、需要"温和不催促"的界面 | 数据看板、高密度后台、需要紧迫感的场景、对色觉障碍要求严格的场景 | `#EFF1F5` |
| **Swiss Grid** `swiss-grid` | stable | professional | 核心 | native | 讲专业 | 浅色 | 中 | 落地页、产品页、案例研究、数据看板、B 端界面、需要显得专业的页面 | 长文阅读、需要情绪的场景、桌面应用外壳 | `#FFFFFF` |
| **Tactile 3D** `tactile-3d` | stable | expressive | 技法 | atropos、react-bits | 讲故事 | 深色 | 松 | 游戏/影视产品页、硬件开箱、作品集、发布会主视觉、可拖拽的选择器、需要"手感"的展示型界面 | 长文阅读、表单、后台管理、需要快速扫读的列表、打印、任何以读字为主的地方 | `#0A0A0B` |
| **Terminal Mono** `terminal-mono` | stable | developer | 变体 | native | 讲技术 | 深色 | 紧 | 技术文档、开发者工具、CLI 配套界面、以日志和代码为主体的页面 | 消费级产品、品牌表达、需要温度的场景 | `#0E1116` |
| **Vaporwave｜蒸汽波** `vaporwave` | beta | retro | 变体 | vaporwave | 讲故事 | 深色 | 中 | 音乐人与专辑/演出落地页、synthwave 与 retrowave 活动页、创意作品集首屏、复古游戏与 Game Jam 页面、潮流服饰与周边、需要强情绪与怀旧感的展示型界面 | 企业官网与后台、表单密集的办事流程、金融医疗政务、长文阅读与论文、需要严肃权威与高信息效率的界面、打印为主的单栏文档 | `#1A0B2E` |

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
