# Design Library

一套给 AI 用、也给自己看的设计风格库。

它把“选风格、看样张、拿 token、做页面、做审计、继续收集”串成一条工作流。每个风格不是形容词，而是一组可执行的约束：颜色、字体、字号、间距、圆角、组件、布局骨架和排他条件。

## 为什么合并

旧版分成两个入口：

- `style-library`：脚本完善，但覆盖的主要是阅读与展示型页面
- `ui-styles`：控制台和工作台经验很深，但索引靠手写，规范与实现容易漂移

现在统一为一个 `design-library`：

- 只有一个风格索引
- 每个风格只有一套正本
- 一个命令负责推荐
- 一个命令负责构建索引与预览
- 一个命令负责完整检查
- 浏览器里可以搜索、筛选和并排比较

全部风格都保留，并按三类组织：

- **核心**：独立承担一种页面职责，默认优先推荐
- **变体**：核心风格的明暗、材料或密度分支
- **技法**：3D、玻璃、氛围等可复用视觉技法

目录同时给出 `family` 与 `sourceRefs`，能从风格追溯回开源来源和提炼卡。
完整入库与分层规则见 [`docs/CURATION.md`](docs/CURATION.md)。

## 快速开始

```bash
# 看全部风格
python3 scripts/designlib.py list

# 描述任务，获得排序和理由
python3 scripts/designlib.py recommend "运维值班台，查看告警并批准 AI 建议"

# 查看某个风格的最小读数路径
python3 scripts/designlib.py show signal-console

# 重建索引与预览
python3 scripts/designlib.py build

# 完整检查
python3 scripts/designlib.py check
```

浏览器打开 `catalog/index.html`，可以搜索任务、筛选风格、查看真实 token 渲染，并最多并排比较三个风格。

## 目录

```text
design-library/
├── SKILL.md
├── README.md
├── PRODUCT.md
├── DESIGN.md                 # 风格库浏览器自身的界面规范
├── principles.md
├── styles/
│   ├── INDEX.md              # 自动生成
│   ├── index.json            # 自动生成
│   └── <slug>/
│       ├── DESIGN.md
│       ├── tokens.css
│       └── prompt.md
├── catalog/                  # 可搜索、筛选、比较的静态浏览器
├── preview/                  # 自动生成的单风格与总览样张
├── docs/
├── references/
├── prompts/
└── scripts/
```

## 在网页里使用

```html
<link rel="stylesheet" href="styles/signal-console/tokens.css">

<div class="ds-signal-console">
  <h1>告警与证据</h1>
  <p>先回答哪里不对劲，再给下一步动作。</p>
</div>
```

颜色、字体、间距和圆角都通过该风格自己的变量引用。不要跨风格复制内部变量名。

## 新风格

```bash
python3 scripts/designlib.py new quiet-report "安静报告"
```

然后填写：

- `styles/quiet-report/DESIGN.md`
- `styles/quiet-report/tokens.css`
- `styles/quiet-report/prompt.md`

最后：

```bash
python3 scripts/designlib.py build
python3 scripts/designlib.py check
```

新增风格只动自己的目录；索引、目录数据和预览都由脚本生成。要不要新增的判断标准见 `principles.md` §8。

从旧入口迁移的路径与命令映射见 [`docs/MIGRATION.md`](docs/MIGRATION.md)。

## 逐项检查

```bash
python3 scripts/lint.py
python3 scripts/slop.py preview/*.html catalog/index.html
python3 -m unittest discover -s tests
```

`designlib check` 会串起以上检查，并额外验证索引、目录数据和本地链接是否一致。

## 让本地 Agent 用上

从仓库根目录安装一次：

```bash
mkdir -p ~/.codex/skills
ln -sfn "$PWD/skills/design-library" ~/.codex/skills/design-library
```

Claude Code 把目标目录改成 `~/.claude/skills/design-library`。使用软链，不复制，保证本地 Agent 始终读同一份正本。
