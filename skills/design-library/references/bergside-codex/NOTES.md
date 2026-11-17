# bergside/awesome-design-skills · `skills/codex`

来源：https://github.com/bergside/awesome-design-skills （3.6k★，67 份 DESIGN.md）
原始路径：`skills/codex/DESIGN.md`（55 行）、`skills/codex/SKILL.md`（81 行）
抓取日期：2026-11-16

> **这份是反面样本。** 它是 GitHub 上唯一一个自称 "Codex 风格" 的 skill，也是「AI 味儿」的活体标本。
> 保存它不是为了学，是为了以后有据可查——**"别人也在做"不等于"有人做对了"**。

## 它是什么

一份 55 行的 DESIGN.md，配色是：

```
primary: #000000
secondary: #FFFFFF
surface: #FFFFFF
text: #111827      ← 这是 Tailwind gray-900
success: #16A34A   ← Tailwind green-600
warning: #D97706   ← Tailwind amber-600
danger: #DC2626    ← Tailwind red-600
neutral: #FFFFFF
typography: Open Sans / JetBrains Mono
```

## 弃

- **全部色值。** 这不是 Codex 的配色，甚至不是任何真实产品的配色。`#000000` 当 primary、`#FFFFFF` 当 surface 和 neutral——三个 token 撞成同一个白，说明它根本没看过真实界面。
- **Open Sans。** Codex 是 macOS 原生 app，用的是系统字体（SF Pro / PingFang SC）。Open Sans 是 Google Fonts 里最"安全"的选择，也就是最没有来源的选择。
- **`sourceScale: "12/14/16/20/24/32"` 这种写法。** 把一个 6 档字号阶写成字符串，等于没有 token——没法被引用、没法被校验、没法被继承。
- **正文模板。** 每一段都是 `- **Primary (#000000):** Token from style foundations.`。同一个句式重复 7 遍，没有一句话是对这个产品的观察。
- **`## Style Foundations` 这一节本身。** 它是把 front matter 的 YAML 用自然语言复述一遍，YAML 里已经有的东西不该在正文再说一次。

## 取

**只有一条，而且是一条反面的方法论：**

它证明了「DESIGN.md 格式合规」和「这份设计文档有价值」是两件完全不同的事。
它通过了格式，却一个真实数值都没有。

由此得到一条本库的判据，已写进 `principles.md` §11：

> **一份 DESIGN.md 里如果没有任何一个"只能是这个产品"的数值，它就是生成物。**
> 检测方法：把产品名遮住，还能套用到别的产品上吗？能 → 废纸。

## 待观察

- 这个仓库有 67 份 DESIGN.md，同一套生成模板。其中有多少份是实拍的、多少份是生成的？
  抽样看了 3 份（codex / linear / stripe），结构和句式完全一致，色值都是 Tailwind 默认色。
  **结论：大概率整批是生成的。** 这个仓库的价值是"格式示范"，不是"设计参考"。
  → 本库的 `fetch-ref.sh` 默认来源应该从它换成 `Meliwat/awesome-ios-design-md` 那种手写的。
