# neobrutalism-components

## 来源

- 仓库：`ekmas/neobrutalism-components`（5.6k★）
- 实际读取：
  - `src/styling/globals.css`（325 行）
  - `src/components/ui/button.tsx`
- 抓取：2026-11-16

一句话：把 neobrutalism 做成 shadcn 风格的组件库。它不是设计规范，是**能直接跑的组件代码**——所以每个值都是"实际在用的"，不是"文档里写的"。

## 取（吸收了什么，落到哪）

### 1. 五个值构成整套语言的骨架

```css
--border-radius: 5px;
--box-shadow-x: 4px;
--box-shadow-y: 4px;
--shadow: 4px 4px 0px 0px var(--border);   /* 零模糊 */
--border: oklch(0% 0 0);                   /* 纯黑 */
```

→ 全部落到 `neobrutalist/tokens.css`。**零模糊是这套风格的命门**：一旦 blur ≠ 0，它就从"纸板"变成"投影"。

### 2. 悬停 = 平移进自己的阴影

```jsx
"border-2 border-border shadow-shadow
 hover:translate-x-boxShadowX hover:translate-y-boxShadowY hover:shadow-none"
```

→ 落到 `button:hover` 的 `transform: translate(4px,4px); box-shadow: none`。

这是整个库里**唯一一个"悬停不是在改颜色"的交互**。它表达的是一件物理事件：纸板被按下去了。抄这个风格只抄边框和阴影会得到 70%，剩下 30% 在这一条里。

### 3. 正文 500 字重

```css
--base-font-weight: 500;
--heading-font-weight: 700;
```

→ 落到 `--nb-weight-body: 500`。这是最容易被抄错的一条：2px 的线条需要更沉的笔画来配，用 400 会让"框比字重"。

### 4. 主色配黑字，不配白字

```css
--main: hsl(217 100% 66%);
--main-foreground: oklch(0% 0 0);
```

→ 落到 `button { color: var(--nb-ink) }`。验证过：#5294FF 上白字只有 2.98:1，黑字 7.05:1。**它不是随便选的，是被对比度逼出来的。**

### 5. 图表五色 + 覆盖层

`#5294ff #ff4d50 #facc00 #05e17a #7a83ff`，overlay `oklch(0% 0 0 / 0.8)`。

→ 落到 `--nb-chart-1..5` 和 `--nb-overlay`。遮罩 0.8 比常见的 0.5 重得多，因为这套风格的遮罩要真的把后面压暗。

### 6. 尺寸档

按钮 h-10 (40px) / px-4 / py-2，图标按钮 40×40。容器 1300px。

→ 落到按钮高度、内边距、`--nb-container`。

## 弃（明确不吸收，为什么）

- **Tailwind 本身。** 这套值全是通过 `@theme inline` 映射到 Tailwind 变量上的。我直接取原始值写进标准 CSS 变量，不引入框架依赖。
- **`@keyframes marquee` / `orbit`（跑马灯、旋转）。** 是这个组件库**官网**自己用的装饰动画，不是这套设计语言的一部分。照抄会让"安静的粗野"变成"嘈杂的粗野"。
- **DM Sans 作为强制依赖。** 保留字体名但允许退化到系统无衬线，不让整个风格依赖一个 Google Fonts 请求。
- **`oklch()` 写法。** 只用它的等价十六进制，因为这个库要被复制到不支持 oklch 的环境里。
- **暗色模式。** 原项目有暗色变量，但粗野主义的暗色版很容易变成"霓虹赛博"，那不是同一套语言。**明确不做**，并写进 Known Gaps。
- **`--chart-active-dot: #000`。** 太细，没搬。

## 待观察

- 原项目的卡片 hover 只有 `translate`，没有 `active` 态。我加了 `active` 平移到 2px、阴影缩到 2px——**这是我补的**，理由见 DESIGN.md（"浮着→按下→按到底"三态叙事）。未验证是否符合原设计意图。
- 图表五色里红/黄/绿对白底不足 3:1，只能做填充。原项目没有提这件事，可能它只在深色底上用图表。
- 移动端没做。
