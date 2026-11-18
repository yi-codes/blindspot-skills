# PaperCSS

## 来源

- 类型：③ 能跑的组件库（SCSS 源码）
- 仓库：`papercss/papercss`（4,198 stars，2026-11-17 查询）
- 路径：`src/core/_config.scss`、`src/core/_mixins.scss`
- 抓取：2026-11-17

## 取（吸收了什么，落到哪）

- 三组双轴不规则圆角 → `sketch-notes` 的 card／button／tag。
- `#0B74D5` 动作蓝、`#DDCD45` 标记黄 → colors.primary 与 highlight。
- `10px 19px 17px -13px` 小投影、hover 投影和 235ms 思路 → 收敛为 160ms 的组件反馈。

## 弃（明确不吸收，为什么）

- Neucha／Patrick Hand SC 用作中文正文 → 无中文字形，只能覆盖英文，中文回退系统无衬线。
- 纯白主背景和完整语义色板 → 改为暖纸色，只保留蓝黄两种功能色。
- 所有组件随机手绘化 → 关键表单与错误流程不纳入本风格。

## 待观察

- 不规则边框对触摸命中区和焦点轮廓的影响。
- 中文与英文混排时的字体灰度差。
