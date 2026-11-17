# GOV.UK Design System

## 来源

- 仓库：`alphagov/govuk-frontend`（官方，非第三方分析）
- 实际读取：
  - `packages/govuk-frontend/src/govuk/settings/_colours-palette--internal.scss`
  - `packages/govuk-frontend/src/govuk/settings/_measurements.scss`
  - `packages/govuk-frontend/src/govuk/settings/_typography-responsive.scss`
  - `packages/govuk-frontend/src/govuk/settings/_spacing.scss`
  - `packages/govuk-frontend/src/govuk/settings/_links.scss`
  - `packages/govuk-frontend/src/govuk/settings/_typography-font.scss`
- 抓取：2026-11-16

**输入类型和之前不一样。** 前四个样本是别人写好的 DESIGN.md（二手分析），这个是**一手源码**。好处是每个值都有出处、还带注释；坏处是要自己从 SCSS map 里读出来。

## 取（吸收了什么，落到哪）

### 1. 七档 tint/shade 的调色板结构

每个色相给了 primary / tint-25 / tint-50 / tint-80 / tint-95 / shade-25 / shade-50。

→ 落到 `styles/civic/DESIGN.md` 的 Colors 一节。但**没有全部搬进 token**——只用了 black 的 tint-25 / tint-50 / tint-95 三档。理由：tint/shade 是给"组织色"（各部门自己的品牌色）用的，我的风格没有组织。

### 2. 字号阶是"用途档"不是"等比数列"

80 / 48 / 36 / 27 / 24 / 19 / 16 / 14，正文 19px。

→ 完整落到 `civic/tokens.css` 的 `--cv-text-*` 八档。这是这次最重要的收获：**19px 正文**说明"正文 16px"不是普适答案。

### 3. 标题行高可以等于 1.0

80px 字号配 80px 行高。

→ 落到 `--cv-leading-2xl: 1`。我的直觉是"标题至少要 1.1"，源码说不用。

### 4. 线宽是分级的，而且分级有语义

`$govuk-border-width: 5px` / `-wide: 10px` / `-narrow: 4px` / `-form-element: 2px` / `-focus: 3px`。

→ 落到 `civic` 的 Shapes 一节，做成了那张 1/2/3/4/5/10 的表。

### 5. 链接悬停靠下划线加粗，不靠变色

`$govuk-link-hover-underline-thickness: max(3px, .1875rem, .12em)`。

→ 落到 `civic/tokens.css` 的 `a:hover`。这条对色觉障碍用户更可靠，是可以推广到别的风格的原则。

### 6. 间距是 5 的倍数，不是 4 或 8

`$govuk-spacing-points: (0: 0, 1: 5px, ... 9: 60px)`。

→ 落到 `--cv-space-*`。

## 弃（明确不吸收，为什么）

- **GDS Transport 字体。** 商用授权。退到它在代码里自己写的 fallback `arial, sans-serif`。这是这个风格最大的损失——GDS Transport 是专门为屏幕小字号调的，Arial 在小字号下差一截。
- **七档 tint/shade 全搬。** 见上面，用不到。
- **组织色（organisation colours）。** 那是给各部门套自己的品牌色用的，属于品牌资产不是风格。
- **蓝色主按钮的惯例？** 恰恰相反——GOV.UK 的主按钮是**绿**的（`$govuk-button-background-colour`），蓝只给链接。这个反直觉的决定我照抄了，并且写进了 Don't。
- **Tag 的全大写 + 1px 字距。** 照抄了，但明确标注"对中文无效"——这是少数"抄了但用不上"的条目。

## 待观察

- 响应式字号在 640px 以下会掉两档（48→32、36→27）。我只写了 tablet 以上，移动端没做。
- `_colours-applied.scss` 那几个文件在仓库里的实际路径和目录列表对不上（可能被 `.import.scss` 分装了），`$govuk-error-colour` 的真实值没读到，所以 `civic` 的 error 用的是 palette 里的 red primary `#ca3535`，不是应用层那个（印象里是 `#d4351c`）。**这是一个未验证的偏离。**
- GOV.UK 的 focus 样式完整写法（`outline: 3px solid transparent` + 双重 box-shadow）我按记忆复现的，没有逐行对照 `_focus.scss`。需要复核。
