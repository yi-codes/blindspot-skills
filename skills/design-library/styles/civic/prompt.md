# Civic · 生图 Prompt 模板

**先说清楚：这个风格基本不该配图。**

Civic 的说服力来自"这是官方信息，没有人在向你推销"。一张精心构图的气氛图会立刻破坏这件事——它把"通知"变成"广告"。所以下面的模板只解决两种被动场景：

1. 页面顶部需要一个**说明这是什么文件**的横幅（比如"办事指南"栏目的头图）
2. 需要一张**实物照片**做信任背书（盖了章的表格、贴了标签的档案袋）

如果你正在犹豫"这里要不要放张图"，答案是不要。

## 主模板 · 文件感氛围图

```
overhead flat lay of an official paper form on a plain white desk,
single form, black ballpoint pen resting diagonally, one rubber stamp beside it,
even neutral daylight from above, no shadows to speak of, no warm grading,
matte paper with visible fibre, slight fold crease,
straight-on top view, generous empty margin at the top for a heading,
plain, bureaucratic, unhurried, no text, no logos
```

`[可替换]`：
- `an official paper form` → `a stack of stapled A4 documents` / `a manila envelope with a typed label` / `a printed table with hand-filled columns`

## 中文说明

- **顶光，平光，不要侧光。** 侧光会造出氛围，氛围是这个风格的反面。要的是"扫描件"那种没有情绪的光。
- **不要暖调。** 一点暖色就会让图变成"手作感"，和这套界面（纯白 + 近黑）冲突。
- **要留白给标题。** 顶部留出 1/3，`empty margin at the top for a heading` 这句别删。
- **不要人手。** 有手就有场景、有情绪、有叙事。这里只需要物。
- **可以有瑕疵**：折痕、印章略歪、笔帽没盖。轻微的不完美是"这件东西真实存在"的证据——但不能是"设计过的复古颗粒"。

## 变体

**章节头图（无主体，纯材质）**
```
macro detail of uncoated white paper, cold neutral light, visible paper fibre only,
no vignette, no gradient, high resolution scan look, extremely plain
```

**"已完成"状态的隐喻图（用在一篇办事指南的结尾）**
```
a single document in a plain folder, closed, on a bare desk,
flat even light, no props, no decoration, quiet and final
```

## 负向词

见 `../../prompts/negative.md` 通用清单，另外本风格额外加：

```
moody lighting, warm color grade, film grain, bokeh, hands, people, coffee cup,
desk plant, laptop, lifestyle props, gradient background, drop shadow,
minimalist branding mockup, isometric illustration, 3d render
```

## 参数建议

| 项 | 建议 |
|---|---|
| 画幅 | 头图 16:9 或 3:1（更扁，像文件抬头）；不要方形 |
| 光线 | 顶光或均匀漫射，不要侧逆光 |
| 色温 | 中性偏冷（5600-6000K） |
| 后期 | 不降饱和、不加颗粒、不加暗角。加任何一个都会变成"设计过的照片" |
| 禁忌 | 人手、道具、暖调、任何渐变 |

## 一句判断

生成出来之后看一眼：**这张图会不会让人觉得"这个页面想让我喜欢它"？** 会，就删掉。
