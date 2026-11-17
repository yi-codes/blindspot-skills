# 开源来源矩阵

这份表只记录“为什么使用它”和“许可边界”，不把项目名字当设计质量证明。

| 来源 | 许可 | 吸收内容 | 落点 | 边界 |
|---|---|---|---|---|
| GOV.UK Frontend | MIT | 表单错误、焦点、公共服务文案 | `civic` | 不复制品牌字体与标识 |
| USWDS | `NOASSERTION` | 移动优先、无障碍表单 | `civic` | 代码使用前逐文件核验 |
| IBM Carbon | Apache-2.0 | 密集表格、状态、企业工作流 | `enterprise-data` | 不复刻 IBM 品牌与默认主题 |
| GitHub Primer | MIT | 开发者文档、代码与工作流 | `developer-docs` | 不使用 GitHub 品牌资产 |
| Radix Themes | MIT | 焦点管理、键盘语义、状态完整性 | `developer-docs`、`enterprise-data` | 不当成完整视觉风格 |
| Material Web | Apache-2.0 | 触控、断点、自适应结构 | `adaptive-companion` | 不使用 Material 默认视觉身份 |
| Microsoft Fluent UI | `NOASSERTION` | 跨设备生产力行为 | `adaptive-companion` | 只作行为参考，暂不复制代码 |
| Vercel Geist | OFL-1.1 | 正文字体与代码字体分工 | `developer-docs` | 字体不是完整设计系统 |

## 使用规则

1. 只吸收能写成 token、组件约束或可验证交互的规则。
2. 记录“弃”的内容，尤其是品牌资产、授权字体和无法迁移的布局。
3. 许可为 `NOASSERTION` 的来源，在逐文件核验前不复制实现。
4. 一个来源不能独立证明一个完整风格；至少需要 token、结构、交互或可访问性三类证据中的两类。

