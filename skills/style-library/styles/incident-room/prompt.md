# Incident Room · 生图 Prompt

这套风格用于事故响应界面和事故复盘背景。事故页面必须由真实 DOM 渲染；生图只负责营造“共同值班、集中注意力、证据充分”的场景。

## 主模板

```
a quiet incident response room at night, one wide matte charcoal display
showing a structured incident timeline and small service topology,
warm neutral black surfaces, thin muted dividers, one amber decision marker,
one restrained coral fault marker, diffuse low light, straight-on composition,
clinical and focused, no readable text, no logos
```

## 四段公式

**材质**：暖黑哑光金属、细纹桌面、磨砂屏幕。避免玻璃反光、强金属高光和发光边框。

**光线**：室内均匀漫射光，屏幕亮度略高于环境但不刺眼。不要戏剧化红蓝光。

**构图**：正对工作台，可保留键盘或纸张作为值班环境；屏幕上的时间线和拓扑可被辨识为结构，但不需要文字。

**色彩**：暖黑、灰褐、低饱和琥珀；故障红极小面积出现。不要把整张图染成警报红或赛博蓝。

## 变体

### 事故指挥台

```
one operator station in a quiet incident room, two matte displays,
the larger screen reserved for a real incident timeline screenshot,
small topology graphic on the second screen, neutral dark surfaces,
diffused overhead light, calm urgent atmosphere, no readable text, no logos
```

### 交接记录背景板

```
minimal warm-black desk surface, left half empty for a real interface
screenshot, right half showing faint chronological embossed marks,
one amber edge light, matte paper notebook closed nearby,
top-down editorial photography, no glow, no readable text
```

## 负向词

```
neon red alert room, cyberpunk, blue-purple gradient, hologram,
glowing edges, cinema red emergency lighting, smoke, lens flare,
gibberish UI, fake charts, watermark, logo, heroic poster composition
```

## 参数建议

| 项 | 建议 |
|---|---|
| 画幅 | 场景 16:9，截图背景 3:2 |
| 光线 | 漫射、安静、屏幕略亮 |
| 色温 | 暖黑与中性灰，少量琥珀 |
| 彩色占比 | 不超过画面 4% |
| 后期 | 保留中间调，不加彩色光晕和强暗角 |

## UI 不用生图

事故状态、时间线、负责人、审批和回滚结果必须来自真实界面。生图无法表达准确时间、状态转换和审计责任。
