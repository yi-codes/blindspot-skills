# Terminal Mono · 生图 Prompt 模板

用于：技术文章头图、工具发布配图、开发者活动物料。

## 主模板（可直接用）

```
extreme close-up of a dark terminal screen displaying [内容],
glowing monospace characters in soft green on near-black background,
low ambient light, faint screen glow illuminating the surrounding bezel,
slight chromatic aberration, subtle moire pattern from pixel grid,
shallow depth of field, moody and quiet, no readable text
```

`[内容]` 建议：`dense log output` / `a code editor with syntax highlighting` / `a progress bar and status lines`

注意：写 `no readable text`，否则模型会生成一串乱码，比没有更糟。

## 中文说明

- **一定要"屏幕感"**：微距 + 像素网格 + 轻微摩尔纹，这三样是这个风格的可信度来源。
- **环境要暗**：环境光比屏幕暗 3-4 档，屏幕成为唯一光源，人物剪影才会出现。
- **绿色是主色**：别用满屏彩虹色，`soft green` 或 `amber` 二选一，多了就廉价。
- **加一点不完美**：色散、光晕、屏幕反光，这些"缺陷"让画面真实。

## 变体

**人物 + 屏幕（深夜写代码的氛围图）**
```
silhouette of a person from behind, facing a glowing monitor in a dark room,
screen light as the only key light, rim light on shoulder,
monospace interface glowing, teal and amber accents,
cinematic, slight film grain, moody
```

**硬件特写（键盘、服务器、设备）**
```
macro shot of a mechanical keyboard in a dark room,
single cool light source raking across the keycaps,
deep shadows, near-black background, one small green LED reflection,
industrial, tactile, high detail
```

**抽象数据流（做技术主题的抽象配图）**
```
abstract visualization of data flow, thin glowing lines in green and amber
on pure black background, nodes and connections, technically precise,
long exposure light trails, dark and restrained, no text
```

## 负向词

见 `../../prompts/negative.md` 通用清单，本风格额外加：

```
bright background, daylight, pastel colors, rainbow, lens flare overload,
readable text, gibberish letters, watermark, cluttered desk, retro CRT scanlines
```

> 注意：`retro CRT scanlines` 放进负向是刻意的 —— 扫描线属于"复古变体"，
> 主风格不要，否则会限制使用场景。

## 参数建议

| 项 | 建议 |
|---|---|
| 画幅 | 头图 16:9；配图 3:2 |
| 光线 | 屏幕光为主光源，环境光极低，可加一盏冷色边光 |
| 色温 | 整体偏冷（6500K+），屏幕绿光本身会带一点青 |
| 后期 | 压黑位、提亮高光处的荧光、加轻微色散和颗粒 |
| 禁忌 | 纯黑纯白、满屏彩色、白天场景、可读文字 |
