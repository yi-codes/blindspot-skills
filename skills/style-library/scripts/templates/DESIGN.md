---
version: alpha
name: __NAME__
description: >-
  __一句话说清气质，再补两句"为什么这些数值长这样"——这是 agent 判断的依据。__
colors:
  canvas: "#FFFFFF"
  surface: "#FFFFFF"
  surface-alt: "#F5F5F5"
  ink: "#111111"
  ink-muted: "#666666"
  ink-faint: "#8F8F8F"
  hairline: "#E0E0E0"
  primary: "#2557D6"
  primary-soft: "#EAF0FD"
typography:
  headline-display:
    fontFamily: "system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.02em
  headline-md:
    fontFamily: "system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.01em
  body-md:
    fontFamily: "system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: 0
  label-caps:
    fontFamily: "system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.06em
rounded:
  none: 0px
  sm: 2px
spacing:
  base: 8px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 32px
  xl: 48px
  section: 96px
  measure: 36em
components:
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.sm}"
    padding: 24px
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
---

## Overview

写三段。

第一段：这个风格是给谁看的、用在什么场景。
第二段：它的性格来自哪几个**具体**的选择（不是形容词，是数值和取舍）。
第三段：读者应该产生什么感觉，以及为什么这套数值会产生这种感觉。

不要写"高级感""现代""简洁"这类词。如果一定要说"高级"，说明它是由哪个数值构成的。

**Key Characteristics**

- 画布 `{colors.canvas}`（#FFFFFF）——为什么用这个值
- 唯一彩色 `{colors.primary}`（色名 + 值）——它只出现在哪里，为什么是这一个
- 字体策略（一族到底 还是 双体分工）——为什么
- 间距节奏（8 的倍数 / 4 的倍数）——为什么
- 圆角与阴影的选择——为什么
- 层级靠什么表达（边框 / 底色差 / 字号 / 投影）

## Colors

每个 token 一条：`{colors.canvas}` — 值：它是干什么的、为什么是这个值。

分组写：Canvas & Surface / Ink / Line / Accent。超过三个色族的必须删掉一个。

## Typography

字号阶、比例（1.25 / 1.333）、字重档位。

明确写出硬规则，例如"只用 400 和 700 两档字重""不设 15/18 这类中间档"。

## Layout

网格模型、间距阶、内容宽度。全部给具体数值。

## Elevation & Depth

有投影就写完整规格（spread / blur / color）。

**没有投影也要写**——写清楚"层级靠边框和底色差表达"。这一节空着是最容易露馅的地方。

## Shapes

圆角策略：统一一个值，还是分层（按钮 2px / 卡片 8px）。

明确写出禁止的用法，例如"不许混用 2px 和 pill"。

## Components

每个组件一段说明 + 对应的 `{components.card}` 引用。至少覆盖 button / card / tag 三种。

## Do's and Don'ts

### Do

- 每条都写成可执行的指令，不是评价

### Don't

- 每条都写清"为什么这样会破功"

## Chinese Typography

必填，不要省。上游 84 个西方样本都没有这一节，这是本库的核心差异。

至少覆盖：行高下限、中西文之间的空格、全角标点、避头尾、不首行缩进、中文字重只有 400/700 有效、引号用法、负字距的安全范围。

## When to Use

**用**：

**别用**：

## Iteration Guide

1. 一次只改一个组件，用 `{components.card}` 指代它。
2. 所有值走 `{token.refs}`，不要内联十六进制。
3. 需要更强调时，先考虑"字号大一级"，最后才考虑"加一个新颜色"——后者基本等于破功。
4. 新增组件前先问：它能不能用现成的边框 + 留白表达。不能，再谈别的。

## Known Gaps

诚实写：哪些场景没覆盖、哪些字体买不到、哪些状态没定义、哪些设备会退化。

这一节让文件可信——读者知道边界在哪，才不会在不该用的地方用它。
