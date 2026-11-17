---
name: design-library
description: 个人设计风格库与界面落地工作流。需要为网页、控制台、桌面应用、文档或生图选择视觉风格，比较现有风格，设计或重设计页面，审计风格一致性，或把新设计收进风格库时使用。把风格选择、token、实现骨架、预览、产物检查和扩展流程收在一个入口里。
metadata:
  version: 2.1.0
---

# Design Library

这是一个**可执行**的设计风格库，不是灵感清单。

每个风格同时提供：

- `DESIGN.md`：选择条件、设计理由、布局骨架、克制清单和已知缺口
- `tokens.css`：可直接引入的 CSS token 与基础组件
- `prompt.md`：同一视觉语言的生图模板
- 自动生成的预览、索引和目录数据

每个风格还声明 `family`、`tier` 和 `sourceRefs`：

- `tier: core`：独立承担一种页面职责，默认优先推荐
- `tier: variant`：核心风格的明暗、材料或密度变体，完整保留但不是第一入口
- `tier: technique`：可复用技法，通常与某个核心风格或组件搭配

**三类都保留。** 分层只影响推荐顺序，不删除风格。

**当前有哪些风格，一律读 [`styles/INDEX.md`](styles/INDEX.md)。不要背名字，也不要从 README 猜。**

---

## The Floor

以下规则永不豁免。违反任意一条，结果不能算完成。

1. 颜色和字体只来自所选风格的 `tokens.css`，产物里不写裸色值或裸 `font-family`。
2. 深色底不用大面积纯黑，浅色底不用大面积纯白；背景向主色偏一档。
3. 不用紫到蓝、紫到粉的渐变，不用 `background-clip: text`。
4. 标题前不放只负责宣布“下面是内容”的装饰小字。
5. 字号、圆角、间距只用 token 阶；要新值，先补 token。
6. 中文正文行高不低于 1.7。界面类可以按该风格声明的行高执行，但不得低于 1.5。
7. 中西文之间留四分之一个空格：`12 个文件`、`用 SF Pro`。
8. 深色正文比浅色少 50 字重，除非风格文档给出了实测理由。
9. 一个页面只使用一种风格，不混用两套硬约束。
10. 每个交互元素都有可见的 `:focus-visible`；动效有 reduced-motion 降级。
11. 交付前运行 `designlib check`；没运行就不能声称通过。
12. 新风格必须四件齐全：`DESIGN.md`、`tokens.css`、`prompt.md`、完整选择字段。

---

## 四个动作

### select

先描述**用户要完成什么**，不要从“想换个感觉”开始。

```bash
python3 scripts/designlib.py recommend "内部 Agent 控制台，任务运行状态和待确认操作"
```

它会按场景、职守、明暗、密度和排除条件排序，并说明为什么推荐。然后只读：

1. `styles/<slug>/DESIGN.md`
2. `styles/<slug>/tokens.css`

不要同时读多套风格；读多了会互相污染。

想先只看主入口：

```bash
python3 scripts/designlib.py list --tier core
```

### apply

```html
<link rel="stylesheet" href="styles/<slug>/tokens.css">
<div class="ds-<slug>"> … </div>
```

先确定这一屏最显眼的东西，让它就是用户最该先看到的东西。布局与组件从所选 `DESIGN.md` 的硬约束推导，不从别的风格借用。

### audit

只读对照所选风格，检查四件事：

1. 是否仍只有一个主问题、一个主行动
2. 颜色、字体、间距、圆角是否全部走 token
3. 交互状态、键盘焦点、空态、错误态是否完整
4. 是否踩中了该风格 `DESIGN.md` 的 `Don't` 和 `Known Gaps`

报告问题，不擅自改代码，除非用户同时要求修复。

### collect

只有“新场景必须违反现有风格的硬约束”时才新增风格。只是换颜色、换字号或想试试新感觉，应修改现有风格。

```bash
python3 scripts/designlib.py new <slug> "<中文名>"
```

然后填写三个文件，再运行：

```bash
python3 scripts/designlib.py build
python3 scripts/designlib.py check
```

---

## 日常命令

```bash
python3 scripts/designlib.py list
python3 scripts/designlib.py show <slug>
python3 scripts/designlib.py recommend "<页面任务>"
python3 scripts/designlib.py build
python3 scripts/designlib.py check
python3 scripts/designlib.py new <slug> "<中文名>"
```

- `list`：紧凑列出全部风格
- `show`：输出一个风格的给 Agent 用的最小读数路径
- `recommend`：按任务描述排序并给出理由
- `build`：重建索引、目录数据和预览页
- `check`：生成检查、文档 lint、链接检查和目录自洽检查
- `new`：创建风格骨架

所有命令都保留全部风格；`--tier` 只用于缩小浏览范围。

浏览器目录直接打开 [`catalog/index.html`](catalog/index.html)。支持搜索任务、按职守/明暗/密度筛选、并排比较和复制接入代码。

---

## 使用顺序

1. 运行 `recommend`，或读 `styles/INDEX.md`。
2. 确认首选风格不在自己的 `avoid` 场景里。
3. 读首选风格的 `DESIGN.md` 与 `tokens.css`。
4. 用该风格的 token 和结构骨架实现。
5. 需要配图时读同一风格的 `prompt.md`。
6. 运行 `designlib check`；交付时报告实际结果。

全都排除了，说明这里需要新风格，不是硬套。

---

## 按需加载

| 遇到什么 | 读什么 |
|---|---|
| 不知道该选哪个 | `styles/INDEX.md` 或运行 `recommend` |
| 要做 UI / 重设计 | 所选风格 `DESIGN.md` + `tokens.css` |
| 中文排版出问题 | `principles.md` §6 + 风格里的 `Chinese Typography` |
| 页面有 AI 味儿 | `principles.md` §11 |
| 想新增风格 | `principles.md` §8 + `docs/ADDING-A-STYLE.md` |
| 收集外部参考 | `references/README.md` |
| 要生图 | 所选风格 `prompt.md` + `prompts/negative.md` |
| 要审计实现 | 所选风格的克制清单、Don't、Known Gaps |

---

## 不该做

- 不要为了“换个感觉”新开风格。
- 不要用生图代替真实 UI 效果图；模型不懂精确圆角、行高和细边框。
- 不要为了让检查变绿而隐藏问题；lint 是下限，不是设计目标。
- 不要复制旧 `style-library` 或 `ui-styles` 的规则到新地方；本目录是唯一正本。
