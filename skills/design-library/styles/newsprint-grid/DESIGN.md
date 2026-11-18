---
version: alpha
name: Newsprint Grid｜新闻纸网格
description: >-
  给真正拥有多条新闻的编辑首页：12 列、细线分栏、衬线标题与无衬线元信息，
  首屏直接进入故事网格而非营销 Hero。提炼自 WIRED 的版面规范；纯白与纯黑被调整为
  暖纸色和墨色，中文行高与字体回退由本库补齐。
cues: 新闻首页、科技杂志、每日简报、专题聚合、多栏目编辑页、需要快速扫读标题的内容流
avoid: 单一产品营销页、作品集、工具后台、复杂表单、内容不足三条的页面、沉浸式品牌叙事
surface: light
density: tight
register: story
family: editorial
tier: variant
status: beta

colors:
  canvas: "#F7F6F2"
  surface: "#FBFAF7"
  ink: "#171817"
  ink-muted: "#595B58"
  ink-faint: "#73766F"
  hairline: "#D9D8D2"
  primary: "#057DBC"
  primary-soft: "#E1EEF3"
  on-primary: "#FBFAF7"
typography:
  display:
    fontFamily: "Georgia, Noto Serif SC, Songti SC, serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -0.01em
  headline:
    fontFamily: "Georgia, Noto Serif SC, Songti SC, serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  body:
    fontFamily: "Inter, PingFang SC, Noto Sans SC, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.75
    letterSpacing: 0
  metadata:
    fontFamily: "Inter, PingFang SC, Noto Sans SC, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
rounded:
  none: 0px
  full: 999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  gutter: 24px
  xl: 32px
  section: 48px
  measure: 40em
components:
  story-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.headline}"
    rounded: "{rounded.none}"
    padding: 16px
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.metadata}"
    rounded: "{rounded.none}"
    padding: 12px 16px
  section-tag:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.metadata}"
    rounded: "{rounded.none}"
---

## Overview

给新闻、杂志、每日简报和多栏目内容聚合用。读者进入页面后要立刻比较多条故事，而不是先看一句品牌口号；如果只有三条内容，这个风格会显得空，应该换 `editorial-serif`。

核心约束是：首屏直接进入 12 列故事网格；1px 细线代替卡片阴影；衬线字体负责标题，无衬线负责作者、时间和栏目；唯一蓝色 `{colors.primary}` 只标记链接与栏目。版面靠标题长度、图片大小和栏宽形成节奏。

来源是 WIRED 的 DESIGN.md 二手分析。保留它的报纸网格、方角和三类文字角色，但去掉品牌专用字体、纯白纯黑和自动派生的 SaaS 组件。这是一套可复用的新闻版式，不是 WIRED 克隆。

**Key Characteristics**

- `{colors.canvas}` 暖纸底， `{colors.ink}` 近黑墨色；不大面积使用纯白或纯黑。
- 12 列网格，16px 故事内距，24px 栏间距，48px 大区分隔。
- 56px 主标题、28px 故事标题、12px 元信息，密度来自小元信息而非缩小正文。
- 所有故事卡方角、无投影，仅使用 `{colors.hairline}` 分隔。
- 栏目色只出现在栏目名和细线上，不涂满故事卡。

## Colors

- `{colors.canvas}` — #F7F6F2，主页面；降低长时间扫读的白底眩光。
- `{colors.surface}` — #FBFAF7，只用于订阅框或需要突出的编辑提示。
- `{colors.ink}` — #171817，标题和主按钮。
- `{colors.ink-muted}` — #595B58，摘要与正文。
- `{colors.ink-faint}` — #73766F，时间、阅读时长；关键事实仍用 muted。
- `{colors.hairline}` — #D9D8D2，分栏和故事分隔线。
- `{colors.primary}` — #057DBC，链接与栏目识别，不作大色块。
- `{colors.primary-soft}` — #E1EEF3，仅用于聚焦或选中背景。
- `{colors.on-primary}` — #FBFAF7，深色按钮上的字。

## Typography

标题只用 Georgia／Noto Serif SC 这一组衬线角色，正文与元信息使用 Inter／PingFang SC。展示标题 400，故事标题可用 700；元信息只用 500，不用全大写加宽字距制造“报纸感”。

字号固定为 12／14／16／20／28／56。中文标题不要套用英文 Didone 的极端粗细对比；用 Noto Serif SC 的 600／700 保持笔画完整。

## Layout

- 容器最大 1400px，12 列，24px 槽沟；首屏允许主故事占 7–8 列，次故事占 4–5 列。
- 同一组故事用 1px 横线或竖线分隔，不再为每条故事增加独立底色。
- 摘要最多 3 行，元信息独占一行；不要用中点把作者、时间、栏目串成一串。
- 768–1023px 改为 8 列；768px 以下单列，主故事仍排第一。
- 正文阅读页最大 `{spacing.measure}`，不要把首页的密度带进长文正文。

## Elevation & Depth

没有投影。Level 0 是纸面；Level 1 是 1px `{colors.hairline}`；Level 2 仅用于主操作或报头，使用 2px `{colors.ink}`。浮层不属于默认新闻版面，必要时另做规范。

## Shapes

按钮、输入框、图片、故事卡全部 `{rounded.none}`。`{rounded.full}` 只允许作者头像。禁止圆角新闻卡、pill 标签和软阴影。

## Components

### story-card

`{components.story-card}` 由栏目、标题、摘要、作者／时间和可选图片组成。图片比例按编辑重要性统一为 16:9 或 4:3，不在同一组里随机变化。

### button-primary

`{components.button-primary}` 是方角墨底按钮，只用于订阅或Newsletter主行动；普通“继续阅读”应是文本链接，不全部做成按钮。

### section-tag

`{components.section-tag}` 是有实际语义的栏目名，用蓝色文字或 2px 顶线，不做标题前的装饰性 eyebrow。

## Do's and Don'ts

### Do

- 用真实故事数量和编辑优先级决定跨列。
- 保持标题、摘要、元信息的角色稳定。
- 用细线和栏宽建立密度，不靠缩小正文。
- 给键盘焦点保留清晰的蓝色轮廓。

### Don't

- 不要把首页做成巨型营销 Hero 加三列功能卡。
- 不要给每条新闻使用不同底色或阴影。
- 不要把所有栏目标签改成全大写宽字距。
- 不要在内容很少时硬凑多栏。

## Chinese Typography

- 中文摘要与正文行高 1.75，元信息 1.5；首页摘要每行约 24–32 个汉字。
- 中文新闻标题不首行缩进，不用全角空格制造对齐。
- 中西文之间留四分之一空格；日期使用本地化完整格式。
- 使用全角标点并启用避头尾；标题避免两行只留一个字。
- 中文展示标题字距为 0，不沿用英文负字距。

## When to Use

**用**：新闻门户、科技杂志、行业日报、编辑精选、多栏目专题、信息中心。

**别用**：单品牌发布页、艺术作品集、设置页、工具控制台、长文沉浸阅读、数据监控大屏。

## Iteration Guide

1. 先用真实标题和摘要验证网格，再调整字体。
2. 密度不足时先减少无意义留白，不降低正文字号。
3. 层级不清时先调整跨列和标题档位，不增加新颜色。
4. 修改 `{components.story-card}` 后同时检查无图、长标题和中文元信息。

## Known Gaps

- 尚未定义实时快讯、股市行情和突发新闻的语义色与更新动效。
- 没有付费墙、评论区和复杂订阅流程组件。
- Georgia 与 Noto Serif SC 的灰度不同，中文主标题需要真实页面复核。
- 来源为二手 DESIGN.md，不是 WIRED 官方授权规范；品牌字体未随库分发。
