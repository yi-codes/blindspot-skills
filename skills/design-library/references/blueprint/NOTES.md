# Blueprint｜工程蓝图 — 来源提炼

## 来源

- 类型：① 网页设计风格词典（显式色板、CSS 变量、AI 提示词、适合/不适合与踩坑）+ ① 在线风格卡（完整 design.md：字阶、间距、组件与禁令）+ ① Agent Skill 规格（连接区块、虚线与标注规则）；三份交叉验证
- 页面一：https://liuyutao.com/ai-studio/design-styles/blueprint
  - 显式值：蓝晒蓝 `#0B3D91`、面板蓝 `#0E4AA8`、图纸白 `#E8F1FF`、浅蓝线 `#9EC1FF`、标注黄 `#FFD36A`；`--ds-radius: 0`；提示词「20px 间距 rgba(232,241,255,0.12) 白线网格」「字体 Space Mono，标题 24–28px 大写加字距，正文 13px」「按钮线框白边透明底，主按钮可白底蓝字」「标注黄仅用于尺寸注记与关键数字」；踩坑「等宽全大写长句难读」「网格 16–24px 即可」「正文用近白 #E8F1FF」
  - 抓取：2026-11-25
- 页面二：https://www.stylekit.top/zh/styles/blueprint
  - 显式值：`--color-blueprint-blue: #1e3a5f`、`--color-pale-blue: #a0c4e8`、`--color-mid-blue: #4a90d9`、`--color-callout-orange: #ff6b35`、`--color-revision-violet: #b071e4`；JetBrains Mono 400/700，字阶 32/22/16/13/11/10px、行高 1.2/1.3/1.65、字距 0.08em/0.16em；base 4px、max-width 1280px、section gap 48px、card padding 20px、element gap 12px；圆角 0；网格 8px 小格白 5% + 80px 大格白 10%；Drafting Card 60% 蓝图蓝 + 12px 模糊 + 1px 白 30% 描边；辅助虚线 dash 4px / gap 4px；按钮 120ms linear；禁令「暖色背景 / 圆润柔和元素 / 渐变填充 / 彩色摄影 / 衬线或无衬线字体 / 辅助线变成装饰」
  - 抓取：2026-11-25
- 页面三：https://www.skill4agent.com/zh/skill/superhq-ai-shuru/blueprint-ui/compare
  - 显式规则：「No rounded corners」「Connected sections…No floating cards with gaps」「Dashed outlines for content boundaries」「Section labels — small monospace uppercase labels positioned over section borders」「Measurement annotations — thin dashed lines with monospace dimension labels」「Dot grid background on the page body」「Numbered elements — small monospace counters like 01, 02, 03」；色板是黑底版（#0a0a0a / #111111 / #f59e0b）
  - 抓取：2026-11-25
- star：不适用（风格词典 / 风格卡 / Agent Skill，非代码仓库）

## 取（吸收了什么，落到哪）

- 词典的五色 CSS 变量 `--ds-bg #0b3d91`、`--ds-surface #0e4aa8`、`--ds-text/--ds-line #e8f1ff`、`--ds-muted #9ec1ff`、`--ds-annotate #ffd36a` → 原样落到 `colors.canvas/surface/ink/line/ink-muted/primary`，`on-primary` 取回画布蓝以复用同一明度关系。这些是页面直接写出的 hex。
- 提示词的「20px 间距 rgba(232,241,255,0.12) 白线网格」 → 落到 `spacing.grid: 20px`、`media.background` 与 `tokens.css` 的 `.preview-root::before` 双层 linear-gradient。没有把它当装饰纹理，而是承担坐标与度量。
- 词典「标注黄仅用于尺寸注记与关键数字」「标注黄不要大面积铺底」 → 落到 `colors.primary` 的单一职责、`prompt.md` 的 ≤5% 面积约束和 `Don't`。
- StyleKit 的 `1px rgba(255,255,255,0.30)` 描边、`dash 4px / gap 4px` 辅助线、`0 0 0 1px rgba(255,255,255,0.30)` 聚焦描边 → 落到 `colors.hairline`、`elevation.e2/e3`、`Shapes` 与 `tokens.css` 的 `--bl-rule*`。纯白换成图纸白，避免裸白。
- StyleKit 的字阶比例（32/22/16/13/11/10，字距 0.08em/0.16em，400/700 两档） → 重排为 56/32/24/18/14px 五档，保留 0.08em 与 0.16em 字距、两档字重；重排理由是本库中文正文 ≥18px/1.7、模数 ≥1.25。
- StyleKit 的 max-width 1280px、base 4px、element gap 12px → 落到 `Layout` 与 `spacing` 的 4/8/12/24/32/48/96px 阶；section gap 48px 加倍为 96px，给中文标题留呼吸（加倍是本库推断）。
- Skill4Agent 的「Connected sections / no floating cards with gaps / numbered elements / section labels / measurement annotations」 → 落到 `Layout` 的共享 1px 边框与 `gap: 0` 卡片网格、`frame-grid::before` 的 `max-width: 1120px` 尺寸标注、卡片 `FIG. 01/02/03` 计数器。
- StyleKit 的按钮 120ms linear、hover 填充 12%、active 20% → 落到 `motion.durationBase: 120ms`、`motion.easing: linear` 与 `Motion & States` 的六态；本库把填充变化改成黄底/蓝底的明确反转，避免半透明叠加。
- 三份来源共同确认的「蓝底白线 + 等宽标注 + 零圆角」 → 作为 `Overview` 的定义句与 `prompt.md` 的四段式骨架，不复制任何具体品牌图纸。
- 词典「正文用近白 #E8F1FF」「浅蓝字对比可能不够」 → 落到 `Colors` 的逐项 WCAG 数字：8.83:1 / 5.51:1 / 7.07:1，并把 `ink-faint` 定在 #8BB8F5（对画布 4.91:1）。

## 弃（明确不吸收，为什么）

- **StyleKit 的画布 `#1E3A5F`** → 与词典 `#0B3D91` 正面冲突。取词典，因为它同时给出完整色板、CSS 变量和可直接执行的提示词；StyleKit 的蓝只作「蓝图确有三档蓝」的旁证。
- **Skill4Agent 的黑底 `#0A0A0A` / 表层 `#111111` / 琥珀 `#F59E0B`** → 黑底触犯本库 The Floor 第 2 条；琥珀与词典的标注黄冲突，双强调色会消解单一信号。
- **StyleKit 的 Mid Blue `#4A90D9`** → 对画布仅 3.01:1，承担链接或选中态不够稳；且会与标注黄形成两个强调色。
- **StyleKit 的 Callout Orange `#FF6B35` 与 Revision Violet `#B071E4`** → 前者对画布 3.54:1 且是暖色，StyleKit 自己禁止暖色背景、词典要求色相固定在蓝晒传统；后者是修订标记专用色，会引入紫相干扰 The Floor 第 3 条。
- **StyleKit 的「蓝图蓝 60% + 12px 模糊」描图纸卡片** → 模糊会把制图线稿变成玻璃拟物，与来源自己的「纯色填充 / 禁止渐变填充」冲突；本库用实色 `#0E4AA8` 面板，层级靠 1px 线框亮度差。
- **StyleKit 的 8px/80px 双层网格** → 与词典 20px 单层网格冲突。取 20px，因为词典提示词直接给出 rgba 透明度与用途，且 8px 在 1280px 宽屏上易产生摩尔纹；词典踩坑也写「16–24px 即可」。
- **词典的 24–28px 标题 / 13px 正文与 StyleKit 的 11/13/16/22px 字号** → 不满足本库中文正文 ≥18px/1.7、模数 ≥1.25；重排为 56/32/24/18/14px，已在 `Typography` 与 `Known Gaps` 标明是改造而非来源原值。
- **Skill4Agent 的 Inter 正文 + JetBrains Mono 标签双字体** → 词典和 StyleKit 都要求全站等宽以维持制图感；本库取全站等宽，中文回退系统黑体并在 `Chinese Typography` 写明不承诺中文等宽。
- **来源的 `text-transform: uppercase` 全大写长句** → 词典踩坑明确「等宽全大写长句难读」；只保留 FIG./DWG. 一类功能性标签，正文用正常句式。
- **彩色摄影、柔和插画、真实建筑事务所/硬件品牌/城市地铁线路图** → 风格卡明令禁止彩色摄影；品牌图纸属于他人资产，本库只写可迁移的排字与线框规则，`prompt.md` 负向词逐条禁用。
- **「高级感 / 未来感 / 精密」等形容词** → 不可写成 token，只保留 hex、20px、1px、0px、4/120ms、dash 4/gap 4 等可检查数值。

## 待观察

- 三份来源的画布色互不相同，取了词典蓝；若日后要做 StyleKit 的 `#1E3A5F` 暗蓝变体或 Skill4Agent 的黑底版，必须另开风格，不能只改 token。
- JetBrains Mono / Space Mono 都不含中文；截图环境若未安装，回退到系统等宽或黑体后中文不再等宽，56px 拉丁 display 换中文标题必须降到 32px，需真机复核。
- 描图纸 12px 模糊被弃用后，卡片层级只剩线框亮度差；在 8bit 屏或关闭 GPU 合成时 30%/60% 两档线框可能不够明显。
- 尺寸标注目前是静态 CSS 文本，没有真实比例、单位与公差体系；本风格是信息设计皮肤，不是施工图工具。
- 来源没有给出输入框、下拉、弹窗、加载态与错误态规格；`Motion & States` 的 disabled / error / open 三态是按本库六态要求推断的，不是来源显式值。
- 20px 网格在低分屏可能出现细线抖动；词典建议 16–24px 区间，尚未做逐设备采样。
