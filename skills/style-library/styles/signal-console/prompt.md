# Signal Console · 生图 Prompt

这套风格服务界面。需要可读的监控、日志、拓扑或 AI 诊断页面时，直接用 `tokens.css` 渲染 HTML。生图只用于控制室氛围、文章头图或真实截图背景板。

## 主模板

```
a calm operations control room at night, one matte dark display showing
a dense monitoring interface, neutral graphite surfaces, thin cool-gray
dividers, small blue status accents, amber and coral reserved for alerts,
precise dense layout, diffused low light, no decorative glow,
straight-on composition, no readable text, no logos
```

## 四段公式

**材质**：matte glass、anodized metal、fine technical surfaces。避免高反光、塑料感和发光边缘。

**光线**：均匀漫射光，只让屏幕成为最亮对象。不要戏剧化侧光、霓虹轮廓和镜头光晕。

**构图**：正对屏幕，能看到操作台与多块信息区的关系。拓扑图、时间轴或日志条纹可成为几何线索，不要求文字可读。

**色彩**：深石墨、冷灰、一个蓝色运行信号；琥珀表示预警，珊瑚红表示故障。彩色面积保持很小。

## 变体

### 值班控制台

```
matte dark operations desk, one wide monitor with a restrained service
topology, thin neutral grid, sparse blue signal paths, two small amber alerts,
diffused overhead light, straight-on editorial technology photograph,
no neon, no readable text, no logos
```

### 事故复盘背景板

```
minimal dark technical workspace, left side reserved for a real screenshot,
right side soft empty graphite surface, subtle timeline marks embossed into
the desk, low neutral light, precise and calm, no glow, no readable text
```

### 硬件与网络证据

```
macro photograph of a matte black network appliance edge, a thin cool-gray
status line, one tiny blue indicator, precise machining, neutral dark gray,
shallow but not blurry, clinical product photography, no logos
```

## 负向词

```
neon, cyberpunk, purple gradient, blue-purple gradient, glowing edges,
rainbow, rgb lighting, gaming aesthetic, dramatic spotlight, rim light,
lens flare, bokeh, heavy vignette, hologram, floating glass cubes,
fake dashboard text, gibberish UI, watermark, logo
```

## 参数建议

| 项 | 建议 |
|---|---|
| 画幅 | 头图 16:9，背景板 3:2 或 4:3 |
| 光线 | 漫射、低对比、屏幕仍是主体 |
| 色温 | 中性偏冷，避免蓝色淹没画面 |
| 彩色占比 | 不超过画面 5% |
| 后期 | 压中间调，不加暖色胶片模拟和强暗角 |

## UI 不用生图

告警、日志、拓扑、时序图和 AI 建议都应由真实 DOM 渲染。生图模型无法保证状态语义、时间窗口、坐标轴、数值对齐和可访问性。
