---
name: style-library
description: 个人视觉风格库。需要为网页/落地页/工具界面定视觉语言、统一配色与排版，或为文章配图、封面确定画面风格时使用。风格以 DESIGN.md 标准格式描述（Google Stitch 规范），每个风格同时提供可引用的 CSS tokens 和生图 prompt 模板，并带收集外部设计样本的流程。
---

# 风格库

一套**可执行**的视觉风格资源。每种风格用 `DESIGN.md` 描述（YAML tokens + 设计理由），同时有两个出口：

- **`tokens.css`** —— 网页 / UI 的直接实现
- **`prompt.md`** —— 生图的模板

## 什么时候用

- 做网页、落地页、小工具界面 → 先在这里定风格，再写 CSS
- 给文章配图、做封面、写生图 prompt → 先选风格，拿模板
- 用户说"帮我设计得好看点""统一一下视觉""这个配色不对" → 先读 `principles.md`
- 用户给你看他喜欢的网站/截图 → 走下面的"收集"流程

**不适用**：纯数据可视化（用图表库默认主题 + 一个品牌色即可）、已有明确设计稿或品牌规范的项目。

## 怎么选风格

| 产出物 | 首选 | 备选 |
|---|---|---|
| 长文、博客、白皮书、品牌故事 | `editorial-serif` | — |
| 落地页、产品页、案例、数据看板、B 端界面 | `swiss-grid` | — |
| 技术文档、开发者工具、CLI 配套界面 | `terminal-mono` | `swiss-grid` |
| 文章配图、封面（偏情绪/质感） | `editorial-serif` | — |
| 产品图、静物、商务物料 | `swiss-grid` | — |
| 技术主题配图、暗调氛围图 | `terminal-mono` | — |

选不出来就问一句：**这个页面的第一读者是谁，他最想确认什么？**
想确认"这人靠谱"→ editorial；"东西好用"→ swiss；"技术过硬"→ terminal。

**不要新建风格**，先看现有的是否够用。

## 怎么用

### 做网页

```html
<link rel="stylesheet" href="styles/swiss-grid/tokens.css">
<div class="ds-swiss-grid"> … </div>
```

变量前缀跟着风格走：`--ed-*` / `--sw-*` / `--tm-*`。
写新组件时用 `var(--sw-space-4)` 这种引用，**不要硬编码颜色和字号**——这是风格能一致复用的前提。

### 做图

读 `styles/<风格>/prompt.md` 的主模板，只替换主体描述。
调风格词查 `prompts/style-words.md`；负向词查 `prompts/negative.md`。

**四段式**：材质 → 光线 → 构图 → 色彩后期，每段最多两个词，总数不超过 8 个。

### 两种都要

先做网页，截图，再用同一风格做生图，并排看是否像一家公司。不像就是风格没落到位。

## 收集（有人给你看他喜欢的设计时）

三层结构，**不要让原料直接进 styles**：

```
inbox/        原料：截图、链接、随手记。扔的时候不筛选
references/   外部样本：原始 DESIGN.md + 你的提炼卡 NOTES.md
styles/       自己的：提炼后才允许进
```

### 三步

1. **抓原文**：`./scripts/fetch-ref.sh <owner/repo> <path> <短名>`
   主力来源 [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)（127k★，84 个真实网站）
2. **拆**：逐条过筛子——能写成 `{token}` 或可检查规则的吸收，只能形容成"高级感"的留在 references
3. **落**：补进现有风格 / 写进 `principles.md` / 或（极少数）新开风格

详细方法见 `references/README.md`。每份样本必配 `NOTES.md`，**"弃"那一栏比"取"重要**。

## 加一个新风格

```bash
./scripts/new-style.sh <slug> "<中文名>"      # 生成 DESIGN.md / tokens.css / prompt.md 模板
# 填内容
./scripts/lint.py                             # 校验
./scripts/build-preview.py                    # 重建预览页
```

**先读 `principles.md` 第 8 节。** 判断标准是"新场景是否必须违反现有风格的硬约束"，不是"想换个感觉"。

## 自检

交付前跑一遍：

```bash
./scripts/lint.py
```

它检查：token 引用是否有效、颜色是否与 CSS 一致（防漂移）、WCAG 对比度、必备章节是否齐全、有没有 `## Chinese Typography`。

再人工过这 6 条：

- [ ] 颜色只用了 tokens 里定义的，没有临时色值
- [ ] 字号只用了 token 阶里的档位，没有 17/18/19 这种中间值
- [ ] 圆角和阴影跟风格的硬约束一致（editorial 0/0、swiss 2px/仅浮层、terminal 4px/内发光）
- [ ] 中文正文行高 ≥ 1.7；中西文之间有空格
- [ ] 页面里最显眼的东西，是用户最该先看到的东西
- [ ] 生图 prompt 是四段式，形容词不超过 8 个

## 文件在哪

```
style-library/
├── SKILL.md              ← 你正在读的
├── principles.md         ← 通用设计原则。写任何风格前必读，第 9 节讲怎么吸收外部风格
├── styles/<slug>/
│   ├── DESIGN.md         ← 唯一真相：YAML tokens + 8 章节设计理由
│   ├── tokens.css        ← 可直接引入的实现
│   └── prompt.md         ← 生图模板
├── references/<name>/
│   ├── DESIGN.md         ← 外部原始存档，只读，不许改
│   └── NOTES.md          ← 提炼卡：取 / 弃 / 待观察
├── inbox/                ← 原料入口
├── prompts/
│   ├── style-words.md    ← 风格词表（光线/材质/构图/色彩/流派）
│   └── negative.md       ← 负向词
├── preview/index.html    ← 对照预览，改完必看
└── scripts/
    ├── lint.py           ← 校验（零依赖）
    ├── build-preview.py  ← 重建预览
    ├── new-style.sh      ← 新建风格脚手架
    └── fetch-ref.sh      ← 抓外部样本
```

## DESIGN.md 格式要点

规范来自 [google-labs-code/design.md](https://github.com/google-labs-code/design.md)。写的时候记住：

- front matter 用 `---` 包住，放 `name` / `description` / `colors` / `typography` / `rounded` / `spacing` / `components`
- prose 里引用 token 用 `{colors.primary}` 这种花括号语法，**lint 会检查它是否有效**
- 章节顺序固定：Overview → Colors → Typography → Layout → Elevation & Depth → Shapes → Components → Do's and Don'ts
- 本库额外要求 `## Chinese Typography`（上游 84 个样本都没有，这是核心差异）和 `## Known Gaps`
- 组件属性只有 8 个合法值：`backgroundColor` / `textColor` / `typography` / `rounded` / `padding` / `size` / `height` / `width`。写 `borderColor` 会被官方 lint 告警（接受，但要知道）
