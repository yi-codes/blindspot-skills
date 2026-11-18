# references/ —— 外部样本层

这里放**别人的**设计，不是我的。作用是供给，不是收藏。

```
references/
├── README.md            ← 你正在读的（方法论）
├── <name>/
│   ├── DESIGN.md        ← 原始存档，只读，不许改（有的话）
│   └── NOTES.md         ← 我的提炼卡：吸收了什么、丢了什么
```

## 现有样本

样本多了以后，只靠目录名看不出它是什么、被谁用了。查这张表。

| 目录 | 类型 | 去了哪 |
|---|---|---|
| `claude` | ① 二手 | `editorial-serif`（墨色不纯黑） |
| `ollama` | ① 二手 | `terminal-mono` |
| `bergside-codex` | ① 二手 | `quiet-dark`（反面样本，存证） |
| `chatgpt-ios` | ② 一手（拆包） | `quiet-dark` 动效与浅色板 |
| `hallmark` | ① 二手 | 促成 `principles.md` 的版式规则 |
| `govuk` | ② 一手（SCSS） | → `civic` |
| `latex-css` | ② 一手（CSS + 推导注释） | → `academic` |
| `neobrutalism` | ③ 组件库（CSS + TSX） | → `neobrutalist` |
| `catppuccin` | ④ 纯调色板 | → `soft-pastel`（**形状是补的**） |
| `react-bits` | ③ 组件库（JSX + CSS） | → `tactile-3d`（弹簧参数、高光衰减） |
| `atropos` | ③ 组件库（JS + SCSS） | → `tactile-3d`（倾角上限、归一化公式） |
| `primer` | ② 一手设计规范 | → `developer-docs` |
| `carbon` | ② 一手设计系统 | → `enterprise-data` |
| `radix` | ③ 组件库 | → `developer-docs`、`enterprise-data` |
| `material-3` | ③ 组件库 | → `adaptive-companion` |
| `fluent-2` | ③ 组件库 | → `adaptive-companion`（仅行为参考，许可待逐文件核验） |
| `uswds` | ② 一手设计系统 | → `civic`（许可待逐文件核验） |
| `geist` | ⑤ 字体资产 | → `developer-docs`（只吸收字体分工） |
| `the-broad` | ① 二手（展陈网站分析） | → `gallery-wall` |
| `awwwards` | ① 二手（获奖站点分析） | → `gallery-wall`（留白与图像策略） |
| `wired` | ① 二手 DESIGN.md | → `newsprint-grid` |
| `risograph-zine` | ① 二手（设计样本） | → `riso-zine` |
| `papercss` | ③ 组件库（SCSS） | → `sketch-notes`（手绘边框实现） |
| `rough` | ③ 组件库（JS） | → `sketch-notes`（roughness/bowing 参数） |
| `nes-css` | ③ 组件库（SCSS） | → `pixel-arcade` |
| `art-deco` | ① 二手（艺术风格分析） | → `deco-ceremony` |

注意最后一列有两种写法：`→ 某风格` 表示这个样本**催生**了该风格；不带箭头表示只是**修了**已有风格。

许可与边界汇总见 [`SOURCES.md`](SOURCES.md)。`NOASSERTION` 来源在逐文件核验前只作行为参考，不复制实现。

## 为什么要单独一层

因为"喜欢的风格"和"我自己的风格"是两件事。

混在一起会有两个后果：库变成收藏夹（越多越没用），或者自己的东西被别人的规则污染（改着改着不知道哪个是自己的）。

分开之后，`references/` 可以无限膨胀而不影响 `styles/` 的一致性。**只有经过提炼、能写成数值的东西，才允许进入 `styles/`。**

## 四种输入，硬度不同

不是所有样本都同样"硬"。拿到一份材料，先判断它属于哪一类——**你只能声称它给你的那部分**。

| 类型 | 例子 | 它给你什么 | 你还能声称什么 |
|---|---|---|---|
| ① 二手 DESIGN.md | `claude`、`ollama`、`bergside-codex` | 别人对某个产品的分析 | 只能声称"有人这么看"，数值要自己验 |
| ② 一手源码 | `govuk`（SCSS 变量 + 注释）、`latex-css` | 每个值 + 为什么 | 颜色、字号、线宽、间距全部可复现 |
| ③ 能跑的组件库 | `neobrutalism`（CSS + TSX） | 实际在用的值 + 交互 | 值可复现，**交互也能复现**（比 ② 多一层） |
| ④ 纯调色板 | `catppuccin`（只给颜色） | 只有色值 | **只有颜色是它的，形状是你补的** |

第 ④ 类最危险：它看起来最"完整"（26 个色、4 个 flavor、版本化管理），实际缺的正是最难的部分——层级怎么分、组件长什么样。而且缺了不会报错，只会做出来"颜色对了，气质不对"。

**规则**：第 ④ 类必须把"形状是我补的"写在 DESIGN.md 第一段。读者有权知道哪些数是查得到的，哪些是定的。

## 怎么用这一层

### 第一步：拿到原始文件

上游主力有两种：

**A. 别人写好的 DESIGN.md** —— [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)（127k★，84 个真实网站）
文件在 `design-md/<品牌>/DESIGN.md`。

```bash
./scripts/fetch-ref.sh <owner/repo> <path> <短名>
# 例：
./scripts/fetch-ref.sh VoltAgent/awesome-design-md design-md/linear/DESIGN.md linear
```

**B. 设计系统自己的源码** —— 这是更硬的一类，2026-11 之后成为主力：

```bash
gh api "repos/alphagov/govuk-frontend/contents/packages/govuk-frontend/src/govuk/settings/_colours-palette--internal.scss" \
  --jq '.content' | base64 -d
```

比 ① 好用的地方：注释里就写着"为什么是这个值"（比如 latex.css 把 `1.463rem` 的推导过程写在注释里）。

也可以从别处来：某个产品官网、自己截图分析、Figma 社区的规范文件。只要能落成 DESIGN.md 格式，就走同一套流程。

### 第二步：拆

拿到一份外部 DESIGN.md，先做一次二分：**哪些能变成数值，哪些只是氛围。**

| 能吸收（写进 NOTES 的"取"） | 不能吸收（写进"弃"） |
|---|---|
| 具体色值和它出现的比例 | "高级感""未来感"这类形容词 |
| 字号阶的比例关系（1.25 还是 1.333） | 只有该品牌有的字体授权 |
| 间距节奏（8 倍数 / 4 倍数） | 特定插画风格、吉祥物 |
| 圆角与阴影的选择逻辑 | 动效的具体曲线（除非有明确数值） |
| Do / Don't 里的硬规则 | 版权标识、logo 用法 |
| 一个风格怎么处理"层级" | 与品牌强绑定的文案语气 |

**判断标准：这一条能不能写成 `{token}` 或一条可检查的规则？**
不能，就是氛围，留在 REFERENCES 里当灵感，别往 styles 里搬。

### 第三步：落

提炼出的东西分三种去处：

1. **补进现有风格**——大部分情况。比如从 Claude 学到"墨色不用纯黑"，直接修 `editorial-serif` 的 `colors.ink`。
2. **成为通用原则**——跨风格都成立的，写进 `principles.md`。比如"颜色不超过三个家族"。
3. **促成新风格**——只有当它**必须违反现有风格的硬约束**时才新开。见 `principles.md` 第 8 节。

### 第四步：写 NOTES.md

每份样本必配一张卡，四个字段不能少：

```markdown
# <品牌>

## 来源
仓库 / 路径 / 抓取日期 / star 数

## 取（吸收了什么，落到哪）
- 具体一条 → 落到 styles/xxx 的哪个 token，或 principles.md 第几节

## 弃（明确不吸收，为什么）
- 具体一条 → 原因（授权 / 与风格冲突 / 只是装饰）

## 待观察
- 还看不懂或没验证的
```

**"弃"这一栏比"取"更重要。** 它记录的是判断力，半年后回头看，你能知道自己当时为什么没抄它。

## 三条纪律

1. **原始存档不改**。`references/<name>/DESIGN.md` 是证据，改了就失去参照价值。要标注批注写在 NOTES 里。
2. **不整份搬进 styles**。搬进来的是提炼结果，不是文件。库里不该出现两个长得一样的风格。
3. **吸收要能追溯**。`styles/x/DESIGN.md` 里如果有一条规则是从外面学来的，在 NOTES 里要能对上。追溯不了，说明是拍脑袋加的。

## 上游动态

- 格式规范：[google-labs-code/design.md](https://github.com/google-labs-code/design.md)（28.9k★），`docs/spec.md`
- 样本库：[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)（127.6k★）
- 官方校验：`npx @google/design.md lint DESIGN.md`（能查 WCAG 对比度、失效引用；不认识 `borderColor` 这类自定义属性，会告警——规范里组件属性只有 8 个）

**找下一份样本时优先去这些地方**（比聚合库硬一个档，值是查得到的不是猜的）：

- [alphagov/govuk-frontend](https://github.com/alphagov/govuk-frontend) —— 政府级无障碍标准，SCSS 变量带注释
- [vincentdoerig/latex-css](https://github.com/vincentdoerig/latex-css) —— 单文件 CSS，把 LaTeX 的排版参数逐条推导
- [ekmas/neobrutalism-components](https://github.com/ekmas/neobrutalism-components) —— 带 TSX，交互行为也能抄
- [catppuccin/palette](https://github.com/catppuccin/palette) —— 纯色板，用来压力测试方法（见上表 ④）
- [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) —— 200+ 动效组件，**动效参数的金矿**（弹簧 ω/ζ、衰减曲线都写在代码里）
- [nolimits4web/atropos](https://github.com/nolimits4web/atropos) —— 5KB 视差倾斜，参数少而干净，适合当"标定值"
