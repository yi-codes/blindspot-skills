---
version: alpha
name: Civic
description: >-
  公共服务的界面。纯白纸、近黑墨、一个黄色焦点环，零圆角零阴影。
  所有尺寸都是为"能被读完、能被填完、能被键盘操作完"服务的，
  没有一处是为了好看。正文 19px 而不是 16，标题行高可以低到 1.0。
# ---------------------------------------------------------------- 选择条件
cues: 政务/公共服务、表单密集的办事流程、需要无障碍合规、给不确定人群看的说明页、政策文件
avoid: 品牌营销、需要"高级感"的官网、创意作品集、需要视觉冲击的页面
surface: light
density: medium
register: professional

colors:
  canvas: "#FFFFFF"
  surface: "#F3F3F3"
  surface-hover: "#CECECE"
  ink: "#0B0C0C"
  ink-secondary: "#484949"
  ink-faint: "#858686"
  hairline: "#B1B4B6"
  hairline-strong: "#0B0C0C"
  link: "#1D70B8"
  link-visited: "#4C2C92"
  link-hover: "#003078"
  focus: "#FFDD00"
  error: "#CA3535"
  success: "#0F7A52"
  success-dark: "#083D29"
  on-accent: "#FFFFFF"

typography:
  headline-xl:
    fontFamily: "GDS Transport, Noto Sans SC, PingFang SC, arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.042
    letterSpacing: 0
  headline-lg:
    fontFamily: "GDS Transport, Noto Sans SC, PingFang SC, arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.111
    letterSpacing: 0
  headline-md:
    fontFamily: "GDS Transport, Noto Sans SC, PingFang SC, arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "GDS Transport, Noto Sans SC, PingFang SC, arial, sans-serif"
    fontSize: 19px
    fontWeight: 400
    lineHeight: 1.316
    letterSpacing: 0
  body-sm:
    fontFamily: "GDS Transport, Noto Sans SC, PingFang SC, arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  label-md:
    fontFamily: "GDS Transport, Noto Sans SC, PingFang SC, arial, sans-serif"
    fontSize: 19px
    fontWeight: 700
    lineHeight: 1.316
    letterSpacing: 0
  tag-md:
    fontFamily: "GDS Transport, Noto Sans SC, PingFang SC, arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 1px
  code-md:
    fontFamily: "ui-monospace, SF Mono, Menlo, monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0

rounded:
  none: 0

spacing:
  base: 5px
  xs: 5px
  sm: 10px
  md: 15px
  lg: 20px
  xl: 30px
  xxl: 40px
  section: 60px
  measure: 40em

components:
  section-rule:
    backgroundColor: "{colors.hairline-strong}"
    height: 4px
  button:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-accent}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 8px 10px 7px
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 8px 10px 7px
  field:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 5px 4px
  tag:
    backgroundColor: "{colors.link}"
    textColor: "{colors.on-accent}"
    typography: "{typography.tag-md}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  error-summary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: 20px
---

## Overview

Civic 不是"做得好看的政务网站"，是**GOV.UK Design System 的那套约束本身**：能被所有人读完、填完、用键盘操作完。

它的所有决定都可以追溯到同一个问题：**这个人现在很焦虑，我要让他一次办成。** 所以它拒绝圆角（会让边界不清楚），拒绝阴影（会让层级不清楚），拒绝灰色小字（会让信息读不到），拒绝把正文做小（19px 而不是 16px）。它甚至拒绝"品牌感"——你在这套界面里找不到任何一处为了好看而存在的东西。

这套风格在库里是特殊的：**它是我唯一一个几乎不用做判断的风格**。GOV.UK 把每个值都写在开源代码里，还写了为什么。我做的事情主要是搬运和翻译，不是设计。

**Key Characteristics**

- 纯白画布 `{colors.canvas}` + 近黑墨 `{colors.ink}`（#0B0C0C，不是 #000）。对比度 19.6:1，是全库最高的。
- **正文 19px** `{typography.body-md}`，不是 16。行高 1.316（25/19）。这是 GOV.UK 做过可用性测试后的结论：19px 在嘈杂环境、老花眼、小屏上都还能读。
- **标题行高可以低到 1.0**。80px 的主标题配 80px 的行高，48px 配 50px。这在网页排版里算激进，但它换来的是标题块的紧凑——政务页的标题经常是两三行。
- **零圆角** `{rounded.none}`，**零阴影**。整个系统没有一处例外。
- **黄焦点环** `{colors.focus}`（#FFDD00）。它不配白色文字（对比度只有 1.35:1），而是把文字变黑、再加一条黑色下投影。
- **线宽分级**：4px 分隔、5px 错误框、10px 提示条、2px 表单边框、1px 表格行线。这个分级不是装饰，是在说"这里有多重要"。
- 间距全部是 5 的倍数（5/10/15/20/25/30/40/50/60），不是常见的 4 或 8。因为基础字号是 19，5 的倍数才能和它对齐。

## Colors

一个黑、一个蓝、一个黄。三件，够用了。

### Canvas & Surface

- **Canvas** (`{colors.canvas}` — #FFFFFF): 页面底。**这是全库唯一的纯白画布**，理由见下面「对 Floor 规则 2 的豁免」。
- **Surface** (`{colors.surface}` — #F3F3F3): 区块底、次级区域的底。黑 tint-95。
- **Surface Hover** (`{colors.surface-hover}` — #CECECE): 次级按钮的悬停态。黑 tint-80。

### Ink

- **Ink** (`{colors.ink}` — #0B0C0C): 正文与标题。GOV.UK 的 black primary，比纯黑柔一点点。
- **Ink Secondary** (`{colors.ink-secondary}` — #484949): 辅助说明、提示文字。对白底 9.7:1。
- **Ink Faint** (`{colors.ink-faint}` — #858686): 最弱一级。对白底 3.9:1——**只给不需要读的字**（禁用态、时间戳），不给任何必须读的内容。

### Line

- **Hairline** (`{colors.hairline}` — #B1B4B6): **装饰性**分隔线。对白底只有 2.08:1，所以它不能承担"必须被看见的边界"这个职责——那是下面那条的工作。
- **Hairline Strong** (`{colors.hairline-strong}` — #0B0C0C): **必须被看见的边界**。表单框、表格表头、区块分隔全用它。这条规则不要混：谁需要用眼睛找到边界，谁就用黑的。

### Link

- **Link** (`{colors.link}` — #1D70B8): 未访问链接。5.17:1。蓝色不是选出来的，是测出来的——它要同时满足"不像正文"和"在白底上够清楚"。
- **Link Visited** (`{colors.link-visited}` — #4C2C92): 已访问。这个颜色在别的风格里几乎绝迹了，但政务场景里它很重要：**用户需要知道哪些步骤已经看过**。
- **Link Hover** (`{colors.link-hover}` — #003078): 悬停加深。

链接的**下划线在悬停时从 1px 变到 3px**。这是这套风格最有辨识度的微交互之一：它不靠变色，靠加粗来回应。因为变色对色觉障碍用户不可靠，加粗对所有人都可靠。

### Focus

- **Focus** (`{colors.focus}` — #FFDD00): 黄。**只做底，不做字。** 它配黑字是 14.55:1，配白字是 1.35:1。
- 焦点样式 = 黄色底 + 上方 -2px 黄、下方 4px 黑的双投影。黑色那条是必要的：在浅色区块上，只有黄色会"糊"进背景。

### 状态

- **Error** (`{colors.error}` — #CA3535): 5.16:1。
- **Success** (`{colors.success}` — #0F7A52): 主按钮底。5.35:1。
- **Success Dark** (`{colors.success-dark}` — #083D29): 按钮底部那 2px 的"厚度"，也是悬停态。

### 对 Floor 规则 2 的豁免（留痕）

`principles.md` 的 Floor 规则 2 说「浅色底不许大面积 #fff」。这个风格违反了，而且是故意的。

理由：**GOV.UK 的价值主张就是最大可读性**，纯白配近黑是这套系统里对比度最高的组合（19.59:1）。把它换成任何"更高级"的米白或冷灰，都是在用可读性换审美——而这套风格存在的前提就是不换。这不是"没想到"，是"想到了并且拒绝"。

这个豁免**只对 civic 生效**，不外溢到任何其他风格。

## Typography

**GDS Transport** 是 GOV.UK 的定制字体，商用授权。这里退到它自己在代码里声明的 fallback：`arial, sans-serif`。中文用系统黑体（PingFang SC / Noto Sans SC）。

字号阶是**八档，一档都不加**：80 / 48 / 36 / 27 / 24 / 19 / 16 / 14。这不是等比数列，是对着具体用途定的档：正文 19、表单标签 19、辅助 16、标签 14、小节标题 24、大节标题 36。

行高：主标题 80/80 = **1.0**。这不是笔误，是 GOV.UK 的做法——大字号的中文和拉丁都不需要额外行距，加了反而散。正文 25/19 = 1.316，比常见的 1.5 紧，因为 19px 的字本身已经够大，不需要靠行距撑开。

字重只有两档：400 和 700。**没有 500、没有 600。** 中间字重在系统字体上渲染不稳定，而 400/700 的对比足够建立层级。

## Layout

- 版心 `{spacing.measure}` 960px，沟槽 30px。这是 2012 年的桌面标准，GOV.UK 一直没改，因为它还在被大量低分辨率设备访问。
- 段落最大宽度 40em（约 19px × 40 = 760px）。超过就断开。
- 间距全部是 5 的倍数：5 / 10 / 15 / 20 / 25 / 30 / 40 / 50 / 60。
- **垂直节奏靠粗线，不靠留白。** 一个区块结束用 4px 黑线，不是靠 60px 的空白。

## Elevation & Depth

**没有层级。** 这个系统里没有"浮起来"的概念——没有弹层、没有阴影、没有 z 轴。

唯一的"深度"来自**线宽**：4 / 5 / 10 / 2 / 1 这五个值，用粗细表达重要程度，而不是用阴影表达远近。按钮底部那 2px `box-shadow: 0 2px 0` 是全系统唯一的"实体感"，按下时它消失、按钮下移 2px——这是模拟一个物理按键被按下去，不是做投影。

## Shapes

**零圆角。** 一个值，没有例外。

圆角在政务界面里是有害的：它让矩形边界的"起点和终点"变模糊，而表单、按钮、提示框的边界是这套界面里最重要的信息。所以它们是方的。

线宽分级（这是这套风格的"形状"）：

| 宽度 | 用途 |
|---|---|
| 1px | 表格行线、装饰性分隔 |
| 2px | 表单边框、按钮边框 |
| 3px | 焦点环 |
| 4px | 区块分隔（narrow rule） |
| 5px | 错误框、错误信息的左条（标准 rule） |
| 10px | 提示条、警告的左条（wide rule） |

## Components

### button

`{colors.success}` 底 + `{colors.on-accent}` 字 + 零圆角 + `0 2px 0 {colors.success-dark}` 的底边。悬停变深，按下时底边消失、整体下移 2px。

**按钮不用蓝色。** 蓝色是链接的颜色，绿色是动作的颜色。这是 GOV.UK 最反直觉的一个决定：全站的主按钮是绿的，不是蓝的。

### button-secondary

`{colors.surface}` 底 + `{colors.ink}` 字 + `0 2px 0 {colors.hairline}` 的底边。用于"返回""取消"这类不推进流程的动作。

### field

标签在输入框**上方**、19px、加粗；提示文字在标签和输入框之间、19px、次要色；输入框 2px 黑边、零圆角、内边距 5px 4px。

三个细节：

1. **标签不加 placeholder 替代。** 占位符会被输入内容覆盖，标签不会。GOV.UK 明确禁止用占位符当标签。
2. **提示在标签和框之间，不在框下面。** 因为提示是"填之前要读的"，不是"填错了才看的"。
3. **错误信息同时出现在三处**：页面顶部的错误摘要（5px 红框）、字段上方的错误信息（5px 红左条 + 加粗红字）、输入框的红色边框。三处都必须有，因为用户可能从任何一个位置进入。

### error-summary

5px 红框 + 20px 内边距，放在页面最顶部、`<h1>` 之前。里面是链接列表，每一条跳到对应的字段。

### tag

蓝底 + 白字 + 零圆角 + 全大写 + 1px 字距。用于状态标记（"已完成""草稿"）。全大写是 GOV.UK 的原样做法，但对中文无效——中文没有大小写。

### inset

左侧 10px 蓝边 + 15px 内边距，**无底色**。用于"需要在正文里强调的一段话"。它不填充背景，因为填充会让人以为它是一个独立模块。

### table

只有横线，没有竖线。表头下方 2px，行与行之间 1px。单元格上内边距 10px、右内边距 20px。

## Do's and Don'ts

### Do

- 正文 19px。觉得大是错觉——它在小屏、老花眼、嘈杂环境下才是对的。
- 所有必须被看见的边界用 `{colors.hairline-strong}` 的 2px 黑线。
- 链接靠**下划线加粗**回应悬停，不靠变色。
- 焦点用黄底 + 黑字 + 黑色下投影，三件一起。
- 错误写清楚"哪里错了、怎么改"，不要写"输入无效"。
- 一个页面只放一个主按钮。
- 表单标签放上方、加粗、19px，和输入框一样大。
- 所有间距走 5 的倍数。

### Don't

- 不要加圆角。一处都不要。
- 不要加阴影表达层级。系统里没有层级。
- 不要用蓝色做按钮。蓝色是链接。
- 不要把正文做小到 16 以下。16 是"辅助文字"档，不是正文档。
- 不要用 `{colors.hairline}` 画表单边框。它只有 2.08:1，看不见。
- 不要用占位符当标签。
- 不要用颜色单独传达状态（红/绿）。永远配文字。
- 不要做"左图右文"的营销版式。这不是营销页。
- 不要在错误态上加红底。红边 + 红字 + 红条已经三处强调了。

## Chinese Typography

- **19px 正文对中文是刚好**。中文字形满格，同样字号下视觉比拉丁大一点，19px 中文接近 18px 拉丁的观感。不要因为它"看着大"就降到 16。
- **行高 1.316 对中文偏紧，可以放宽到 1.5**。这是对 GOV.UK 原值的必要偏离：拉丁的 1.316 靠字内空间撑住了，中文撑不住。长段落尤其明显。
- **标签上方、加粗、和正文同字号**这条规则对中文尤其有效：中文标签短而密，加大加粗比缩小更容易扫到。
- **全大写对中文无效**：`text-transform: uppercase` 不会改变汉字，只会把混排的拉丁字母拉宽。中文标签不要设这个属性。
- **中西文之间留 1/4 空格**：`2026 年 11 月`、`用 PDF 提交`。
- **数字用等宽**：表单里的日期、金额、编号必须能对齐。
- **不要用「」以外的手写体或衬线**：政务界面里衬线字会被读成"文件"而不是"界面"。

## When to Use

**用**：政务服务、办事流程、申请表、政策与法规页面、需要无障碍合规（WCAG AA）的界面、面向不确定人群的说明页、任何"读完才能办成"的场景。

**别用**：品牌营销页、需要"高级感"的官网、创意作品集、需要视觉冲击的落地页、密集数据看板（它的密度对数据来说太松）。

## Iteration Guide

1. 加任何东西之前先问：GOV.UK 有没有这个组件？有就照抄，没有就先怀疑自己。
2. 颜色只有六个能用：黑、近黑、灰、蓝、黄、红。绿色只给主按钮。
3. 线宽只有 1 / 2 / 3 / 4 / 5 / 10 六个值。不要发明 6、8。
4. 需要强调时：先加粗，再加线宽，最后才考虑颜色。
5. 每个新组件都要过一遍键盘：Tab 能不能到、焦点看不看得见、Enter 能不能触发。

## Known Gaps

- **GDS Transport 拿不到。** 现在退到 arial，观感会差一截（GDS Transport 是专门为屏幕小字号调的）。自托管一个近似字体是唯一的解法。
- 没有定义 cookie banner、通知 banner、选项卡（tabs）、步骤指示器（task list）。这些 GOV.UK 都有，但要么用得少，要么实现复杂，暂未搬。
- 没有定义移动端断点。GOV.UK 的响应式字号在 640px 以下会掉两档（48→32、36→27），本文件只写了 tablet 以上。
- 深色模式不存在。GOV.UK 没有深色主题，硬做会破坏对比度基线。
- 全大写的 tag 对中文无效，中文场景需要另定一套标签样式。
- 生图侧说明在 `prompt.md`——但这套风格几乎不该配图，配图会削弱"这是官方信息"的权威感。
