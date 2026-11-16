# Style Library · 个人视觉风格库

一套给 AI 用、也给自己看的视觉风格资源。

风格用 **`DESIGN.md`** 描述——这是 [Google Stitch 推出的开放格式](https://github.com/google-labs-code/design.md)（28.9k★），YAML 写 token、Markdown 写设计理由，官方还带 lint。选它的理由很简单：**这个生态已经有 84 个真实网站的样本**（[awesome-design-md](https://github.com/VoltAgent/awesome-design-md)，127.6k★），用同一套格式，才能真正把它们吸收进来。

每种风格有两个出口：

- **`tokens.css`** —— 网页 / UI，引入即可，容器加一个 class 就切换
- **`prompt.md`** —— 生图，主模板换掉主体描述就能出图

已有的三个风格不是"三种好看"，是三种**职守**：讲故事的、讲专业的、讲技术的。

## 快速看效果

直接打开 `preview/index.html`（浏览器双击即可）。同一份内容渲染三遍，一眼看出差别。

## 目录

```
style-library/
├── SKILL.md                # AI 入口：怎么选、怎么用、怎么自检
├── principles.md           # 通用设计原则（写任何风格前必读）
│
├── styles/                 # 自己的风格
│   ├── editorial-serif/    #   编辑感：长文、博客、白皮书
│   │   ├── DESIGN.md       #     唯一真相：token + 设计理由（8 章节）
│   │   ├── tokens.css      #     可直接引入的实现
│   │   └── prompt.md       #     生图模板
│   ├── swiss-grid/         #   瑞士网格：产品页、案例、数据看板
│   └── terminal-mono/      #   终端感：技术文档、开发者工具
│
├── references/             # 外部样本（别人的，不是我的）
│   ├── README.md           #   怎么拆解一份外部设计
│   ├── claude/             #   原始 DESIGN.md + 提炼卡 NOTES.md
│   └── ollama/
│
├── inbox/                  # 原料入口：截图、链接、随手记
│
├── prompts/
│   ├── style-words.md      # 风格词表：光线 / 材质 / 构图 / 色彩 / 流派
│   └── negative.md         # 负向词通用清单
│
├── preview/index.html      # 三风格对照预览（脚本生成，勿手改）
└── scripts/
    ├── lint.py             # 校验：引用有效性 / 对比度 / CSS 一致性
    ├── build-preview.py    # 重建预览页
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

变量前缀跟着风格走：`--ed-*` / `--sw-*` / `--tm-*`。
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

判据一句话：**让你觉得好看的不是那个看得见的东西，是它周围那套约束。**

## 加一个风格

```bash
./scripts/new-style.sh brutalist "粗野主义"
# 填 styles/brutalist/ 下的 DESIGN.md、tokens.css、prompt.md
./scripts/lint.py
./scripts/build-preview.py
```

但先看 `principles.md` 第 8 节：**要不要加，判断标准是"新场景是否必须违反现有风格的硬约束"**，不是"想换个感觉"。
风格库的价值在少而准。三个各司其职的风格，比二十个互相打架的强。

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
- **改了 `DESIGN.md` 的色值，必须同步改 `tokens.css`**，否则 lint 报错——这是防漂移的唯一手段
- 新增色值先进 token，再进组件。**组件里不许出现裸色值**
- 改完就跑 `./scripts/lint.py`，它比眼睛可靠
