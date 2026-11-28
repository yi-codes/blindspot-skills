---
name: 数据外壳型
slug: data-shell
version: 1
status: beta
density: dense
register: professional
frame: [frame-data-shell, frame-data-side, frame-data-main, frame-filterbar, frame-nav]
sample: ../preview/enterprise-data.html
---

# 数据外壳型 · data-shell

## 适用任务

运维报表、交易明细、告警列表、用户管理后台。用户来这里是扫读、筛选、定位某一行，
不是阅读 narrative。信息密度是特性，不是缺陷。

## 主角与视线

唯一主角是 **`frame-data-main` 里的表格**。所有其余元素（侧栏、筛选条、统计卡）
都为"更快读懂这张表"服务。视线路径：`筛选条（我现在看的是哪一批）→ 表头 → 目标行`。
统计数字若做成大卡片墙，会盖过表格，别这么做。

## 网格与密度

- 密度 `dense`：`frame-data-shell` 为 `minmax(9rem,12rem) : minmax(0,1fr)`，
  几乎是满屏，不用 `frame-story` 那种大留白。
- 表格 `width: 100%; border-collapse: collapse`，`font-variant-numeric: tabular-nums`
  保证数字列对齐；单元格 `padding: 0.65rem 0.55rem`，靠细底线分行而非卡片。
- `frame-filterbar` 上下各一根线，是唯一的条件区；筛选条件用带边框的小标签，
  不用下拉堆砌。
- 48rem 以下：侧栏塌成 4 列横向 nav，`frame-data-main` 允许 `overflow-x: auto`
  ——横向滚动是表格的合理降级，不是失败。

## 挂载点

| 结构类 | 挂什么 | 状态要求 |
|---|---|---|
| `frame-data-side` | 数据集/视图切换 | 当前项 `aria-current` |
| `frame-filterbar` | 已生效的筛选条件 | 可移除、有空条件态 |
| `frame-data-main table` | 主数据表 | 空态、加载态、错误态、无结果态 |
| `frame-data-main th` | 列头（0.75rem / 550 / 0.72 opacity） | 排序状态可感知 |

`--frame-sep: 1px solid currentColor`，专业类靠描边，数据表里尤其不能靠阴影分层。

## 与风格的咬合

适合 `register: professional` / `family` 为 enterprise、industrial 的风格，
以及任何字阶紧凑、行高偏小仍可读的 token 体系。
低对比新拟态、强装饰复古、氛围渐变风格都被 `avoid` 明确排除：
密集细线在这些风格里会失去分辨力。

## 禁用项

- 只有一个指标要展示：表格外壳会把一个数字埋进空白，换叙事引导型或分屏型。
- 单元格里需要长文本段落：`white-space: nowrap` 会逼出不可读的长行，换工作台侧栏型 + 详情抽屉。
- 需要在窄屏完整操作（编辑、批量动作）：横向滚动只能看不能改，另做移动布局。
