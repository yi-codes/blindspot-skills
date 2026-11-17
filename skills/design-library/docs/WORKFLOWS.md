# 三个常用工作流

## apply

1. 运行 `designlib recommend "<任务>"`。
2. 读命中风格的两个文件：`DESIGN.md` 与 `tokens.css`。
3. 先确定这一屏唯一的主角。
4. 用该风格的组件与结构骨架实现。
5. 运行 `designlib check`。

## audit

只读检查，不直接改代码：

1. 找出现有实现声明或使用的风格。
2. 对照该风格 `DESIGN.md` 的 Do's、Don'ts、Known Gaps。
3. 检查颜色、字体、间距、圆角是否绕过 token。
4. 检查键盘焦点、空态、错误态、加载态与 reduced-motion。
5. 输出按严重度排序的问题；只有用户要求时才修复。

## redesign

默认保留路由、内容意图和交互结构，只替换视觉层：

1. 先确认现有产品和任务不变。
2. 重新运行推荐，不沿用旧风格。
3. 只读新风格的 `DESIGN.md` 与 `tokens.css`。
4. 先替换 token 与外壳，再逐个处理最破坏风格一致性的组件。
5. 对照 preview 和真实数据重新检查，不只看静态截图。

