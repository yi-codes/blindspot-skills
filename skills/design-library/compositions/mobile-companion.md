---
name: 移动伴侣型
slug: mobile-companion
version: 1
status: beta
density: medium
register: companion
frame: [frame-adaptive, frame-grid, frame-mobile-nav, frame-actions]
sample: ../preview/adaptive-companion.html
---

# 移动伴侣型 · mobile-companion

## 适用任务

手机为主、单手可达、状态优先：硬件伴侣 App、健康/睡眠记录、播放器、
智能家居控制、随手记录工具。用户抬手只看一眼，需要立刻知道"现在怎么样"。

## 主角与视线

唯一主角是 **首屏当前状态**（数值、播放中、设备状态），不是导航也不是品牌。
视线路径：`header 状态 → 主操作 → 下方内容 → 底部 tab`。
底部 `frame-mobile-nav` 是拇指区，任何时候可见；把主操作放顶部会违反单手逻辑。

## 网格与密度

- 密度 `medium`：容器 `width: min(100%, 30rem)` 居中，`min-height: calc(100dvh - 2rem)`，
  在桌面上也保持手机宽度，不拉伸成宽屏网页。
- `frame-adaptive` 内 `frame-grid` 覆写为 `grid-template-columns: 1fr`——单列是硬约束，
  不是响应式降级后的结果。
- 底部导航 4 等分，`position: sticky; bottom: 0`，顶部一根细线分隔。
- 桌面预览时不用额外断点，这个骨架本身就是窄屏形态。

## 挂载点

| 结构类 | 挂什么 | 状态要求 |
|---|---|---|
| `frame-adaptive header` | 状态 + 标题 | 加载/离线/已同步三态 |
| `frame-actions` | 主操作（1 个，最多 2 个） | 触摸目标 ≥44px、焦点环 |
| `frame-grid`（单列） | 记录/条目列表 | 空态有明确下一步 |
| `frame-mobile-nav` | 4 个 tab | `aria-current`、图标+文字双标 |

状态变化优先用文字与数值，不靠纯颜色；`prefers-reduced-motion` 下过渡降到 1ms。

## 与风格的咬合

适合 `family: companion`、`register: tool` 且圆角偏大、触控目标偏大的风格。
它和新拟态这一类"控件与底同色、靠双向投影表达按压"的语言天然合拍，
但密集表格、长文、多列风格会被 `min(100%,30rem)` 直接挤坏，遵守它们自己的 `avoid`。

## 禁用项

- 需要并排比较多列数据：单列硬约束会把对照变成上下翻页，换数据外壳型。
- 桌面为主要场景且要利用宽屏：30rem 居中会留出大片无用空白，换工作台侧栏型。
- 长文阅读与表单密集流程：拇指区导航会持续占用视口，行高 ≥1.7 下无法显示足够内容。
