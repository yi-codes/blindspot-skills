# Bauhaus

## 来源

- 类型：① 二手设计风格分析（三份交叉验证）
- 页面一：https://aesthetic.fyi/bauhaus
- 页面二：https://vocab.design/bauhaus-style
- 页面三：https://www.stellae.design/learn/bauhaus-design-principles
- 抓取：2026-11-19
- star：不适用

## 取（吸收了什么，落到哪）

- aesthetic.fyi 给出的显式色值 `#EB4034`（红）、`#2D5DA1`（蓝）、`#F5C518`（黄）与"80px+ 标题 / 16px 正文"的极端尺度差 → 落到 `styles/bauhaus` 的 Typography 与 Colors；三值作参照，最终改用对比度更稳的 #D40000 / #003DA5 / #FFD500（后两来自 stellae 的显式值）。
- aesthetic.fyi 的 `border-radius: 50%` 画圆、`clip-path: polygon` 画三角、`::before/::after` 做大面积色块 → 落到 `styles/bauhaus/tokens.css` 的形状实现与 `media.iconRule`。
- vocab.design 的形状—颜色配对（三角=黄、方=红、圆=蓝）、单条对角线、flush-left 不对称网格 → 落到 Layout、Shapes 与 `media.emptyState`。
- vocab.design 的"几何无衬线适合展示、正文要换开放字腔字族"警告 → 落到双字族分工：DM Sans 管标题、Inter 管正文。
- stellae.design 的显式值 `#D40000 / #003DA5 / #FFD500 / #1A1A1A / #FAFAFA`、8px 网格、直角组件、2px 实边 → 落到 Colors、spacing.base 与 `components.card`。
- 三份来源一致的"无渐变、无纹理、无投影、功能优先" → 落到 `elevation`（steps=1，e1–e3 全为 none）与 Don't。

## 弃（明确不吸收，为什么）

- 纯白 `#FFFFFF` 底 → 本库 The Floor 要求底色向主色偏一档，改为暖纸白 `#F4F0E6`。
- aesthetic.fyi 的 `#EB4034` 红 → 与暖纸白对比只有约 3.5:1，按钮白字不足 4.5:1，改用 #D40000。
- 全小写英文与 0.2em 以上宽字距 → 中文不成立，且损伤可读性；标签字距收敛到 0.08em。
- 具体海报、品牌与历史人物的图像资产、宣传语气 → 不可迁移，只写规则不写资产。
- "对角线驱动构图"作为硬约束 → 只在图片生成的变体中保留，页面布局仍用网格与面积差，避免与 swiss-grid 的秩序感混淆。
- 三原色直接当状态色 → 红/蓝在界面里已被"错误/链接"占用，本风格把它们重新定义为结构色，表单语义需单独复核。

## 待观察

- DM Sans / Futura 不含中文，中文标题的实际气质依赖 PingFang SC 回退，需要真机复核。
- 深色 Bauhaus 变体与复杂表单、多步流程未定义。
- 形状配色的语义冲突（红=主行动 vs 红=错误）在含表单页面上的实际影响尚未验证。
