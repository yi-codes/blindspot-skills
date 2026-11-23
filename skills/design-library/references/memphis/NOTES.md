# Memphis｜孟菲斯海报 — 来源提炼

## 来源

- 类型：② 风格卡 + ② 中文风格词典，辅以两篇网页设计文章交叉验证；深底复兴变体作为反例旁证
- 页面一：https://designmd.app/library/memphis （显式设计系统：色板、字号、布局、组件、动效、禁忌）
- 页面二：https://liuyutao.com/ai-studio/design-styles/memphis （显式 CSS 变量、prompt、图案参数、适合/不适合、常见踩坑）
- 页面三：https://www.city-design.cn/News/980.html （形态旁证：扁平矢量、明亮高饱和色、几何图形、扭曲曲线、无衬线）
- 页面四：https://www.swdyz.com/html/view-23594-1.shtml （形态旁证：厚重笔触、伪 3D 阴影、字体选择、微动效）
- 页面五：https://designbycurio.com/zh/learn/vaporwave-no-wait-lofi （Memphis Web Pattern Revival：近黑李子紫底 + 图案，作为未采纳变体）
- 抓取：2026-11-23
- star：不适用

## 取（吸收了什么，落到哪）

- 中文词典的显式 CSS 变量 `--ds-bg #fff8ec`、`--ds-text #111111`、`--ds-pink #ff5c8a`、`--ds-yellow #ffd23f`、`--ds-mint #3bceac`、`--ds-indigo #5b5bd6` → 落到 `colors` 的 canvas / ink / accent / highlight / secondary / primary。这五个 hex 是页面直接写出的值，不是从图里猜的。
- 中文词典 prompt 的 `--ds-border: 3px solid #111111` 与 `--ds-shadow: 6px 6px 0 #111111` → 落到 `elevation.e1/e2/e3`（3px / 6px / 10px 无模糊硬影）与 `tokens.css` 的 `--me-rule`。"不用模糊"是来源原话。
- 中文词典 FAQ 的图案公式：`radial-gradient(circle, #3BCEAC 3px, transparent 3.5px)` + `background-size: 14px 14px`；`repeating-linear-gradient(-45deg, #5B5BD6 0 5px, transparent 5px 11px)` → 原样落到 `.ds-memphis.preview-root::before/::after`，并写进 `media.background` 与 `prompt.md`。
- 中文词典的"黄色、薄荷绿底上用白色文字对比度不足，一律用墨黑文字"与"装饰图案不得压在文字后面" → 落到 `Colors` 的 `on-accent`、`media.imageTreatment`、Props 的 `Don't` 和 `prompt.md` 负向词。经计算：墨黑对玫红 6.43:1、对柠檬黄 13.08:1、对薄荷 9.54:1。
- 中文词典的字体主张："标题使用 Archivo Black，字号 36px；中文系统黑体；真实项目可用 Rubik / Fredoka / Poppins ExtraBold" → 取开源可迁移的 Archivo Black + Poppins，headline 取显式 36px；Rubik / Fredoka 未采用以避免三族混用。
- designmd.app 的布局与动效参数："1280px 居中、1.5rem 侧边距、base unit 8px、no 3-equal-columns、768px 折单列、rotate(5deg) 装饰、pop-in 480ms、hover scale 1.03" → 落到 `Layout` 的 1120px / 24px 列距 / 1.25fr 1fr 0.8fr 不等宽三卡 / 768px 断点，以及 `motion` 的倾斜回正与 `Shapes` 的 ±5° 静态倾斜。
- designmd.app 的"几何图形是装饰不是结构""拒绝层级、图案与内容平等竞争""平涂优先" → 落到 `Overview` 对后现代装饰性的定义，以及"装饰从一开始就是信息的一部分"的取舍说明；这是它区别于 `bauhaus`（几何作结构）与 `neobrutalist`（装饰更少、版式规整）的核心。
- 两篇中文网页设计文章共同确认的形态特征：扁平矢量、明亮高饱和色、方形/圆形/三角形并置、厚重线条与伪 3D 阴影、无衬线/气泡字、微妙动效 → 作为旁证写进 `Overview` 与 `Shapes`，未从配图里声称任何数值。
- designbycurio 的 Memphis Web Pattern Revival 提供了"近黑李子紫底 + 彩纸圆点 + Bacterio 波浪"的当代变体描述 → 只在 `Known Gaps` 记为未覆盖方向，说明因与库内 `vaporwave` 深底霓虹定位重叠而不收录。

## 弃（明确不吸收，为什么）

- **designmd.app 的八色高饱和扩展板**（`#FF1493` 玫红、`#0066FF` 电蓝、`#FFD700` 金、`#FF3333` 红、`#00E5A0` 薄荷、`#FF7F50` 珊瑚、`#9B59B6` 紫、`#1ABC9C` 青）→ 与词典的四色方案冲突，且八色同屏会让每屏主色消失。取词典明确给出 CSS 变量的四色，designmd.app 的色板只作为"撞色来源不同"的旁证，不进本库。
- **`#FFFFFF` 纯白画布与 `#000000` 纯黑描边**：前者触犯本库 The Floor 第 2 条，后者同时被本库与 designmd.app 点名禁止。画布改 `#FFF8EC`，描边改 `#111111`。
- **designmd.app 的 `0 2px 12px rgba(0,0,0,0.06)` 软影与"drop shadows belong to other systems"** → 与词典"6px 6px 0 硬影、不用模糊"直接冲突。本库取后者的显式规格；软影会把塑料贴面变成 Material Design，且无偏移发光触犯 slop S7。
- **designmd.app 的 `rounded.sm/md/lg = 2/4/8px` 与"sharp edges 0px"同时出现** → 圆角阶自相矛盾。本库只保留 0px 容器 / 0px 标签 / 999px 主按钮，正圆仅给图形。
- **designmd.app 的 spring stiffness 120 / damping 20、pop-in 序列与 3D 抽象主视觉** → LAYERS.md 规定弹簧只用于拖拽/手势，本风格无拖拽组件；序列动画与 3D 主视觉无法用 token 复现，只保留可检查的 CSS 倾斜与硬影。
- **designmd.app 的正文 16px/1.6、小字 14px 与字重 500/600** → 不满足本库"中文正文 ≥18px 且行高 ≥1.7""字重只用两档"。提到 20px/1.7，字重收拢到 400/700，已在 `Typography` 注明是改造而非来源原值。
- **`background-clip: text` 或紫蓝/紫粉渐变**：来源没有，也不引入；它触犯 The Floor 第 3 条，且会破坏平涂海报质感。
- **Memphis Group 商标、Carlton 书架、Bob Dylan 歌名、品牌吉祥物、真实海报扫描件** → 商标与版权资产不可迁移；`media.logoRule` 只写排字规则，`prompt.md` 负向词明确禁用。
- **"快乐 / 叛逆 / 政治性的品味"等形容词当数值** → 形容词不进契约，只保留能写成 token 或可检查规则的部分（hex、3px、6px、20% 面积、45°/5px/14px 图案参数）。

## 待观察

- 两来源对主色、阴影与圆角存在正面冲突；本库以给出完整 CSS 变量的中文词典为准，若日后要贴近 designmd.app 的"高饱和八色 + 无阴影"版本，需要另开风格而不是改本风格的 token。
- Archivo Black 与 Poppins 都不含中文；中文回退到 PingFang SC / Noto Sans SC 后标题的 Black 字面会消失，56px 降 36px 的规则需在真机复核。
- 靛蓝斜纹与薄荷圆点在低端设备或关闭 GPU 合成时可能出现色带；图案层只用了 `background-repeat` 平铺，未做逐项降级开关。
- 中文词典提醒"图案叠层过多会拖慢绘制"，本库限制为两处、≤20% 面积、不进滚动列表，但未做真实低端机性能实测。
- designbycurio 描述的是深底复兴分支，与浅色原版差异很大；本库只保留浅色版本，深底 Memphis 若要收录，需要先解决与 `vaporwave` 的场景重叠。
- 来源没有给出输入框、下拉、弹窗的 Memphis 规格；`Motion & States` 里的 error / disabled 态是按本库六态要求推断的，不是来源显式值。
