# Quiet Dark · 生图 Prompt 模板

**先说清楚定位**：这套风格是**界面**风格，不是"图片"风格。它的色值是从真实桌面客户端里抠出来的，最佳呈现方式是直接用 `tokens.css` 渲染 HTML，而不是让模型画一张"看起来像 UI"的图——模型画的 UI 永远是错的（字是乱码，间距是错的，圆角对不上）。

所以这个 `prompt.md` 只解决**两件事**：

1. 做这个风格的**氛围图 / 头图**（用来说"这是一个安静的深色工具"）
2. 做这个风格的**产品截图背景板**（即把真实截图放进一张氛围图里）

如果需要 UI 效果图，跳到最后一节"不要用生图做 UI"。

**这套风格现在有浅色模式（`ds-quiet-light`），但生图只做深色。** 浅色是给界面用的，氛围图如果做成浅色就会变成"一尘不染的北欧办公室"，跟这套语言要的气质相反。要浅色界面，用 `tokens.css` 渲染。

## 主模板 · 氛围图

```
a quiet dark workspace, single matte-black display showing a minimal
grayscale interface, no color anywhere except one small blue focus ring,
even diffused low light, no harsh highlights,
deep neutral blacks (#0d0d0d) with soft mid-gray panels (#181818, #212121),
matte surfaces, no reflections, no gloss,
large rounded corners on every visible panel, generous negative space,
shot on a 50mm lens, f/4, straight-on, centered composition,
restrained, calm, precision-engineered, no visible text
```

`[可替换]`：
- `a quiet dark workspace` → `a developer's desk at night` / `an empty design studio` / `a minimal control room`
- 想要更"冷"就把 `even diffused low light` 换成 `one soft top light, everything else falls into shadow`

## 中文说明 · 四段公式

这个库统一用**材质 → 光线 → 构图 → 色彩后期**四段来写。Quiet Dark 的四段是：

**材质**：`matte`（哑光）是核心词。一定不要 `glossy` / `reflective` / `glass`。哑光 + 深灰 = 专业感；一旦反光就变成廉价消费电子广告。关键词：`matte black`、`anodized`、`soft-touch`、`non-reflective`。

**光线**：`diffused`（漫射）+ `no harsh highlights`。这套风格**没有强光**——界面本身就是平的，光也必须是平的。别写 `dramatic lighting` / `rim light` / `chiaroscuro`，那些属于终端风格。

**构图**：`straight-on`（正对）+ `centered`。Quiet Dark 是正的、对称的、不倾斜的。别用俯拍、别用 45 度角、别用景深虚化——虚化会让人觉得这是"产品渲染图"，而它要的是"截图"。

**色彩后期**：**只有灰**。后期只调两件事：压住中间调让黑更沉，和保住那一点点蓝。绝对不要加暖色、不要加胶片颗粒的暖调、不要加暗角（暗角是"电影感"，这套要的是"工程感"）。

## 变体

**A. 产品截图背景板（最实用）**

真实截图贴上去之前的底图。留出大面积干净区域。
```
minimal dark desk surface, matte dark gray, an empty rectangle of clean
negative space in the center reserved for a screen,
diffused overhead light, no objects, no props, no cables,
neutral grayscale, subtle vignette-free falloff, top-down flat lay,
extremely minimal, nothing distracting
```
> 之后用 Figma / CSS 把真实截图叠在中间那块空区上。**不要**让模型直接画界面。

**B. 硬件特写（讲"工具"的语境）**

```
macro detail of a matte black aluminum edge, 2mm chamfer catching
a thin soft highlight, precise machining, uniform anodized surface,
neutral dark gray, no logos, no texture noise,
shallow but not blurry, product photography, clinical and quiet
```
> 这套风格的"物"是**精度**，不是"质感"。要的是倒角那条线，不是皮革、木纹、金属划痕。

**C. 空房间（讲"专注"的语境）**

```
an empty minimal room at dusk, one dark monitor on a bare desk,
no chair, no objects, walls in flat neutral gray,
light coming from a single window out of frame, soft and even,
the screen is the brightest thing in the frame but still dim,
muted, silent, architectural photography, wide shot
```

**D. 抽象层次（讲"结构"的语境）**

```
abstract composition of three overlapping rounded rectangles in
dark neutral grays (#0d0d0d, #181818, #212121), flat lighting,
large corner radii, no gradients, no glow, no perspective,
one thin 1px line of muted blue at one single edge,
graphic design, swiss, restrained, vector-like
```
> 这是唯一允许"抽象"的变体，因为它其实是在用图形复述这套风格的**分层逻辑**（三档底色 + 一条蓝线）。

## 负向词

见 `../../prompts/negative.md` 通用清单。**本风格必须额外加**（这套的失败模式很集中）：

```
glossy, reflective, screen glare, neon, cyberpunk, purple gradient,
blue-purple gradient, glowing edges, rainbow, rgb lighting, gaming aesthetic,
dramatic lighting, rim light, lens flare, bokeh, heavy vignette,
3d render, clay render, plastic toy look, isometric,
readable text, gibberish UI, fake interface, watermark, logo
```

⚠️ **经验教训（写在这里免得再犯）**：负向词必须描述**"它长什么样"**，不能只写"不要 XX"。
之前给 `terminal-mono` 写 `no CRT`，结果模型照样画了一台 CRT 显示器——因为它不知道"不要 CRT"之后该画什么。
正确写法是列出 CRT 的**特征**：`curved glass, thick bezel, scanlines, phosphor glow, beige plastic`。
同理，这套风格如果只写 `no cyberpunk` 是不够的，要写 `neon, purple gradient, glowing edges, rgb lighting`。

## 参数建议

| 项 | 建议 |
|---|---|
| 画幅 | 头图 16:9；产品背景板 4:3 或 1:1（方便裁）；氛围图 3:2 |
| 光线 | 漫射为主，无强高光。宁可平，不要立体 |
| 色温 | 中性偏冷，但**不要蓝调**（蓝调会让它变成"科技感"，这套要的是"无感"） |
| 对比 | 低对比。中间调要厚，不要拉成"黑底白线"那种硬边 |
| 后期 | 只压中间调。不加颗粒、不加暗角、不加色散 |
| 禁忌 | 任何彩色（除一处蓝）、任何反光、任何发光边缘、任何"未来感"元素 |

## 不要用生图做 UI

这是这套风格最重要的一条。

**生图模型画不出可信的界面**，原因不是画质，是它不懂约束：

- 它不知道卡片圆角必须是 16px，会随机给 6-24px
- 它不知道正文必须是 15px / 行高 1.5
- 它不知道边框是 `rgba(255,255,255,0.08)`，会画成实心灰线
- 它一定会写字，而且一定是乱码

所以：

| 想要什么 | 用什么 |
|---|---|
| 一张"这个风格长什么样"的 UI 图 | `tokens.css` 渲染 HTML，然后截图 |
| 一张"这个风格的气质"的图 | 本文件的模板 |
| 一张"这个风格的产品宣传图" | 本文件模板 A 出底图 + 真实截图合成 |

判断标准很简单：**图里有没有界面元素**。有 → 渲染，没有 → 生图。
