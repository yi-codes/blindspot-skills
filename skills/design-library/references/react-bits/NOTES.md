# DavidHDev/react-bits · `Components/TiltedCard` + `InfiniteMenu`

来源：https://github.com/DavidHDev/react-bits （52.1k★，"largest open-source library of animated, interactive components"）
原始路径：
- `src/content/Components/TiltedCard/TiltedCard.jsx`（562 行）、`TiltedCard.css`（170 行）
- `src/content/Components/InfiniteMenu/InfiniteMenu.jsx`（896 行，WebGL 球面菜单）
- 看过但没用：`src/content/Animations/Cubes/Cubes.jsx`（677 行，纯 canvas，没有可提取的 CSS 数值）
抓取日期：2026-11-16
许可证：**MIT + Commons Clause v1.0**——可以随产品分发，不能单独售卖这个库本身。
所以本库只取**数值与手法**，不复制代码；弹簧积分器是照公开的半隐式欧拉自己重写的。

## 取

### 1. 弹簧参数（最大收获）
源码里 `smoothness` 是个 0–1 的旋钮，真实参数由它算出来：

```js
omega = 20 * Math.pow(0.2, smoothness)   // 0.6 → 7.6 rad/s
zeta  = 1 - 0.3 * smoothness             // 0.6 → 0.82
```

落到 `styles/tactile-3d` 的 `--t3-omega` / `--t3-zeta`。
这个 ζ=0.82 是整套"丝滑"的核心：略欠阻尼，松手有一点回弹，但不是弹簧床。
另外三个场景各有自己的参数，也一并取了：
- 按下 `ω=26, ζ=0.80`（要立刻有反应）
- 翻面 `ω=9.5, ζ=0.72`（要慢、要有一点重）
- 提示浮层跟手 `τ=35ms`（`1 - exp(-dt/0.035)`）

### 2. 1/240 秒子步进
`step()` 里把每帧 dt 切成 1/240 的子步再积分。落地帧率 30fps 时也不发散——
这是"跟手"的技术前提，也是我原来没意识到的一层。写进了 `--t3-substep`。

### 3. 高光的非线性衰减
不是 `0.34 → 0` 平均分，而是 10 档手调：0.34 / 0.331 / 0.285 / 0.202 / 0.108 / 0.035 / 0.003 / 0。
本库取 7 档，写进 `tokens.css` 的 `::after`。
**这个衰减曲线才是"反光"和"灰雾"的区别**，第一版我用 `farthest-corner` + 线性分档，
渲染出来是一团脏斑，改成固定 90px 半径 + 非线性分档才像反光。

### 4. 阴影跟着倾角走
```
offsetX = -sin(ry) * 22
offsetY = 12 + 16 * lift + sin(rx) * 18
```
固定投影是"贴纸"，跟手投影才是"东西"。落到 `showcase/tactile-3d.html` 的 JS。

### 5. 拖拽 / 点击的 6px 判定
`FLIP_THRESHOLD = 6`：位移超过 6px 就不触发点击。没有这个数，"拖完松手"必然误触。

### 6. 三层 z（−24 / 0 / +30）
封面压在卡面下形成内凹，标题浮在卡面上形成视差。这是"真 3D"和"画了个阴影"的分界。

## 弃

- **`rotateAmplitude` 之外的 20 多个 props**（陀螺仪、floating、trackWindow、axis、reverse…）。
  能用，但每个都要单独验证；本库只留了最核心的六个数，其余记在 `Known Gaps`。
- **InfiniteMenu 的 WebGL 球面菜单实现**。它用 `inertia 0.6 / tileSize 0.63 / zoom 1.65 / stretch 0.6`
  在 shader 里做球面布局，抄不动也不该抄——本库的环是 CSS 3D + 弹簧，同一件事的轻量做法。
- **`Cubes.jsx`**：纯 canvas 画的立方体网格，没有 CSS 数值可提取，做不成 token。
  但记住它存在：真要做"六面盒子"应该走 canvas/WebGL，不是 6 个 div。
- **它的组件 API**。本库要的是视觉规格，不是 React 组件。

## 待观察

- 52k★ 的库里有 200+ 组件，我只读了 3 个。`GlareHover`、`ModelViewer`、`Ballpit` 可能有别的维度。
- 它的 `smoothness` 默认 0.6 是否在 120Hz 屏上调过，源码里没写。iOS 上体感会更快，没实测。
- Commons Clause 的边界：把数值当"设计规格"写进自己的文档，肯定没问题；
  但如果哪天要把这些东西打包成付费模板卖，得回头看许可证。
