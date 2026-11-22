# Frutiger Aero｜晴空拟物

## 来源

- 类型：① 二手设计风格分析 / 风格 prompt 与技能卡（四份交叉验证）
- 页面一：https://chrislemke.github.io/website_designs/examples/Frutiger_Aero.html
- 页面二：https://designmd.app/library/frutiger-aero
- 页面三：https://github.com/musicalbee/design-ontology/blob/HEAD/skills/frutiger-aero/SKILL.md
- 页面四：https://sarunasvaitkus.com/demo/vibestyle/pages/frutiger-aero.html
- 抓取：2026-11-22
- star：不适用

## 取（吸收了什么，落到哪）

- chrislemke 参考库给出的时代定位（2004–2013、"科技与自然和谐"）与九条视觉特征（Glossy Surfaces / Aero Glass / Nature Imagery / Water & Liquid / Bokeh / Skeuomorphic / Rounded Rectangles / Portal Compositions）→ 落到 `DESIGN.md` 的 Overview 与 Key Characteristics，确定这是"明亮乐观、可触摸"的展示型风格而非工具风格。
- chrislemke 的完整色板：Sky Blue `#4FC3F7`、Cerulean `#0288D1`、Fresh Green `#66BB6A`、Leaf Green `#43A047`、Water Cyan `#00BCD4`、Bubble Aqua `#80DEEA`、Sunlit Yellow `#FFD54F`、Deep Ocean `#0A4C8C` → 取 `#0288D1` 作 `primary/line-strong`、`#43A047` 作 `secondary`、`#00BCD4` 作 `water`、`#FFD54F` 作 `highlight`、`#0A4C8C` 作 `deep`。
- designmd.app 的显式 token：`bg #eaf6ff`、`surface rgba(255,255,255,0.55)`、`text #0b3d2e`、`text-muted #2f6b57`、`primary #38b6ff`、`accent #7ed957`、`sky #8fd3ff`、`green #5bd06a`、`aqua #00c2c7` → `#EAF6FF` 作 `canvas`、`#F5FBFF` 作 `surface`、`#8FD3FF` 作 `line`、`#7ED957` 作 `accent`、`#2F6B57` 作 `ink-muted`。
- anti-boring 的 Navy text `#0B2A4A` → `ink` 与 `on-primary`；对画布 13.24:1，替代来源里对比度不足的深绿正文，落进 Colors 的 Ink 组。
- design-ontology 的系统指令："玻璃按钮 = 垂直渐变 + 上半部白色高光 + 1px 浅边""天空到草地渐变、亮度 45%–95%""自然意象占主视觉 20%–60%""容器 6–12px 圆角、仅主按钮胶囊""阴影模糊 8–20px、轻发光 4–8px" → 落到 `tokens.css` 的按钮 `::before` 高光条、全幅渐变、气泡伪元素、圆角阶与 e1/e2/e3 阴影阶。
- design-ontology 的网格："960px 居中、12 列、20px 栏距；留白 25%–40%；标题→360–480px 主视觉→3/4 玻璃卡""间距 4/8/12/20/32/56px" → 落到 Layout 与 spacing 阶（收拢到 8 倍数）。
- design-ontology 的 Guardrails 反例（无渐变纯色填充、硬偏移黑影与粗黑描边、暗沉单色、破损纸纹、全 0px 直角、铬银赛博与像素字、无自然参照的抽象几何）与"何时不用"（扁平极简品牌、数据密集、已有扁平设计系统）→ 落到 `Don't` 与 `avoid`。
- chrislemke 的字体分工（Nunito 800 展示 / Nunito 700 标题 / Nunito Sans 400 正文 / Quicksand 600 强调）与 designmd.app 的 Frutiger / Myriad Pro 人文无衬线主张 → 取 Nunito + Nunito Sans 两族落到 `typography`，把 800 降到 700；字号取 anti-boring 的 43/34/27/21/17/13.5 量级，收拢成 64/40/28/20/16 五档，比值均 ≥1.25。
- anti-boring 的动效观察（"气泡上升、鱼游动、玻璃球轻浮；缓慢循环的屏保感"）与 designmd.app 的 `prefers-reduced-motion` 要求 → 落到 `motion` 的 480ms 基准档、`fr-float` keyframes 与 reduced-motion 降级。
- designmd.app 的玻璃阴影规格 `--shadow-gloss: inset 0 1px 0 rgba(255,255,255,0.9), 0 8px 20px rgba(56,182,255,0.25)` → 拆成 e1/e2/e3 的 inset 顶高光 + 带偏移外影。

## 弃（明确不吸收，为什么）

- **`#38B6FF` 亮蓝作 primary、纯白 `#FFFFFF` 画布**：前者对 `#EAF6FF` 画布只有 2.06:1，达不到强调色 3:1；后者触犯本库"浅色底不用大面积纯白、背景向主色偏一档"。primary 改取来源色板里的 Cerulean `#0288D1`（3.51:1），画布取 designmd.app 的 `#EAF6FF`。已在 Overview / Colors / Known Gaps 标注这是对来源的改造。
- **Frutiger / Myriad Pro 商业字体与 Quicksand 400 以外的多字重**：商业字体不可自由迁移、品牌辨识过强；改用可自由使用的 Nunito 家族，并把 800/600 收拢到 700/400 两档，符合本库"字重只用两档"。
- **真实热带鱼、草地、Windows XP "Bliss" 壁纸与品牌吉祥物照片**：授权与品牌资产，不可迁移；只写"物件类型 + 处理参数"，`prompt.md` 明确禁真实照片与 logo。
- **Windows / iOS 徽标、品牌专属拟物图标**：商标不可迁移；`media.logoRule` 只写字标规则，`prompt.md` 负向词列明禁徽标。
- **全盘 `auto-glow` 与无偏移居中发光**：触犯本库"阴影必须有偏移、深色靠明度不靠投影"与 slop S7；改为有偏移的 e1/e2/e3，发光只落在装饰气泡与按钮高光条。
- **`background-clip: text` 渐变字与紫到蓝/紫到粉渐变**：来源 r4ve 提到"白色到蓝色渐变填充标题"，前者触犯 The Floor 第 3 条且对比度不可控，后者来源本就没有、不引入；文字一律纯色 HTML 排版。
- **spring 物理与"鱼游动"复杂动效**：本风格无拖拽 / 手势组件，LAYERS.md 规定弹簧只用于拖拽场景，`motion.dragUsesSpring` 记为 false；鱼群动画属品牌素材，收拢成可复现的 `fr-float` 上下浮动。
- **"乐观 / 怀旧 / 乌托邦"等形容词当数值**：形容词不进契约，只保留能写成 token 或可检查规则的部分（色值、圆角、模糊半径、面积占比、对比度）。

## 待观察

- Nunito 与 Nunito Sans 都不含中文，中文靠 PingFang SC 回退；圆头人文感在中文上会打折，已在 Chinese Typography 里给出 64px 降 40px 的降档规则，需真机复核。
- 天蓝→草绿渐变与玻璃高光在低端设备或关闭 GPU 合成时可能出现色带或 `backdrop-filter` 失效；已提供 reduced-motion 降级但未做逐项开关。
- `#EAF6FF` 画布上 `#F5FBFF` 卡片与 `#DDF1FF` 面板的明度差较小，层级主要靠描边与阴影补偿；超宽屏（>1920px）与极浅显示器的可辨识度需单独标定。
- 来源 chrislemke 与 designmd.app 对同一风格给出的主色不同（Cerulean vs 亮蓝），本库取深一档以满足对比度；若要贴近某个具体品牌回放，需要重新标定，但须在 The Floor 允许的范围内。
- anti-boring 与 r4ve 的检索页含大量氛围描述但只有部分给出精确 hex；本库数值以四份来源中明确标注的色值为准，形容词仅作方向旁证，未从图集里声称任何数值。
