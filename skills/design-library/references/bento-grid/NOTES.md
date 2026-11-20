# Bento Grid｜便当格

## 来源

- 类型：① 二手设计风格分析（三份交叉验证）
- 页面一：https://cusps.net/guide/bento
- 页面二：https://vibe-hub.org/style-bento
- 页面三：https://www.awesomeskills.dev/zh-CN/skill/design-ontology-bento-grid-ui
- 抓取：2026-11-20
- star：不适用

## 取（吸收了什么，落到哪）

- cusps.net 的显式色板：Base `#F4F4F5`、Ground `#FFFFFF`、Highlight `#6366F1`、Accent `#F59E0B`、Text `#18181B`，以及逐色 WCAG 对比度实测（Text 16.38:1 可正文、Highlight 4.13:1 仅大字、Accent 1.99:1 仅填充）→ 落到 `styles/bento-grid` 的 Colors 与 contrast 说明；三色保留角色分工（灰底白卡、靛蓝强调、琥珀只做填色）。
- cusps.net 的字体搭配 Display＝Plus Jakarta Sans、Body＝Inter（均为开源可商用 Google Fonts）→ 落到 Typography 的双字族分工。
- cusps.net 的「每格一个点、一致圆角与均匀间距不可妥协、每格只给一件事（数字/图标/小图）、用大小变化做节奏」→ 落到 Overview 的性格描述、`components.card` 与 Don't。
- vibe-hub.org 的「大格放核心、小格补信息」「卡片大小反映优先级」「颜色用来分组或强调，保持整体对比一致」「16–24px 圆角、统一格距」→ 落到 Layout 的 12 列跨度规则、rounded.card 与 Do's。
- awesomeskills.dev 的硬护栏：4/12 列网格、12–16px 统一 gap、20–28px 统一圆角、每格一信息（≤8 词标题）、首屏不超过 8 格、单格不超过 30 词、无厚边框与硬阴影、不出现破坏矩形的空洞 → 落到 spacing.sm/md、rounded.card、Layout、Don't 与 Key Characteristics。
- 三份来源一致的「避免长表单、密集数据、强线性流程、少于 5 格」→ 落到 avoid 字段与 When to Use 的「别用」。

## 弃（明确不吸收，为什么）

- Highlight `#6366F1` 原值当主按钮底 → WCAG 白字仅 4.47:1，来源自己也标 "Large only"；正文级按钮不达标，调深一档到 `#4F46E5`（白字 6.29:1、对画布 5.72:1）。NOTES 与 Known Gaps 均标注这是对来源的修正而非原值。
- 来源里的 Apple / M4 芯片规格、具体品牌文案与产品截图 → 品牌专属资产与文案，不可迁移；只写「一格一信息、大格放核心」的规则，不搬任何品牌内容。
- 来源明确指向的 Are.na 参考板、Dribbble / Mobbin 截图 → 只作风格存在性与饱和度的证据，不是可复现参数，不写进 styles。
- 纯白 `#FFFFFF` 铺满画布 → 本库 The Floor 要求底色向主色偏一档；纯白只保留给卡片，画布改浅灰（恰好也是来源的 Base 值）。
- 「对角线驱动 / 视差」「具体动效曲线」→ 来源未给可复现数值，按本库 motion 契约自定，不声称来自来源。

## 待观察

- Plus Jakarta Sans 不含中文，中文标题气质依赖 PingFang SC 回退，需真机复核。
- 主色修正值 #4F46E5 与严格照抄趋势指南的页面存在色差；若将来要贴近某品牌，需重新标定。
- 格子跨度＝优先级的语义在含表单或强顺序的页面上可能与阅读顺序冲突，这类场景本风格不覆盖。
- 深色 bento 变体与超过 8 格的长页未定义，来源也没有给出对应规范。
