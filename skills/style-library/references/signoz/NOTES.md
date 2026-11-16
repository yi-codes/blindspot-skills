# SigNoz

## 来源

- https://github.com/SigNoz/signoz
- https://github.com/SigNoz/design-tokens
- `frontend/src/constants/theme.ts`
- `frontend/src/containers/AlertHistory/Statistics/StatsCard/StatsCard.styles.scss`
- `frontend/src/components/Logs/RawLogView/styles.ts`
- `src/tokens/semantic-tokens.json`
- `src/tokens/radius.json`
- `src/tokens/spacing.json`
- `src/tokens/typography.json`
- 抓取日期：2026-11-16

## 取

- Inter 正文与 Geist Mono 数据字体分工 → Signal Console / Typography。
- 13px 正文、11px 小标签和 20 / 18px 行高构成的密集运维阅读节奏 → Signal Console / Typography。
- 4px 基础圆角、2px 小控件圆角 → Signal Console / Shapes；比 Codex 桌面工具更硬朗。
- 日志行使用 13 / 24px 等宽排版，强调逐行扫描 → Signal Console / Components / code-block。
- 语义 token 覆盖背景、边框、状态、调用提示和日志高亮 → Signal Console / Colors。

## 弃

- SigNoz 的完整 Ant Design 组件体系不直接复制；本库只冻结视觉决策。
- 多套产品主题和大规模图表色板不进入新风格；只保留五个有稳定语义的系列色。
- 不使用其页面中的大写小标签作为默认规则，中文界面仍使用原样大小写。

## 待观察

- 大规模日志虚拟滚动、拓扑边标签避让和 AI 助手嵌入方式仍需要在真实页面验证。
