---version: alpha
name: Tactile 3D
description: >-
  会动的卡片。透视 800px，倾角 12°，弹簧 ω=7.6/ζ=0.82——数值全部来自两个
  能跑的组件库，不是估的。核心不是"有阴影"，是**阴影和高光都跟着指针走**：
  光从哪来、卡有多厚、手推到哪儿，三件事在同一个坐标系里。
  这一份的形状是它的，动效也是它的（第 ③ 类输入），只有排版节奏是本库补的。
# ---------------------------------------------------------------- 选择条件
family: expressive
tier: technique
sourceRefs: atropos,react-bits
cues: 游戏/影视产品页、硬件开箱、作品集、发布会主视觉、可拖拽的选择器、需要"手感"的展示型界面
avoid: 长文阅读、表单、后台管理、需要快速扫读的列表、打印、任何以读字为主的地方
surface: dark
density: roomy
register: story

colors:
  canvas: "#0A0A0B"
  surface: "#141416"
  surface-hi: "#1C1C1F"
  surface-lit: "#2A2A30"
  surface-lo: "#0E0E10"
  ink: "#F5F5F7"
  ink-soft: "#A1A1A6"
  ink-faint: "#6E6E73"
  line: "rgba(255, 255, 255, 0.08)"
  line-hi: "rgba(255, 255, 255, 0.16)"
  accent: "#FF6B3D"
  accent-ink: "#180A05"

typography:
  display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'PingFang SC', system-ui, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.03em
  headline:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'PingFang SC', system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.03em
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'PingFang SC', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: -0.005em
  label:
    fontFamily: "ui-monospace, 'SF Mono', Menlo, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em

rounded:
  sm: 8px
  md: 16px
  lg: 22px
  pill: 999px

spacing:
  base: 8px
  xs: 6px
  sm: 10px
  md: 16px
  lg: 24px
  xl: 36px
  section: 56px
  measure: 32em

components:
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: 24px
  card-hover:
    transform: "translate3d(0, -2px, 24px) scale(1.05)"
  box:
    backgroundColor: "{colors.surface-hi}"
    rounded: "{rounded.md}"
    aspectRatio: "4 / 5"
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.accent-ink}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  tag:
    backgroundColor: "{colors.surface-hi}"
    textColor: "{colors.ink-soft}"
    rounded: "{rounded.pill}"

elevation:
  lightSource: top-left
  steps: 3
  e1: "inset 0 0 0 1px {colors.line}"
  e2: "inset 0 0 0 1px {colors.line}, 0 1px 0 rgba(255,255,255,0.04)"
  e3: "inset 0 0 0 1px {colors.ink-faint}, 0 8px 24px rgba(0,0,0,0.32)"
  topHighlight: "inset 0 1px 0 rgba(255,255,255,0.06)"
  borderLight: "{colors.line}"
  borderDark: "{colors.ink-faint}"
  separator: shadow
media:
  logoType: wordmark
  logoRule: "字标沿用显示字族，右侧留 0.5em；图形标只用单色 {colors.ink}，最小 24px"
  imageRadius: "{rounded.md}"
  imageRatio: "4:3"
  imageTreatment: "去饱和 6%，不加投影；与底色相接处用 1px 描边收口"
  background: "纯色 {colors.canvas}，无纹理、无氛围渐变"
  iconRule: "1.6px 描边，20px 基准，与正文同色，不使用彩色图标"
  emptyState: "淡底 + 一行说明文字，不放装饰插画和大号图标"
motion:
  easing: "cubic-bezier(0.2, 0.8, 0.2, 1)"
  durationFast: 120ms
  durationBase: 200ms
  hover: "背景升一档明度，位移 0；有阴影时抬高一级"
  focusRing: "3px solid {colors.accent}，offset 2px，不被圆角裁切"
  openTransition: "scaleY 0→1，transform-origin top，120ms"
  reducedMotion: "全部过渡降到 1ms，去掉位移"
  dragUsesSpring: false
---
## Overview

给需要"手感"的地方用：游戏和影视产品页、硬件开箱、作品集首页、发布会主视觉、可拖拽的选择器。**它不适合任何以读字为主的界面**——这套东西的全部力气都在让一个平面看起来有厚度，字越多越亏。

性格来自四个具体的选择，不是形容词：

1. **透视 800px**（单卡）/ **1400px**（成环）。800 是 `TiltedCard` 的默认值，再近会明显梯形失真，再远立体感就没了。多卡成环必须拉到 1400，否则边缘卡片被拉成喇叭口。
2. **倾角 12°**（单卡）/ **15°**（大面积容器）。超过 15° 文字开始斜向变形，低于 8° 看不出在动——这两个库各自独立收敛到 12 和 15，不是巧合。
3. **弹簧 ω=7.6 / ζ=0.82**。ζ 略小于 1，所以松手时有一点回弹；完全临界阻尼（ζ=1）会"啪"一下停死，那是廉价感的主要来源。
4. **高光上限 0.34**。这是最容易被做坏的一个数：调到 0.4 以上就从"表面受光"变成"自己发光"，也就是常见的 AI 塑料感。

**Key Characteristics**

- 画布 `{colors.canvas}`（#0A0A0B）——比 `quiet-dark` 更黑。高光是靠 `mix-blend-mode: screen` 叠上去的，底越黑，同一个 alpha 的亮度差越大。
- 唯一彩色 `{colors.accent}`（#FF6B3D）——信号橙，只出现在按钮和链接上。选它是因为 3D 渲染里"被照亮的表面"就是这个色相区间，冷色会显得像塑料。
- 深度用**三层 z**：封面 −24px、卡面 0、标题 +30px。只有一层投影的"假 3D"没有这个。
- 间距 6/10/16/24/36/56，比 8 倍数更密一点——因为卡片本身有大圆角和内阴影，视觉上已经比实际尺寸"厚"了一圈。
- 圆角 16px（卡片）/ 22px（大盒面）。斜面边缘的圆角要比平面更大一点，才不会有阶梯感。

## Colors

**Canvas & Surface**

- `{colors.canvas}` — #0A0A0B。近黑但不是纯黑（纯黑会让 `screen` 混合的高光失去对比对象）。
- `{colors.surface}` — #141416。卡片主体，比画布亮 10 个亮度值。
- `{colors.surface-hi}` — #1C1C1F。卡面上沿的受光面，用于 180° 渐变的上端。
- `{colors.surface-lo}` — #0E0E10。卡面下沿的背光面。

**Ink**

- `{colors.ink}` — #F5F5F7，对 #0A0A0B 是 **18.18:1**。不用纯白：纯白在深色卡面上会轻微晕光（halation），而且会让高光层无处可去。
- `{colors.ink-soft}` — #A1A1A6，**7.69:1**。正文默认色。
- `{colors.ink-faint}` — #6E6E73，**3.90:1**。只给 ≤14px 的辅助文字，且不上卡面（在 #1C1C1F 上是 3.35:1，刚过装饰线）。

**Line**

- `{colors.line}` — rgba(255,255,255,0.08)。环形边缘。深色界面里"边框"必须是透明白，不是灰色，否则会显脏。
- `{colors.line-hi}` — rgba(255,255,255,0.16)。悬停时边缘提亮。

**Accent**

- `{colors.accent}` — #FF6B3D，对画布 **6.99:1**，可以直接当链接文字。
- `{colors.accent-ink}` — #180A05，橙底上的字 **6.84:1**。是暖黑（带一点红），不用纯黑也不用白——白字在橙上只有 2.4:1。

## Typography

字号阶：12 / 14 / 16 / 20 / 28 / 40 / 56，比例约 **1.4**，比工具界面（1.25）跳得狠。理由：3D 场景里字号差一小截，透视一压就看不出来了。

字重只有 400 / 600 / 700 三档，但**只用 700 做大字**。600 留给按钮——按钮在 3D 里会被缩放，500 缩放后笔画会糊。

字距是这套风格的隐形关键：display 用 **−0.03em**。大字号在斜面上会被透视拉伸，负字距是唯一能把"被拉宽"抵消掉的手段。正文字距 −0.005em，几乎为零，不要跟 display 用同一个值。

## Layout

- 单卡舞台：`perspective: 800px`，卡片宽 200–320px，`aspect-ratio: 4/5`（盒面）或 16/10（横向卡）。
- 环：7–9 个卡片，半径 340px，`perspective: 1400px`，`perspective-origin: 50% 45%`——原点高于中心，让环看起来是"从上方一点看下去"，比正中看更有展台感。
- 间距阶 6/10/16/24/36/56。
- 正文 measure 32em（比 `editorial-serif` 的 34 更窄）：视线在这个风格里要频繁离开文字去看卡片，行太长会丢。
- **但 32em 是"正文"的规矩，不是所有段落的。** tokens.css 里 `:where(p){max-width:32em}` 是无差别生效的：放进**居中**的铭牌、标签、图注里，每个 `<p>` 会按自己的字号算出一个不同宽度（10px→320px、11.5px→368px、32px→1024px 但被父级卡住），而块本身靠左排，"段内居中"就不等于"牌面居中"——四行字的中心能差出 150px，看起来像文字整体往左偏。这类容器里必须显式写 `max-width: none`。

## Elevation & Depth

**这一节是这个风格的主体。** 完整的四件事：

**① 透视**
单卡 `800px`，成环 `1400px`。CSS 的 `perspective` 在父元素上，`transform-style: preserve-3d` 在卡片上，两个都要写，少一个 z 轴就失效。

**② 三层 z**
| 层 | z | 作用 |
|---|---|---|
| 封面图 | −24px | 压在卡面之下，形成内凹的"窗" |
| 卡面 | 0 | 基准面 |
| 标题/浮层 | +30px | 浮在卡面之上，视差最明显 |

**③ 阴影**
- 卡片投影：`0 18px 40px -12px rgba(0,0,0,0.75)`
- 地面投影（`::before`）：左右各缩 8%，高 20px 的椭圆，`blur(20px)`，中心 `rgba(0,0,0,0.55)`，72% 处衰减到 0。
- 天地投影的位置**跟着倾角变**，公式来自 TiltedCard：`x = −sin(ry)·22`、`y = 12 + 16·lift + sin(rx)·18`。固定投影是"贴纸"，跟手投影才是"东西"。

**④ 高光**
`mix-blend-mode: screen` 的径向渐变，7 档非线性衰减（0.34 → 0.285 → 0.202 → 0.108 → 0.035 → 0.003 → 0），60% 处归零。中心位置 `50% ± 46%` 随倾角移动。

**⑤ 两个会静默毁掉整个场景的坑**

做陈列室那一页时踩的。共同点：画面里少一整块，控制台一声不响，你会以为是配色问题。

**俯角的正负。** `rotateX(+pitch)` 是把场景顶部往观察者反方向翻，等于把相机往下沉，不是往上抬。水平面的法线是 `(0, −cos p, −sin p)`，要朝向观察者必须满足

`tan p < 相机高出该平面的高度 ÷ 透视距离`

陈列室里是 `150 ÷ 1400 ≈ 0.107`，也就是 **pitch 必须小于 6°**。超过这个角，台面、盒顶、接触阴影会一起被判成背面剔除——盒子本身还好好的，所以看起来只是"忽然没有地面了"。

| 想看到的 | pitch 符号 |
|---|---|
| 台面、盒顶、地面上的投影 | 负 |
| 盒底、仰视 | 正 |

**前后顺序按质心算，不是逐像素。** `preserve-3d` 里浏览器按元素的变换质心排绘制顺序。一块 2600×800 的台座质心在 z=0，盒子放在 z=−40，整块台座就会盖在盒子上，盒子底边齐刷刷被切掉一条。规则：**子物体必须站在父级质心的前方**（盒子的 z 要大于台座的 z）。同理，不要指望一块巨大的独立地板和台座共存——两者质心一前一后，地板会翻过来盖住台座。

**为什么是弹簧，不是 CSS 过渡。** 两个源库在这点上分歧：atropos 用 `transition: 300ms ease-out`，TiltedCard 用速度状态 + 半隐式欧拉积分。**拖拽场景必须用弹簧**——过渡一旦开始就必须走完整段，手指中途反向会打架；弹簧每一帧都在重新求解，可以随时被打断。所以本风格取弹簧，`300ms` 只作为无 JS 时的降级值。

参数：`ω = 20 × 0.2^smoothness`，`smoothness 0.6 → ω≈7.6`；`ζ = 1 − 0.3 × smoothness = 0.82`。按 1/240s 子步进积分，低帧率下不抖。

**⑥ CSS 3D 的尽头：一条判定线**

前五条都是"怎么做对"。这一条是"什么时候别做"——因为下面这个限制调不出来。

**CSS 3D 没有深度缓冲。** `preserve-3d` 的绘制顺序按每个元素变换后的**质心** z 值排序，不是逐像素比较深度。这一点决定了它能表达什么：

| 场景 | 能不能 | 为什么 |
|---|---|---|
| 卡在面板上方浮动 | 能 | 两个物体只有前后关系，整体一个在前一个在后 |
| 六面盒（每面独立 z） | 能 | 六个面互不穿插，凸多面体的任意两面只有前后 |
| 九张牌立在桌面上 | **不能** | 牌的下半截在桌面之前、上半截在桌面之后——同一对物体，遮挡关系互相矛盾 |
| 一本书压在另一本上且书页外翻 | **不能** | 同上，穿插处无法用单一排序解决 |

真正的判据只有一句：**当"物体 A 的一部分在 B 之前、另一部分在 B 之后"时，CSS 3D 出局。** 这不是参数问题——把 z 调到哪里都会有一半是错的。

陈列室那一页就撞在这上面。九张立牌站在同一张桌子上，桌子的质心在 z=0，牌子的质心在 z>0，于是**整张桌子被画在牌子之后**：牌子的脚不见了。反过来把桌子 z 拉高，桌面又会盖住牌子的正面。最终交付的版本是靠"把桌面做成钟面、牌子只露出上半截"绕过去的——绕过去了，但那是回避，不是解决。

**成为 CSS 3D 的地盘，三个条件要同时成立：**

1. 每个元素只有一个深度（整体在前或整体在后）。
2. 物体之间只发生前后关系，不发生交叉遮挡。
3. 需要立体的面数在几十个以内。

六面盒 + 一块台座 + 六个盒子 = 42 个面，这条线还在 CSS 3D 这边（`showcase/pages/gallery.html` 撑住了）。再往上就该走 WebGL。

**换 WebGL 的账要算清楚，不是"更高级"。**

| | CSS 3D | WebGL |
|---|---|---|
| 深度 | 按质心排序 | 逐像素深度缓冲，任意穿插都对 |
| 明暗 | **画**出来的（预生成渐变） | **算**出来的（法线 + 衰减 + 阴影贴图） |
| 相机 | 固定在一个倾角上 | 可以自由绕转 |
| 文字 | 就是 DOM，可选中、可搜索、可读屏 | 要么 overlay 回 HTML 层，要么画进纹理等于放弃 |
| 体积 | 0 KB | three.js 压缩后 ~675 KB |
| 命中测试 | 浏览器免费给 | 自己写 raycaster，焦点态、悬停态全部重做 |

一句话：**CSS 3D 的立体感来自美术，WebGL 的立体感来自物理。** 前者在固定机位下更可控、零成本、文字是真文字；只有当"机位要动"或"物体互相穿插"变成核心需求时，后者才划算。

**还有一个两边都成立的坑：不要 billboard。** 让每张牌都 `lookAt(camera)`，等于每个观察角度渲出来的像素完全一样——世界没有"侧面"，也就没有"存在"。3D 感来自**必须绕到背面才能读到的东西**，而不是来自透视。WebGL 里这个错更容易犯，因为 `lookAt` 太顺手了。

反过来也要防：只想要"页面里有一块会转的东西"，别上 three.js。一段预渲染视频、一张 `<model-viewer>`，或者干脆就是这个风格的倾斜卡片，成本低两个数量级，而且文字还能选中。

## Shapes

- 卡片 16px，大盒面 22px，按钮/标签 pill。
- **不许混用**：同一屏里出现 8px 和 22px 两种卡片圆角，就等于承认没有规矩。
- 圆角在 3D 里有个额外要求：`border-radius` 必须写在**被倾斜的那个元素**上，写在父层会被投影裁掉。

## Components

### card

`background` 是 180° 三段渐变（`surface-hi → surface → surface-lo`），这是"一盏灯从上方照下来"的最简表达。三段而不是两段：两段会在中间出现一条硬边。

环状边缘用 `inset 0 0 0 1px rgba(255,255,255,0.08)`，上沿单独一条 `inset 0 1px 0 rgba(255,255,255,0.12)`。这两条内阴影就是"厚度"的全部来源，比投影重要。

### box（游戏盒 / 产品盒）

`aspect-ratio: 4/5` 是实体游戏盒的真实比例（DVD 盒 1.4，游戏主机盒接近 1.25）。盒面左上角一个大番号，`translateZ(30px)`——比标题浮得更高，因为它在实体包装上本来就是印在表面的。

### ring（可拖拽选择器）

CSS-only 也能转：`--t3-spin` 一个角度变量即可。拖拽的数值接口：
- 位移 → 角度：`1px ≈ 0.22°`
- 松手吸附：弹簧 ω=12 / ζ=0.85（比悬停更硬，吸附要有"咔"感）
- 拖拽判定阈值 **6px**：位移超过 6px 就不算点击。这是"拖完松手别误触"的唯一手段。

### button

橙底 + 暖黑字，`hover` 前移 12px，`active` 回落并缩到 0.98。按下时位移方向**反转**——这是物理正确性：手指按住时东西被压回去，不是继续前进。

## Do's and Don'ts

**Do**

- 让阴影和高光都有同一个"光源位置"，并且随指针移动。
- 拖拽用弹簧积分，松手有一下轻微回弹。
- 大字用 700 + −0.03em。
- 给 `prefers-reduced-motion` 把幅度降到 30%，不是关掉。

**Don't**

- 不要用 `box-shadow` 堆三层来做"立体"——那是贴纸。要么有透视，要么承认是平面。
- 不要把高光调到 0.4 以上。超过就不是受光，是发光。
- 不要在同一个 3D 场景里混用两种透视值。
- 不要给正文段落加倾角。文字一斜就不可读。

### 三处 Floor rule 破例（限定在本风格内）

| 规则 | 破例内容 | 为什么 |
|---|---|---|
| §11.2 S1 渐变 | 卡片 180° 三段渐变、高光 7 档径向渐变 | 立体 = 有光源，光源 = 有衰减，衰减 = 渐变。**判据：跟着指针坐标走、有非线性衰减曲线、有混合模式 → 是受光；固定 45° 双色、无衰减、无混合 → 是装饰。** |
| §11.2 S7 模糊/发光 | `filter: blur(20px)` 的地面投影 | 真实阴影没有硬边。模糊半径 20px 对应光源大小，不是"氛围感"。 |
| Floor rule 2 纯黑白 | 近黑 #0A0A0B 画布 | 不是纯黑；且深色是 `screen` 混合的前提，浅底做不了受光。 |

三条都只在本风格的容器内生效，**不外溢到其他风格**。

## Chinese Typography

- 中文不倾斜。`transform` 只加在卡片容器上，段落文字不参与旋转——中文笔画密度高，斜 5° 以上就开始糊。
- 中文标题字距 **−0.02em**（比英文的 −0.03 松一点）。中文字面本身已经排满，跟英文同一个值会挤。
- 行高 1.65：比 `quiet-dark`（1.75）紧。这个风格不承担长文阅读，紧一点让卡片里的两三行更"实"。
- 盒面上的中文标题最多 6 字。超过就换行，不要缩小字号——缩了就和番号抢层级。

## When to Use

用它：

- 游戏、影视、硬件的产品页和开箱页。
- 作品集首页：需要"这东西能上手"的第一印象。
- 可拖拽的选择器（选游戏、选模板、选封面）。
- 发布会主视觉、大屏展示。

别用它：

- 任何超过 300 字的正文。这套东西的全部力气在厚度，读字是净亏。
- 表单、后台、设置页。需要的是稳，不是手痒。
- 打印。透视在纸上没有意义。

## Iteration Guide

改这个风格时按顺序动这几处：

1. **先动透视**（`--t3-perspective`）。800 → 600 更夸张，→ 1200 更克制。一次只动这一个，其他先别碰。
2. **再动倾角**（`--t3-tilt-max`）。12 → 8 会明显"变懒"，→ 15 开始有轻微变形。
3. **手感想变，就动 ω/ζ**。要更黏：ω 降到 5；要更跟手：ω 升到 11；要回弹明显：ζ 降到 0.7；要不回弹：ζ 升到 0.95。**别同时动两个**，否则说不清是哪个起的作用。
4. **高光只在 0.25–0.34 之间调**。出界就是另一种东西了。
5. 改完跑 `python3 scripts/lint.py tactile-3d`，再截图看真实渲染——3D 的数值光看代码判断不了。

## Known Gaps

- **只有深色。** 浅底做不了 `screen` 混合的高光，白底上叠白光是零。要做浅色版本得换 `multiply` 或改成"阴影驱动"，那是另一套模型，没做。
- **弹簧只在 showcase 里实现，不在 tokens.css 里。** CSS 写不了弹簧，`--t3-omega` 只是给 JS 读的声明性参数。谁用这个风格，得自己把那 20 行积分器抄过去（`showcase/tactile-3d.html` 里有）。
- **陀螺仪没做。** 源库在移动端接了 `deviceorientation`（除 22 换算），本库没实现，也没测。
- **六面盒子的成本是真的。** `showcase/pages/gallery.html` 里做了真六面盒（每面独立 transform + 逐面法线 + 每帧实时光照），代价是每个盒子 6 个 DOM 节点、每帧 6 次矩阵乘，六个盒子加一块台座一共 42 个面。
- **但这个风格真正的上限不是面数，是遮挡。** 早期版本想在桌子上立九张牌，怎么调 z 都不对——牌和桌面是交叉遮挡关系，CSS 3D 处理不了。详见 Elevation & Depth ⑥。性能只是次要理由，排序模型才是硬边界。
- **大面积的明暗衰减是预生成的。** 台座正面那道"越往下越暗"和台沿的收光边都写死在 CSS 里——它们只跟距离有关，与相机姿态无关。绕到接近俯视的极端角度时，这两处会和逐帧算出来的其它面有轻微不一致。要彻底解决得改用 WebGL 写 shader。
- **动效参数没有在真机上标定过。** ω=7.6 是源库默认值在桌面浏览器的表现，iOS Safari 的 120Hz 屏上体感会更快。


## Material & Elevation

光从 `{elevation.lightSource}` 来，固定这一个方位。共 `{elevation.steps}` 级：
`{elevation.e1}` 贴面、`{elevation.e2}` 卡片、`{elevation.e3}` 浮层。
深色上层级靠明度与内描边，浅色上靠带偏移的阴影——不做居中发光。
主分隔手段是 `{elevation.separator}`，其余只做辅助。

## Mark & Media

标识：`{media.logoRule}`（`{media.logoType}`）。
图片：比例 `{media.imageRatio}`、圆角 `{media.imageRadius}`、处理 `{media.imageTreatment}`。
背景：`{media.background}`。图标：`{media.iconRule}`。空态：`{media.emptyState}`。
只写规则不写品牌资产；图片处理都是可复现参数。

## Motion & States

过渡曲线 `{motion.easing}`，快档 `{motion.durationFast}`、基准 `{motion.durationBase}`。
hover：`{motion.hover}`；焦点：`{motion.focusRing}`；展开：`{motion.openTransition}`。
交互组件逐项覆盖 default / hover / focus-visible / active / disabled / error 六态。
`prefers-reduced-motion` 时 `{motion.reducedMotion}`。
