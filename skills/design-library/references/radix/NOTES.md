# Radix Themes

## 来源

- 仓库：[`radix-ui/themes`](https://github.com/radix-ui/themes)
- 许可：MIT
- 角色：焦点管理、键盘语义、状态完整性
- 落点：`styles/developer-docs/`、`styles/enterprise-data/`、全局 Floor

## 取

- 所有交互元素必须有即时可见的 `:focus-visible`。
- 菜单、弹层与抽屉需要可返回原焦点，不能把键盘用户留在空处。
- 禁用、加载、错误和成功状态必须与正常状态共享几何。
- 组件可组合不等于页面可以混用多种视觉语言。

## 弃

- 不把 Radix 的默认主题当成风格；它首先是交互与可访问性基础设施。
- 不复制组件 API 作为本库的 API。

## 待观察

- 复杂命令面板的焦点陷阱与撤销行为。
- 嵌套弹层的返回路径需要在浏览器中逐条验证。

