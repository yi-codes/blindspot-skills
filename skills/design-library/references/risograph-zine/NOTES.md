# Risograph Zine Aesthetic

## 来源

- 类型：① 二手设计规范（艺术设计样本）
- 页面：https://designmd.app.br/library/risograph-zine-aesthetic
- 抓取：2026-11-17
- star：不适用

## 取（吸收了什么，落到哪）

- 纸色 `#FDFBF6`、墨色 `#1C1C5E`、粉 `#E63E85`、蓝 `#0078BF` → `riso-zine`。
- 1–3px 套印错位、multiply 叠印、纸纹和不对称构图 → Layout 与 Elevation。
- 150ms 颜色反馈和静态优先 → tokens.css 动效约束。

## 弃（明确不吸收，为什么）

- 8px 通用卡片圆角与柔和阴影 → 改为直角和 6px 实色错位层，避免变成普通营销模板。
- 三列功能卡、通用 SaaS 结构与 shimmer → 不属于 zine 的核心场景。
- 黄、绿额外专色 → 默认每屏只保留粉蓝两色，避免花乱。

## 待观察

- CSS 点阵不是实际 Riso 墨粒，需要真实印刷或扫描样本标定。
- 中文标题分色仅允许 1px，仍需字体级验证。
