# 新艺术运动（Art Nouveau）— 来源提炼

## 来源

- 类型：① 网页风格卡 + ① 在线风格词典 + ① 中文风格谱 + ① 设计系统展示页 + ① 二手 DESIGN.md；五份交叉验证，均为公开网页
- 页面一：https://www.stylekit.top/en/styles/art-nouveau
  - 显式值：Deep Green `#2d5016`、Ivory `#f5f0e1`、Gold `#c9a227`、Wisteria `#8b6db5`、Leaf `#4a7c3f`、Bright Green `#4bc542`、Soft Ivory `#faf7ef`；Playfair Display 400/700，字阶 16/20/26/36/48/60px，行高 1.1（display）/1.25（headings）/1.8（body），字距 0.01em（display）/0.12em（大写标签）；圆角 cards 32px / buttons 999px / inputs 999px / frames 48px；base 8px、max-width 1080px、section gap 128px、card padding 36px、element gap 24px；Vine Button 深绿底象牙字 1px 金边 15px 字 16px/32px padding 柔影 `0 4px 15px rgba(45,80,22,0.20)`、hover 金底 `0 8px 25px rgba(201,162,39,0.40)`、active scale 0.98、500ms ease-in-out；Vine Card 32px 圆角、1px 金边 35%→60%、36px padding、藤蔓 hover 转 3deg、700ms；Wave Divider 8px 振幅 / 120px 波长；Blossom Mark 32–64px 每屏 ≤3；Curved Frame 上两角 999px / 下两角 8px；禁令「无直角几何形、无霓虹高饱和、无现代无衬线标题、无 150/200ms 短过渡、无硬边阴影」；适合「艺廊、奢侈品牌、剧院、婚礼、插画师作品集」，不适合「开发者工具、数据看板、移动工具、企业软件、快新闻」
  - 抓取：2026-11-26
- 页面二：https://aesthetic.fyi/art-nouveau/
  - 显式值：Mucha 海报四色 Gold `#C8A951`、olive `#6B7B3C`、cream `#F5EFE0`、burgundy `#8B2252`；不对称圆角 `60% 40% 55% 45%`；Playfair Display 700 italic 标题 / 400 正文；双层三层金框用伪元素叠出；金色用于边框、分隔、装饰与 hover；Good For / Not For 清单
  - 抓取：2026-11-26
- 页面三：https://styleatlas.art/styles/art-nouveau
  - 显式值：主 `#5F7550` 70% / 辅 `#B96C49` 25% / 强调 `#D2B56C` 5%；核心命题「1890–1910 年整体设计运动」；识别基因「非对称垂直延展 + 整体装饰框架」「鞭状曲线 + 植物形体 + 扁平剪影」「橄榄绿/赭石/柔金/粉彩随地域变化」「海报平面光、工艺环境光」「平版印刷、彩色玻璃、铸铁、木材、陶瓷、马赛克」；数字界面必须降低装饰密度，正文/按钮/状态/键盘焦点优先；满版结构容易挤压标题与功能信息
  - 抓取：2026-11-26
- 页面四：https://www.styleui.net/atelier/libertyDS.html
  - 显式值：Gilded Gold `#B8892A`、Peacock Teal `#2D6B6B`、Antique Rose `#9B4E5A`、Garden Sage `#7A8C6E`、Warm Ivory `#F7F3E9`；Amarante 700 标题 / Cormorant Garamond 300 italic 正文；字阶 82/48/32/22/16/10px；按钮 Teal/Gold/Outline/Rose/Ghost 五变体与 Disabled 态；输入框金色边框在 focus 时唤醒；下拉展开态、错误态；通知四态
  - 抓取：2026-11-26
- 页面五：https://designmd.app.br/library/art-nouveau-florido
  - 显式规则：曲线主导结构而非只装饰边缘；装饰必须承担导视功能；拥抱非对称平衡；颜色像金箔/旧纸/彩窗等物理材料；负空间是画框；非对称网格、No 3-equal-columns、max-width 1280px、section gap clamp(4rem,8vw,8rem)、768px 以下折叠；No pure black、saturation cap 80%、No 3-column equal-width feature layouts；横幅视觉 density 5/10、variance 8/10、motion 6/10
  - 抓取：2026-11-26
- star：不适用（风格卡 / 风格词典 / 设计系统展示页，非代码仓库）

## 取（吸收了什么，落到哪）

- StyleKit 的 `#2d5016` / `#f5f0e1` / `#c9a227` / `#4a7c3f` / `#faf7ef` → 落到 `colors.ink` / `canvas` / `line` / `leaf` / `surface` 与 `tokens.css` 同名变量；`primary` 复用深绿，`on-primary` 复用奶油纸，避免新增色相。
- aesthetic.fyi 的 burgundy `#8B2252` 与 cream `#F5EFE0` → 落到 `colors.accent` 与 `colors.canvas`；画布取它而不是 StyleKit 的 `#f5f0e1`，因为它同时给出了酒红与橄榄的配套关系。
- 风格谱的 70/25/5 面积比 → 落到 `Overview` 的「深绿占大头、金色 ≤5%」、`prompt.md` 的金色面积约束与 `Do's and Don'ts`。
- StyleKit 的 Playfair Display 400/700 与 16/20/26/36/48/60px 字阶、1.1/1.25/1.8 行高、0.01em/0.12em 字距 → 原样落到 `typography` 六档；只把正文从 16px 档移到 20px 档以满足本库中文 ≥18px/1.7。
- StyleKit 的 cards 32px / buttons 999px / frames 48px / arch 上 999px 下 8px → 落到 `rounded.card` / `rounded.button` / `rounded.frame` / `rounded.image` 与 `.preview-root::before` 的拱形金框。
- aesthetic.fyi 的 `60% 40% 55% 45%` → 落到 `rounded.whiplash`，用于 `.preview-root::after` 的鞭状曲线与卡片藤蔓伪元素，明确排除对称圆。
- StyleKit 的 Wave Divider 8px 振幅 / 120px 波长 → 落到 `spacing.base` / `spacing.wave`、`Layout` 与 `prompt.md` 的章节分隔变体。
- StyleKit 的 `0 4px 15px rgba(45,80,22,0.20)` 与 hover `0 8px 25px rgba(201,162,39,0.40)` → 落到 `elevation.e1/e2`；本库拒绝无偏移发光，来源这两级都有明确偏移。
- StyleKit 的 500/700ms ease-in-out、藤蔓转 3deg、按钮 active scale 0.98 → 落到 `motion` 与 `Motion & States` 的六态。
- StyleUI Liberty 的金色焦点边框与下拉展开态 → 落到 `motion.focusRing` 与 `Motion & States` 的 open 态，不复制它的 Amarante/Cormorant 字体组合。
- designmd.app 的「No 3-equal-columns / 非对称网格 / 曲线主导结构 / 负空间是画框」→ 落到 `Layout` 的 2 列错位网格、第一张跨两行第三张跨两列，以及 `prompt.md` 的非对称构图规则。
- 风格谱的「数字界面降低装饰密度、正文与键盘焦点优先」→ 落到 `media.background` 的 pointer-events: none、每屏 ≤3 朵花与 `motion.focusRing`。

## 弃（明确不吸收，为什么）

- **StyleKit 的 Wisteria `#8B6DB5` 与 Bright Green `#4BC542`** → 前者是紫相情感强调，触犯本库 The Floor 第 3 条的紫蓝渐变风险；后者高饱和「新芽标记」，与风格谱「低饱和、非霓虹」冲突。
- **designmd.app 的 Mauve `#E0B0FF` 与 Peacock Blue `#005F9E`** → 品牌扩展色，合进来会让低饱和海报变成多色拼贴；本库酒红已承担唯一第二强调。
- **aesthetic.fyi 的 `#C8A951` 与 StyleKit 的 `#C9A227` 冲突** → 取后者，因为它同时给出 35%/60% 的边框透明度和完整组件规格；前者只作同色旁证。
- **StyleKit 的 Leaf `#4A7C3F` 承担正文** → 对奶油底 4.31:1，不达本库 4.5 门槛；调深到 `#3F6B35`（5.44:1）作 `ink-muted`，原值只留给非文字藤蔓线。
- **金色 `#C9A227` 当小字色** → 对纸底仅 2.11:1；只走 1px 线、边框、大按钮 hover 底与焦点环，绝不进正文。
- **StyleKit 的「深/黑背景禁用」与 styleui 的深色变体** → 本库取浅色纸底路线；需要黑金对称典礼时应选 `deco-ceremony`，不靠改本风格 token 实现。
- **来源的 150/200ms 短过渡、硬边阴影、弹簧与玻璃拟物** → StyleKit 逐条点名禁止；本库连 0 模糊硬影也不留，阴影一律带偏移。
- **Playfair Display / Amarante / Cormorant 的字形资产与 Mucha 原作** → 字体只取家族与字重规则，中文回退宋体类；真实画作、车站入口与酒店徽标是他人资产，`prompt.md` 负向词逐条禁用。
- **风格谱的维也纳分离派几何分支** → 同一运动内路线冲突；本库只收鞭状曲线路线，几何对称交给 `deco-ceremony`。
- **「高级感 / 未来感 / 优雅」等形容词** → 不可写成 token；只保留 hex、32/999/48px、8px/120px、500/700ms、35%→60% 这些可检查数值。

## 待观察

- 五份来源的纸底色不同（`#F5EFE0` / `#F5F0E1` / `#F7F3E9` / `#FFFFF0`），取 aesthetic.fyi 的奶油纸；若要做更冷的 `#F7F3E9` 版本，必须另开风格而不是只改 token。
- Playfair Display 与宋体类回退在截图环境可能缺失；中文斜体为合成效果，60px display 不宜直接用于中文标题，需真机复核。
- 金色 1px 线在 8bit 屏或关闭 GPU 合成时可能抖动；35%/60% 两档金框是否足够区分，尚未逐设备采样。
- 波纹分隔与藤蔓目前是静态 CSS 伪元素，不是可编辑 SVG 路径；需要精确花形时仍需单独插画资产。
- 来源没有给出输入框、下拉、弹窗、加载态与错误态规格；`Motion & States` 的 disabled / error / open 三态是按本库六态要求推断的，不是来源显式值。
- 风格谱提醒新艺术运动在数字界面要降低装饰密度；本库的拱框与藤蔓是否仍偏重，需要真实页面截图评审后再定。
