# WIRED

## 来源

- 类型：① 二手 DESIGN.md
- 仓库：`VoltAgent/awesome-design-md`（127,928 stars，2026-11-17 查询）
- 路径：`design-md/wired/DESIGN.md`
- 原站：https://www.wired.com
- 抓取：2026-11-17

## 取（吸收了什么，落到哪）

- 衬线叙事标题 + 无衬线结构信息 → `newsprint-grid` 的字体分工。
- 故事网格、1px 细线、方角按钮、无投影 → `styles/newsprint-grid/`。
- 56px 主标题与 12px 元信息的尺度差 → Typography 与 Layout。

## 弃（明确不吸收，为什么）

- 纯黑／纯白大面积画布 → 改为暖纸色与近黑墨色。
- WiredDisplay、BreveText、Apercu → 专有字体不分发，改用可回退字体。
- 自动派生的 pricing、cart、SaaS 示例 → 与新闻场景无关。
- 全大写宽字距栏目 → 中文不适用，也不作为默认装饰。

## 待观察

- 实时快讯、突发新闻和付费墙需要独立语义与状态。
- 中文长标题在 56px 档位下需要真实内容测试。
