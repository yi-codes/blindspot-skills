---
version: alpha
name: Blueprint｜工程蓝图
description: >-
  把氰版晒图的工程图纸语法搬进网页：蓝晒蓝 #0B3D91 底上铺 20px 白线网格，
  1px 图纸白线框把区块连成一张图，尺寸虚线、十字准星和 FIG. 编号说明每块是什么，
  标注黄 #FFD36A 只给关键数字与主行动。用于建筑/硬件项目页、技术发布会、开发者活动
  和需要「先给结构，再给细节」的规格展示页。参数取自 liuyutao 风格词典的显式色板与提示词、
  StyleKit 工程蓝图卡的 CSS 变量与组件规格、Blueprint / Wireframe UI 的边缘与连接规则；
  标为 beta/variant。为符合本库 The Floor，把来源 13px 正文提到 18px/1.7、
  字重收进 400/700 两档，并弃用黑底、紫标与暖橙高亮。
cues: 建筑与硬件项目页、开发者大会与黑客松活动页、众筹产品结构展示专题、技术方案与规格说明页、需要展示「未建成图纸」感的作品集
avoid: 温馨消费品牌主站、长篇散文与小说阅读、需要柔和亲和插画的消费 App、无障碍要求下的长表单默认皮、金融医疗政务等需要权威稳重的页面、打印为主的单栏文档
surface: dark
density: medium
register: technical
family: developer
tier: variant
sourceRefs: blueprint
status: beta

colors:
  canvas: "#0B3D91"
  surface: "#0E4AA8"
  surface-alt: "#092F73"
  ink: "#E8F1FF"
  ink-muted: "#9EC1FF"
  ink-faint: "#8BB8F5"
  hairline: "rgba(232, 241, 255, 0.30)"
  line: "#E8F1FF"
  primary: "#FFD36A"
  on-primary: "#0B3D91"
typography:
  display:
    fontFamily: "JetBrains Mono, Space Mono, ui-monospace, SFMono-Regular, Menlo, Consolas, PingFang SC, Microsoft YaHei, monospace"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0.08em
  headline:
    fontFamily: "JetBrains Mono, Space Mono, ui-monospace, SFMono-Regular, Menlo, Consolas, PingFang SC, Microsoft YaHei, monospace"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.08em
  cardTitle:
    fontFamily: "JetBrains Mono, Space Mono, ui-monospace, SFMono-Regular, Menlo, Consolas, PingFang SC, Microsoft YaHei, monospace"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.04em
  body:
    fontFamily: "JetBrains Mono, Space Mono, ui-monospace, SFMono-Regular, Menlo, Consolas, PingFang SC, Microsoft YaHei, monospace"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: 0
  label:
    fontFamily: "JetBrains Mono, Space Mono, ui-monospace, SFMono-Regular, Menlo, Consolas, PingFang SC, Microsoft YaHei, monospace"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.16em
rounded:
  card: 0px
  tag: 0px
  button: 0px
spacing:
  base: 4px
  xs: 8px
  sm: 12px
  md: 24px
  lg: 32px
  xl: 48px
  section: 96px
  measure: 34em
  grid: 20px
components:
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: 24px
    border: "1px solid {colors.hairline}"
  button-primary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.label}"
    rounded: "{rounded.button}"
    padding: "12px 24px"
    border: "1px solid {colors.primary}"
  tag:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.tag}"
    padding: "8px 12px"
elevation:
  lightSource: top-left
  steps: 2
  e1: "none —— 图纸是平的，贴面不投影"
  e2: "0 0 0 1px rgba(232, 241, 255, 0.30) —— 卡片与区块的 1px 线框"
  e3: "0 0 0 1px rgba(232, 241, 255, 0.60) —— 选中与展开态把线框提亮一档"
  topHighlight: "none —— 没有玻璃高光，层级靠线框亮度和底色明度差"
  borderLight: "{colors.hairline}"
  borderDark: "{colors.line}"
  separator: border
media:
  logoType: wordmark
  logoRule: "字标用 {typography.headline} 的等宽字形，右侧留 0.5em；只写排字规则，不搬任何真实建筑事务所、硬件品牌或地铁系统的标识"
  imageRadius: "{rounded.card}"
  imageRatio: "4:3"
  imageTreatment: "只收剖面图、平面图、爆炸图与流程图；图纸线稿取 {colors.ink} 描边、透明底，叠 8% 网格；彩色照片一律先去色再转线稿，不用景深"
  background: "{colors.canvas} 实色底 + 20px 间距的 rgba(232, 241, 255, 0.12) 双向白线网格 + 一处细十字准星；网格 pointer-events: none，不压正文"
  iconRule: "1px 描边方角图标，20px 基准，颜色取 {colors.ink-muted}；不引入圆点、渐变图标与拟物符号"
  emptyState: "{colors.surface-alt} 底 + 1px 虚线框 + 一行 {colors.ink-muted} 说明，写清缺失的尺寸或数据，不放插画"
motion:
  easing: linear
  durationFast: 75ms
  durationBase: 120ms
  hover: "线框从 30% 白提到 60% 白，卡片填充不变；按钮由透明翻成 {colors.primary} 实色，文字翻成 {colors.on-primary}，不位移"
  focusRing: "2px solid {colors.primary}，offset 2px；在蓝底与面板蓝上都可见"
  openTransition: "展开区块只变虚线框与 1px 亮边，120ms linear；不缩放、不淡入整块内容"
  reducedMotion: "所有过渡降到 1ms；线框、网格与编号保留静态终态，信息零丢失"
  dragUsesSpring: false
---

## Overview

工程蓝图给建筑事务所、硬件与制造项目、开发者大会、众筹结构展示，以及任何需要先理解结构再理解文案的规格页用。它要确认的不是「这件事打动人」，而是「这一块是什么、它和相邻那块怎么连接、关键尺寸是多少」。

性格来自五个可指认的选择。画布 `{colors.canvas}`（#0B3D91）是蓝晒纸的蓝，不是数据大屏的黑底青光；20px 网格用 `rgba(232, 241, 255, 0.12)` 画出坐标感；所有区块用 `{colors.hairline}` 的 1px 线框连成同一张图，不用浮动卡片与间隙；`{colors.primary}`（#FFD36A）只落在尺寸注记、编号与主行动；字族全站等宽，让每个字都像图纸上的标注。实测对比：图纸白对蓝底 8.83:1、浅蓝 5.51:1、标注黄 7.07:1，均过 WCAG AA。

读者先看到网格和线框组成的图面，再沿 `FIG. 01` 编号定位段落，最后才读到正文与按钮。动效也服从制图语言：120ms linear 的线框提亮、无位移、无弹性。把网格换成霓虹发光、把线框换成阴影浮卡、把标注黄铺成大色块，风格立刻垮成普通科技落地页。

它和库内其他深色/技术风格的分工：`terminal-mono` 是黑底绿字逐行执行命令，`signal-console` 是运营态的告警时间线，`developer-docs` 是并列阅读的文档；本风格用**图纸坐标、连接线框与尺寸标注**表达结构，主体是一张还没施工的图。

**Key Characteristics**

- 蓝晒蓝画布 `{colors.canvas}`（#0B3D91）+ 20px 白线网格：来源词典的显式色值与提示词，网格用低透明白线，不用发光点阵。
- 唯一强调色 `{colors.primary}`（#FFD36A）：只给尺寸注记与关键数字，来源词典「标注黄不要大面积铺底，只做点缀数字」。
- 1px 线框与虚线辅助线：StyleKit 的 `1px 白 30%` 描边与 `dash 4px / gap 4px` 虚线，区块相连而非悬浮。
- 全站等宽字体，两档字重 400/700：来源要求「字体必须是等宽以维持制图感」，本库把 13px 正文提到 18px/1.7。
- 0px 圆角、零投影：来源「所有元素都是锐利边缘」「the drawing is flat」，层级靠线框亮度与底色明度差。
- 编号与尺寸标注：`FIG. 01`、`01/02/03`、`max-width: 1120px` 写在边框上或边框之间，是信息不是装饰。

## Colors

**Canvas & Surface**

- `{colors.canvas}` — #0B3D91，页面底。来源词典 `--ds-bg` 显式值，蓝晒工艺的蓝；对图纸白 8.83:1，不是纯黑也不是深夜蓝。
- `{colors.surface}` — #0E4AA8，卡片、代码框与图块面板。来源词典 `--ds-surface` 显式值，比画布亮一档；图纸白在其上 7.20:1。
- `{colors.surface-alt}` — #092F73，空态、次级面板与注记背景。由画布加深得到的推断值（来源未给第三层蓝），图纸白在其上 11.08:1，不引入第四色相。

**Ink**

- `{colors.ink}` — #E8F1FF，正文与主线条。来源词典 `--ds-text` / `--ds-line` 显式值，「正文用近白 #E8F1FF」；不是 #FFFFFF。
- `{colors.ink-muted}` — #9EC1FF，次要说明与图例线。来源词典 `--ds-muted` 显式值，对画布 5.51:1、对面板 4.50:1，是能承担正文的第二档。
- `{colors.ink-faint}` — #8BB8F5，编号与尺寸文本。由浅蓝线调亮一档的推断值，对画布 4.91:1、对面板 4.01:1，不再往下调。

**Line & Accent**

- `{colors.line}` — #E8F1FF，1px 主实线、十字准星与焦点外框的底色；与 `{colors.ink}` 同值，来源把线框和文字都定义为图纸白。
- `{colors.hairline}` — rgba(232, 241, 255, 0.30)，默认 1px 线框。StyleKit 显式给出 `1px rgba(255,255,255,0.30)`，本库把白换成图纸白以免出现裸纯白。
- `{colors.primary}` — #FFD36A，标注黄，只给尺寸数字、编号与主按钮。来源词典 `--ds-annotate` 显式值，对画布 7.07:1，限定面积就能既是信号又不抢图面。
- `{colors.on-primary}` — #0B3D91，标注黄底上的字，与画布同值，对 `{colors.primary}` 7.07:1；来源「主按钮可白底蓝字」被改成黄底蓝字，保留同一明度关系。

不设 `secondary` / `revision` 色。StyleKit 的 Mid Blue #4A90D9（对画布仅 3.01:1）、Callout Orange #FF6B35（3.54:1）与 Revision Violet #b071e4 全部弃用，详见 NOTES「弃」与 `Known Gaps`。

## Typography

字号五档：display 56px、headline 32px、cardTitle 24px、body 18px、label 14px。相邻比值为 1.75、1.33、1.33、1.29，全部不低于 1.25；不设 11/13/16/22px 这些来源档位。来源词典给 24–28px 标题与 13px 正文、StyleKit 给 32/22/16/13/11/10px 字阶；本库以 StyleKit 的 32px 作 headline，并把正文提高到中文可读的 18px/1.7，26px 以上只留给 display 的 56px。

字重只用两档：700 给 display / headline / cardTitle / label，400 给 body。来源 StyleKit 也只列 400 与 700，本库不引入 500/600。字族全站等宽：JetBrains Mono → Space Mono → ui-monospace → SFMono-Regular → Menlo → Consolas，中文回退 PingFang SC / Microsoft YaHei；拉丁字距 0.08em（label 0.16em）来自 StyleKit，中文归零以免把小字拉散。

全大写是图纸标签的原生语法，只出现在 `FIG. 01` 一类功能性标签上；正文一律正常句式，来源词典也提醒「等宽全大写长句难读」。

## Layout

- 页面最大宽 1280px、容器内边距 16px、图块间距 12px，来自 StyleKit 的显式布局值；本库把图块内边距提到 24px，以容纳 18px 中文正文。
- 背景网格间距 `{spacing.grid}` 20px，来自来源词典提示词「20px 间距 rgba(232,241,255,0.12) 白线网格」；网格铺满 `.preview-root`，`pointer-events: none`，不参与阅读顺序。
- 区块共享 1px 左右边框，相邻区块上下用虚线分隔，形成一条连续的图面；卡片网格 `gap: 0`，用共用边框代替浮动间距，来自 Blueprint / Wireframe UI 的「Connected sections / no floating cards with gaps」。
- 每页 1–2 条尺寸标注：虚线 + `{typography.label}` 文本，放在区块之间；十字准星只出现在图面角落，面积不超过视口 1%。
- 区块间距 `{spacing.section}` 96px（由 StyleKit 的 48px section gap 加倍得到，给中文标题留呼吸），正文最大宽 `{spacing.measure}` 34em。
- 768px 以下保留 20px 网格与 1px 竖线，卡片折成单列并把共享边框改为上下相邻；不产生横向溢出。
- 主分隔手段只有 `border`：1px 实线给区块，虚线给辅助关系；投影和底色差都不是分隔器。

## Elevation & Depth

图纸是平的，不设投影阶梯：`{elevation.e1}` 为 none，卡片贴面不抬起；`{elevation.e2}` 与 `{elevation.e3}` 是 `0 0 0 1px` 的线框提亮，分别给默认边界与选中/展开边界。两者模糊半径均为 0，避免深色底上的发光阴影（slop S7）。

层级靠三件事表达：底色从 `{colors.canvas}` → `{colors.surface}` → `{colors.surface-alt}` 的明度差，线框从 30% 白到 60% 白的亮度差，以及字号落差。`{elevation.topHighlight}` 明确为 none——没有玻璃高光，光源 `{elevation.lightSource}` 只用于统一说明「线框上边缘略亮于下边缘」的方向感，不画真实光照。

StyleKit 给「Card focus: 0 0 0 1px rgba(255,255,255,0.30)」；本库把纯白换成图纸白并扩展到三档线框用途，没有新增模糊。

## Shapes

卡片 `{rounded.card}`、标签 `{rounded.tag}`、按钮 `{rounded.button}` 全部 0px。来源三条硬规则一致：「不要用圆润柔和元素」「Never use rounded-* classes」「cards / buttons / inputs radius 0」。圆点、胶囊、有机曲线、圆角图标一律不进内容与组件层；十字准星用两条 1px 直条交叉，方角装饰只取矩形与 45° 引出线。

辅助虚线的 dash 4px / gap 4px 是 StyleKit 显式值，只用于「这条线与那个对象有关」；把虚线当分隔纹理或背景图案会破功。

## Material & Elevation

材质是氰版晒图纸：蓝底、白线、低透明白网格，没有景深、没有玻璃、没有渐变填充。StyleKit 写「the drawing is flat」并禁止渐变填充，本库照收；网格用两层 `linear-gradient` 画硬边白线，属于制图工具而非氛围光。

四级表面只有蓝晒蓝 #0B3D91 → 面板蓝 #0E4AA8 → 深蓝 #092F73 三档明度加图纸白线与标注黄；光源从左上统一，表现方式是上边框 60% 白、其余边 30% 白，而不是加投影。主分隔手段只有 `border`；任何一处出现居中发光、软影、紫蓝渐变或暖色画布，就不再是蓝图。

## Mark & Media

标识：`{media.logoRule}`（`{media.logoType}`）；不搬建筑事务所招牌、硬件品牌字标与任何城市地铁系统的线路标识。图片：比例 `{media.imageRatio}`、圆角 `{media.imageRadius}`、处理 `{media.imageTreatment}`；只接受线稿化的技术图，删除测试里若一张图删掉后读者仍能理解尺寸或连接关系，就把它删掉。背景：`{media.background}`。图标：`{media.iconRule}`。空态：`{media.emptyState}`。

网格与十字准星都是静止帧，未加载任何素材时仍可完成阅读；`prefers-reduced-motion` 只停过渡，不隐藏标注。文字、按钮、表格数据一律真实 HTML/CSS 排版，不让生图模型画字。

## Motion & States

过渡曲线是 `{motion.easing}` linear，快档 `{motion.durationFast}` 75ms、基准 `{motion.durationBase}` 120ms；StyleKit 的按钮规格明确写 120ms linear，本库不引入 ease-in-out 与弹簧。hover：`{motion.hover}` 只提亮线框，主按钮从透明翻成标注黄实色、文字翻蓝，元素不位移；焦点：`{motion.focusRing}`，2px 黄环在蓝底 7.07:1，offset 2px 不会被 1px 线框吞掉。展开：`{motion.openTransition}`。

交互组件逐项覆盖六态：default 为透明底、30% 白线框与图纸白字；hover 把线框提到 60% 白；focus-visible 加黄色外环；active 主按钮变成 `{colors.on-primary}` 底、`{colors.primary}` 字，线框保持黄；disabled 用 `{colors.surface-alt}` 底、`{colors.ink-faint}` 字、虚线框，不靠变淡的黄；error 用 1px `{colors.primary}` 虚线框加一行 `{colors.ink}` 说明，不新增警示色。组合框另有 open 态：虚线框保持、亮边停在终态。

`prefers-reduced-motion` 时执行 `{motion.reducedMotion}`：过渡降到 1ms，线框与网格保留静态终态。本风格没有拖拽/手势组件，`motion.dragUsesSpring` 为 false。

## Components

### card

`{components.card}` 是 `{colors.surface}` 底、1px `{colors.hairline}` 线框、0px 圆角的图块，内边距 `{spacing.md}` 24px。左上角放 `FIG. 01` 一类等宽编号，右上角放尺寸注记；相邻卡片共用边框，`gap: 0`，不浮起来。hover 只把线框提到 60% 白，不放大字号、不位移。

### button-primary

`{components.button-primary}` 是透明底、1px `{colors.primary}` 线框、标注黄字的直角按钮，padding `12px 24px`，承担一屏唯一主行动。来源词典「按钮线框白边透明底；主按钮可白底蓝字」被改成黄边黄字、按下黄底蓝字，以符合本库单一强调色；hover 时线框与文字同步提亮，不改尺寸。

### tag

`{components.tag}` 用 `{colors.surface-alt}` 底、`{colors.ink-muted}` 字、0px 圆角、1px 虚线框，padding `8px 12px`（StyleKit 来源写 `6px 12px`，本库把 6px 收进 8px token 阶），只标注事实与编号。它不放在标题前当装饰序言；中文标签把 0.16em 字距归零。

## Do's and Don'ts

### Do

- 蓝晒蓝底上铺 20px 低透明白线网格，图面角落留一处细十字准星。
- 区块共享 1px 线框、卡片网格零间隙，每页给 1–2 条虚线尺寸标注。
- 标注黄只落在关键数字、编号与主按钮，面积控制在图面 5% 以内。
- 全站等宽、两档字重，正文 18px/1.7，中文标签字距归零。
- 层级靠底色明度差与线框亮度差，圆角恒为 0、投影恒为 none。

### Don't

- 不要用 #0A0A0A 一类黑底、#FFFFFF 一类纯白画布或暖色背景——前者触犯本库 The Floor 第 2 条，后两者被两份来源直接禁止。
- 不要用 Mid Blue #4A90D9、Callout Orange #FF6B35、Revision Violet #b071e4 扩色板；对蓝底对比不足且会消解单一标注黄。
- 不要用发光霓虹、渐变填充、玻璃模糊、软阴影和圆角——来源逐条点名禁止，也会把晒图纸变成科幻 HUD。
- 不要让辅助虚线变装饰、不要让标注黄铺底、不要把等宽全大写用成长句正文；来源明确「等宽全大写长句难读」。
- 不要把任何城市的地铁线路图、真实建筑事务所标识或硬件品牌图纸当素材搬进来；只迁移可复现的图纸语法。
- 不要拿它做长篇阅读、柔和消费主站、无障碍长表单默认皮与金融医疗政务页面——蓝底白线和图纸编号会持续暗示「未完成」。

## Chinese Typography

- 中文正文行高不低于 1.7（18px × 1.7），标签 14px/1.4 也不低于 1.5。
- 中西文之间留四分之一个空格：`20px 网格`、`用 JetBrains Mono`。
- 中文标签的 0.16em 正字距归零；display/headline 的 0.08em 在纯中文标题上减半到 0.04em，避免出现字间裂缝。
- 使用全角标点，段落不首行缩进，启用避头尾；标题不用引号包整句。
- 中文字重只有 400/700 两档可靠，本风格正文取 400、标题与标签取 700；合成字重可能在低端 Android 上变粗，需真机复核。
- 等宽字体在中文字体缺位时会回退到系统黑体，宽度不再严格等宽；本库只把「标注感」写进规则，不承诺中文字符的等宽网格。
- 56px display 只给拉丁短词与数字；中文标题降到 `{typography.headline}` 32px，仍保留 0.04em 字距与 1px 下边框。

## When to Use

**用**：建筑与硬件项目页、开发者大会与黑客松活动页、众筹产品结构展示专题、技术方案与规格说明页、需要展示「未建成图纸」感的作品集。

**别用**：温馨消费品牌主站、长篇散文与小说阅读、需要柔和亲和插画的消费 App、无障碍要求下的长表单默认皮、金融医疗政务等需要权威稳重的页面、打印为主的单栏文档。

## Iteration Guide

1. 一次只改一个组件，用 `{components.card}` 指代它；不要同时动网格、字阶与标注黄。
2. 所有值走 token，不写裸 hex；想加第二种强调色前，先确认标注黄是不是被误用成了装饰。
3. 想加强风格时先把 20px 网格、1px 线框和虚线标注调准，最后才考虑加图元——加色会直接破功。
4. 新增装饰前先跑删除测试：删掉它读者会不会失去坐标或连接关系；不会就删掉。
5. 改完必须重跑 `designlib check` 并重新截图；网格密度与标注黄面积只能靠真实渲染判断。

## Known Gaps

- 三份来源的蓝互相冲突：词典是 #0B3D91 / #0E4AA8，StyleKit 是 #1E3A5F，Blueprint / Wireframe UI 是 #0A0A0A。以给出完整色板与提示词的词典为准，黑底版本触犯本库 The Floor，记在 NOTES「弃」。
- StyleKit 的「描图纸 60% 蓝 + 12px 模糊」被弃用：模糊会把制图线稿变成玻璃拟物，与来源自己的「纯色填充、禁止渐变填充」冲突；本库用实色 `#0E4AA8` 面板。
- StyleKit 的网格是 8px/80px 双层、词典是 20px 单层；两者都写进 NOTES 的冲突栏，本库取 20px，因为词典的提示词直接给出了 rgba 透明度与用途。
- 来源字阶最小 10px、正文 13px；本库把正文提到 18px/1.7、标签 14px，5 档字阶是本库重排的结果，不是来源原值。
- 等宽字体不含中文；中文回退后不再等宽，56px 拉丁 display 换到中文标题必须降到 32px。
- 来源没有给出输入框、下拉、弹窗、加载态与错误态的规格；`Motion & States` 里的 disabled / error / open 三态是按本库六态要求推断的，不是来源显式值。
- 十字准星与尺寸标注只做了静态实现；真实工程图里的比例、单位与公差标注未建模，不能当作施工图使用。
