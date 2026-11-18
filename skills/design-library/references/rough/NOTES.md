# Rough.js

## 来源

- 类型：③ 能跑的图形库（官网 API + GitHub）
- 仓库：`rough-stuff/rough`（21,391 stars，2026-11-17 查询）
- 官网：https://roughjs.com
- 抓取：2026-11-17

## 取（吸收了什么，落到哪）

- Canvas／SVG 双出口、hachure／cross-hatch 等填充模型 → `sketch-notes` 的图形实现建议。
- roughness、bowing、strokeWidth、fillWeight、hachureGap 等可调参数 → Layout 的图形约束。
- 固定 seed 的复现要求 → `sketch-notes` 的 Do 与 Iteration Guide。

## 弃（明确不吸收，为什么）

- 每次渲染随机变化 → 页面与构建结果不可复现，必须固定 seed。
- 把 Rough.js 强加到所有正文和控件 → 只负责图形；组件边框使用 PaperCSS 参数。
- 运行时为静态插图加载库 → 可预生成 SVG，避免不必要依赖。

## 待观察

- 建议值 roughness 1.3／bowing 1.2／strokeWidth 1.6 尚需多尺寸实测。
- 滚动描边动画不在当前 tokens.css 范围内。
