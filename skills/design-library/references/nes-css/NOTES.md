# NES.css

## 来源

- 类型：③ 能跑的组件库（SCSS 源码）
- 仓库：`nostalgic-css/NES.css`（21,859 stars，2026-11-17 查询）
- 路径：`scss/base/variables.scss`、`scss/base/color-palette.scss`
- 抓取：2026-11-17

## 取（吸收了什么，落到哪）

- Press Start 2P、16px 基准、4px 边框 → `pixel-arcade` 的排版与组件骨架。
- `#108DE0` 主操作蓝、`#F7D51D` 奖励黄、`#212529` 墨色和 `#ADAFBC` 投影灰 → colors。
- NES 硬件受限色板思路 → 每屏只保留蓝黄与中性色。

## 弃（明确不吸收，为什么）

- 完整 54 色硬件色板 → 不需要也不应全部进入界面。
- 纯白画布 → 改为 `#F8F8F0` 与 `#FCFCF4`。
- 中文正文使用 Press Start 2P → 字体无中文字形，必须回退系统无衬线。
- 专用 cursor 与像素图标资源 → 尚未随库提供，不假装已覆盖。

## 待观察

- 高 DPI 与中文回退字体的实际渲染。
- 100ms steps(2) 的反馈是否过弱，需要真实交互测试。
