# Tactile 3D · 生图 Prompt 模板

这套风格的配图逻辑是**产品渲染图**——一盏灯、一个台面、一件有厚度东西。不是插画，不是平涂，也不是"发光科技感"那种 CG。

判据只有一条：**能不能指出光从哪来。** 指不出来，就不是这个风格。

## 主模板 · 单灯台面

```
product photograph of [主体], single large softbox at upper left,
dark near-black seamless backdrop, one accent rim light from behind right,
shallow depth of field, crisp specular highlight along the top edge,
soft grounded contact shadow, subtle surface texture, no text
```

`[主体]` 换成：
- `a matte black game box standing upright, slight three-quarter angle`
- `a pair of over-ear headphones, three-quarter view`
- `a handheld console lying at a 15 degree angle`
- `a stack of three thin boxes, slightly rotated against each other`

## 中文说明

- **一盏灯，不是三盏。** 多灯会抹掉明暗交界，立体感靠的就是那条交界。
- **光要能定位。** `upper left` 这种方位必须写，否则模型会给"均匀照明"——均匀就是平。
- **接触阴影比投影重要。** `contact shadow` 是物体和台面接触处那条极窄的暗边，少了它就"飘"。悬浮感来自这条影子，不是来自模糊。
- **高光要窄。** `crisp specular highlight` 沿上边缘一条线；高光一宽就变成塑料玩具。
- **背景近黑但不是纯黑。** 纯黑背景 + 高光 = 发光物，不是受光物。

## 变体

**可拖拽的盒子阵列（对应 `.ds-ring`）**
```
seven identical matte boxes arranged in a wide shallow arc on a dark reflective table,
camera at eye level slightly above, one box lit brighter as if selected,
consistent single light source from upper left, soft falloff into black at the edges,
no text, no logos, wide 21:9 crop
```

**盒面特写（对应 `.ds-box`）**
```
extreme close-up of a matte printed game box surface, large embossed numeral in the
upper left corner catching a thin rim of light, fine paper grain visible,
dark surroundings, single light from the left, shallow focus, no text
```

**动效关键帧（做交互说明用）**
```
a single box shown mid-tilt at 12 degrees, motion implied by a faint smeared highlight
along the leading edge, dark studio backdrop, one light source, high shutter speed look
```

**材质参考板（配色阶段用）**
```
four material samples side by side on dark background: matte black plastic,
brushed dark aluminium, soft-touch coated card, clear acrylic edge,
lit by one softbox from upper left, macro, no text
```

## 负向词

见 `../../prompts/negative.md` 通用清单，另外本风格额外加：

```
neon, glow, lens flare, volumetric light, purple gradient, holographic,
glassmorphism, isometric flat illustration, cartoon, claymorphism,
multiple light sources, flat even lighting, pure black background,
oversaturated, HDR halos, floating without shadow, watermark
```

## 参数建议

| 项 | 建议 |
|---|---|
| 画幅 | 4:5（盒面）/ 16:9（产品页主图）/ 21:9（阵列） |
| 光线 | 单一主光，左上或右上；加一条窄轮廓光 |
| 色温 | 4200–4800K，偏中性略暖。太暖像食品摄影，太冷像医疗器械 |
| 对比 | 高，但暗部要留细节，不要压成死黑 |
| 后期 | 只加轻微暗角；不要加发光、不要加镜头光晕 |
| 禁忌 | 霓虹、光晕、紫蓝渐变、无影悬浮 |

## 一句判断

把图缩到 200px 宽看一眼：**还能看出这东西有多厚吗？** 能，就对了。如果只剩一个剪影或者一团发光的形状，说明模型把"受光"做成了"发光"——重来。
