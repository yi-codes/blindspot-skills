# 负向词（通用清单）

## 为什么要有这个

生图模型的默认倾向是"多、满、艳、锐"。你什么都不说，它就往这个方向跑。
负向词的作用不是"排除某个东西"，而是**把模型拽回你要的那一侧**。

## 通用负向（几乎所有场景都加）

```
text, watermark, signature, logo, gibberish letters,
oversaturated, HDR, heavy vignette, lens flare overload,
cluttered, busy background, tilted horizon, dutch angle,
low resolution, jpeg artifacts, deformed hands, extra fingers
```

> `text` 这条最重要：不加的话模型会自作主张加各种假字，比空白难看得多。
> 如果你**确实要**文字，别用生图，用 HTML/CSS 渲染再截图。

## 按风格追加

| 风格 | 追加负向 |
|---|---|
| Editorial Serif | `neon colors, pure white background, glossy plastic, stock photo smile` |
| Swiss Grid | `warm orange tones, film grain, bokeh, vintage, dramatic lighting, clutter` |
| Terminal Mono | `bright background, daylight, pastel colors, rainbow, retro CRT scanlines` |

## 按需求追加

**要干净商业感** → `grain, noise, dust, scratches, moody`
**要真实生活感** → `studio perfect, plastic skin, symmetrical, sterile`
**要留白放文字** → `busy composition, full frame subject, centered clutter`
**要人物自然** → `posed, looking at camera, forced smile, over-retouched, plastic skin`

## 一个反直觉的点

负向词**不是越多越好**。堆三十个词，模型会把权重摊薄，该排除的反而排除不掉。
经验值：**8-12 个**，挑最要命的。

真正管用的顺序是：
1. 先改正向词（大概率是正向描述冲突了）
2. 再从上面清单里挑 2-3 个对的
3. 还不行，就换一个风格模板重来，别在原地加词
