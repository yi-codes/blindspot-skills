---
name: 分屏对照型
slug: split-manifesto
version: 1
status: beta
density: sparse
register: professional
frame: [frame-split, frame-stats, frame-nav, frame-actions]
sample: ../preview/civic.html
---

# 分屏对照型 · split-manifesto

## 适用任务

需要把"一句立场"和"一组事实"并置：机构/城市的介绍页、年报摘要、关于我们、
政策说明、简历首屏。左边是断言，右边是可核对的数字，两者互为证据。

## 主角与视线

唯一主角是 **左栏的大标题**，右栏 `frame-stats` 是它的证据而不是并列内容。
视线路径：`左栏 H1 → 右栏第一组数字 → 左栏 lede/actions`。
`align-items: end` 让两栏底边对齐，这条对齐线本身就是"两者相关"的视觉声明。

## 网格与密度

- 密度 `sparse`：`frame-split` 为 `minmax(0,1.25fr) : minmax(15rem,0.75fr)`，
  `gap: clamp(2rem,6vw,5rem)`，`padding-top: clamp(3rem,8vw,7rem)`。
- 右栏 `frame-stats` 固定单列，每组 `dt/dd` 用 `space-between` + 顶部细线，
  数字基线对齐而不是做成卡片。
- 48rem 以下塌成单栏，顺序为"立场 → 事实"，证据不能跑到断言前面。

## 挂载点

| 结构类 | 挂什么 | 状态要求 |
|---|---|---|
| `frame-split` 左 | H1 + lede + `frame-actions` | 主行动唯一 |
| `frame-stats` | 3–5 组 dt/dd | 数字用等宽或 tabular-nums |
| `frame-nav` | 字标 + 少量入口 | `aria-current` |

`--frame-sep: 1px solid currentColor`（`frame-professional`）：数字之间的细线是尺子，
不是装饰分区线，别加粗、别换成阴影。

## 与风格的咬合

适合 `register: professional` / `family` 为 editorial、civic、swiss 的网格化风格，
字阶里必须有清晰的 display 与 label 两档，否则数字会显得和正文一样重。
需要大面积氛围图或强材质的风格不适合：这个骨架的张力来自留白与对齐，
加背景图会同时削弱两者。

## 禁用项

- 右栏没有可核对的真实数据：编造的数字一旦被替换成"敬请期待"，整个结构失效。
- 需要展示 6 组以上事实：单列 stats 会被拉成长条，换叙事引导型的 grid（1 主 2 佐）。
- 有多个并列主张：分屏只能承载一个断言，换工作台侧栏型组织多任务。
