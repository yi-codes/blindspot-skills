# Neobrutalist · 生图 Prompt 模板

这套风格的配图逻辑是**印刷品**，不是照片，也不是 3D 渲染。

它的视觉来源是丝网印刷和 Riso 印刷：大面积平涂色块、边界锐利、颜色之间不混、纸有纤维感。所以配图应该是"印刷出来的东西"，而不是"拍出来的东西"或"渲染出来的东西"。

## 主模板 · 丝网印刷海报感

```
a bold screen-printed poster composition, [主体], rendered in flat solid color blocks,
only three flat colors: pale blue, pure black, and one saturated accent,
hard sharp edges with no gradients, visible slight misregistration between layers,
uncoated paper texture, no photographic shading, no depth of field,
high contrast, poster-like crop, generous flat negative space, no text
```

`[主体]` 换成：
- `a chair, side view, geometric`
- `a hand holding a tool, simplified to flat shapes`
- `an abstract arrangement of circles and bars`
- `a pair of sneakers, exploded flat view`

## 中文说明

- **只有三色。** 浅蓝（对应画布）+ 黑（对应边线）+ 一个饱和色（对应图表五色里的一个）。第四色一出现就散了。
- **平涂，不混色。** 相邻色块之间是硬边，不是渐变过渡。这是丝网印刷的物理限制，也是这套风格的可信度来源。
- **套印错位是加分项。** `slight misregistration` 这句不要删——它让图看起来是"印歪了的真东西"，而不是"设计软件里做出来的图"。
- **不要投影、不要景深。** 照片语言在这套风格里是错的。
- **裁切要狠。** 主体可以出画，边缘可以被切断——海报不追求完整。

## 变体

**扁平插画（用在功能说明里）**
```
flat vector illustration of [场景], thick 4px black outlines on every shape,
flat fills only, no gradients, minimal geometry, off-white background,
bold and crude rather than polished, no shadows
```

**产品截图背景板（把真实截图贴上去用）**
```
a flat pale blue field with a few solid black geometric shapes at the edges,
completely empty center, no texture, no gradient, poster margin proportions
```

**人像版（团队页）**
```
high contrast portrait of [人物], lit from one side into near-flat tones,
printed in three flat colors only, visible halftone dots in the midtones,
plain background, direct gaze, slightly confrontational crop
```

## 负向词

见 `../../prompts/negative.md` 通用清单，另外本风格额外加：

```
gradient, soft shadow, drop shadow, glow, blur, bokeh, glassmorphism,
3d render, claymorphism, isometric, photorealistic, soft focus,
muted pastel, low contrast, thin hairline strokes, watermark
```

## 参数建议

| 项 | 建议 |
|---|---|
| 画幅 | 4:5 或 1:1（海报比例），也可 16:9 做横幅 |
| 对比 | 高。压暗部、提亮部，中间调尽量少 |
| 颜色数 | 严格三色，最多四色 |
| 后期 | 加一点套印错位和纸纹；不要加颗粒噪点（那是复古，不是粗野） |
| 禁忌 | 渐变、模糊、3D、柔和阴影 |

## 一句判断

把生成的图缩到手指大小看一眼：**还能看出是几个色块拼的吗？** 能，就对了。如果糊成一团颜色过渡，说明模型偷偷加了渐变——重来。
