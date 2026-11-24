# Constructivism｜构成主义海报 — 来源提炼

## 来源

- 类型：① 网页设计风格卡（显式 CSS 变量 + Tailwind 规格 + 交互规则）+ ① 在线设计辞典（词条 + 机器可读 design.md）+ ① 风格卡（完整字阶/间距/组件/动效规格）；三份交叉验证
- 页面一：https://luckymaomi.github.io/ui/styles/constructivism
  - 显式值：`--cstv-red #cc0000`、`--cstv-paper #f2e8d5`、`--cstv-black #1a1a1a`、`--cstv-gold #d4a843`、`--cstv-brown #8b4513`；`border-4`、`shadow-[2px/4px/6px_0_0_#1a1a1a]`、`rounded-none`、`font-black uppercase`、h1 `text-6xl md:text-8xl lg:text-9xl`、h2 `text-3xl md:text-4xl`、h3 `text-lg`；交互 Block Invasion / Diagonal Aggression / Line Snap / Mechanical Easing / Soviet Reversal
  - 抓取方式：WebFetch 返回空正文，改用 `curl` 取页面源码后提取脚本内规格；2026-11-24
- 页面二：https://indexstyle.org/zh/styles/constructivism 与 https://indexstyle.org/styles/constructivism/design.md
  - 显式值：Ground `#e8ddc7`、Memorable colour `#d8251d`、Text/outlines `#11100e`；「重窄体大写」「沿对角主轴让照片与文字相撞」「粗网点、抠图、只用三色」；网页转译要求保留键盘焦点、对比度、缩放与 reduced-motion；伦理提醒「宣传联想强，须检查语境」
  - 抓取：2026-11-24
- 页面三：https://www.stylekit.top/styles/kinetic-constructivism
  - 显式值：纸 `#EFE9DC`、暖墨 `#17130E`、构成红 `#E0231B`、群青 `#1C4A87`、金黄 `#F4B301`；Inter 700/900，display 72px/0.95/-0.03em、heading 48px、subheading 32px、body-lg 22px、body 16px/1.5、label 13px/0.08em；base unit 8px、max-width 1200px、section gap 96px、card padding 24px；禁令「无圆角/阴影/渐变/发光/模糊、无第四色、一屏只有一组主导运动、只动 transform」
  - 抓取：2026-11-24
- star：不适用（风格辞典/风格卡，非代码仓库）

## 取（吸收了什么，落到哪）

- 风格卡的三色 CSS 变量 `--cstv-red #cc0000`、`--cstv-paper #f2e8d5`、`--cstv-black #1a1a1a` → 落到 `colors.primary` / `colors.canvas` / `colors.ink` 与 `colors.line`。这是页面直接写出的 hex，不是从海报配图猜的。
- 风格卡 `border-4 border-[#1a1a1a]` 与 `shadow-[4px_4px_0_#1a1a1a]` / `6px` / `2px` → 落到 `elevation.e1/e2/e3`（2/4/6px，模糊半径 0）与 `tokens.css` 的 `--co-rule`。零模糊是本库 slop S7 允许硬影的前提。
- 风格卡的字体规格 `font-sans font-black uppercase tracking-widest`、`text-6xl md:text-8xl`、`tracking-[0.2em]/[0.3em]` → 落到 display 72px/900/-0.03em、headline 36px/900、label 14px/700/0.08em；拉丁大写写在文案里，不用 CSS `text-transform`。72px 与 0.08em 的数值由 stylekit 的显式字阶交叉确认。
- 风格卡的「绝对禁止」清单：圆角、柔和阴影、渐变、柔和字重、曲线与有机形状、超过三色体系、超过 duration-100 的过渡 → 原样落到 `Shapes`、`Don't`、`motion.durationFast/durationBase`（75ms/100ms）与 `motion.easing: linear`。
- 风格卡的四条交互规则 → 落到 `motion.hover` / `motion.openTransition` / `Motion & States` 的六态：Block Invasion（侵入层 -100%→0，100ms linear）、Diagonal Aggression（translate 4px 4px、影 6→2）、Line Snap（分隔线 -2°→0）、Soviet Reversal（红黑反转、active 阴影归零）。
- 风格卡构图规则「左对齐为主、对角线分割、几何块面碰撞、极端字重对比」与辞典「以对角线为主轴、照片与文字相撞」 → 落到 `Layout` 的 1.2fr/1fr/0.8fr 不等宽卡片、-2° 静态倾斜、-12° 红楔、1200px 左对齐骨架；这是与 `bauhaus`（几何作结构）、`memphis`（图案作装饰）、`neobrutalist`（规整卡片）不同的核心。
- 辞典 design.md 的「只用三色」「粗网点、抠出的照片」「一字 dominance、两字 support」「宣传语境伦理检查」 → 落到 `media.imageTreatment`（3:2 硬边黑白裁切）、`media.background`（粗网点 ≤20% 且避开正文）、`prompt.md` 负向词与 `Known Gaps` 的伦理边界。
- stylekit 的显式布局值 max-width 1200px、section gap 96px、card padding 24px、base unit 8px → 落到 `spacing`（8/16/24/40/64/96）与 `Layout`。
- stylekit 的 `prefers-reduced-motion` 规则「循环停在构成终态，信息零丢失」 → 落到 `motion.reducedMotion`：过渡降 1ms，侵入层停在终态，倾斜与红楔保留静态原样。
- 三份来源共同确认的三色关系（红/墨/纸）与硬边零圆角 → 作为 `Overview` 的定义句，不把任何一家的插画或海报构图搬进来。

## 弃（明确不吸收，为什么）

- **风格卡的金星色 `#D4A843` 与棕色 `#8B4513`** → 来源自己写「严格三色体系，禁止超过三色」，且金色对纸底仅 1.82:1。本库只保留红/墨/纸三色，金色与棕色记在 NOTES，不进 token。
- **stylekit 的群青 `#1C4A87` 与金黄 `#F4B301`** → 属于动力学变体的三原色方案，与静态海报变体的三色封顶正面冲突；若要做动态版本应另开风格。
- **辞典的 `#d8251d` / `#e8ddc7` / `#11100e` 与 stylekit 的 `#E0231B` / `#EFE9DC` / `#17130E`** → 三份来源的红与纸各不相同。取风格卡的 hex，因为它是面向网页、给出完整 CSS 变量和组件规格的那一份；另外两套只作「构成主义确有三色关系」的旁证。
- **纯白画布 `#FFFFFF` 与绝对黑 `#000000`** → 前者触犯本库 The Floor 第 2 条；后者来源风格卡写作「纯黑」但显式 hex 是 `#1A1A1A`，按显式值取近黑。
- **风格卡的 `rounded-full` / 柔和 `shadow-sm|md|lg|xl` / `bg-gradient-to-*`** → 出现在来源的 forbidden 清单里，与 `rounded-none`、零模糊硬影直接冲突，全部弃用。
- **stylekit 的完全禁影与「一屏只有一组主导运动」** → 与本库取的 2/4/6px 硬影冲突；本库取静态海报变体的显式规格，零模糊不触犯 slop S7。动力学圆盘/钟摆/行进方块不迁移到静态变体，记录在 `Known Gaps`。
- **来源的 `text-sm md:text-base`（14/16px）正文与 `font-medium/light` 等中间字重** → 不满足本库「中文正文 ≥18px/1.7、字重两档」；提到 18px/1.7，字重收拢到 900/700，已在 `Typography` 注明是改造而不是来源原值。
- **`background-clip: text`、紫蓝/紫粉渐变、玻璃高光、发光** → 来源没有，也不引入；触犯本库 The Floor 第 3 条与 slop S1/S7。
- **历史海报构图、El Lissitzky / Rodchenko 的原作、政治标识、口号与名人肖像** → 版权与伦理边界；辞典明确要求把参考作品当证据而非素材，本库只写排字规则与几何语法，`prompt.md` 负向词逐条禁用。
- **「革命感」「紧迫感」等形容词** → 形容词不进契约，只保留能写成 token 或可检查规则的部分（hex、4px、2/4/6px、-2°/-12°、75/100ms、20% 网点面积）。

## 待观察

- 三份来源的色板、阴影态度与字体族互相冲突；本库以风格卡为准，若日后要做「辞典原色版」或「动力学版」，必须另开风格，不能只改本风格的 token。
- Impact / Haettenschweiler / Arial Narrow 都不含中文；回退到 PingFang SC 后 900 字重靠合成，72px 中文标题的窄黑字面需在真机复核。本库规定中文标题降到 36px，但仍需实机看倾斜是否切字。
- 按钮的色块侵入用 `linear-gradient` 硬停 + `background-position` 位移实现，避免 DOM 里必须包一层 `span`；它在旧版浏览器的渲染差异未做实测。
- 粗网点在关闭 GPU 合成或低端屏上可能出现摩尔纹；只做 `prefers-reduced-motion` 降级，未做逐项性能开关。
- 来源没有给出输入框、下拉、弹窗、加载态与错误态的规格；`Motion & States` 里的 disabled / error / open 三态是按本库六态要求推断的，不是来源显式值。
- 辞典提醒构成主义带有强烈宣传联想；本风格只迁移视觉语法，不提供政治口号与历史事件的迁移方案，使用者需自行做语境伦理判断。
