---
name: 文档三栏型
slug: docs-three-column
version: 1
status: beta
density: medium
register: technical
frame: [frame-docs, frame-docs-nav, frame-docs-main, frame-docs-toc, frame-nav]
sample: ../preview/developer-docs.html
---

# 文档三栏型 · docs-three-column

## 适用任务

长文档、API 参考、知识库、规范手册。用户有两个并行的需求：知道自己在全站哪一节，
以及跳到本页哪一段。三栏分别服务"全站 / 正文 / 本页"。

## 主角与视线

唯一主角是 **`frame-docs-main` 的正文**。左右两栏都是索引，必须比正文轻。
视线路径：`左栏当前节 → 正文 H2 → 右栏本页目录（只在需要跳转时）`。
正文 `h1` 不限宽到 17ch，那是叙事骨架的规则；这里正文行长控制在 60–75ch。

## 网格与密度

- 密度 `medium`：`frame-docs` 为 `minmax(9rem,12rem) : minmax(0,1fr) : minmax(8rem,10rem)`，
  限宽 76rem。左右两栏窄、正文宽，比例本身就是"正文优先"。
- 左右栏 `position: sticky; top: 1rem; align-self: start`，跟随滚动但不抢版面。
- 技术类用 `--frame-sep: 1px dashed currentColor`（`frame-technical` 的职守分化），
  与工具台的实线、叙事的留白区分开。
- 48rem 以下：三栏塌单栏，左栏变 3 列横排，右栏本页目录 `display: none`。

## 挂载点

| 结构类 | 挂什么 | 状态要求 |
|---|---|---|
| `frame-docs-nav` | 全站章节树 | 当前节 `aria-current` |
| `frame-docs-main` | 正文、代码块、表格 | 锚点可聚焦、代码块可横向滚动 |
| `frame-docs-toc` | 本页 H2/H3 锚点 | 滚动高亮（可选），键盘可达 |
| `frame-nav` | 顶部全局入口 | — |

代码块 `pre` 必须 `overflow: auto`，不能让长行撑破三栏 grid。

## 与风格的咬合

适合 `family` 为 editorial / technical / professional 的风格，尤其是字阶层次清楚的衬线或等宽体系。
强装饰、大圆角、氛围渐变风格会让三栏索引显得浮夸，且挤压正文行长。
`frame-docs-main` 内的表格/代码块全部走所选风格的 `tokens.css`，不写裸色值。

## 禁用项

- 内容短到没有 H2 分节：右栏本页目录会空，三栏变两栏半，直接换叙事引导型。
- 需要并排比较多份文档：三栏把正文压到中间，换工作台侧栏型 + 分栏视图。
- 移动端为主要阅读场景：本页目录被隐藏是降级不是等价，需另做折叠目录。
