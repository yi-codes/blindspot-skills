# 夜色舞台 · 生图 Prompt 模板

这套风格的配图逻辑是**现场摄影**，不是产品图。

区别在主体：`tactile-3d` 拍**一件东西**，光是为了说明它有多厚；这一套拍**一个空间**，光是为了说明它有多深。所以画面里要留出"没被照到的地方"——那不是留白，那是这套风格的主角。

判据只有一条：**能不能指出光从哪来，并且画面里有没有一块明显更暗的地方。** 两条缺一，就不是这个风格。

## 主模板 · 单光源现场

```
photograph of [场景], a single warm tungsten lamp as the only light source,
deep shadows falling into complete darkness at the frame edges,
visible dust in the air catching the light, matte surfaces with no specular
highlights, one quiet object half-lit at the edge of the pool of light,
35mm, natural vignette, no text
```

`[场景]` 换成：

- `an attic room with a low wooden table, stacked books and a single candle`
- `a stone cellar with barrels along a low wall, one hanging bulb`
- `a small chapel interior at night, one candle on the stone floor`
- `a belfry with a rope and a wooden ladder, moonlight through a narrow opening`

## 中文说明

- **一盏灯，写在 prompt 里。** 不写就会给"环境光充足"，那是白天。
- **必须留出纯黑的一角。** 这块面积小于画面 15% 时，画面读起来是"暗色调产品图"，不是"夜里"。这是最容易漏的一条。
- **哑光要显式禁止高光。** `no specular highlights`、`matte`、`chalky` 都要写。模型默认会给一层润泽表面——那是塑料，不是纸和木。
- **尘是深度的证据。** `visible dust in the air catching the light` 这一句让画面有了"空气"，而空气是"房间"和"背景板"的分界线。
- **钨丝灯，不是"金色光效"。** `warm tungsten lamp` 是光源，`golden glow` 是滤镜。前者有方向和衰减，后者只是染色。
- **主体只被照到一半。** `half-lit` 比 `fully lit` 好，因为明暗交界线本身携带信息——它告诉你光是从哪边来的。

## 变体

**票根 / 纸张特写（对应 `.ds-ticket`）**
```
macro photograph of a thick letterpress ticket lying on a dark wooden surface,
one warm lamp from the upper right raking across it, visible paper fibre and
embossed edge catching a thin line of light, the left third of the ticket
falling into shadow, matte, no gloss, no text
```

**招牌（对应 `.ds-marquee`）**
```
a painted wooden signboard above a doorway at night, only the light from below
reaching it, the upper half sinking into darkness, chipped matte paint,
no neon, no bulbs, no reflections, straight-on view
```

**场景对照（做多主题版本时用，对应三套光）**
```
three photographs side by side of the same small room, each lit by one different
source: a warm tungsten bulb, a green-shaded work lamp, a cold blue moonlit
window. identical furniture and camera position, only the light changes,
matte surfaces, deep shadow, no text
```
这一组是用来验证"换场景只换灯"这个主张的——**家具不动，光是变量。**

**氛围参考板（配色阶段用）**
```
four material samples on a black surface lit by one distant warm lamp:
worn dark wood, matte cream paper, tarnished brass edge, blackened stone.
the near edges fall out of the light entirely, no gloss, macro, no text
```

## 负向词

见 `../../prompts/negative.md` 通用清单，另外本风格额外加：

```
neon, neon sign, glow, bloom, lens flare, volumetric god rays, purple gradient,
golden hour, studio softbox, even lighting, ambient fill, glossy, wet look,
specular highlight, chrome, metallic sheen, HDR, oversaturated,
claymation, 3d render, isometric, flat illustration, watermark
```

## 参数建议

| 项 | 建议 |
|---|---|
| 画幅 | 3:2（现场）/ 4:5（票根、招牌特写）/ 21:9（舞台横幅） |
| 光线 | 单一实用光源（灯、烛、窗），位置写死；不要柔光箱 |
| 色温 | 2600–3200K 为主光。冷调场景走 5600K 月光，但要单独说明 |
| 对比 | 高，且**允许暗部死黑**。这一套和 `tactile-3d` 正好相反：那边暗部要留细节，这边暗部就该是黑的 |
| 后期 | 加暗角，压 0.5–0.7；不加发光、不加光晕、不加颗粒以外的东西 |
| 禁忌 | 霓虹、光晕、紫蓝渐变、均匀照明、釉面高光 |

## 一句判断

把图缩到 200px 宽看一眼：**还能看出这个房间有多深吗？** 能，就对了。

如果只剩一团被照亮的东西浮在黑底上，说明模型把"现场"做成了"产品图"——它拍的是物体，不是空间。重来，并且把 `dust in the air` 和"must leave a black corner"写得更明确。
