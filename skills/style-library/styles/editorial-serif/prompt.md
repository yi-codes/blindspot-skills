# Editorial Serif · 生图 Prompt 模板

用于：博客头图、文章配图、封面、品牌故事页背景。

## 主模板（可直接用）

```
editorial still life, [你的主体], resting on textured cream paper,
single soft window light from the left, gentle falloff into shadow,
muted earth palette of bone white, warm grey and one small rust-red accent,
analog film grain, medium format look, shallow depth of field,
generous negative space on the right for text,
quiet and considered mood, no text
```

把 `[你的主体]` 换掉即可，例如：
- `a folded linen cloth`
- `a ceramic cup and a mechanical pencil`
- `a closed hardcover book with worn edges`
- `a single dried branch`

## 中文说明

- **主体选材质，不选场景**：纸、布、陶、木、金属的质感是这个风格的灵魂，不要"一个人坐在咖啡馆"这类叙事画面。
- **必须留白**：右侧或上方留出一大块空地给标题用，`negative space on the right for text` 这句别删。
- **要一个赭红小物件**：面积控制在画面 5% 以内，起到视觉锚点的作用。
- **颗粒感**是必需的：这个风格靠"不完美"建立真实感，太干净会变成影棚产品图。

## 变体

**给长文做纹理底图（无主体）**
```
seamless texture of aged cream paper, subtle fiber and foxing spots,
raking light revealing surface relief, warm neutral, high resolution scan look
```

**人物版（作者头像位、访谈配图）**
```
environmental portrait, [人物描述], seated near a window, natural side light,
warm neutral color grade, slight desaturation, film emulation,
looking away from camera, candid, negative space above
```

## 负向词

见 `../../prompts/negative.md` 通用清单，另外本风格额外加：

```
neon colors, pure white background, glossy plastic, HDR, heavy vignette,
stock photo smile, busy composition, centered symmetrical layout
```

## 参数建议

| 项 | 建议 |
|---|---|
| 画幅 | 头图 16:9 或 21:9；配图 4:5 或 1:1 |
| 光线 | 单侧自然光，柔，别用柔光箱（太均匀就死了） |
| 色温 | 略暖（4800-5200K） |
| 后期 | 降饱和 10-15%，加颗粒，抬黑位一点点（不要纯黑） |
| 禁忌 | 不要 HDR、不要锐化过度、不要纯白背景 |
