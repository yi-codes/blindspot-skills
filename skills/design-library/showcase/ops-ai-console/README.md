# Meridian Ops · 运维 AI 控制台样张

一套三屏运维 AI 控制台概念样张：

| 页面 | 职责 | 风格 |
|---|---|---|
| [日常告警分诊](daily.html) | 当前哪里不对、证据是什么、是否批准建议 | `signal-console` |
| [重大事故响应](incident.html) | 事实、假设、动作、验证和接班摘要 | `incident-room` |
| [Agent 执行回放](agent-replay.html) | 计划、命令、文件、验证与待批准动作 | `liquid-glass` |

入口：[总览样张](index.html)

## 共同原则

- 一屏只回答一个主问题。
- AI 结论与系统事实分开。
- 每个数字都有时间窗口与单位。
- 待批准动作紧邻证据、风险和影响范围。
- 不展示隐藏推理，只展示计划摘要、工具调用和可验证结果。
- 所有交互都是本地样张，不连接真实系统。

## 设计选择

**Hallmark · v2.0.0**

- **Mode** · Operate
- **Screen** · 日常分诊、事故响应、Agent 回放三屏
- **Styles** · `signal-console`、`incident-room`、`liquid-glass`
- **Signature** · 从信号到证据再到待批准动作的连续工作区
- **Material** · 示例服务名、指标、日志和命令，不冒充真实生产数据
- **States** · 筛选切换、证据标签、审批对话框和运行回放
- **Sweep** · Hallmark app scope 与 Impeccable detector 均通过

## 本地打开

```bash
open showcase/ops-ai-console/index.html
```

重新生成截图：

```bash
node scripts/capture-ops-showcase.mjs
```

截图保存在 `screens/`。样张数据只用于展示信息结构与视觉表达。

