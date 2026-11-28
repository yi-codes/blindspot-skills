---
name: 叙事引导型
slug: editorial-lede
version: 1
status: beta
density: sparse
register: story
frame: [frame-story, frame-nav, frame-context, frame-lede, frame-actions, frame-grid]
sample: ../preview/bauhaus.html
---

# 叙事引导型 · editorial-lede

## 适用任务

一个主张需要被先读懂、再被接受：作品集首页、产品发布页、独立开发者介绍、
长文封面、募款/招募页。用户来这里不是找功能，是判断"这值不值得继续看"。

## 主角与视线

唯一主角是 **H1 那一句主张**（最多 17ch，`max-width: 17ch` 强制换行）。
视线路径：`H1 → lede（58ch 内的一段解释）→ actions（1 主 1 次）→ grid（三块支撑）`。
`frame-context` 是 eyebrow，但按 The Floor 第 4 条，它不能只是宣布"下面是内容"，
必须带信息（日期、期号、分类、状态）。

## 网格与密度

- 密度 `sparse`：首屏 `padding-top: clamp(3rem, 8vw, 7rem)`，靠留白而非描边分段。
- 主体 `frame-story` 限宽 70rem 居中。
- `frame-grid` 为 `1.45fr : 0.8fr : 0.8fr`，第一块是主证据，后两块是佐证。
  这个比例本身就是层级声明——不是三等分卡片墙。
- 48rem 以下三栏塌成单栏，顺序保持"主证据在前"。

## 挂载点

| 结构类 | 挂什么 | 状态要求 |
|---|---|---|
| `frame-nav` | 字标 + 不超过 4 个入口 | 当前项 `aria-current` |
| `frame-context` | 有信息的 eyebrow | 无信息则整块删除 |
| `frame-lede` | 一段解释主张的正文 | 中文 ≥18px / 行高 ≥1.7 |
| `frame-actions` | 主按钮 + 次级链接 | 焦点环、reduced-motion |
| `frame-grid` | 三个 `.ds-card` | 空态写一行说明，不放插画 |

## 与风格的咬合

骨架只定"谁先被看到、占多大"，配色、字族、圆角、材质全部走所选风格 token。
适合 `family` 为 editorial / expressive / geometric 的风格；
`frame-story` 的 `--frame-sep: none` 明确声明"叙事靠留白不靠线"，
所以套用强调描边分区的工具类风格（register: tool）会打架，别硬套。

## 禁用项

- 控制台、数据看板、任何需要多任务并行的界面：首屏大面积留白会把操作入口推到折叠线以下。
- 内容超过 5 个并列重点时：`1.45:0.8:0.8` 会逼着你把重要信息塞进小格，层级失真。
- 没有真实主张、只有"欢迎来到我们的网站"时：这个骨架会把空洞放大，换工作台型更诚实。
