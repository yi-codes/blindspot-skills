# Soft Pastel · 生图 Prompt 模板

这套风格的配图是**水彩和晨雾**，不是照片，不是插画，不是 3D。

它的界面是低对比、多层半透明色叠出来的，所以配图也必须"没有硬边、没有纯色、没有一个锐利的转折"。照片里的清晰边缘会和界面打架。

## 主模板 · 柔光水彩

```
a soft watercolor wash of [主体], very low contrast, edges bleeding into wet paper,
desaturated pastel palette of dusty lavender, pale blue-grey and warm blush,
no hard outlines, no black anywhere, generous white paper showing through,
diffused morning light, no shadows darker than 15%,
calm and unhurried, lots of empty space, no text
```

`[主体]` 换成：
- `a few overlapping circles`
- `a branch with small leaves`
- `a cup and saucer, barely suggested`
- `an abstract field of soft color`

## 中文说明

- **没有黑。** 图里一个纯黑像素都不要有——这套配色的墨是 #4C4F69（带紫的近黑），不是黑。图里出现黑边会立刻显得"硬"。
- **对比度要压到 15% 以内。** 阴影不能深，因为深阴影 = 强光源 = 戏剧感，而这个风格的全部努力是不戏剧化。
- **边缘必须是"洇开的"**。`bleeding into wet paper` 这句是核心：它保证了没有锐利边缘。
- **色相贴着界面走**：薰衣草紫、灰蓝、暖粉。不要引入绿和橙——界面里绿橙在浅色版根本不能当文字色，配图里也不该抢。
- **留白要过半。** 柔色的图如果把画面填满，就会变成"一坨颜色"。

## 变体

**纹理底图（页面区块的背景）**
```
soft watercolor gradient wash on cold-press paper, lavender to pale blue-grey,
extremely low contrast, no visible brush strokes, no vignette, seamless
```

**人物版（社区头像、团队页）**
```
soft portrait of [人物] in diffused window light, low contrast, pastel grading,
desaturated and slightly hazy, no harsh shadows, plain pale background,
gentle expression, looking slightly away, no strong color in the frame
```

**空状态插图（用在小程序/产品里）**
```
a minimal soft illustration of [空的容器], flat pastel fills with no outlines,
rounded organic shapes, very light and airy, off-white background,
a single small accent of dusty lavender, no text
```

## 负向词

见 `../../prompts/negative.md` 通用清单，另外本风格额外加：

```
high contrast, harsh shadow, pure black, hard outline, sharp edge, neon,
saturated, neon gradient, hdr, glossy, metallic, 3d render, clay render,
photorealistic, dramatic lighting, vignette, heavy texture
```

## 参数建议

| 项 | 建议 |
|---|---|
| 画幅 | 16:9 或 4:5，看用在哪 |
| 对比 | 主动压。生成完可以在后期把黑场抬到 20% |
| 饱和度 | 降 20-30% |
| 后期 | 轻微高斯模糊 0.3-0.5px（把边缘洇开）；不要加噪点 |
| 禁忌 | 黑、锐边、强光源、高饱和 |

## 一句判断

把生成的图缩到 20% 大小时，它应该**几乎看不清是什么**，只剩一团柔和的颜色——这对。如果缩到 20% 还能一眼看出主体轮廓，说明边缘太硬了，这套界面会压不住它。
