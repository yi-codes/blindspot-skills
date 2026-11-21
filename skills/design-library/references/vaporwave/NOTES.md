# Vaporwave｜蒸汽波

## 来源

- 类型：① 二手设计风格分析 / 风格 prompt（多份交叉验证）
- 页面一：https://designmd.app/library/vaporwave-aesthetic
- 页面二：https://designmd.app/library/vaporwave-314
- 页面三：https://designforai.dev/style/vaporwave
- 页面四：https://stealthis.dev/r/style-vaporwave
- 页面五：https://chrislemke.github.io/website_designs/designs/Vaporwave.html
- 色板旁证：https://colorui.io/palettes/vaporwave-dream
- 抓取：2026-11-21
- star：不适用

## 取（吸收了什么，落到哪）

- 五份来源高度一致的核心色板：霓虹粉 `#FF71CE`、青 `#01CDFE`、薄荷 `#05FFA1`、紫 `#B967FF`、淡黄 `#FFFB96` → 落到 `styles/vaporwave` 的 `colors.primary / secondary / accent / line-strong / highlight`，角色分工照搬（粉主色、青链接与焦点、其余点缀）。
- designforai.dev 显式深底 `#1a0b2e` 与 stealthis.dev 的 `#0D0015` → 取 `#1A0B2E` 作 `colors.canvas`（深紫偏主色，满足本库深色底不用纯黑）；chrislemke 的 Grid Purple `#2D1B4E` → `colors.surface`，Static `#8B7E96` → `ink-faint`、Marble Gray `#C4B7C9` → `ink-muted`、VHS White `#FFFBFC` → `ink`。
- designforai.dev 的 14/20/28/40/56/80px 字号阶与 8/16/24/48px 间距节奏 → 取 14、20、28、40、80 五档作 `typography`（比值均 ≥1.25），8 倍数作 `spacing`。
- stealthis.dev 的 Orbitron 标题 + Space Mono 正文、designforai.dev 的 Major Mono Display / Cormorant Garamond 衬线对比 → 三档分工落到 `typography.display / cardTitle / body`，放弃纯像素字族以保证可读性。
- 四份来源共同列出的五大 motif（透视网格地板、条纹落日、CRT 扫描线、色差 / RGB 分离、glitch 抖动）→ 分别落到 `elevation`/`media.background` 的透视网格、`tokens.css` 的 `.frame-sun` 条纹落日、`motion` 与 keyframes 的 glitch；统一收口为可复现 CSS 参数。
- designmd.app 的 z-index 契约（base 0 / sticky 100 / overlay 200 / modal 300 / toast 500）与「1280px 居中、1.5rem 侧边距、768px 折单列」→ 落到 `Layout` 的宽度、断点与分层说明。
- designforai.dev 的 Do（粉青成对、透视网格、有意义的日文副标题）与 Don't（不做企业站、不做干净现代、不与赛博朋克混淆） → 落到 `Do's and Don'ts`、`When to Use`、`avoid`；日文副标题一条被弃（见下）。
- designmd.app 的 spring 物理参数（stiffness 120 / damping 20）与「只动 transform / opacity」→ 前项弃（见下），后项落到 `Motion & States` 只对辉光与位移做过渡。

## 弃（明确不吸收，为什么）

- **紫到蓝、紫到粉渐变与 `background-clip: text` 渐变字**：vaporwave 的标志性天空渐变与镀铬字，但直接触犯本库 The Floor 第 3 条（禁紫→蓝/紫→粉渐变、禁 `background-clip: text`），且渐变字对比度不可控、无法干净降级。改造为粉 `#FF71CE` + 青 `#01CDFE` 双霓虹 text-shadow 与条纹落日实色挖空，视觉语言保留、手法合规。DESIGN.md 的 Overview / Don't / Known Gaps 均标注这是对来源的改造。
- **来源里大面积霓虹发光投影（如 `0 0 20px` 多层 box-shadow 铺满卡片）**：触犯本库「阴影必须有偏移、禁居中发光、深色靠明度不靠投影」。改为有偏移的 `--va-e2/--va-e3`，且同屏 e3 最多一次，分层主要靠 `#1A0B2E → #2D1B4E → #3D2566` 的明度阶梯。
- **「日文 katakana 副标题 / 招牌」与品牌专属资产（Macintosh 专辑、Vapor95、Poolsuite 等）**：文字内容属品牌与版权资产，且让生图模型画假日文是典型破功点。只保留「年代错位」的规则，不搬任何日文字符或品牌名；prompt 明确禁日文招牌。
- **真实石膏胸像 / 棕榈 / 海豚照片与商标**：授权与不可迁移资产；`media` 只写可复现的图片处理参数，prompt 只描述物件类型，不指定具体图源。
- **spring 物理 stiffness 120 / damping 20**：本风格无拖拽 / 手势组件，LAYERS.md 规定弹簧只用于拖拽场景；`motion.dragUsesSpring` 记为 false，避免无的放矢。
- **把「日文副标题」当成可迁移元素、把主观的「dreamy / uncanny」当数值**：形容词不进契约；只保留可写成 token 或可检查规则的部分。
- ** `#FF00FF` 纯品红 / `#E50086` 热粉等扩展色**：超出三色家族约束且对比度不稳，收窄到粉青双霓虹 + 薄荷 / 淡黄小点缀。

## 待观察

- Orbitron、Cormorant Garamond、Space Mono 均不含中文，中文靠 PingFang SC 回退；霓虹辉光与宽字距在中文上的实际观感需真机复核，已在 Chinese Typography 里给出降档规则。
- 粉青改造版与严格照抄来源紫粉渐变的页面会有明显色差；若要贴近某个具体品牌，需要重新标定，但须在 The Floor 允许的范围内。
- 透视网格灭点随容器宽高比变化，`tokens.css` 用 35% 高度 + rotateX(62deg) 作近似，超宽屏（>1920px）与移动端需要单独复核。
- glitch 用 `steps(1)` 的 CSS keyframes 而非来源里的 JS 随机化，视觉节奏更可控但更规律；低端设备的动画性能与色觉障碍用户的扫描线 / 色差耐受度未做用户测试。
- Awwwards 与 Designspiration 的 vaporwave 检索页为纯图集（无文字参数），仅作风格存在性与饱和度的旁证，未从其中声称任何数值。
