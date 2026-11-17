# nolimits4web/atropos · `src/atropos.js`

来源：https://github.com/nolimits4web/atropos （3.6k★，"Stunning touch-friendly 3D parallax hover effects"）
原始路径：`src/atropos.js`（479 行）、`src/atropos.scss`
抓取日期：2026-11-16

一句话：一个 5KB 的视差倾斜库，Swipers 作者的另一个作品。它和 react-bits 的 TiltedCard
在做同一件事，但**实现哲学完全相反**——这个差别比数值本身有用。

## 取

### 1. 默认参数（一份干净的标定值）
```
rotateXMax: 15, rotateYMax: 15   // 度
activeOffset: 50                 // 悬停时整体前移 px
shadowOffset: 50, shadowScale: 1 // 阴影落在 z=-50 处
duration: 300                    // ms，ease-out
```
`15°` 和 TiltedCard 的 `12°` 各自独立收敛到同一区间，说明这是"文字不变形"的经验上限。
本库的 `--t3-tilt-max-wide: 15deg` 直接取它，单卡用 TiltedCard 的 12。

### 2. 旋转公式（归一化而不是累计）
```js
rotateY = -(rotateYMax * (x - cx)) / (w / 2)
rotateX =  (rotateYMax * (y - cy)) / (h / 2)
```
指针位置**归一化到 ±1** 再乘上限，天然不会越界。比"累计位移"稳，也不需要额外 clamp。
强烈推荐这个写法：本库的 demo 里 tilt 部分用的就是它。

### 3. 高光的低成本做法
```js
highlightEl: translate3d(-rotateY% * 0.25, rotateX% * 0.25, 0)
opacity = max(|rotateX%|, |rotateY%|) / 100
```
一个位移 + 一个透明度，就能让高光跟着倾角走。比算渐变中心便宜得多。
本库选了 react-bits 的写法（移动渐变中心），但记录了这条低成本替代。

### 4. `duration: 300ms` 作为无 JS 的降级
本库 `--t3-dur-snap: 300ms` 就是从这儿来的，只在没有 JS 时生效。

## 弃

- **用 CSS transition 做倾斜**。atropos 的核心是"给 rotateEl 设置 transform + `transition: 300ms ease-out`"。
  看起来很省事，但**拖拽场景不能用**：过渡一旦开始就必须走完整段，手指中途反向会打架。
  这是本库选弹簧的直接理由，写在 `DESIGN.md` 的 Elevation & Depth 里。
- **`stretchX/Y/Z`**（默认全 0）。原理是把倾斜百分比映射成 `translate3d` 的百分比位移，
  开了会有"果冻"感。和本库的克制取向冲突，没开。
- **它的 DOM 脚手架**（`atropos-scale / rotate / inner` 三层嵌套）。值得知道，但本库的
  `.ds-card` 用自己的三层结构（封面/边框/文字），不需要照搬。
- **它的 JS 依赖**（`$setTransform` / `queue` 微任务批处理）。这是性能优化，对规格文档没用。

## 待观察

- `perspective` 在 atropos 里由 CSS 变量控制，源码没给默认值，用的是浏览器默认（通常 0 = 无透视？）。
  实际组件里由 `.atropos` 的 SCSS 给，但我没读到那一行——**这是一个未核实的点**。
- `activeOffset: 50` 比本库的 `--t3-lift-hover: 24px` 大一倍。它面向的是"浮起"效果，
  本库面向"卡片被推近"，24 更合适。这个下调是判断，不是提取。
