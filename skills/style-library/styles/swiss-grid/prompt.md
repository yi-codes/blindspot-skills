# Swiss Grid · 生图 Prompt 模板

用于：产品视觉、功能配图、案例封面、B 端物料。

这个风格的生图**不是画网页**，而是做"有严格几何秩序的产品静物"。
如果你需要的是网页截图效果，用 tokens.css 直接渲染，别用生图。

## 主模板（可直接用）

```
minimal product still life of [你的主体], on a seamless white surface,
large softbox from above, crisp defined shadow edge,
strictly centered geometric composition, camera perfectly level,
palette limited to off-white, light grey and near-black
with a single saturated blue accent object,
high key, clean negative space, swiss design sensibility,
sharp focus throughout, no text
```

主体示例：
- `a matte aluminium cube`
- `a stack of three ceramic tiles`
- `a pair of wireless earbuds`
- `a glass of water with a clean meniscus`

## 中文说明

- **相机必须水平**：稍微俯拍或仰拍就破坏了网格感。加 `camera perfectly level, eye-level` 保险。
- **阴影要"锐"**：柔光箱 + 边缘清晰的投影，这是瑞士风格的关键 —— 光柔和，但影子有边界。
- **一个饱和色锚点**：全画面灰白的时候，一个高饱和的小物件（通常是蓝色）撑起整个画面。
- **不要道具堆叠**：一个主体 + 一个陪体，最多两个，再多就乱。

## 变体

**抽象几何（做章节封面、模式图）**
```
abstract geometric composition, [圆形/条纹/网格] objects arranged on a strict grid,
hard shadows, off-white background, single blue accent,
flat lay, top-down, architectural photography style, precise, no gradient
```

**办公/工作场景（团队页、招聘页）**
```
bright minimal workspace, white desk, one laptop and one notebook aligned to grid,
large window soft light, neutral palette, no clutter,
slightly elevated three-quarter view, architectural interior photography
```

**人物版（团队头像位）**
```
studio portrait of [人物描述], plain light grey backdrop, two-point lighting,
sharp shadow under chin, neutral expression, centered, shoulders square to camera,
corporate but not stiff, high key
```

## 负向词

见 `../../prompts/negative.md` 通用清单，本风格额外加：

```
tilted horizon, dutch angle, warm orange tones, film grain, bokeh, clutter,
vintage, retro, textured background, dramatic lighting, moody
```

## 参数建议

| 项 | 建议 |
|---|---|
| 画幅 | 案例封面 4:3 或 3:2；配图 1:1 |
| 光线 | 大面积柔光 + 硬投影，光比控制在 1:2 以内 |
| 色温 | 中性偏冷（5500-6000K） |
| 后期 | 提亮高光、压暗中间调一点点、**不要加颗粒** |
| 禁忌 | 暖调、颗粒、浅景深、倾斜、装饰性背景 |
