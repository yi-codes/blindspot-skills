---
version: alpha
name: Deco Ceremony｜装饰艺术典礼
description: >-
  给精品酒店、晚宴、珠宝与颁奖典礼用的 Art Deco 页面。严格中轴对称、
  1–2px 双线金框、48px 高对比衬线和 500ms 缓慢过渡；只使用实色金，
  不做渐变金字。视觉参数提炼自 Art Deco 艺术风格分析，中文规则由本库补齐。
cues: 精品酒店、高级餐厅、珠宝与腕表、晚宴与典礼、电影节、会员制俱乐部、历史建筑与品牌纪念页
avoid: 日常工具、数据后台、儿童产品、折扣电商、开发文档、密集表单、轻松亲民的消费 App
surface: dark
density: roomy
register: story
family: ceremonial
tier: variant
status: beta

colors:
  canvas: "#1A1A1A"
  surface: "#242321"
  ink: "#F5F0E8"
  ink-muted: "#C8BFAE"
  ink-faint: "#9B9283"
  hairline: "#7B6838"
  primary: "#D4AF37"
  primary-soft: "#3A3221"
  on-primary: "#1A1A1A"
typography:
  display:
    fontFamily: "Playfair Display, Noto Serif SC, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.08em
  headline:
    fontFamily: "Playfair Display, Noto Serif SC, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.04em
  body:
    fontFamily: "Cormorant Garamond, Noto Serif SC, serif"
    fontSize: 17px
    fontWeight: 350
    lineHeight: 1.75
    letterSpacing: 0
  label:
    fontFamily: "Cormorant Garamond, Noto Serif SC, serif"
    fontSize: 12px
    fontWeight: 350
    lineHeight: 1.5
    letterSpacing: 0.04em
rounded:
  none: 0px
spacing:
  base: 8px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 32px
  xl: 48px
  section: 80px
  measure: 34em
components:
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    borderColor: "{colors.primary}"
    rounded: "{rounded.none}"
    padding: 32px
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: 16px 32px
  tag:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
---

## Overview

给精品酒店、餐厅、珠宝、晚宴、电影节和品牌纪念页用。读者应该感到“这是一个有仪式的场合”，而不是“这是一个效率工具”。它通过中轴、双线框、留白和慢速过渡建立秩序。

Art Deco 的关键不是金色渐变，而是几何纪律：所有主区块沿垂直中轴镜像；金线 1–2px；装饰采用阶梯、菱形和放射结构；标题字重保持 400。这里刻意禁止渐变金字和发光，因为那会从建筑感变成促销感。

来源是 aesthetic.fyi 等 Art Deco 设计分析，属于艺术风格二手资料而非具体品牌官方规范。本库重新定了深色正文 350、中文 1.75 行高、焦点态和 reduced-motion。

**Key Characteristics**

- `{colors.canvas}` 深炭底， `{colors.ink}` 奶油白正文， `{colors.primary}` 实色黄铜金。
- 48px 展示衬线标题，字距 0.08em；中文降为 0.04em，不强行全大写。
- 中轴对称、成对栏目、双线金框；装饰线同时承担分隔和构图。
- 区段间距 80px，卡片内距 32px；不靠堆内容制造“丰富”。
- 动效 500ms、无回弹；reduced-motion 下直接呈现最终状态。

## Colors

- `{colors.canvas}` — #1A1A1A，主背景，不是纯黑。
- `{colors.surface}` — #242321，卡面和菜单纸面。
- `{colors.ink}` — #F5F0E8，标题与正文。
- `{colors.ink-muted}` — #C8BFAE，说明与次级信息。
- `{colors.ink-faint}` — #9B9283，编号和非关键装饰文字。
- `{colors.hairline}` — #7B6838，次要金线与分隔。
- `{colors.primary}` — #D4AF37，实色金，只用于线、主按钮和关键符号。
- `{colors.primary-soft}` — #3A3221，选中或聚焦底，不作大面积金色发光。
- `{colors.on-primary}` — #1A1A1A，金底上的深字。

## Typography

英文展示用 Playfair Display，正文用 Cormorant Garamond；中文回退 Noto Serif SC。标题 48／24px、400；正文 17px／350／1.75；标签 12px／350／1.5。

英文主标题可全大写，字距 0.08em；标签不全大写、不拉到 0.2em。中文不做全大写模拟，标题字距上限 0.04em，正文为 0。

## Layout

- 容器最大 1200px，主视觉和章节标题沿同一垂直中轴。
- 使用成对 6:6 栏或 4:4:4 对称栏；不允许故意打破中轴的随机错位。
- 卡片内距 32px，区块间距 80px；正文最大 `{spacing.measure}`。
- 装饰图形只能使用中轴放射、阶梯、菱形和双线框，不添加随机艺术涂鸦。
- 768px 以下按中轴单列，装饰线缩短，不缩小正文。

## Elevation & Depth

不使用模糊投影。层级来自深底、金线和双线框：外框 1px `{colors.primary}`，间隔 4px `{colors.canvas}`，内框 1px `{colors.primary}`。禁止金色光晕与渐变金属字。

## Shapes

所有卡片、按钮和输入框 `{rounded.none}`。允许菱形、阶梯和扇形放射；禁止 pill、气泡圆角、随意切角和不对称卡片。

## Components

### card

`{components.card}` 使用深一阶纸面与双线金框，内容居中。卡片用于房型、菜单、奖项或场次，不用于仪表盘模块。

### button-primary

`{components.button-primary}` 使用实色金底与深字，hover 仅改为 `{colors.primary-soft}` 底和金字；500ms 过渡，无位移回弹。

### tag

`{components.tag}` 只表达日期、场次、会员权益等事实，透明底、1px 金线。不要把标题前的装饰小字全部做成标签。

## Do's and Don'ts

### Do

- 先画中轴和成对栏，再放装饰。
- 使用实色金与完整焦点态。
- 让装饰线同时承担分隔或框定内容的功能。
- 在 reduced-motion 下直接显示最终状态。

### Don't

- 不要用渐变金字、背景光斑或金色发光投影。
- 不要混入圆角卡片、休闲插画或年轻化表情符号。
- 不要把密集表格和后台操作塞进双线金框。
- 不要为了“奢华”把所有文字都拉宽字距或改成金色。

## Chinese Typography

- 中文正文 17px／350／1.75；如果字体不支持 350，使用 300 而非伪粗。
- 中文标题 400，字距 0.02–0.04em；正文为 0。
- 中西文之间留四分之一空格；日期、价格、场次分行，不用中点串联。
- 使用全角标点、避头尾、不首行缩进；引号使用“”。
- 中文主标题最多 12 字，超出时主动换行并保持中轴对称。

## When to Use

**用**：精品酒店、餐厅菜单、珠宝腕表、晚宴邀请、颁奖典礼、电影节、品牌纪念页。

**别用**：日常 App、数据看板、开发工具、折扣促销、儿童教育、复杂表单、高频生产工具。

## Iteration Guide

1. 先检查对称与留白，再检查金色使用量。
2. 太朴素时增加一条结构金线，不加发光或渐变。
3. 太隆重时减少装饰层数，不降低正文对比度。
4. 修改 `{components.card}` 后检查中文居中、焦点和长价格文本。

## Known Gaps

- 尚未提供复杂预订、日历选择、支付与库存状态组件。
- Art Deco 图案库未内置，只提供双线框和几何约束。
- Playfair Display 与 Cormorant Garamond 不含中文，中文效果依赖 Noto Serif SC。
- 来源为艺术风格分析而非品牌官方设计系统，不应复刻具体酒店或珠宝品牌资产。
