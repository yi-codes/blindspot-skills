# latex.css

## 来源

- 仓库：`vincentdoerig/latex-css`（3.4k★，785 行 CSS）
- 实际读取：`style.css` 全文
- 抓取：2026-11-16

一句话：把 LaTeX 的排版观感搬进网页。它自己说"一个 CSS 文件，给 HTML 一个 LaTeX 的样子"。

## 取（吸收了什么，落到哪）

### 1. 段落缩进是算出来的，不是拍的

```css
--text-indent-size: 1.463rem;
/* \parindent =~ 17.625pt;
   1pt[LaTeX] = (72 / 72.27) * 1pt[HTML];
   17.625 * (72/72.27) / 12 = 1.463rem */
```

→ 原样落到 `academic/tokens.css` 的 `--ac-indent`，连推导注释一起搬。**这是整个库里唯一一个"数值有推导过程"的 token。**

### 2. 段间不留空行 + 首行缩进

`.indent-pars p { text-indent: var(--text-indent-size) }`，同时 `p { margin-top: 1rem }` 只在需要时加。

→ 落到 `academic` 的 `p { margin: 0; text-indent: ... }`。这是最反网页的一条，也是这个风格成立的关键。

### 3. 版心用 ch 不用 em

`max-width: 80ch`。

→ 落到 `--ac-measure: 80ch`。**单位选择的理由**：ch 跟字号无关，换字号版心不变。用 em 的话 20px 字号下版心会翻倍。

### 4. 线宽是分数像素

`--border-width-thin: 1.36px` / `--border-width-thick: 2.27px`。

→ 落到 `--ac-border-thin/thick`，没有取整。

### 5. 两端对齐 + 自动断字

`text-align: justify; hyphens: auto; text-rendering: optimizeLegibility;`

→ 落到 `academic` 的 base。

### 6. 边注挂在版心外面

`.sidenote { margin-right: -20vw; width: 18vw }`。

→ 落到 `.ds-sidenote`，但把 `-20vw` 改成了固定的 `-64px` 负外边距。理由：vw 在窄容器里会跑到屏幕外，固定值可控。

### 7. 标题字号阶

h1 2.5rem / h2 1.7rem / h3 1.4rem / h4 1.2rem / h5 1rem / h6 1rem italic。

→ 落到 `--ac-text-h1..h4`。注意 h2 行高 32/27 ≈ 1.176，比正文紧得多——标题靠字号建立层级，不靠行距。

### 8. 深色版是自带的

`.latex-dark` 类，`--body-color: hsl(0 0% 86%)` on `hsl(0 0% 16%)`。

→ 落到 `.ds-academic-dark`，值原样。**这是库里第一个"深色不是我反推的"风格。**

## 弃（明确不吸收，为什么）

- **`--table-border-color: black/white` 在深浅两套里硬切。** 照抄了，但把它写成 `--ac-rule`，因为纯黑纯白在 token 里需要名字。
- **未访问链接的颜色。** 原项目**没有定义**——沿用浏览器默认蓝。我借了它的 `--link-focus-outline`（hsl 220 90% 52%）当链接色。**这是一处主动偏离，已在 DESIGN.md 里标注。**
- **`filter: invert(80%)` 处理证明符号（□）。** 太 hack，我用字符直接写。
- **主题切换的 JS / `prefers-color-scheme` 自动切换。** 库里所有风格都是显式双 class，不做自动。
- **LaTeX 的 `\parindent` 只在正文段落生效，列表内不缩进。** 这个细节我实现了（`ol/ul` 里不缩进），但没写进 DESIGN.md。

## 待观察

- Latin Modern / Libertinus 都是需要自托管的字体。现在退到 Georgia，x-height 比 Latin Modern 大，1.8 行高会显得空。
- 双栏（twocolumn）没做。
- 公式（MathML / KaTeX）没做，这是学术场景的硬缺口。
- 边注在 <1024px 会跑出屏外，降级方案没定。
