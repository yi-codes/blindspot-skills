---
name: style-library
description: 个人视觉风格库。为网页、落地页、桌面 app、技术文档定视觉语言、统一配色与排版，或为文章配图确定画面风格时使用。风格用 DESIGN.md 描述，同时给出可直接引用的 tokens.css 和生图 prompt 模板。不用于已有设计稿或品牌规范的项目。
---

# 风格库

一套**可执行**的视觉风格资源。每个风格两个出口：`tokens.css`（网页/UI）和 `prompt.md`（生图）。

**当前有哪些风格，读 [`styles/INDEX.md`](styles/INDEX.md)，不要记名字。** 那份索引是脚本从每个风格的 front matter 长出来的，风格会越来越多。

---

## The Floor（永不豁免）

不管读没读别的，这十二条必须守。**违反任何一条，产物就是废的。**

| # | 规则 | 谁查 |
|---|---|---|
| 1 | 颜色和字体**只来自**该风格 `tokens.css` 的变量。产物里不许出现裸色值、裸 `font-family` | 人+脚本 |
| 2 | 深色底不许用 `#000`；浅色底不许用大面积 `#fff`。往主色偏一档 | `slop.py` |
| 3 | 不许紫到蓝/紫到粉的渐变，不许 `background-clip: text` 的渐变文字 | `slop.py` |
| 4 | 不许在标题前放"宣布下面是什么"的装饰小字。署名、`<time>`、文件名、序号合法 | `slop.py` |
| 5 | 字号、圆角、间距**只用 token 阶里的档位**。要阶外值，先加 token 再用 | `lint.py` |
| 6 | 中文正文行高 ≥1.7。界面类可到 1.5，但必须等于该风格 `DESIGN.md` 里写的那个数 | 人 |
| 7 | 中西文之间留四分之一个空格：`12 个文件`、`用 SF Pro` | 人 |
| 8 | 深色风格的正文比浅色少 50 字重（亮字在深底上有光渗，400 → 350） | 人 |
| 9 | 交付前必须跑 `lint.py` 和 `slop.py`，**两个都是 0 错误**。不许跳过，不许"差不多就行" | 脚本 |
| 10 | 不许编造通过记录。没跑就说没跑 | 人 |
| 11 | 一个页面只用**一种**风格。混用等于两套硬约束互相打架 | 人 |
| 12 | 新风格必须四件齐全：`DESIGN.md` / `tokens.css` / `prompt.md` / front matter 的选择字段。缺一件它在索引里就不存在 | `lint.py` |

`slop.py` 的 **E 是上述硬线**；它报的 W 是"看流派"的（全大写小标签、拉开的字距，在编辑/瑞士/终端三种排版传统里是原生语法），要你自己判。

---

## Flow

### 1 · 选风格

读 `styles/INDEX.md`。它有两张表：

- **决定表** —— 先问"这篇东西要让读者确认什么"，定职守，再在那一组里挑
- **全表** —— 每个风格的 `cues`（什么时候用）和 `avoid`（什么时候**别**用）

`avoid` 里列的不是"不推荐"，是"别用"。用错了出来的东西一定像模板——那个风格没为那个场景做过约束。

**都排除了，说明这里该开新风格，不是硬套。** 判据见 `principles.md` §8。

### 2 · 取

只读两个文件：`styles/<slug>/DESIGN.md`（设计理由、Do/Don't、Known Gaps）和 `tokens.css`（可直接引用的实现）。

**不要读其它风格。** 读多了会互相污染，最后做出来一个四不像。

```html
<link rel="stylesheet" href="styles/<slug>/tokens.css">
<div class="ds-<slug>"> … </div>
```

组件里写 `var(--xx-space-4)`，不要硬编码。变量前缀见该文件顶部注释。

### 3 · 做

先定"这一屏最显眼的东西"，让它就是用户最该先看到的东西。剩下的从 `DESIGN.md` 的硬约束里推——圆角、行高、层级手段、颜色上限都是给定的，不用重新想。

要配图就读该风格的 `prompt.md`，只换主体描述。四段式：材质 → 光线 → 构图 → 色彩后期，形容词不超过 8 个。

### 4 · 自检

```bash
python3 scripts/lint.py                 # 文档层：token 引用、对比度、章节、DESIGN.md ↔ CSS 全量对齐
python3 scripts/slop.py <产物.html>      # 产物层：AI 味儿
```

两个都是 0 错误才算完。`lint.py` 查文档自洽，`slop.py` 查产物——**它们查的东西不重叠，少跑一个等于没查。**

### 5 · 报

说清：用了哪个风格、为什么是它（引 `cues`）、跑了什么、结果是几个 0。
哪条破了例、理由是什么，一起说。**破例要留痕**，见 `principles.md` §11.4。

---

## 按需加载

不要通读全部文件。按这张表取：

| 遇到什么 | 读什么 |
|---|---|
| 页面被说"太普通 / 有 AI 味儿" | `principles.md` §11（12 条一眼假 + 深色三条规矩） |
| 中文排版出事（行高、标点、混排） | `principles.md` §6 + 该风格 `DESIGN.md` 的 `## Chinese Typography` |
| 想新开一个风格 | `principles.md` §8，然后 `scripts/new-style.sh` |
| 有人给你看他喜欢的设计/网站 | `references/README.md`（三层漏斗：inbox → references → styles） |
| 要做深色 / 双模 | `principles.md` §11.3 + `references/hallmark/NOTES.md` |
| 要写界面文案、元信息、日期 | `principles.md` §11.2 第 5 条（中点、箭头、状态点） |
| 要生图 | 该风格 `prompt.md` + `prompts/style-words.md` + `prompts/negative.md` |
| 不确定某个风格怎么来的、可不可信 | `references/*/NOTES.md`（"弃"那一栏比"取"重要） |

---

## 不该做

- **不要为了"换个感觉"新开风格。** 判据是"新场景是否必须违反现有风格的硬约束"。
- **不要用生图做 UI 效果图。** 模型不懂 16px 圆角、15px/1.5 行高、8% 白边框，它一定会画错，还会写字。界面就用 `tokens.css` 渲染。
- **不要为了过 lint 而改设计。** lint 是下限，不是目标。它只保证"没说谎"，不保证"好看"。

---

## 加一个风格（扩展性在这里）

**加风格 = 动一个目录。SKILL.md、README、索引、预览，一个字都不用改。**

```bash
./scripts/new-style.sh <slug> "<中文名>"
#   生成 DESIGN.md / tokens.css / prompt.md 三份骨架（front matter 的选择字段已带好）

# 填内容，然后：
python3 scripts/lint.py          # 校验（缺字段直接报 E）
python3 scripts/build-index.py   # 自动进 styles/INDEX.md 和 index.json
python3 scripts/build-preview.py # 自动进对照预览页
```

`DESIGN.md` 的 front matter 里这四项是**索引的输入**，缺一项这个风格就选不出来：

```yaml
cues: 用它的场景1、场景2、场景3      # 触发信号
avoid: 绝对别用的场景1、场景2        # 排他条件
surface: light | dark | mixed
register: story | professional | technical | tool   # 职守
```

要加新的选择维度（比如 `density: loose | dense`），改 `scripts/build-index.py` 顶部的 `FIELDS` 表，索引自动多一列。**加维度不改任何风格的正文。**

解析器只有一份，在 `scripts/_designmd.py`，lint / build-index / 其它脚本共用——不要各写一份。

---

## 文件在哪

```
style-library/
├── SKILL.md              ← 你正在读的（闸门 + 流程）
├── principles.md         ← 判断标准。11 节，按需读，不要通读
├── styles/
│   ├── INDEX.md          ← 【自动生成】选风格读这个（决定表 + 全表）
│   ├── index.json        ← 【自动生成】给脚本读
│   └── <slug>/           ← DESIGN.md（含选择字段）/ tokens.css / prompt.md
├── showcase/             ← 深度样张（手工，只覆盖部分风格）
├── preview/index.html    ← 【自动生成】全风格对照预览
├── references/<name>/    ← 外部样本原文（只读）+ NOTES.md（取/弃/待观察）
├── inbox/                ← 原料入口，扔的时候不筛选
├── prompts/              ← 风格词表 + 负向词
└── scripts/
    ├── _designmd.py      ← 共用解析器（写新脚本前先看它，别各写一份）
    ├── lint.py           ← 查文档：token / 对比度 / 章节 / 数值阶对齐
    ├── slop.py           ← 查产物：AI 味儿
    ├── build-index.py    ← 生成 INDEX.md + index.json
    ├── build-preview.py  ← 生成对照预览
    ├── new-style.sh      ← 新建风格脚手架
    └── fetch-ref.sh      ← 抓外部 DESIGN.md 样本
```

`DESIGN.md` 的格式要点见 `references/README.md` 末尾。核心三条：prose 里用 `{colors.primary}` 引用 token（lint 会校验有效性）、章节顺序固定、本库额外要求 `## Chinese Typography` 和 `## Known Gaps`。
