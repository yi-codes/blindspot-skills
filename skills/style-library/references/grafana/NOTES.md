# Grafana

## 来源

- https://github.com/grafana/grafana
- `packages/grafana-data/src/themes/themeDefinitions/visual_refresh_dark.json`
- `packages/grafana-data/src/themes/themeDefinitions/visual_refresh_light.json`
- `packages/grafana-data/src/themes/createShadows.ts`
- `packages/grafana-data/src/themes/createShape.ts`
- `packages/grafana-data/src/themes/createTypography.ts`
- `packages/grafana-ui/src/themes/GlobalStyles/card.ts`
- 抓取日期：2026-11-16

## 取

- 14px 正文、12px 小字和 22px 行高组成稳定的控制台阅读节奏 → Signal Console / Typography。
- 4 / 8 / 12px 圆角分层 → Signal Console / Shapes；普通卡片与输入保持窄圆角。
- 普通卡片的 `box-shadow: none`，层级依靠表面底色与边框；阴影只用于 z1–z3 浮层 → Signal Console / Elevation & Depth。
- 状态色按 error / warning / success / info 定义，图表系列色另列 → Signal Console / Colors。
- 表格有表头、行条纹、悬停和选中底色 → Signal Console / Operations Layout。

## 弃

- Grafana 的品牌橙色高亮和大面积官方主题外观不直接复制；控制台需要与用户产品身份结合。
- 多套可切换主题色板不进入个人风格库；保留深色主态和一套中性浅色即可。
- 图表组件库和查询编辑器实现细节不属于视觉规范。

## 待观察

- Grafana 的顶部导航和 Explore 页面需要进一步做响应式样本；当前只吸收 token 和卡片规则。
