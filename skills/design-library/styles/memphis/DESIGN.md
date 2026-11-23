---
version: alpha
name: Memphis｜孟菲斯海报
description: >-
  把 1981 年米兰 Memphis Group 的后现代装饰语言做成一套可直接用的展示型界面：
  奶白底、玫红/柠檬黄/薄荷/靛蓝四色撞色、3px 墨黑描边、6px 无模糊硬投影，
  波点与 45° 斜纹只待在角落，圆/方/三角/波浪线故意错落。
  用于儿童与文创品牌、展览活动、创意市集、社交媒体视觉和需要强烈 80 年代态度的落地页。
  参数提炼自 designmd.app 的 Memphis 风格卡与 liuyutao.com 的中文风格词典（两份都给出显式数值）交叉验证；
  标为 beta/variant。为符合本库 The Floor，把来源的纯白画布改为奶白、把来源的 Poppins 正文 16px/1.6 提到 20px/1.7，
  并把 designmd.app 的模糊软影换成词典里明确写出的硬投影。
cues: 儿童教育与玩具文具品牌站、展览与创意市集活动页、音乐与时尚编辑页面、社交媒体封面与包装插画、需要强烈 80 年代后现代态度的展示型落地页
avoid: 金融法律医疗等严肃场景、长文阅读与产品文档、需要极简克制品牌气质的产品、高密度后台与长表单、需要精确扫读的数据页、政务与公共服务
surface: light
density: medium
register: story
family: expressive
tier: variant
sourceRefs: memphis
status: beta

colors:
  canvas: "#FFF8EC"
  surface: "#FFFDF5"
  surface-alt: "#FFF1D6"
  ink: "#111111"
  ink-muted: "#3D3D3D"
  ink-faint: "#6A6A6A"
  line: "#111111"
  primary: "#5B5BD6"
  secondary: "#3BCEAC"
  accent: "#FF5C8A"
  highlight: "#FFD23F"
  on-primary: "#FFF8EC"
  on-accent: "#111111"
typography:
  display:
    fontFamily: "Archivo Black, PingFang SC, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.01em
  headline:
    fontFamily: "Archivo Black, PingFang SC, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.01em
  cardTitle:
    fontFamily: "Archivo Black, PingFang SC, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  body:
    fontFamily: "Poppins, PingFang SC, Noto Sans SC, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: 0
  label:
    fontFamily: "Poppins, PingFang SC, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0.02em
rounded:
  card: 0px
  tag: 0px
  button: 999px
spacing:
  base: 8px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 32px
  xl: 48px
  section: 64px
  measure: 36em
components:
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: 24px
    border: "3px solid {colors.line}"
    shadow: "{elevation.e2}"
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.label}"
    rounded: "{rounded.button}"
    padding: 12px 24px
  tag:
    backgroundColor: "{colors.highlight}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.tag}"
    padding: 6px 12px
elevation:
  lightSource: top-left
  steps: 3
  e1: "3px 3px 0 {colors.ink}"
  e2: "6px 6px 0 {colors.ink}"
  e3: "10px 10px 0 {colors.ink}"
  topHighlight: "none —— 平涂色块不加内高光，避免把后现代海报做成玻璃拟物"
  borderLight: "{colors.line}"
  borderDark: "{colors.ink}"
  separator: border
media:
  logoType: wordmark
  logoRule: "字标用 {typography.display}，右侧留 0.5em；只写排字规则，不搬 Memphis Group 商标、Carlton 书架轮廓或任何品牌吉祥物"
  imageRadius: "{rounded.card}"
  imageRatio: "4:3"
  imageTreatment: "none；图片落在 {colors.surface} 色块内做 4:3 裁切，不叠渐变、不混色；图案不压在文字后面"
  background: "平涂 {colors.canvas} + 至多两处角落 CSS 图案：{colors.primary} 45° 斜纹（5px 实线 / 6px 间隔）与 {colors.secondary} 圆点（3px 圆 / 14px 网格）；图案总面积 ≤20% 且不进正文区"
  iconRule: "3px 描边、24px 基准，和 {colors.ink} 同色；只用圆、方、三角、波浪线四类"
  emptyState: "{colors.surface-alt} 底 + 3px {colors.ink} 描边 + 一行 {colors.ink-muted} 说明，不放插画"
motion:
  easing: "cubic-bezier(0.2, 0.8, 0.2, 1)"
  durationFast: 160ms
  durationBase: 320ms
  hover: "装饰性倾斜 ±3deg 归零、translateY -4px，硬影从 6px 增到 8px，不产生模糊"
  focusRing: "3px solid {colors.primary}，offset 2px；方角与胶囊容器都可见"
  openTransition: "opacity 0→1 且 translateY 8px→0，160ms"
  reducedMotion: "全部过渡降到 1ms，关闭倾斜回正与斜纹位移"
  dragUsesSpring: false
---

## Overview

给儿童教育、玩具文具、创意市集、展览海报、音乐与时尚编辑页，以及任何需要"我们不正经但很认真"的展示型页面用。它要确认的不是"这条信息准确"，而是"这个品牌有能量、敢撞色、不按现代主义的规矩办事"。

性格来自五个可指认的选择。画布 `{colors.canvas}`（#FFF8EC）是奶白而不是纯白，给撞色一个暖底；四色 `{colors.accent}` / `{colors.highlight}` / `{colors.secondary}` / `{colors.primary}` 分别只玫红、柠檬黄、薄荷、靛蓝，来自中文词典的显式 CSS 变量，不用 designmd.app 那套饱和度更高的八色扩展板。`{colors.line}` 与 `{colors.ink}` 同为 #111111，所有卡片、按钮、标签统一 3px 描边；`{elevation.e2}` 是 6px 6px 0 的无模糊硬投影，制造 1980 年代"塑料贴面"的伪 3D 感。圆角只给主按钮 `{rounded.button}` 999px，容器一律 `{rounded.card}` 0px 方角；正圆只属于图形装饰。背景图案用 CSS 渐变画在角落，正文区域保持纯色底。

读者应先看见错落的色块与线条，再读到标题，最后读到正文。装饰从一开始就是信息的一部分——这是后现代装饰性，不是结构完成后的贴花；但当图案压到文字后面，它就从风格变成噪声。把硬投影换成模糊阴影、把奶白换成纯白、把撞色收敛成一个强调色，风格立刻垮成普通扁平页或新野兽派。

**Key Characteristics**

- 画布 `{colors.canvas}`（#FFF8EC）：来源词典显式值，暖白承托四色撞色，避开纯白与纯黑两端。
- 四色固定分工：玫红主按钮、柠檬黄标签与卡片、薄荷卡片、靛蓝链接与底部信息条，均为来源显式 hex；每屏只让玫红承担唯一主行动。
- 3px 墨黑描边 + 6px 6px 0 硬投影：`{elevation.e2}` 是来源明确写出的规格，模糊半径必须为 0。
- 标题 Archivo Black、正文 Poppins：来源词典点名的开源字体，标题自带 Black 字面，正文字重只取 400/700 两档。
- 容器方角、主按钮胶囊：`{rounded.card}` 0px 与 `{rounded.button}` 999px 同屏并存，但各有明确职责，不是混用圆角。
- 图案与文字分区：斜纹与波点只在角落、面积 ≤20%，正文区保持 `{colors.surface}` 纯色，来源"常见踩坑"条目明确要求。

## Colors

**Canvas & Surface**

- `{colors.canvas}` — #FFF8EC，页面底色；中文词典的 `--ds-bg` 显式值，奶白偏暖，符合本库"浅色底不用大面积纯白"。
- `{colors.surface}` — #FFFDF5，卡片与正文容器底；来源把卡片写成"白"，这里向画布偏一档成暖白，避免纯白大色块，对 `{colors.ink}` 18.54:1。
- `{colors.surface-alt}` — #FFF1D6，空态与次级面板；由 `{colors.highlight}` 向画布稀释得到的推断值，用于不抢主行动的浅底。

**Ink**

- `{colors.ink}` — #111111，标题、正文、描边与投影同色；词典显式值 `--ds-text`，不是纯黑，对比度 17.89:1。描边与文字同色是 Memphis 风格"粗黑勾边"的关键。
- `{colors.ink-muted}` — #3D3D3D，次要说明；词典 prompt 的显式值，对画布 10.29:1。
- `{colors.ink-faint}` — #6A6A6A，编号、日期、元信息；推断值，对画布 5.12:1，仍高于 3:1 硬线，不用更浅的灰。

**Line**

- `{colors.line}` — #111111，3px 描边色；来源"所有卡片、按钮与标签都有 3px 纯黑描边"，用 `{colors.ink}` 的墨黑替代纯黑，满足本库与来源"不用 #000000"的共同要求。

**Accent**

- `{colors.primary}` — #5B5BD6，靛蓝，链接、焦点环、底部信息条与斜纹；词典显式值 `--ds-indigo`，对画布 5.08:1。不要拿它做正文。
- `{colors.secondary}` — #3BCEAC，薄荷，卡片填色与波点；词典显式值 `--ds-mint`，压 `{colors.ink}` 9.54:1。
- `{colors.accent}` — #FF5C8A，玫红，唯一主按钮；词典显式值 `--ds-pink`，压 `{colors.on-accent}` 6.43:1。对画布仅约 2.8:1，因此不做正文或链接色。
- `{colors.highlight}` — #FFD23F，柠檬黄，标签与卡片填色；词典显式值 `--ds-yellow`，压 `{colors.ink}` 13.08:1。
- `{colors.on-primary}` — #FFF8EC，靛蓝底上的字；与画布同值，对 `{colors.primary}` 5.08:1。
- `{colors.on-accent}` — #111111，玫红按钮上的字；与 `{colors.ink}` 同值。黄色、薄荷与玫红色块上一律用墨黑字，来源明确提醒白字对比度不足。

## Typography

字号五档：display 56px、headline 36px、cardTitle 28px、body 20px、label 16px。相邻比值为 1.56、1.29、1.40、1.25，全部不低于 1.25；不出现 18、24、32、48px 这类中间档。headline 的 36px 来自中文词典的显式值；display 的 56px 落在 designmd.app 的 Hero `clamp(2.5rem, 5vw, 4rem)` 区间内，比 36px 高两档，给海报式首屏足够的落差。

字重只有 400 与 700 两档。Archivo Black 字面本身就是黑体，但环境缺字时会回退到中文黑体，所以 display / headline / cardTitle 在 CSS 里统一用 700 合成重量，保证海报感不因回退而消失；Poppins 正文 400、标签 700。来源 designmd.app 写了 500/600，本库按"只用两档"收拢。中文回退 PingFang SC / Noto Sans SC；display 的 -0.01em 负字距对中文减半到 -0.005em，label 的 0.02em 正字距在中文归零，避免小字被拉散。

designmd.app 给的正文是 1rem/1.6（16px/1.6），不满足本库"中文正文 ≥18px 且行高 ≥1.7"，因此提到 20px/1.7；这是显式记录的改造，不是从图里猜的。

## Layout

- 12 列网格、最大宽 1120px 居中、列距 24px；根基来自 designmd.app 的 1280px 居中与 1.5rem 侧边距，收窄到 1120px 让四色卡片不至于过宽。
- 首屏故意不对齐：主标题跨 7 列、装饰色块跨 5 列并下移 32px；三张卡片用 5/4/3 列不等宽，不用三等分。来源 designmd.app 明确写"No 3-equal-columns"。
- 区块间距 `{spacing.section}` 64px，标题与正文之间 `{spacing.xl}` 48px，卡内 Padding `{spacing.md}` 24px，斜纹与波点离正文至少 `{spacing.lg}` 32px。
- 正文最大宽度 `{spacing.measure}`；768px 以下所有多列折成单列，装饰图案保留在角落但不参与滚动布局，不产生横向溢出。
- 层级主分隔手段是 3px `border`，不用阴影当分隔；阴影只负责"这块是塑料贴面"的材质感。

## Elevation & Depth

三级硬影，光从 `{elevation.lightSource}` 左上统一照下来，所以偏移永远向右下：`{elevation.e1}` 3px 3px 0 给标签与小按钮，`{elevation.e2}` 6px 6px 0 给卡片（来源显式值），`{elevation.e3}` 10px 10px 0 只给浮层，一屏最多一处。模糊半径恒为 0；一旦出现 `0 8px 20px` 这类软影，塑料贴面就变成 Material Design， Memphis 的伪 3D 感消失。

层级靠 3px 描边与底色差表达，不靠亮度渐变。同一屏所有硬影颜色都等于 `{colors.ink}`，不另引入中性黑或彩色阴影；阴影与描边同色才像从同一张黑色卡纸上裁下来的。

## Shapes

容器 `{rounded.card}` 0px、标签 `{rounded.tag}` 0px、主按钮 `{rounded.button}` 999px。来源 designmd.app 要求 base radius 0px，词典要求主按钮胶囊；两者不冲突——方形容器负责"海报拼贴"，胶囊按钮负责"可点击"，职责不同。正圆 `border-radius: 50%` 只给图形装饰（圆点、气泡、波浪线的端点），不给任何内容容器。

形状词汇限定四类：方、圆、三角、波浪线；三角用 `clip-path: polygon()` 画，波浪线用 SVG 或 `radial-gradient` 拼，不引入第五种动物、星星或笑脸图标。装饰元素允许 ±5° 静态倾斜（来源显式给出 5deg），文字容器倾斜不超过 2°，否则影响扫读。

## Material & Elevation

材质是平涂塑料贴面：无内高光、无模糊、无玻璃感，`{elevation.topHighlight}` 明确为 none。画布 #FFF8EC → 卡片 #FFFDF5 → 空态 #FFF1D6 三档暖色明度差承担"贴在上面"的感觉，再叠 3px 墨黑描边与右下硬影完成伪 3D。主分隔手段只有 `border`；阴影是材质，不是分隔器。

角落图案由 CSS 绘制：靛蓝 45° 斜纹用 `repeating-linear-gradient(-45deg, ... 0 5px, transparent 5px 11px)`，薄荷圆点用 `radial-gradient(circle, ... 3px, transparent 3.5px)` 配 14px 网格——两者都是中文词典 FAQ 给出的显式参数。图案只出现 2 处、总面积 ≤20%，不进列表滚动区；来源"常见踩坑"明确说叠层过多会拖慢绘制。

## Mark & Media

标识：`{media.logoRule}`（`{media.logoType}`）；不搬 Memphis Group 的标志、Carlton 书架轮廓或任何真实品牌资产。图片：比例 `{media.imageRatio}`、圆角 `{media.imageRadius}`、处理 `{media.imageTreatment}`；贴图只用来承载真实照片，不用生图替代 UI 排版。背景：`{media.background}`。图标：`{media.iconRule}`。空态：`{media.emptyState}`。

删除测试：斜纹与圆点若删掉，页面仍有撞色与硬影，但会失去后现代海报的热闹感——所以它们只在角落保留两处，不承担信息；若某个装饰删除后读者完全无感，就删掉它。所有图案都有静止帧，未加载时奶白底、标题与卡片仍成立。文字、按钮、表单与数据标签一律真实 HTML/CSS 排版，不让生图模型画字；中文词典明确要求装饰图案不得压在文字后面。

## Motion & States

过渡曲线 `{motion.easing}`，快档 `{motion.durationFast}`、基准 `{motion.durationBase}`；比 Frutiger Aero 的 480ms 快，符合"活泼"而非"屏保"。hover：`{motion.hover}`；焦点：`{motion.focusRing}`，靛蓝在奶白上 5.08:1，offset 2px 不会被 3px 描边吞掉；展开：`{motion.openTransition}`。交互组件逐项覆盖 default / hover / focus-visible / active / disabled / error 六态：active 时 translate 1px 1px 且硬影缩到 1px 1px 0，像被按下；disabled 降到 `{colors.ink-faint}` 描边与 `{colors.surface-alt}` 底；error 用 `{colors.primary}` 3px 描边加一行 `{colors.ink}` 说明，不新增红色。

装饰元素允许 CSS keyframes 做 5° 摆动，但只作用于图形；`prefers-reduced-motion` 时执行 `{motion.reducedMotion}`。本风格没有拖拽排序组件，不使用弹簧过渡，`motion.dragUsesSpring` 为 false；designmd.app 提到的 spring stiffness 120 / damping 20 不迁移。

## Components

### card

`{components.card}` 是 `{colors.surface}` 底、3px `{colors.line}` 描边、`{elevation.e2}` 硬影的方角卡。卡标题用 `{typography.cardTitle}`，正文用 `{typography.body}`，右上角可放 `{components.tag}`。三张卡分别填 `{colors.highlight}` / `{colors.surface}` / `{colors.secondary}`，来自词典"三张卡片分别填黄、白、薄荷绿"；hover 只把硬影从 6px 增到 8px 并把静态倾斜归零，不放大字号。

### button-primary

`{components.button-primary}` 是玫红胶囊、墨黑字、3px 描边与 3px 硬影，承担一屏唯一主行动，只出现一次。来源词典明确写"按钮为胶囊形玫红底黑字"；hover 上移 4px 且硬影增到 8px，active 下压 1px 且硬影缩到 1px。次按钮用透明底、靛蓝描边与靛蓝字，尺寸一致；禁用态不靠变淡的玫红，改用 `{colors.surface-alt}` 底。

### tag

`{components.tag}` 用 `{colors.highlight}` 底、`{colors.ink}` 字、3px 描边、0px 圆角，只标注事实。它不放在标题前当装饰序言，也不承担正文；来源要求"标签用黄色底加黑边"。

## Do's and Don'ts

### Do

- 奶白底上同时出现至少两种撞色块、3px 墨黑描边与 6px 6px 0 无模糊硬影。
- 每屏只让玫红 `{colors.accent}` 承担一个主按钮，其余颜色做信息块或装饰。
- 黄色、薄荷与玫红色块上一律用 `{colors.ink}` 墨黑字，并复核 4.5:1。
- 图案只用 CSS 画在角落，面积 ≤20%，离正文至少 32px。
- 容器方角、主按钮胶囊、正圆只给图形，三者职责不互换。

### Don't

- 不要用纯白画布或纯黑描边——前者触犯本库 The Floor，后者来源词典自己列为禁忌；用 #FFF8EC 与 #111111。
- 不要把硬影改成模糊阴影或居中发光——那会把塑料贴面变成 Material Design 或 AI 氛围光。
- 不要把波点、斜纹压在正文后面——来源"常见踩坑"第一条就点名它会毁掉可读性。
- 不要三张等宽卡片、居中对称构图——来源明确要求不对称与 varied card sizes，整齐会杀死能量。
- 不要照搬 Memphis Group 商标、Carlton 书架、Bob Dylan 歌名做文案，也不要用来源的八色高饱和扩展板（本库只保留四色 + 墨黑）。
- 不要拿它做金融、法律、医疗、长文阅读或数据后台——热闹会直接削弱可信度与扫读效率。

## Chinese Typography

- 中文正文行高不低于 1.7（20px × 1.7），标签可降到 1.5，但不低于 1.5。
- 中西文之间留四分之一个空格：`一张卡片`、`用 Poppins`。
- 中文 label 的 0.02em 正字距归零，Archivo Black 的 -0.01em 负字距对中文减半到 -0.005em，避免挤字或拉散。
- 使用全角标点，段落不首行缩进，启用避头尾；标题不使用引号包整句。
- 中文只有 400 与 700 两档有效字重；Archivo Black 与 Poppins 都不含中文，回退到 PingFang SC / Noto Sans SC 后 Black 字面会消失，标题用 700 合成重量并靠字号与描边维持海报感。
- 56px display 用于中文时降到 36px（headline 档），避免宽字面撑破 1120px 容器；装饰倾斜在中文标题上不超过 2°。

## When to Use

**用**：儿童教育与玩具文具品牌站、展览与创意市集活动页、音乐与时尚编辑页面、社交媒体封面与包装插画、需要强烈 80 年代后现代态度的展示型落地页。

**别用**：金融法律医疗等严肃场景、长文阅读与产品文档、需要极简克制品牌气质的产品、高密度后台与长表单、需要精确扫读的数据页、政务与公共服务。

## Iteration Guide

1. 一次只改一个组件，用 `{components.card}` 指代它；不要同时动配色和图案。
2. 所有值走 token，不要内联十六进制；想加第五种颜色前，先确认四色里哪一种已经承担了两个职责。
3. 想加强风格时先把硬影或描边调准，最后才考虑加图案——加色和加图案都容易破功。
4. 新增装饰前先跑删除测试：删掉它读者会不会失去方向或状态理解；不会就删掉。
5. 改完必须重跑 `designlib check` 并重新截图；图案密度是否过头只能靠真实渲染判断。

## Known Gaps

- 只覆盖浅色展示型界面；深色 Memphis（designbycurio 描述的近黑李子紫底）未收录，因为与库内 `vaporwave` 的深底霓虹定位冲突。
- Archivo Black 与 Poppins 都不含中文，中文回退后标题的黑体字面会减弱；56px 降 36px 的规则需在真机复核。
- 两来源对主色、圆角与阴影存在冲突：designmd.app 用 #FF1493 且主张无阴影、方角；词典用 #FF5C8A 且有硬影与胶囊按钮。本库取词典的显式 CSS 变量为准，已在 NOTES「弃」记录。
- designmd.app 的 spring 物理、pop-in 序列动画与 3D 抽象主视觉未迁移；本库只保留可复现的 CSS 倾斜与硬影。
- 来源的塑料贴面实物纹理、家具摄影与真实海报扫描件未迁移；背景只用 CSS 渐变绘制的两处图案，复杂插画留给 `prompt.md`。
- 图案在低端设备或关闭 GPU 合成时可能出现色带；reduced-motion 已降级但未做逐项开关。
