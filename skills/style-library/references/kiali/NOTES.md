# Kiali

## 来源

- https://github.com/kiali/kiali
- `frontend/src/pages/Overview/OverviewStyles.ts`
- `frontend/src/pages/Graph/styles/styleNode.tsx`
- `frontend/src/pages/Graph/styles/styleEdge.tsx`
- `frontend/src/pages/Graph/SummaryPanelStyle.tsx`
- 抓取日期：2026-11-16

## 取

- 拓扑节点同时显示服务身份、状态背景和流量标签，读者不必在多个视图之间拼接上下文 → Signal Console / Operations Layout。
- 选中边使用统一强调色，未命中对象降低透明度；颜色和空间位置共同表达关系 → Signal Console / Components。
- 详情面板使用发丝边框和接近方形的圆角，轻微阴影只帮助浮层脱离底图 → Incident Room / Elevation & Depth。
- 搜索命中、trace 覆盖和当前焦点使用不同覆盖语义，而不改变节点本体 → Signal Console / Do's and Don'ts。

## 弃

- Kiali 继承的 PatternFly 页面框架和品牌色不直接复制。
- 高密度拓扑中的浮动摘要面板不适用于所有运维页面，只在需要上下文检查时出现。
- 流量动画只在真实流量数据存在时启用；个人风格库禁止装饰性拓扑动效。

## 待观察

- 复杂 graph 布局性能和窄屏节点标签策略未覆盖；后续应在真实拓扑数据上验证。
