# 页面的六层构成

> 这是设计库的**结构宪法**。风格不是一包颜色，是一张页面自下而上叠出来的六层。
> 只写上面两层，产出必然停在"整齐但廉价"；高级感住在第 4、5 层。

---

## 为什么需要这一页

以前的原则回答"风格能不能被精确执行"，`principles.md` 回答"是不是 AI 味儿"。
但它们都没回答一个基础问题：**一张页面到底由哪些东西组成？**

结果是库把 色板 / 字族 / 字号 / 间距 / 圆角 写成了严格契约，
而高光、阴影阶梯、logo、背景图、控件展开态几乎没有定义。
生成器只要凑齐前两类字段就判"通过"，产出停在"整齐但廉价"。

这一页把六层固定下来，让每一层都有**必填字段**和**合格线**。

---

## 六层总表

| 层 | 名字 | 它决定什么 | 库里的位置 | 合格线 |
|---|---|---|---|---|
| 1 | 基础变量 | 色、字、距、圆角的取值 | front matter `colors` `spacing` `rounded` | 23/23 已有 |
| 2 | 排版 | 标题/正文/标签的字号行高字距 | front matter `typography` | 23/23 已有 |
| 3 | 组件 | 按钮/卡片/输入/导航/表格/弹窗的形态与状态 | front matter `components` + `tokens.css` | 补状态维度 |
| 4 | 材质体积 | 高光、阴影阶梯、边框明暗、质感 | front matter `elevation` | 本轮新增 |
| 5 | 标识图像 | logo、图片裁切/圆角/混色、背景、图标 | front matter `media` | 本轮新增 |
| 6 | 动效交互 | hover/focus/展开/切换的过渡与曲线 | front matter `motion` | 本轮新增 |

**第 1、2 层决定"不出错"，第 4、5 层决定"高不高级"。**

---

## 第 1 层 · 基础变量（Foundation）

**回答**：这个风格用什么颜色、多大字号、多少间距、什么圆角。

**字段**：`colors`（必填 canvas/surface/ink/line/primary）、`spacing`、`rounded`

**合格线**：
- 每个色值能用一句话说清"它出现在哪、为什么是这个值"
- `rounded` 不是单值凑数——语义化到 `card` / `button` / `tag` 各是什么形制
- 已有，不再扩建

---

## 第 2 层 · 排版（Typography）

**回答**：标题、正文、标签各自的字体、字号、行高、字距。

**字段**：`typography` 下至少 `display` / `body` / `label` 三档

**合格线**：
- 字号模数 ≥1.25；字重只用两档；中文正文 ≥18px / 行高 ≥1.7
- 已有，不再扩建

---

## 第 3 层 · 组件（Components）

**回答**：按钮、卡片、标签、输入框、导航、表格、弹窗长什么样，各状态下什么样。

**字段**：`components` + `tokens.css` 里的 `.ds-*` 组件类

**合格线**：每个交互组件至少定义 6 个状态——
`default` / `hover` / `focus-visible` / `active` / `disabled` / `error`。
组合框还要加 `open`（展开态）。

**当前缺口**：组件种类不少（约 40 个 `.ds-*` 类），但按风格零散分布，状态维度不齐。
重点补：下拉展开态、空态、加载态、错误态。

---

## 第 4 层 · 材质体积（Material & Elevation）

**回答**：块是平的还是浮的？光从哪来？靠什么表达层级？

**字段**：front matter 新增 `elevation`，结构如下：

```yaml
elevation:
  lightSource: top-left        # 固定一个方位，能指认
  steps: 4                     # 阶梯级数
  e1: "0 1px 2px rgba(...)"    # 贴面
  e2: "0 4px 12px rgba(...)"   # 卡片
  e3: "0 12px 32px rgba(...)"  # 浮层
  e4: "0 24px 64px rgba(...)"  # 弹窗
  topHighlight: inset 0 1px 0 rgba(255,255,255,0.08)
  borderLight: "{colors.hairline}"
  borderDark: "{colors.line-strong}"
  separator: border           # border | shadow | whitespace —— 主分隔手段只能选一个
```

**合格线**（呼应 `principles.md` §11.3 / §12）：
- 深色画布上**层级靠明度不靠投影**；每升一层 +3~4% L，或内描边
- 能指认光源——`lightSource` 必填，四处都有光就是 slop
- 阴影必须有偏移；`0 0 40px` 居中发光禁止
- 主分隔手段只有一个，其余退到辅助位（否则就是廉价感）

**当前缺口**：只有单值 `--xx-shadow`，12/23 有；`drop-shadow` 0/23。没有阶梯、没有高光。

---

## 第 5 层 · 标识与图像（Mark & Media）

**回答**：logo 怎么画，图片怎么切、怎么圆角、怎么和底色融合，背景是什么。

**字段**：front matter 新增 `media`：

```yaml
media:
  logoType: wordmark          # wordmark | symbol | combo
  logoRule: "字标用 {typography.display}，右侧留 0.5em，不缩放不小于 96px"
  imageRadius: "{rounded.card}"
  imageRatio: "4:3"
  imageTreatment: "去饱和 8%，叠 {colors.primary} 12% 正片叠底"  # 或 none
  background: "纯色 {colors.canvas}，无纹理"  # 纹理/渐变/图片要写具体参数
  iconRule: "1.6px 描边，20px 基准，和正文同色"
  emptyState: "用 {colors.surface-alt} 底 + 一行说明，不放插画"
```

**合格线**：
- 依赖品牌资产（真实 logo / 吉祥物 / 授权字体）→ 写"规则"不写"资产"
- 图片处理必须写成可复现的参数（比例、圆角、混色模式、透明度）
- 背景若为渐变，必须能指认光源（见 §12）；无来源的氛围渐变禁止

**当前缺口**：logo 0/23、背景图 0/23、图片策略 4/23。这是完成度的主要来源。

---

## 第 6 层 · 动效交互（Motion & States）

**回答**：hover 怎么变、下拉怎么展开、焦点环长什么样、过渡用什么曲线。

**字段**：front matter 新增 `motion`：

```yaml
motion:
  easing: "cubic-bezier(0.2, 0.8, 0.2, 1)"
  durationFast: 120ms
  durationBase: 200ms
  hover: "背景升一档明度，位移 0"
  focusRing: "3px solid {colors.primary}，offset 2px"
  openTransition: "transform scaleY 0→1，transform-origin top"
  reducedMotion: "全部过渡降到 1ms"
```

**合格线**：
- 拖拽/手势场景不用 CSS transition，用弹簧（见 §12）
- `prefers-reduced-motion` 必写
- 焦点环不能被不规则边框吞掉

**当前缺口**：只有 `--xx-duration` 一个值，没有曲线、没有展开态定义。

---

## 怎么用这一页

1. **新增风格**：`DESIGN.md` 的 front matter 必须含 `elevation` / `media` / `motion` 三组，正文必须含对应三节。模板已更新。
2. **检查**：`designlib check` 把六层列为必填，缺层报 E。
3. **验收**：`principles.md` §11 的 AI 味自查 + 本页每层的合格线。两层都过才算成立。

**记住**：lint 通过 ≠ 设计成立。但 lint 不查这几层，连"该有的东西有没有"都保证不了。
