# Nutlope/hallmark · `skills/hallmark`

来源：https://github.com/Nutlope/hallmark （55.6k★，"Anti-AI-slop design skill for Claude Code, Cursor, and Codex"）
抓取：`skills/hallmark/SKILL.md`、`references/gates.md`（243 行）、`references/dark-mode.md`（49 行）
抓取日期：2026-11-16

> **这是这次找到的最有价值的一份东西**，而且它解决的不是"风格"问题，是"AI 味儿"问题。
> 它是一套 **70 多条 gate（闸门）**，每一条描述一种"一看就是机器做的"的具体特征，然后给修法。
> 它把这个叫 slop（泔水）。它甚至带一个 `scripts/sloplint.mjs`。

## 它的结构值得抄

每条 gate 三个字段，这是它比"设计原则"强的地方：

| 字段 | 含义 | 为什么重要 |
|---|---|---|
| **Tier** | Floor（永不豁免）/ Reflex（可豁免但要写理由）/ Finish（不阻塞）/ Ledger | **承认"规则不是绝对的"**，但要求你为破例写明理由 |
| **Class** | M（CSS 静态检查）/ R（渲染后检查）/ J（人判断） | 明确哪条能自动化、哪条只能人看 |
| **The tell / The fix** | 症状 / 修法 | 不是"要好看"，是"看到 X 就改成 Y" |

`§ 3 Pre-emit critique` 还有一个六轴自评（Philosophy / Hierarchy / Execution / Specificity / Restraint / Variety，各 1-5 分），
**低于 3 分就先改再动手**。其中 Specificity 的定义是：**"能不能属于别的产品"——不能才是 5 分**。

自己那条“Signature / 签名”的判据跟 bergside 那份假文档的差别，就在这里。

## 取 —— 直接命中我自己的 6 条

我拿它的 gate 表过了自己那四个风格 + `showcase/codex.html`，**中了 6 条，其中 3 条是真问题**：

| Gate | 症状 | 我哪里中了 | 判定 |
|---|---|---|---|
| **65** | 米色纸 + 高对比衬线 + 陶土色（"AI 最认得出的一种长相"） | **`editorial-serif` 就是这个**：`#FBF8F3` 米色 + 衬线 + `#A63D2F` 陶土红 | 真问题。这就是用户说的"太普通"的根源 |
| **67** | 15px 以下、全大写、字距 >0.03em 的小标签 | `codex.html` 的 `.eyebrow`：`uppercase` + `letter-spacing:.09em` | 真问题。而且**我自己的 DESIGN.md 里写着"界面标签不用全大写"，demo 却违反了自己** |
| **63** | 用中点 `A · B · C` 拼元信息串 | `codex.html`：`12 分钟前 · 已合并`、`20/20 通过 · 耗时 42.6s · 分支…` | 半真。App 的元信息行确实这么写，但一口气三个点就是模板感 |
| **54** | eyebrow：标题前面那句"宣布下面是什么"的短标签 | `codex.html` 里 `<div class="eyebrow">CODEX</div>` | 真问题。删掉它什么都没丢，说明它只是个名字 |
| **7a** | `#000` / `#fff` 出现在 token 块之外 | `.pill.solid:hover { background:#ffffff }` | 真问题。一行的事 |
| **1** | 系统字体当 display | `quiet-dark` 全用系统字体 | **不成立**。它的 guard 是"风格的材料本身就是系统字体"——一个 macOS 原生 app 界面，系统字体是唯一正确答案，换别的才是造假 |
| **2a** | 紫到蓝的渐变 | — 我没有 | 逃过 |

### 抽出来的三条通用判据

1. **`Specificity` 是唯一真指标。** 拿掉产品名，这份设计还站得住吗？站得住 = 它不属于任何产品 = 它是模板。
2. **"宣布型标签"是机器最爱的装饰。** 标题前面加一行小字说"下面是标题"，是 typographic 版的"请注意"。删掉试试，什么都不丢，就该删。
3. **豁免要写理由，且理由得跟这个页面有关。** 它的 waiver 规则：少于 24 个字符、套话、或者跟别处一字不差 → 驳回。**这条比规则本身更重要**——它把"例外"变成了要留痕的动作，而不是随口一说。

## 取 —— 一条我完全没有的暗色规则

`dark-mode.md` 里这句，四个风格里没有一处提到：

> **Reduce body `font-weight` by 50 units (400 to 350) in dark; light-on-dark text reads optically heavier.**

深色底上的亮字，视觉上会比实际更粗（光渗 / irradiation）。
所以同一套排版，深色版的正文应该减 50 字重。我原来 `quiet-dark` 所有正文都是 400，在 `#0d0d0d` 上确实偏重。
→ 已写进 `quiet-dark/tokens.css`（`--qd-weight-body: 350`）和 `principles.md` §11。

## 取 —— 它验证了我的两个判断

- **`--color-paper` L 12-18%，never `#000`** / **`--color-ink` L 92-96%，never `#fff`** → 我的 `#0d0d0d` / `#f7f7f7` 正好落在区间内（画布比它的下限还暗，因为 Codex 真的更黑）。
- **"Elevation is lighter: +3% L per level"** → 我的 `#0d0d0d → #181818 → #212121` 每档正好 +4% 左右。
- **"Shadows off in dark. Elevation is lightness or an inset hairline ring."** → 跟我在 `quiet-dark` 里写的一字不差（`box-shadow: inset 0 0 0 1px`）。两条独立路径撞到同一个结论。

## 弃

- **它整套是给「落地页 / 营销页」写的。** 一半以上的 gate 在管 hero 高度、section 间距、CTA 位置、邮件订阅栏——这些在 app 界面里根本不存在。
  gate 58「一个 900px 视窗不超过约 80 个词」用在 Codex 的 diff 视图上就是荒谬的。**不能整套搬。**
- **它要求每个产物留一个 CSS 注释戳**（`/* Hallmark · pre-emit critique: P5 H4 … */`）。这套自我审计的仪式感对单人使用的风格库太重了。
- **它的 gate 74「不许用框架默认色板」** 和我的实际处境冲突：`terminal-mono` 里 `#A3A3A3` 就是 Tailwind `neutral-400`，我改它是因为对比度不达标，不是因为"用了默认色"。**规则要对，但不能为了合规而合规。**

## 待观察

- 它还有 `references/genres/`（atmospheric / editorial / modern-minimal / playful）四个"流派"文件，每个流派有自己的豁免条款。
  我只有四个风格，还没到需要"流派"的规模。等风格超过 8 个再说。
- `scripts/sloplint.mjs` 我没扒——它把 gate 里标 M 的那批做成了静态检查。
  **如果我的 `lint.py` 要升级，这是现成的参照**：现在只查 token 一致性，没有任何"AI 味儿"检查。
  → 记在这里，作为下一步的候选。
