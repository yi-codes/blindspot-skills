---
version: alpha
name: Art Nouveau｜新艺术曲线
description: >-
  把 1890–1910 年新艺术运动的海报语法搬进网页：奶油纸底上的鞭状曲线、拱形画框、
  1px 烫金描边与高对比衬线标题，深绿负责正文和主行动，酒红只留在印章级强调。
  显式参数取自 StyleKit 新艺术风格卡（色板、Playfair Display 字阶、32/999/48px 圆角、
  500–700ms ease-in-out、组件与禁令）、aesthetic.fyi 的 Mucha 海报四色与
  60% 40% 55% 45% 不对称圆角、风格谱的 70/25/5 面积比与「非对称垂直延展 + 整体装饰框架」、
  以及 StyleUI Liberty 的金色焦点与展开态；标为 beta/variant。
  为符合本库 The Floor，把来源 16px 正文提到 20px/1.8、字重收进 400/700 两档，
  弃用紫藤色、亮绿与霓虹饱和色，阴影只保留来源里带偏移的柔影。
cues: 美术馆与画廊展览页、精品酒店与珠宝腕表品牌页、剧院演出与婚礼请柬、插画师作品集与主视觉、需要手工装饰感的品牌发布页
avoid: 开发者工具与技术文档、数据看板与密集表格、高频交易与监控台、移动优先的工具型 App、快速新闻流、无障碍优先的长表单默认皮、打印为主的单栏正文
surface: light
density: medium
register: story
family: expressive
tier: variant
sourceRefs: art-nouveau
status: beta

colors:
  canvas: "#F5EFE0"
  surface: "#FAF7EF"
  surface-alt: "#2D5016"
  ink: "#2D5016"
  ink-muted: "#3F6B35"
  ink-faint: "#6B7B3C"
  leaf: "#4A7C3F"
  hairline: "rgba(201, 162, 39, 0.35)"
  line: "#C9A227"
  primary: "#2D5016"
  on-primary: "#F5EFE0"
  accent: "#8B2252"
typography:
  display:
    fontFamily: "Playfair Display, Georgia, Songti SC, Noto Serif CJK SC, STSong, serif"
    fontSize: 60px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0.01em
  heading-lg:
    fontFamily: "Playfair Display, Georgia, Songti SC, Noto Serif CJK SC, STSong, serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0.01em
  heading:
    fontFamily: "Playfair Display, Georgia, Songti SC, Noto Serif CJK SC, STSong, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  subheading:
    fontFamily: "Playfair Display, Georgia, Songti SC, Noto Serif CJK SC, STSong, serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  body:
    fontFamily: "Playfair Display, Georgia, Songti SC, Noto Serif CJK SC, STSong, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.8
    letterSpacing: 0
  label:
    fontFamily: "Playfair Display, Georgia, Songti SC, Noto Serif CJK SC, STSong, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.12em
rounded:
  card: 32px
  button: 999px
  tag: 999px
  frame: 48px
  image: 8px
  whiplash: "60% 40% 55% 45%"
spacing:
  base: 8px
  xs: 16px
  sm: 24px
  md: 36px
  lg: 48px
  xl: 64px
  section: 128px
  measure: 34em
  wave: 120px
  ornament: 32px
components:
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: 36px
    border: "1px solid {colors.hairline}"
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.button}"
    padding: "16px 32px"
    border: "1px solid {colors.line}"
  tag:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.accent}"
    typography: "{typography.label}"
    rounded: "{rounded.tag}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
elevation:
  lightSource: top-left
  steps: 3
  e1: "0 4px 15px rgba(45, 80, 22, 0.20) —— StyleKit 卡片的显式柔影"
  e2: "0 8px 25px rgba(201, 162, 39, 0.40) —— 来源 hover 的金影"
  e3: "0 12px 32px rgba(45, 80, 22, 0.28) —— 本库推断的浮层，只给展开面板"
  topHighlight: "inset 0 1px 0 rgba(201, 162, 39, 0.35) —— 拱框上沿的金线"
  borderLight: "{colors.hairline}"
  borderDark: "{colors.line}"
  separator: border
media:
  logoType: wordmark
  logoRule: "字标用 {typography.heading} 的衬线斜体，右侧留 0.5em；只写排字规则，不搬 Mucha 原作、巴黎车站海报或任何真实品牌字标"
  imageRadius: "{rounded.image}"
  imageRatio: "3:4"
  imageTreatment: "只收植物形态、拱窗与平涂海报式插画；剪影取 {colors.leaf} 与 {colors.ink}，金线 {colors.line} 勾边；照片先去色再叠 12% {colors.canvas} 正片叠底，不用景深"
  background: "{colors.canvas} 实色纸底；外层拱形金框 inset 16px、上两角 999px 下两角 8px，左上角一处鞭状曲线伪元素；无纹理无渐变"
  iconRule: "1px 描边藤蔓与花朵图标，20px 基准，颜色取 {colors.leaf}，和正文同族；不用几何实心图标"
  emptyState: "{colors.surface} 底 + 1px {colors.hairline} 拱框 + 一行 {colors.ink-muted} 说明，不放插画"
motion:
  easing: ease-in-out
  durationFast: 500ms
  durationBase: 700ms
  hover: "卡片金框 35%→60%、金影 15px→25px、藤蔓顺时针转 3deg；按钮深绿翻金底、字翻深绿；位移不超过 2px"
  focusRing: "2px solid {colors.line}，offset 2px；奶油底与深绿底上都可见"
  openTransition: "展开用 480ms ease-out 的透明度与 16px 位移，只动 transform 与 opacity"
  reducedMotion: "所有过渡降到 1ms，拱框、藤蔓与金线保留静态终态，信息零丢失"
  dragUsesSpring: false
---

## Overview

新艺术曲线给美术馆与画廊、精品酒店与珠宝腕表、剧院演出与婚礼请柬、插画师作品集，以及任何需要「手作感先于效率感」的品牌发布页用。它要确认的不是「这条信息最快被扫到」，而是「这场展出/这件物件值得停下来看」。

性格来自五个可指认的选择。纸底 `{colors.canvas}`（#F5EFE0）来自 aesthetic.fyi 的 Mucha 海报奶油色，不是纯白；`{colors.line}`（#C9A227）的 1px 金线勾出拱框、波纹与藤蔓，来自 StyleKit 的「金色描边跟踪每一条曲线」；`{rounded.whiplash}` 的 60% 40% 55% 45% 不对称圆角让容器像植物生长而不是几何切割；标题用 Playfair Display 700 斜体让字本身成为装饰；`{motion.durationBase}` 700ms ease-in-out 把交互压到植物摆动的节奏，明确拒绝 150/200ms 的短促回弹。实测对比：深绿对奶油纸底 8.06:1、调深后的次级绿 5.44:1、酒红 7.48:1；金色对纸底只有 2.11:1，所以只走线和边框，不进正文。

读者先看到拱框与藤蔓构成的整体装饰框架，再沿非对称的斜向动线读到斜体大标题，最后才读正文与金边按钮。金色面积压在 5% 左右、深绿占大头，装饰才不会吞掉阅读区；一旦把金色铺成背景、把按钮改成直角胶囊、把过渡缩到 150ms，风格立刻垮成普通「复古皮肤」。

它和库内相近风格的分工：`deco-ceremony` 是轴线对称的黑金几何典礼，`art-nouveau` 是非对称的奶油纸底植物曲线；`editorial-serif` 用衬线做长文节奏，`art-nouveau` 用衬线做装饰字形并主动降低信息密度；`memphis` 的曲线是几何拼贴，`art-nouveau` 的曲线必须来自藤蔓生长逻辑。

**Key Characteristics**

- 奶油纸底 `{colors.canvas}`（#F5EFE0）+ `{colors.surface}`（#FAF7EF）两层纸色：来源显式值，不用纯白也不用深色底。
- 单一描边色 `{colors.line}`（#C9A227）承担拱框、藤蔓、波纹与焦点：金色是材质不是填充色。
- 深绿 `{colors.primary}`（#2D5016）占最大文字面积与主按钮，酒红 `{colors.accent}`（#8B2252）只做印章级强调，面积 ≤5%。
- Playfair Display 400/700 两档、60/48/36/26/20/16px 六档字阶，标题斜体，字本身参与装饰。
- 拱形裁切 `{rounded.frame}` 48px、卡片 `{rounded.card}` 32px、按钮与标签 `{rounded.button}` 999px，容器与图片边缘一律不成直角。
- 层级靠纸色差、1px 金线密度与带偏移的柔影表达；`{elevation.separator}` 只选 border。

## Colors

**Canvas & Surface**

- `{colors.canvas}` — #F5EFE0，页面底。aesthetic.fyi 显式给出「Cream #F5EFE0」，是泛黄的旧海报纸；对深绿 8.06:1，不是 #FFFFFF。
- `{colors.surface}` — #FAF7EF，卡片与软面板。StyleKit 显式「Soft Ivory #faf7ef」，比纸底亮一档；深绿在其上 8.64:1。
- `{colors.surface-alt}` — #2D5016，深色区块，与 `{colors.ink}` 同值。StyleKit 显式「Deep Green」，用于承载浅色字的局部深色带。

**Ink**

- `{colors.ink}` — #2D5016，正文与标题。StyleKit 显式 `--color-deep-green`，植物茎叶的绿；对纸底 8.06:1。
- `{colors.ink-muted}` — #3F6B35，次要说明与藤蔓旁注。由 StyleKit 的 Leaf #4A7C3F 调深得到的推断值：来源值对纸底只有 4.31:1，不达本库 4.5 门槛；调整后 5.44:1，仍在同一绿色族内。
- `{colors.ink-faint}` — #6B7B3C，图例与最弱标签。aesthetic.fyi 显式「olive #6B7B3C」，对纸底 4.05:1，只承担 ≥3:1 的非正文信息。
- `{colors.leaf}` — #4A7C3F，藤蔓描边与图标线。StyleKit 显式 `--color-leaf`；它是线不是字，4.31:1 足够承担图形边界。

**Line & Accent**

- `{colors.line}` — #C9A227，金色描边、波纹与焦点环。StyleKit 显式 `--color-gold`，「描边与高光，用于勾出曲线的边缘」；对深绿 3.82:1，在深底上仍可辨，对纸底 2.11:1，禁止当小字色。
- `{colors.hairline}` — rgba(201, 162, 39, 0.35)，卡片默认金线。StyleKit 显式「1px gold border at 35%」，hover 提到 60%。
- `{colors.primary}` — #2D5016，主按钮填充，深绿实色；`{colors.on-primary}` — #F5EFE0，按钮上的字，两者 8.06:1。
- `{colors.accent}` — #8B2252，酒红印章与章节标记。aesthetic.fyi 显式「burgundy #8B2252」，对纸底 7.48:1；来源要求它只出现在极小面积。

不设第二强调色：StyleKit 的 Wisteria #8B6DB5 与 Bright Green #4BC542、designmd.app 的 Mauve #E0B0FF 全部弃用，详见 NOTES「弃」与 `Known Gaps`。

## Typography

字号六档：display 60px、heading-lg 48px、heading 36px、subheading 26px、body 20px、label 16px。相邻比值 1.25、1.33、1.38、1.30、1.25，全部不低于 1.25；这是 StyleKit 显式 16/20/26/36/48/60px 阶的原值，本库只是把正文从 16px 档移到 20px 档，删掉 14px 标签档。

字重只用两档：700 给 display / heading-lg / heading，400 给 subheading / body / label。StyleKit 与 aesthetic.fyi 都明确 400/700，本库不引入 designmd.app 的 500/600。字族一族到底：Playfair Display → Georgia → Songti SC → Noto Serif CJK SC → STSong → serif；StyleKit 给的 Substitute 就是 Georgia 与 Songti SC，中文不另起黑体。

display 与 heading-lg 用斜体（aesthetic.fyi 的「bold italic for headings」），正文与标签保持正体。`{typography.label}` 保留来源的 0.12em 字距，但只给短标签与按钮，不写成全大写长句；中文标签在真实渲染中若出现字间裂缝，把字距归零（见 `Chinese Typography`）。

## Layout

- 页面最大宽 1080px，来自 StyleKit 的显式 `page max-width: 1080px`；两侧 padding `{spacing.sm}` 24px。
- 间距阶 8 / 16 / 24 / 36 / 48 / 64 / 128px，基数 `{spacing.base}` 8px 来自 StyleKit；36px 是来源的 card padding 显式值，128px 是来源的 section gap 显式值。
- 卡片间距 `{spacing.sm}` 24px，来自 StyleKit 的 element gap；正文最大宽 `{spacing.measure}` 34em（20px × 34 ≈ 680px）。
- 卡片网格不用三等列：两列布局，第一张跨两行、第三张跨两列，呼应 designmd.app「No 3-equal-columns / zig-zag or asymmetric grid」与风格谱的「非对称垂直延展」。
- 外层拱框 `inset: 16px`，上两角 `{rounded.frame}` 48px、下两角 `{rounded.image}` 8px；section 结束处允许弧线收口，正文左边缘仍保持整齐。
- 波纹分隔线：1px 金线，振幅 `{spacing.base}` 8px、波长 `{spacing.wave}` 120px，取 StyleKit Wave Divider 的显式参数。
- 768px 以下折成单列，拱框缩进减半，藤蔓伪元素缩到 `{spacing.ornament}` 32px，不产生横向溢出。
- 主分隔手段只有 `border`（金线/纸色差辅助），投影只负责体积，不承担分栏。

## Elevation & Depth

三级柔影全部带偏移：`{elevation.e1}` 是卡片的 `0 4px 15px rgba(45,80,22,0.20)`（StyleKit 显式），`{elevation.e2}` 是 hover 的 `0 8px 25px rgba(201,162,39,0.40)`（StyleKit 显式），`{elevation.e3}` 是本库为展开面板推断的 `0 12px 32px rgba(45,80,22,0.28)`。没有 `0 0 Npx` 的居中发光。

`{elevation.lightSource}` 固定 top-left：上沿用 `{elevation.topHighlight}` 的 inset 金线表示金箔受光，左下阴影加深，四边不同时有光。深色区块 `#2D5016` 上的层级靠纸色文字亮度与 1px 金线表达，不再叠黑影。

`{elevation.separator}` 只选 border：金色细线是主分隔器，纸色差是辅助，阴影只给「这张卡片浮起来了」一个含义。StyleKit 明令禁止 hard-edge shadow，本库连 0 模糊硬影也不留。

## Shapes

圆角是语义化的四档：卡片 `{rounded.card}` 32px、按钮与标签 `{rounded.button}` 999px、拱框 `{rounded.frame}` 48px、图片下角 `{rounded.image}` 8px；装饰块另用 `{rounded.whiplash}` 的 60% 40% 55% 45% 不对称圆角。StyleKit 的显式值原样保留。

禁止直角与几何形：容器、按钮、图片、分隔线都不出现 0px 圆角；SVG 图标用藤蔓和花苞，不用方框、三角与齿轮。拱形裁切的上两角必须是 999px，下两角 8px，不能改成四角同圆。装饰性的五瓣花 32–64px、每屏不超过三处，来自 StyleKit 的 Blossom Mark 显式约束。

## Material & Elevation

材质是平版印刷的旧海报纸加金箔：奶油纸底、柔金线、深绿墨、酒红印章。`{elevation.lightSource}` 为左上，海报本身用平面光，只在拱框上沿与卡片边界用金线暗示反射；风格谱明确「海报多用平面光，建筑和工艺品使用环境光呈现金属、玻璃与釉面」，本库取前者，不为网页硬加玻璃反光。

纸色三层 `#F5EFE0` → `#FAF7EF` → `#2D5016` 是明度阶梯；金色只走 1px 线与上沿高光。主分隔手段仍是 border；出现大面积金色填充、玻璃模糊、霓虹或 0 模糊硬影即破功。

## Mark & Media

标识：`{media.logoRule}`（`{media.logoType}`）；不搬 Mucha 原作、新艺术车站入口或任何真实品牌字标，只迁移排字规则。图片：比例 `{media.imageRatio}`、圆角 `{media.imageRadius}`、处理 `{media.imageTreatment}`；删除测试问的是「删掉这张植物/拱窗插画，读者是否失去季节、场所或材质线索」，四问皆否就删掉。背景：`{media.background}`。图标：`{media.iconRule}`。空态：`{media.emptyState}`。

每张媒体都有静止帧：插画未加载时拱框与金线仍在，正文与按钮照常可读；`prefers-reduced-motion` 只停过渡与藤蔓旋转，不隐藏装饰框架。文字、按钮、表单、数据标签一律真实 HTML/CSS 排版，不让生图模型画字。

## Motion & States

过渡曲线 `{motion.easing}`，快档 `{motion.durationFast}` 500ms、基准 `{motion.durationBase}` 700ms，全部来自 StyleKit 的「500 到 700ms ease-in-out，像植物移动」；明确拒绝 150/200ms 短促过渡。hover：`{motion.hover}` 把金线与金影同时升一档，位移不超过 2px，按钮翻成金底深字；焦点：`{motion.focusRing}` 2px 金环 offset 2px，在奶油底与深绿底都可见（StyleUI Liberty 的金色焦点规则）。展开：`{motion.openTransition}` 只动透明度与 16px 位移，480ms ease-out。

交互组件逐项覆盖六态：default 为深绿字、35% 金线与柔影；hover 把线提到 60%、金影变宽、藤蔓转 3deg；focus-visible 加 2px 金环；active 按钮 scale 0.98 并回到深绿底（来源按压规格）；disabled 用 35% 金线、虚化文字、无阴影，不靠降低透明度；error 用 `{colors.accent}` 的 1px 酒红线加一行 `{colors.ink}` 说明，不新增警示色。下拉另有 open 态：花苞式展开，只动 transform 与 opacity。

`prefers-reduced-motion` 时执行 `{motion.reducedMotion}`：过渡降到 1ms，拱框、金线与藤蔓保留静态终态。没有拖拽/手势组件，`motion.dragUsesSpring` 为 false。

## Components

### card

`{components.card}` 是 `{colors.surface}` 底、1px `{colors.hairline}` 金框、`{rounded.card}` 32px 圆角、`{spacing.md}` 36px 内边距的柔影卡片。左上角一条 1px `{colors.leaf}` 藤蔓沿边生长并带两三片叶；标题用 `{typography.heading}` 斜体深绿，正文用 `{typography.body}`。hover 只提亮金框、加宽金影并把藤蔓转 3deg，700ms ease-in-out，不改字号不位移整块。

### button-primary

`{components.button-primary}` 是 `{colors.primary}` 深绿实底、`{colors.on-primary}` 奶油字、1px `{colors.line}` 金边、`{rounded.button}` 999px 胶囊，padding `16px 32px`，标签用 `{typography.label}`。hover 翻成金底深绿字并把箭头右移 `{spacing.base}` 8px 的一半，active scale 0.98；500ms ease-in-out。来源要求「fully rounded、serif、gold border」，本库照收。

### tag

`{components.tag}` 用 `{colors.surface}` 底、`{colors.accent}` 酒红字、`{rounded.tag}` 999px 胶囊、1px `{colors.hairline}` 金线，padding `8px 16px`。它是章节标记或状态印章，不放在标题前宣布「下面是内容」；每屏最多三枚，中文标签把 0.12em 字距归零。

## Do's and Don'ts

### Do

- 纸底用 `{colors.canvas}`，卡片用 `{colors.surface}`，两层都是偏黄的米色而不是纯白。
- 每条边界都走 1px 金线：拱框、波纹分隔、卡片、按钮、焦点环共用 `{colors.line}`。
- 标题用 Playfair Display 700 斜体，正文 20px/1.8，字重只有 400 与 700。
- 容器用拱形裁切与 `{rounded.whiplash}` 不对称圆角，藤蔓沿边生长并带叶。
- 过渡 500–700ms ease-in-out，hover 提亮金线而不是位移整块；金色面积 ≤5%。

### Don't

- 不要用直角、几何图标、三等分网格和无装饰裸框——StyleKit 把它们列头号禁令，会让海报变成表单。
- 不要用紫藤 #8B6DB5、亮绿 #4BC542、Mauve #E0B0FF 或霓虹高饱和色：来源之间互相冲突且触犯本库 The Floor。
- 不要把金色铺成背景或写成小字——对纸底仅 2.11:1；金色只能走线、边框和大面积高光边缘。
- 不要用 150/200ms 短促过渡、0 模糊硬影、弹簧回弹或玻璃模糊——来源逐条点名禁止。
- 不要搬 Mucha 原作、真实车站入口、酒店徽标或任何品牌专属字体资产；只迁移可复现的排字与曲线规则。
- 不要拿它做长文阅读、数据后台、表单密集流程与无障碍优先页面——装饰框架和慢速动效会持续抢走注意。

## Chinese Typography

- 中文正文行高 `{typography.body}` 的 1.8（20px × 1.8 = 36px），高于 1.7 下限；标签 16px/1.5 也不低于 1.5。
- 中西文之间留四分之一个空格：`32px 圆角`、`用 Playfair Display`；中文段落不首行缩进，启用避头尾，使用全角标点。
- `{typography.label}` 的 0.12em 是拉丁短标签的显式值；纯中文标签把它归零，避免小字被拉散。display 的 0.01em 在纯中文标题上同样归零。
- Playfair Display 不含中文，回退到 Songti SC / Noto Serif CJK SC / STSong；标题的斜体由中文回退字体合成，需在真机确认字形不过度变形。
- 中文字重只有 400/700 两档可靠；本库正文 400、标题 700，不用 500/600。
- 60px display 只给拉丁短词与数字；中文标题降到 `{typography.heading}` 36px，仍保留斜体与金线下边框。
- 章节标题不用引号包整句；酒红印章文字不超过六个汉字，避免小字号酒红压过深绿正文。

## When to Use

**用**：美术馆与画廊展览页、精品酒店与珠宝腕表品牌页、剧院演出与婚礼请柬、插画师作品集与主视觉、需要手工装饰感的品牌发布页。

**别用**：开发者工具与技术文档、数据看板与密集表格、高频交易与监控台、移动优先的工具型 App、快速新闻流、无障碍优先的长表单默认皮、打印为主的单栏正文。

## Iteration Guide

1. 一次只改一个组件，用 `{components.card}` 指代它；不要同时动拱框、字阶与金色面积。
2. 所有值走 token，不写裸 hex；想加第二种强调色前，先确认酒红是不是被误用成了装饰。
3. 想加强风格时先把拱框、藤蔓和波纹分隔调准，最后才考虑加图元——加色会直接破功。
4. 新增装饰前先跑删除测试：删掉它读者会不会失去季节、场所或材质线索；不会就删掉。每屏花朵不超过三处。
5. 改完必须重跑 `designlib check` 并重新截图；金色面积与慢速动效只能靠真实渲染判断。

## Known Gaps

- 五份来源的画布色不同：aesthetic.fyi 是 #F5EFE0，StyleKit 是 #F5F0E1，StyleUI 是 #F7F3E9，designmd.app 是 #FFFFF0；取 aesthetic.fyi 的奶油色，因为它同时给出酒红与橄榄的配套关系。
- StyleKit 的 Leaf #4A7C3F 对奶油底只有 4.31:1，`{colors.ink-muted}` 因此调深到 #3F6B35（推断值）；原值保留给非文字的藤蔓线条。
- StyleKit 的 Wisteria #8B6DB5 / Bright Green #4BC542 与 designmd.app 的 Mauve #E0B0FF / Peacock Blue #005F9E 被弃用：前者是情感强调与「新芽」标记，后者是品牌扩展色，合进来会让低饱和海报变成霓虹拼贴。
- aesthetic.fyi 的 `#C8A951` 与 StyleKit 的 `#C9A227` 是同一个金箔色的两个近似值；取 StyleKit，因为它同时给出 35%/60% 的边框透明度和组件规格。
- 风格谱提醒「维也纳分离派走几何秩序」，本库只收鞭状曲线路线；需要黑金对称典礼时应选 `deco-ceremony`，不要改本风格 token。
- 来源字阶最小 16px、正文 16px/1.8；本库把正文提到 20px/1.8、标签保留 16px，六档阶是本库重排的结果，不是来源原值逐字照搬。
- 来源没有给出输入框、下拉、弹窗、加载态与错误态规格；`Motion & States` 的 disabled / error / open 三态是按本库六态要求推断的，不是来源显式值。
- Playfair Display / Amarante / Cormorant 在截图环境可能缺失；中文回退到宋体类字族后，斜体与高对比衬线的装饰性会减弱，`{typography.display}` 的中文使用场景有限。
- 波纹分隔与藤蔓目前是静态 CSS 伪元素，不是可编辑的 SVG 路径；需要精确花形时仍需单独插画资产。
