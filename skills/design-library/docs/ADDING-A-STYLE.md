# 新增一个风格

## 先判断

只有新场景**必须违反现有风格的硬约束**时才新增。只是换色、换字号、换圆角，应修改现有风格。

## 创建

```bash
python3 scripts/designlib.py new <slug> "<中文名>"
```

一个风格目录至少包含：

```text
styles/<slug>/
├── DESIGN.md
├── tokens.css
└── prompt.md
```

**开工前先读 [`LAYERS.md`](../LAYERS.md)。** 它定义页面的六层构成；
`DESIGN.md` 的 front matter 必须包含 `elevation`（材质体积）、`media`（标识图像）、
`motion`（动效交互）三组新字段，正文必须有对应的三节。只写色板和字号不算完成。

`DESIGN.md` 的 front matter 必填：

```yaml
name: 名称
description: 一句话说明气质与用途
cues: 使用场景1、使用场景2、使用场景3
avoid: 排他场景1、排他场景2
surface: light | dark | mixed
density: tight | medium | roomy
register: story | professional | technical | tool
family: reading | professional | developer | workbench | operations | enterprise-data | companion | expressive | trusted-service
tier: core | variant | technique
sourceRefs: 来源 slug，用英文逗号分隔
status: beta | stable
```

正文必须包含：

- Overview
- Colors
- Typography
- Layout
- Elevation & Depth
- Shapes
- Components
- Do's and Don'ts
- Chinese Typography
- When to Use
- Iteration Guide
- Known Gaps

## 实现

1. 在 `tokens.css` 定义一个稳定的容器 class，例如 `.ds-<slug>`。
2. 所有颜色、字体、字号、间距、圆角以变量声明。
3. 基础组件至少覆盖标题、正文、按钮、卡片和标签。
4. 包含 `:focus-visible` 与 reduced-motion 降级。
5. 不从其他风格复制变量名，不引用多个风格的 token。

## 检查

```bash
python3 scripts/designlib.py build
python3 scripts/designlib.py check
```

检查失败时修风格，不要修改生成物绕过。

