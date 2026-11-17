---
version: alpha
name: 夜色舞台
description: >-
  一盏灯，一圈黑。深度不来自投影，来自**离灯有多远**——四档底色就是四个距离。
  哑光：没有任何镜面高光，和 `tactile-3d` 正好站在对立面。
  三套光（阁楼暖金 / 地窖苔绿 / 教堂冷蓝）共用一套布局，换场景只换灯，不换家具。
colors:
  canvas: "#0B0A09"
  surface: "#15120E"
  surface-sunk: "#070606"
  surface-raised: "#1F1A14"
  surface-lit: "#33291D"
  ink: "#EFE6D5"
  ink-muted: "#A99A82"
  ink-faint: "#7A6C59"
  hairline: "#2B2419"
  hairline-strong: "#443826"
  primary: "#E8B76A"
  primary-soft: "#2A2114"
  primary-ink: "#1A1206"
  ember: "#E4572E"
  key-cellar: "#84C4A6"
  surface-lit-cellar: "#1B2A22"
  key-chapel: "#9DBCF5"
  surface-lit-chapel: "#212739"
# ---------------------------------------------------------------- 选择条件
family: expressive
tier: variant
sourceRefs: native
cues: 桌游/剧本杀的产品页与发行页、活动与票务、沉浸式叙事产品、需要悬念的落地页、夜间模式的展示型界面
avoid: 白天阅读的长文、后台与表单、数据密集型列表、需要平等比较多个选项的界面、打印
surface: dark
density: medium
register: story

typography:
  display:
    fontFamily: "'Songti SC', 'STSong', 'Noto Serif SC', serif"
    fontSize: 58px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: -0.01em
  headline:
    fontFamily: "'Songti SC', 'STSong', 'Noto Serif SC', serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.24
    letterSpacing: -0.01em
  title:
    fontFamily: "'Songti SC', 'STSong', 'Noto Serif SC', serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.32
    letterSpacing: 0
  lead:
    fontFamily: "'PingFang SC', 'Hiragino Sans GB', 'Noto Sans SC', sans-serif"
    fontSize: 21px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.01em
  body:
    fontFamily: "'PingFang SC', 'Hiragino Sans GB', 'Noto Sans SC', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.8
    letterSpacing: 0.01em
  label:
    fontFamily: "'PingFang SC', 'Hiragino Sans GB', 'Noto Sans SC', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.02em
  micro:
    fontFamily: "ui-monospace, 'SF Mono', Menlo, monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em

rounded:
  none: 0px
  sm: 2px
  md: 5px
  lg: 9px
  pill: 999px

spacing:
  base: 8px
  xxs: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  section: 56px
  measure: 34em

components:
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: 24px
  ticket:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: 16px
  marquee:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display}"
    rounded: "{rounded.none}"
    padding: 56px
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.primary-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
  tag:
    backgroundColor: "{colors.primary-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.pill}"
---

## Overview

给"要让人停下来、往里看"的地方用：桌游和剧本杀的产品页、活动与票务页、沉浸式叙事产品的落地页、夜间模式下的展示型界面。**它不承担高密度信息**——一屏说一件事，说完就该往下滚。

它的性格来自四个具体的选择：

1. **一盏灯。** 场景里只有一个光源，所有明暗都是"到它的距离"。这不是比喻：`{colors.surface-lit}` → `{colors.surface-raised}` → `{colors.surface}` → `{colors.surface-sunk}` 四档底色，就是四个距离，不是四个层级。做界面时先问"这个元素离灯多远"，而不是"它比谁重要"。
2. **全哑光。** 没有任何镜面高光，`specular` 恒为 0。这是与 `tactile-3d` 的分界线：那套的全部力气在"受光面"，这一套的全部力气在"没被照到的地方"。
3. **没有悬浮投影。** 一盏顶光下，桌面上的东西影子被压在正下方、几乎没有长度，肉眼读不到。所以这里的立体感来自**边缘内收的暗边**（1px `{colors.hairline}`）和四档亮度差，不来自 `box-shadow`。加投影反而错——它暗示了一个不存在的侧光。
4. **三套光，一套布局。** 阁楼暖金 `{colors.primary}`、地窖苔绿 `{colors.key-cellar}`、教堂冷蓝 `{colors.key-chapel}`。换场景只换两个变量（主光色 + 受光面），版式一点不动。

**Key Characteristics**

- 画布 `{colors.canvas}`（#0B0A09）——暖近黑，不是纯黑。纯黑让暗角无处可叠（暗角是往画布上再压一层黑，底已经黑了就没层次），而且暖黑与金色同色相，光晕边缘不发灰。
- 唯一彩色 `{colors.primary}`（#E8B76A）——**被钨丝灯照亮的白纸**的颜色，不是"奢华金"。#C9A227 那种饱和金是金属铬在反射，不是灯光在照射。
- `{colors.ember}`（#E4572E）只用一处：正在发生的事（剩余 3 席、本场即将开始）。它不参与装饰。
- 字号阶 11 / 13 / 16 / 21 / 30 / 42 / 58，比例约 **1.32**。
- **字体分工由字号决定，不由"标题/正文"决定**：≥30px 用宋体，≤21px 用黑体。因为宋体的横细竖粗在 21px 以下会断，黑体的均匀笔画在 42px 以上会呆。
- 圆角 2 / 5 / 9，比同类风格小一档：剧院的东西是纸、木、铜，边角是直的。
- 层级只靠三样：字号、亮度档、1px 描边。不靠投影、不靠色块、不靠图标。

## Colors

四档底色不是层级，是**到灯的距离**。整份文件最重要的一个概念。

**Surface（由近到远）**

- `{colors.surface-lit}` — #33291D。光锥正下方的那一块：主视觉卡片、票根正面、被强调的引文。一屏只用一次，用两次就没有"最亮"了。
- `{colors.surface-raised}` — #1F1A14。一级卡片、表单、列表行。
- `{colors.surface}` — #15120E。默认面板底色。大部分内容应该在这里。
- `{colors.surface-sunk}` — #070606。比画布更暗：凹槽、被压下去的东西、输入框内部。它比画布暗，是这个风格唯一一处"比背景还深"的层次。

**Ink**

- `{colors.ink}` — #EFE6D5，对画布 **15.97:1**。奶油白，不是纯白。纯白在暖黑上会发青，而且把金色的暖衬没了。
- `{colors.ink-muted}` — #A99A82，**7.19:1**。正文默认色。注意它本身就带暖调——中性灰在这个画布上会显脏。
- `{colors.ink-faint}` — #7A6C59，**3.88:1**。只给 ≤13px 的辅助文字、时间戳、编号。不要用它承载任何"读了会影响决定"的内容。

**Line**

- `{colors.hairline}` — #2B2419。唯一的分隔手段。1px，永远是 1px，不做 2px。
- `{colors.hairline-strong}` — #443826。用于"这里是一个边界"（票根撕口、面板外框），不用于装饰。

**Accent**

- `{colors.primary}` — #E8B76A，对画布 **10.75:1**，可以直接当链接和正文强调。
- `{colors.primary-ink}` — #1A1206，金底上的字 **10.07:1**。是暖黑（带一点褐），不用纯黑——纯黑在金底上像印刷错误。
- `{colors.primary-soft}` — #2A2114。金色的极暗版本，只做标签底和悬停底。
- `{colors.ember}` — #E4572E，对画布 **5.37:1**。只用于"正在发生"。

**Scene（三套光）**

- `{colors.key-cellar}` + `{colors.surface-lit-cellar}` — 地窖：苔绿主光，受光面偏冷绿。
- `{colors.key-chapel}` + `{colors.surface-lit-chapel}` — 教堂：冷蓝主光，受光面偏靛。
- 阁楼不是第三套，是默认值（`{colors.primary}` + `{colors.surface-lit}`）。

**只有两个变量变，其余全不动。** 这是硬约束：如果换场景需要改第三样东西（比如按钮颜色、描边颜色），说明这个场景不合适，删掉它，而不是加变量。

配套的一条分工：**被照到的东西跟着光变，动作不变。**

| 跟着 `--nc-key` 变 | 永远是 `{colors.primary}` |
|---|---|
| 标签文字、数据值、引文里的强调 | 按钮、链接、悬停描边 |

理由不是美学，是可用性：同一个「取票」按钮在地窖里变绿、在教堂里变蓝，用户会以为换了个功能。动作需要一个跨场景的固定身份。

## Typography

字号阶 11 / 13 / 16 / 21 / 30 / 42 / 58，比例 **1.32**。比工具界面（1.25）跳得明显，比展示型（1.4）收一点——因为这一套有正文，不是纯海报。

**分工不看"标题/正文"，看字号。** 这是这套排版唯一需要记住的规则：

| 字号 | 字体 | 为什么 |
|---|---|---|
| ≥30px（`{typography.title}` 及以上） | 宋体 | 横细竖粗的对比要够大才成立；30px 是它的下限 |
| ≤21px（`{typography.lead}` 及以下） | 黑体 | 宋体的细横在小字号会断墨，黑体的均匀笔画才清楚 |

所以会出现"30px 的宋体小节标题下面跟 21px 的黑体导语"——这不是混搭，是同一条规则的两端。

字重只有 **400 / 700** 两档。宋体没有真正的 600，用 700 顶替；黑体 600 在暗底上会糊（暗底的笔画周围有轻微渗色，等于给笔画又加了一圈）。

字距：宋体大标题 **−0.01em**（宋体字面本来偏松，收紧一点才有分量）；黑体正文 **+0.01em**（暗底上正字距能抵消渗色）；标签 **+0.02em**。全部不超过 ±0.03em——超过就不是排字，是在拉条。

行高：正文 **1.8**。比浅色界面（1.7）松，因为暗底的字符轮廓更模糊，行距要替它补一点呼吸。

## Layout

- 单栏 measure `{spacing.measure}`（34em）。这是"一屏说一件事"的物理约束。
- 纵向节奏 4 / 8 / 12 / 16 / 24 / 32 / 56。段间用 24，节间用 56。**节间不用分割线**，用亮度换挡。
- 双栏只在"主视觉 + 票根"这种组合里出现，比例 7:3。票根永远在右侧：阅读方向从左到右，票根是"结果"，不是"入口"。
- 舞台构图：主体偏离正中 **1/6–1/8**。正中的主体配一盏灯，读起来是证件照；偏一点，才有"被光照到的一侧"和"沉进暗处的另一侧"。
- 上下留白大于左右。`{spacing.section}` 是 56px，但首屏顶部的实际留白要在 96–120px。暗背景下边缘越空，越像舞台的台口。
- 内容宽度上限 1080px；再宽，暗角就没地方落了。

## Elevation & Depth

**这一节没有投影。** 写清楚"为什么没有"，比写一堆参数重要。

一盏顶光下，桌面上物体的影子被压在正下方、长度几乎为零，肉眼读不到。凡是"卡片下方有一片柔和阴影"的画面，光都来自侧上方——那是另一个场景。所以这里禁用 `box-shadow` 做层级。

取代它的三样：

**① 四档亮度差（主手段）**

`{colors.surface-sunk}` → `{colors.surface}` → `{colors.surface-raised}` → `{colors.surface-lit}`。相邻两档的亮度比约 1.4:1。低于 1.3 读不出层次，高于 1.6 会出现"打了聚光灯"的舞台感（只在 `{colors.surface-lit}` 这一档允许）。

**② 内收暗边**

1px `{colors.hairline}` 描边，外加一条 `inset 0 1px 0` 的极淡暖光（`rgba(232, 183, 106, 0.06)`）。这条内阴影是"上沿被光照到"的唯一线索——它比投影轻，但方向正确。

**③ 暗角（Vignette）**

`radial-gradient` 从 70% 处开始压暗，到边缘 `rgba(0, 0, 0, 0.62)`。这是整页的深度来源：它假装画框外面是黑的，于是内容有了"被一束光罩住"的边界感。

两种模式，默认是安全的那种：

| 模式 | 怎么写 | 用在哪 |
|---|---|---|
| 容器内（默认） | `position: absolute`，`inset: 0` | 一块 section、一张卡片、一个组件。不往视口外溢 |
| 整页镜头（可选） | 根容器再加 `.ds-nocturne-page` → `position: fixed` | 整页是一个舞台时 |

默认用 `absolute` 不是胆小，是因为**组件级别的 class 不该改动视口**：在预览页里 `fixed` 会把整页压黑，包括别人的风格。

整页模式下不能挂在会滚动的元素上——一滚就跟着内容跑，就不再是"镜头"了，而变成一张贴在画布上的暗角贴纸。

**为什么这一套能成立：** 几何投影说的是"东西有厚度"，光衰减说的是"东西有距离"。前者适合桌面上的小物件（`tactile-3d` 做的就是这个），后者适合一个房间。这套风格处理的是房间。

### 三处 Floor rule 破例（限定在本风格内）

| 规则 | 破例内容 | 为什么 |
|---|---|---|
| §11.2 S1 渐变 | 暗角、受光面的径向渐变 | 光有衰减，衰减就是渐变。**判据：跟着光源位置走、有明确的衰减半径、压暗而不是提亮 → 是光照；固定角度双色过渡、无半径 → 是装饰。** 这套只用前者，且只用于"变暗"。 |
| Floor rule 2 纯黑白 | `{colors.surface-sunk}` #070606 比画布更暗 | 不是纯黑；且"比背景更深"是这个风格唯一的凹陷语言，去掉它就没有"沉下去"这件事。 |
| §12 不用投影表达层级 | 全篇无 `box-shadow` | 不是省事，是物理正确：顶光下没有可读的投影。层级全部由亮度档承担。 |

三条都只在本风格的容器内生效，**不外溢到其他风格**。

## Shapes

- 圆角只有三档：`{rounded.sm}`（2px，票根、输入框）、`{rounded.md}`（5px，卡片）、`{rounded.lg}`（9px，主视觉面板）。`{rounded.none}` 用于整幅的舞台图和分隔带。
- `{rounded.pill}` 只给"状态"，不给按钮。胶囊形是消费电子的语言（软、可点、亲），而这里的按钮是印在纸上的字；状态用胶囊，是因为它本来就是个印章。
- **不许混用**：同一屏里出现 2px 和 9px 两种卡片，等于承认没有规矩。
- 描边永远 1px。要更重，换 `{colors.hairline-strong}`，不加粗——2px 在暗底上会显脏（亮边两侧的渗色让 2px 看起来像 2.5px）。

## Components

### card

`background` 是 `{colors.surface}` 平涂，**不是渐变**。加渐变就等于承认"有一束光打在卡片上"，而卡片离灯远近不同，光斑位置不该固定在卡片自身的坐标里。

结构：1px `{colors.hairline}` 外框 + `inset 0 1px 0 rgba(232, 183, 106, 0.06)` 上沿受光 + `{rounded.md}`。悬停时只做两件事：底色升一档（`{colors.surface}` → `{colors.surface-raised}`）、外框换 `{colors.hairline-strong}`。**不动位置、不放大**——这张卡是在桌上的，不是浮起来的。

### ticket（票根）

左侧一条 2px 竖向虚线（`repeating-linear-gradient`，8px 实 + 6px 空）作为撕口，`{colors.hairline-strong}` 色；底部一条 1px 实线当撕痕。右上角 `{typography.micro}` 的场次编号，等宽字体，`tabular-nums`。

虚线两侧各留 `{spacing.sm}`（12px）空白。少于 12px，虚线会贴在文字上，读起来像删除线。

### marquee（招牌）

`{typography.display}` 宋体，`{colors.ink}`，上下各一条 `{colors.hairline}` 横线（左右各缩进 8%）。下面一行 `{typography.micro}` 的 `{colors.ink-faint}` 说明。招牌只出现在首屏，而且**一屏只有一个**——它回答"这是什么地方"，不是"这张图叫什么"。

### button-primary

`{colors.primary}` 底 + `{colors.primary-ink}` 字，`{rounded.sm}`，无阴影。悬停时底色和文字都不变，只把外框换成 `1px solid {colors.primary}` 并向内收（`outline-offset: -1px`）——像被手指按住的那一下。按下时降到 `{colors.primary-soft}` 底 + `{colors.primary}` 字，**反色**：这是"按进去了"，不是"变亮了"。

### tag

`{colors.primary-soft}` 底 + `{colors.primary}` 字，`{rounded.pill}`，`{typography.micro}`。用途只有一个：标记场景或章节（"午夜场""第三幕"）。超过 6 个字就不是标签，是小标题。

### divider

`1px solid {colors.hairline}`，上下各 `{spacing.lg}`。**能用亮度换挡的地方就不要用它**——分割线是最后一个手段，不是第一个。

## Do's and Don'ts

**Do**

- 每次要强调，先问"它在不在光里"——能升一档底色就不要加第三个颜色。
- 一个视口里只允许一个 `{colors.surface-lit}`。
- `{colors.ember}` 只出现在"正在发生"上。出现第二次就说明有件事该删。
- 换场景时只改主光色和受光面，其余一律不动。
- 宋体和黑体的分界按字号执行：30px 起用宋体，21px 止用黑体。中间没有过渡带。
- 给 `prefers-reduced-motion` 把过渡时长降到 1ms，但保留底色变化——那是信息，不是动效。

**Don't**

- 不要加 `box-shadow` 做层级。它在这个光源下不成立：顶光没有可读的影子。
- 不要给卡片加渐变。渐变意味着卡片自己会发光，或者有一束光固定在卡片上。
- 不要在暗底上用中性灰。所有灰都必须带暖（`{colors.ink-muted}` 就是 #A99A82，不是 #999）。
- 不要用纯黑 #000 做"更深的黑"——`{colors.surface-sunk}` 是 #070606，纯黑会吃掉描边。
- 不要让亮色超过画面的 15%。这是"一盏灯"的物理比例，超了就变成"白天"。
- 不要在同一页混用两套光。地窖的绿和教堂的蓝放在一起，观众读到的是"配色失败"，不是"两个场景"。

## Chinese Typography

- **宋体只在 30px 以上用。** 宋体的横画细到 1px 以下时，暗底会把它的边缘吃掉，看起来像缺字。这是本库唯一一条"字体由字号合法化"的规则。
- 中文不设负字距。英文大标题的 −0.03em 在中文会挤到笔画粘连——汉字字面本来已经排满 92%，没有余量。
- 行高 1.8（比浅色界面的 1.7 松）。暗底字符轮廓模糊，需要更多纵向留白来分句。
- 中西文之间手动留 1/4 em 的间隙：`活动 Night Shift 开场`。不要用 `text-spacing` 之类的实验属性，浏览器支持不一致。
- 全角标点用全角，且不压缩。`，。？！` 后不加空格——中文标点自带右侧空隙。
- 避头尾：`line-break: strict`。禁则在暗底上尤其要守，因为一行的末尾会直接顶到暗角里去，读起来像被裁掉了。
- 不首行缩进。用 `{spacing.md}` 的段间距离分段。
- 中文可用字重只有 400 / 700。600 在暗底上会和 400 分不清（渗色让笔画变粗），等于白设一档。
- 引号用「」『』，不用直角以外的弯引号。在双语混排里直角引号的识别度更高，而且不依赖字体是否含中文弯引号。

## When to Use

**用**：

- 桌游、剧本杀、密室、演出、展览的产品页和票务页。
- 沉浸式叙事产品的落地页（第一屏要"进入"，不是"了解"）。
- 需要悬念和现场的展示型界面：一场发布会、一次开幕。
- 深夜场景下的品牌页——这套的默认亮度就是"晚上"。

**别用**：

- 白天要读的长文、白皮书、文档。暗底长文是折磨。
- 后台、表单、设置页。它们要的是"看得清"，不是"有氛围"。
- 数据密集的列表和表格。四档底色在密集排布下会变成噪声。
- 需要平等比较多个选项的界面。一盏灯的意思是"有一个最重要"，比较页需要的正好相反。
- 打印。暗角、光衰减、暗底全部失效。

## Iteration Guide

1. **先调主光色**（`--nc-key`），一次只动这一个。它决定整个页面的"时间"：更橙是黄昏，更白是月光，更绿是地下室。
2. **再调四档底色的间距**。相邻两档亮度比 1.4:1 是基准；读不出层次就往 1.5 走，觉得假就往 1.35 走。**四档要一起动，保持比值**——单独调一档会让"距离"变成"分层"。
3. **暗角只在 0.45–0.68 之间调**。低于 0.45 感觉不到画框，高于 0.68 边缘开始吃掉内容。
4. **要更强的主张，先换字号，再换亮度档，最后才加 `{colors.ember}`。** 顺序反了就会变成"到处都是重点"。
5. 改完跑 `python3 scripts/lint.py nocturne`，再截图。**暗色风格的对比度在代码里看不出来**——同一组数值在 OLED 屏和普通 IPS 上差很多。

## Known Gaps

- **只有深色。** 这一套的全部机制（暗角、光衰减、亮度档）都以"背景是黑的"为前提。做浅色版等于换一套物理模型，没做。
- **三套光只定义了两个变量。** 如果某个场景需要改描边色或按钮色，说明它超出了"换灯"的范围——目前没有第三、第四个变量的设计，也没有测试过。
- **宋体依赖系统字体。** `Songti SC` 只在 macOS / iOS 上有，Windows 会退到 `STSong`（装了 Office 才有），再退就是衬线 fallback。跨平台一致性没有验证过，引入 webfont 会让页面重 2–4 MB。
- **暗角在超宽屏上会变形。** `radial-gradient` 默认是椭圆，`aspect-ratio` 超过 2.4:1 时左右两侧压得比上下轻。要么接受，要么改用 `circle`，没有两全。
- **没有动效语言。** 除组件状态过渡（150ms），这个风格没有定义"东西怎么出现"。真正的舞台感需要入场编排（帘子、追光、错开的时间差），那是一个独立的话题。
- **`{colors.ember}` 只有一个色相。** 需要"警告 / 危险 / 成功"三种状态时不够用，而加三个颜色会破掉"一盏灯"。这类界面不该用这个风格。
