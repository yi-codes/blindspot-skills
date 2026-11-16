# Academic · 生图 Prompt 模板

**这套风格的"配图"应该是图表，不是照片。**

论文里的图是论据的一部分：坐标轴、单位、图例、误差棒。用模型生成一张照片放在论文体里，相当于在参考文献里插了一页广告。所以下面的模板只服务两类图：

1. **示意图 / 结构图**（方法流程、系统架构、实验装置）
2. **数据图的视觉骨架**（真正要画数据时请用代码画图，这里的模板只用来定"长什么样"）

真要做图表，优先用 Vega / D3 / matplotlib 直接出图，用 `tokens.css` 里的颜色。生成图只在你需要一张"概念示意"时用。

## 主模板 · 黑白示意图

```
a minimal black and white technical diagram, [画什么],
thin uniform strokes, no fill, no shading, no perspective,
serif labels in small caps, generous white space,
straight orthogonal connectors with right angles,
looks like a figure in a printed journal, no text artifacts
```

`[画什么]` 换成：
- `three boxes connected left to right in a pipeline`
- `a cross-section of a layered structure`
- `a scatter of points with a fitted line`

## 中文说明

- **只用黑线。** 蓝色只出现在链接上，图里出现蓝色会让人以为它是可点的。
- **线宽统一。** 示意图里 0.5pt 和 2pt 混用是排版错误，不是层次。
- **不要填充、不要渐变、不要透视。** 这三样一出现，图就从"论文插图"变成"商业幻灯片"。
- **标签要能被替换成真字。** 生成图里的文字一定是错的，所以宁可让它少字、留白，之后用 HTML 覆盖上去。
- **宁可空，不要满。** 论文插图的留白比图本身占的面积还大。

## 变体

**数据图骨架（用来定样式，不用来出数据）**
```
a clean line chart skeleton on white, thin grey axes, no gridlines,
serif axis labels, small tick marks pointing outward,
single black data line, no legend, no title, no annotation
```

**实验装置示意**
```
a simple line drawing of laboratory apparatus, [装置], flat orthographic view,
uniform hairline strokes, no labels, no hatching, white background
```

## 负向词

见 `../../prompts/negative.md` 通用清单，另外本风格额外加：

```
gradient, drop shadow, glow, 3d render, isometric, glassmorphism,
colorful chart, neon, dark background, texture, paper grain, vignette,
stock photo, realistic photo, hand-drawn sketch
```

## 参数建议

| 项 | 建议 |
|---|---|
| 画幅 | 4:3 或 3:2。论文插图不用宽银幕 |
| 线宽 | 让模型统一，不要"有粗有细" |
| 颜色 | 纯黑或纯白，不要灰阶过渡 |
| 后期 | 不降饱和（本来就没彩色）；可以二值化 |
| 禁忌 | 渐变、阴影、透视、填充、彩色 |

## 一句判断

把生成的图缩小到 40% 看一眼：**它还能读出来在讲什么吗？** 论文插图要在缩略尺寸下依然成立——因为它在纸上是小的。读不出来，就是画得太满。
