# Style Library · 个人视觉风格库

一套给 AI 用、也给自己看的视觉风格资源。

风格用 **`DESIGN.md`** 描述——这是 [Google Stitch 推出的开放格式](https://github.com/google-labs-code/design.md)（28.9k★），YAML 写 token、Markdown 写设计理由，官方还带 lint。选它的理由很简单：**这个生态已经有 84 个真实网站的样本**（[awesome-design-md](https://github.com/VoltAgent/awesome-design-md)，127.6k★），用同一套格式，才能真正把它们吸收进来。

每种风格有两个出口：

- **`tokens.css`** —— 网页 / UI，引入即可，容器加一个 class 就切换
- **`prompt.md`** —— 生图，主模板换掉主体描述就能出图

**现在有哪些风格、各自负责什么，看 [`styles/INDEX.md`](styles/INDEX.md)。**
那份索引是脚本从每个风格的 front matter 长出来的——加风格不用改这个 README。

每个风格不是"一种好看"，是一种**职守**：这段东西要让读者确认什么。
`quiet-dark` 的色值是**从 OpenAI 桌面客户端的 `app.asar` 里反推**的（解开 Electron 包、grep 出 CSS 自定义属性），
不是手调的；这条路的产出和手调的不是一个可信度，那个 `DESIGN.md` 里单独标了来源。

## 快速看效果

直接打开 `preview/index.html`（浏览器双击即可）。同一份内容渲染三遍，一眼看出差别。

## 目录

```
style-library/
├── SKILL.md                # AI 入口：怎么选、怎么用、怎么自检
├── principles.md           # 通用设计原则（写任何风格前必读）
│
├── styles/                 # 自己的风格
│   ├── INDEX.md            #   【自动生成】决定表 + 全表 —— 选风格读这个
│   ├── index.json          #   【自动生成】给脚本读
│   └── <slug>/             #   一个风格一个目录
│       ├── DESIGN.md       #     唯一真相：token + 选择字段 + 8 章节理由
│       ├── tokens.css      #     可直接引入的实现
│       └── prompt.md       #     生图模板
│
├── references/             # 外部样本（别人的，不是我的）
│   ├── README.md           #   怎么拆解一份外部设计
│   ├── claude/             #   原始 DESIGN.md + 提炼卡 NOTES.md
│   ├── ollama/
│   ├── bergside-codex/     #   自称 Codex 风格的那份 —— 反面样本
│   ├── chatgpt-ios/        #   ChatGPT iOS 拆解，验证了 quiet-dark 的色值
│   └── hallmark/           #   反 slop 闸门表：AI 味儿怎么枚举（→ principles.md §11）
│
├── inbox/                  # 原料入口：截图、链接、随手记
│
├── prompts/
│   ├── style-words.md      # 风格词表：光线 / 材质 / 构图 / 色彩 / 流派
│   └── negative.md         # 负向词通用清单
│
├── showcase/
│   ├── web.html            # 三风格 × 网页整页样张
│   ├── app.html            # 三风格 × 手机端样张
│   └── codex.html          # quiet-dark × 桌面 app 三屏（线程 / diff / 空状态）
│
├── preview/index.html      # 【自动生成】全风格对照预览（覆盖全部风格）
└── scripts/
    ├── _designmd.py        # 共用解析器 —— 写新脚本前先看它，别各写一份
    ├── lint.py             # 查文档：token 引用 / 对比度 / 章节 / 数值阶对齐
    ├── slop.py             # 查产物：AI 味儿（principles §11 的静态版）
    ├── build-index.py      # 生成 styles/INDEX.md + index.json
    ├── build-preview.py    # 重建对照预览
    ├── new-style.sh        # 新建风格脚手架
    └── fetch-ref.sh        # 抓外部 DESIGN.md 样本
```

## 在网页里用

```html
<link rel="stylesheet" href="style-library/styles/swiss-grid/tokens.css">

<div class="ds-swiss-grid">
  <h1>标题</h1>
  <p>正文……</p>
</div>
```

变量前缀跟着风格走（`--ed-*` / `--sw-*` / `--qd-*` …），见该文件顶部注释。
写新组件时用 `var(--sw-space-4)` 这种引用，不要硬编码 —— 这是风格能一致复用的前提。

## 收集（这个库怎么长大）

三层，顺序不能乱：

| 层 | 放什么 | 规则 |
|---|---|---|
| `inbox/` | 截图、链接、随手一句 | **扔的时候不筛选**。它是漏斗，不是待办清单 |
| `references/` | 外部 DESIGN.md + 提炼卡 | 原文只读不改，提炼写进 `NOTES.md` |
| `styles/` | 自己的风格 | 只有能变成数值的东西才允许进 |

抓一份外部样本：

```bash
./scripts/fetch-ref.sh VoltAgent/awesome-design-md design-md/linear/DESIGN.md linear
```

然后按 `references/README.md` 的三步拆：**能写成 `{token}` 的吸收，只能形容成"高级感"的留在 references。**

**选来源比拆解更重要。** 2026-11 的一次调研结论：GitHub 上唯一自称 "Codex 风格" 的 DESIGN.md
（`bergside/awesome-design-skills`）是批量生成的，`primary: #000000` + `surface: #FFFFFF` + Open Sans，
跟真产品没有一毛钱关系。判据不是星数，是**"遮住产品名还站得住吗"**。
反面样本留在 `references/bergside-codex/`，不是为了学，是为了有据可查。

判据一句话：**让你觉得好看的不是那个看得见的东西，是它周围那套约束。**

## 加一个风格

```bash
./scripts/new-style.sh brutalist "粗野主义"
# 填 styles/brutalist/ 下的 DESIGN.md、tokens.css、prompt.md
# DESIGN.md 的 front matter 里 cues / avoid / surface / register 四项必须填
./scripts/lint.py                # 缺选择字段会直接报 E
./scripts/build-index.py         # 自动进索引
./scripts/build-preview.py       # 自动进对照页
```

**加一个风格 = 动一个目录。** SKILL.md / README / 索引 / 预览，一个字都不用改。

但先看 `principles.md` 第 8 节：**要不要加，判断标准是"新场景是否必须违反现有风格的硬约束"**，不是"想换个感觉"。
风格库的价值在少而准。四个各司其职的风格，比二十个互相打架的强。

## 让本地 Agent 用上

仓库放 GitHub，Agent 读的是本机路径。做法是软链，不是复制（复制会产生两份真相）：

```bash
ln -sfn <本仓库路径>/style-library ~/.workbuddy/skills/style-library
```

改完仓库内容，Agent 下次会话自动读到最新版。
如果用的是别的 Agent（比如 Claude Code），软链到它对应的 skills 目录即可，这个库不绑定任何一个。

## 维护约定

- 风格目录名用小写短横线（`editorial-serif`），中文名写 `DESIGN.md` 的 `name` 字段
- 每个风格必须三个文件齐全，缺 `prompt.md` 的只能用于网页、不能用于配图，lint 会警告
- **改了 `DESIGN.md` 的色值/字号/圆角/间距，必须同步改 `tokens.css`**，否则 lint 报错——这是防漂移的唯一手段
- 新值先进 token，再进组件。**组件里不许出现裸值**
- 改完跑两个脚本，它们查的东西不重叠，少跑一个等于没查：

| 脚本 | 查什么 | 目标 |
|---|---|---|
| `lint.py` | **文档层**：token 引用、WCAG 对比度、8 章节、颜色/字号/圆角/间距与 CSS 全量对齐、选择字段是否齐全 | 0 错 0 警 |
| `slop.py` | **产物层**：AI 味儿（渐变、eyebrow、大写字距、中点串、纯黑白、氛围光） | 0 错 |

E 是硬线；W 看流派（编辑/瑞士/终端的全大写小标签是原生语法）。要破例就在那一行写 `/* slop-ok S3: 理由 */`，理由少于 12 字不算。
