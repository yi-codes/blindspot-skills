---
version: alpha
name: Riso Zine｜孔版独立志
description: >-
  用两种专色、1–3px 套印错位和可见纸纹做独立出版物。8 列不对称网格，
  层级来自错位色块而不是阴影。色彩与叠印参数来自 Risograph 设计样本；
  中文行高、组件可用性与移动端退化规则由本库补齐。
cues: 独立杂志、音乐节与演出海报、独立出版、诗歌与小册子、艺术活动页、乐队与唱片、创意工作坊
avoid: 企业年报、金融医疗政务、密集表单、数据看板、长文阅读、需要严肃可信的公共服务
surface: light
density: medium
register: story
family: zine
tier: variant
status: beta

colors:
  canvas: "#FDFBF6"
  surface: "#F5F0E6"
  ink: "#1C1C5E"
  ink-muted: "#515174"
  ink-faint: "#73738A"
  hairline: "#C9C3B6"
  primary: "#E63E85"
  primary-soft: "#F9D6E5"
  secondary: "#0078BF"
  on-primary: "#FDFBF6"
  grain: "rgba(28, 28, 94, 0.12)"
typography:
  display:
    fontFamily: "Work Sans, Arial, PingFang SC, sans-serif"
    fontSize: 64px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: -0.025em
  headline:
    fontFamily: "Work Sans, Arial, PingFang SC, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.01em
  body:
    fontFamily: "Work Sans, Arial, PingFang SC, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.75
    letterSpacing: 0
  label:
    fontFamily: "Work Sans, Arial, PingFang SC, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
rounded:
  none: 0px
  sm: 2px
spacing:
  base: 8px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  section: 64px
  measure: 38em
components:
  card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 24px
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: 12px 24px
  tag:
    backgroundColor: "{colors.primary-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
---

## Overview

给独立杂志、演出、唱片、诗歌册子和艺术工作坊用。它把页面当作一张孔版印刷品：纸色、专色、错位和不对称版面都有功能，不是通用 SaaS 页面加一层噪点。

核心只有两条：每屏最多两种专色 `{colors.primary}` 与 `{colors.secondary}`；套印错位限制在 1–3px。超过 3px 不是手工感，是读不清。卡片层次由 6px 的实色错位层表达，不用柔软投影。

来源是 Risograph Zine Aesthetic 二手规范与公开实现分析。保留纸色、专色、multiply 叠印和 1–3px 错位；拒绝它模板化的三列组件、8px 圆角和通用营销结构。本库重新定了直角、8 列网格和中文规则。

**Key Characteristics**

- `{colors.canvas}` 是纸，不是白底；允许细小颗粒可见。
- 粉 `{colors.primary}` 与蓝 `{colors.secondary}` 只作专色，交叉时用 `mix-blend-mode: multiply`。
- 64px 粗标题配 16px 正文；标题可错位，正文绝不错位。
- 8 列不对称网格，卡片可跨 3／5 列，禁止三列等宽功能卡。
- 默认直角；2px 仅用于小标签。不用玻璃、柔光和圆角浮卡。

## Colors

- `{colors.canvas}` — #FDFBF6，主纸色。
- `{colors.surface}` — #F5F0E6，另一张纸或插页，不与主纸同时大面积相邻。
- `{colors.ink}` — #1C1C5E，正文与主按钮；也是套印时的深色骨架。
- `{colors.ink-muted}` — #515174，摘要和说明。
- `{colors.ink-faint}` — #73738A，编号与非关键印刷标记。
- `{colors.hairline}` — #C9C3B6，裁切线和分隔线。
- `{colors.primary}` — #E63E85，荧光粉专色，不大段充当正文文字。
- `{colors.primary-soft}` — #F9D6E5，粉色浅层，只用于标签和局部底。
- `{colors.secondary}` — #0078BF，蓝专色，用于套印和偏移层。
- `{colors.on-primary}` — #FDFBF6，墨底按钮文字。
- `{colors.grain}` — 12% 墨色颗粒，只作低对比纹理。

## Typography

标题 64／28px，字重 700；正文 16px／400／1.75；标签 14px／500。字族保持 Work Sans 或系统无衬线，不使用等宽字体扮演“独立出版”。

标题字距 −0.025em，中文收紧到 −0.01em。错位只作用于图形或不承担阅读的大号英文标题；中文标题最多错位 1px，长句禁用。

## Layout

- 容器 1100px，8 列，24px 槽沟；区块间距 64px。
- 主视觉可按 5:3 分割，后续内容允许 2:6、4:4 但避免三张等宽卡。
- 色块错位 1–3px；卡片背后的实色层固定 6px，不能与文字错位混为一谈。
- 768px 以下取消叠印重叠与旋转，按阅读顺序堆叠，保留纸纹和专色。
- 正文最大 `{spacing.measure}`；印刷装饰不得进入正文栏。

## Elevation & Depth

不用模糊投影。层级只有纸面、1px 墨线和 6px 实色错位层。`multiply` 仅用于两种专色真实相交的区域，不用来让整页变暗。

## Shapes

卡片与按钮 `{rounded.none}`，小标签 `{rounded.sm}`。允许裁切标记、角线与简单几何专色块；禁止 pill、气泡、圆形图标底座和多层柔影。

## Components

### card

`{components.card}` 使用 1px 墨线与 6px 蓝色错位底层。悬停可平移 1px 表示“重新套准”，不要浮起或发光。

### button-primary

`{components.button-primary}` 用墨底纸色字，保证可读；粉色只作 hover 的 2px 侧层，不用白字直接压在粉底上。

### tag

`{components.tag}` 用于期号、场次、媒介等真实信息。每屏最多两种标签底色，不给所有标题加标签。

## Do's and Don'ts

### Do

- 把套印错位限制在图形和短标题。
- 保留纸色与低对比颗粒，让专色相交产生第三色。
- 用不对称网格安排真实内容。
- 移动端取消重叠，保证阅读顺序。

### Don't

- 不要把正文也做成分色重影。
- 不要使用紫蓝渐变或把 multiply 当作渐变替代品。
- 不要加柔和阴影、玻璃拟态或圆角营销卡。
- 不要在一屏引入四种以上专色。

## Chinese Typography

- 中文正文 16px／1.75，标签 14px／1.5；不以手写体代替正文。
- 中西文之间留四分之一空格，期号与日期独立成行。
- 中文标题不做 3px 分色；如使用错位，上限 1px 且不超过 8 个字。
- 使用全角标点、避头尾、不首行缩进。
- 中文标题负字距最大 −0.01em；正文为 0。

## When to Use

**用**：zine、独立出版物、展览活动、音乐与演出、艺术课程、唱片封面、创意品牌活动。

**别用**：企业正式报告、公共事务、医疗金融、长文、后台、数据比较、复杂交易。

## Iteration Guide

1. 先确定两种专色和纸张，再调网格。
2. 太花时先减少重叠与色块，不要降低文字对比度。
3. 太规整时先改跨列比例，不增加随机旋转。
4. 每次改 `{components.card}` 都检查错位是否影响点击区域和正文。

## Known Gaps

- 纸纹目前只用 CSS 点阵近似，不是真实 Riso 墨粒扫描。
- 尚未提供可打印的 CMYK／专色分版文件，也不能把屏幕色值当作印刷色彩证明。
- 中文大号标题的套印可读性需要实际字体复核。
- 复杂表单、电商和可访问性高要求流程不在本风格范围内。
