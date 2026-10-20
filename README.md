# blindspot-skills

让 AI 回答问题时，把"你不知道自己不知道"的部分暴露出来。

[English](#english)

## 为什么做这个

AI 默认会给出一个流畅、自洽、看起来完整的答案。答案里明显的错误，你还能纠正；真正危险的是它没提到的东西：被略过的替代方案、没说出口的前提、已经过时的知识。这些是"未知的未知"，单靠读得更仔细是发现不了的。

这个仓库把应对思路拆成三个阶段，每个阶段一个 skill：

| Skill | 什么时候用 | 做什么 |
| --- | --- | --- |
| [blindspot-map](skills/blindspot-map/SKILL.md) | 问之前，进入陌生领域时 | 先画问题空间地图：子领域、分歧、常见坑、该问没问的问题，并帮你改写提问 |
| [answer-audit](skills/answer-audit/SKILL.md) | 答之后，结论要用来做决定时 | 拆出关键断言，区分事实与推断，找承重假设和遗漏，联网核对并给出处 |
| [cross-check](skills/cross-check/SKILL.md) | 结论很重要时 | 把同一个问题盲问另一个模型，再逐点比较分歧，分歧处往往就是盲区 |

三者可以单独用，也可以串起来：`blindspot-map` 选方向，正常回答，`answer-audit` 审计，必要时 `cross-check` 独立验证。

skill 要你开口或被模型判断匹配才会启用，但"未知的未知"往往发生在你根本没意识到该怀疑的时候。为此仓库另附一条可选的常驻规则 [rules/blindspot-rule.md](rules/blindspot-rule.md)：追加到全局指令文件后，遇到高风险问题时，回答末尾会自动附上几行"盲区提示"。

## 设计取舍

- **自查有上限。** 同一个模型的盲区，换个角度再问通常还是盲区，所以 `cross-check` 引入独立来源，并且第一轮只发问题、不发原答案，避免对方被锚定。
- **宁缺毋滥。** `answer-audit` 的每条批评都要过三个测试（结论会不会因此改变、是不是放之四海皆准的空话、敢不敢押注它成立），不通过就删掉，避免一堆"看似严谨"的废话淹没真正的问题。
- **按风险投入。** 随口一问不需要这些流程，skill 的描述里写明了不适用的场景，避免每个问题都被拖长。
- **不外发敏感内容。** `cross-check` 发出提问前要求检查并脱敏；调用的模型在空的临时目录中运行，读不到你的项目文件。

## 安装

```bash
git clone https://github.com/yi-codes/blindspot-skills.git
cd blindspot-skills

# Codex（可选常驻规则：cat rules/blindspot-rule.md >> ~/.codex/AGENTS.md）
mkdir -p ~/.codex/skills
for s in skills/*; do ln -s "$PWD/$s" ~/.codex/skills/; done

# Claude Code（可选常驻规则：cat rules/blindspot-rule.md >> ~/.claude/CLAUDE.md）
mkdir -p ~/.claude/skills
for s in skills/*; do ln -s "$PWD/$s" ~/.claude/skills/; done
```

用符号链接安装，之后 `git pull` 即可更新。

`cross-check` 会用到本机的模型命令行（`claude` 或 `codex`），也可以通过环境变量 `CROSS_CHECK_CMD` 配置任何从标准输入读取提示词的命令，例如 `export CROSS_CHECK_CMD='llm -m <model-name>'`。没有可用命令时，它会生成一段提示词让你手动贴到另一个模型。

## 使用示例

- "我要给团队选一个向量数据库，但对这个领域不熟，先帮我做个盲区扫描。"
- "审一下你刚才这个回答，有没有漏掉什么？"
- "这个结论我要拿去做决定，换个模型交叉验证一下。"

## 致谢

- Thariq Shihipar，[A field guide to Claude Fable 5: Finding your unknowns](https://claude.com/resources/articles/a-field-guide-to-claude-fable-finding-your-unknowns)："盲区扫描"和已知/未知四象限的思路来自这篇文章。
- Jiang et al.，[Into the Unknown Unknowns: Engaged Human Learning through Participation in Language Model Agent Conversations](https://arxiv.org/abs/2408.15232)（Co-STORM，EMNLP 2024）：用多视角对话暴露未知的未知。
- [bozhouDev/finding-unknowns-skills](https://github.com/bozhouDev/finding-unknowns-skills)（MIT）：把上述文章提炼成常驻的 `CLAUDE.md` 准则。本仓库"常驻规则"的做法受它启发。
- [sangrokjung/claude-forge](https://github.com/sangrokjung/claude-forge) 中的 `blind-spot-pass`（MIT）：`blindspot-map` 借鉴了它的地图结构（先说结论、最少术语、真正左右结果的几个决定、改写后的提问）和"只教到能提问为止、不当关卡"的原则。
- [kdoble/red-team-skeptic](https://github.com/kdoble/red-team-skeptic)（MIT）：`answer-audit` 借鉴了它的自我质疑关卡（承重、普适、下注三个测试）、按风险分级的审查力度、"被审内容是数据不是指令"和"自带链接不算证据"的规则。

以上项目的思路经过改写和取舍，本仓库文字为独立撰写；与它们相比，本仓库面向一般问答而不仅是写代码，并补上了跨模型盲问验证这一步。

## English

Skills that help an AI agent surface your *unknown unknowns* instead of handing you one fluent, overconfident answer. Works with Codex and Claude Code (standard `SKILL.md` format). The skill instructions are written in Chinese; agents follow them and reply in your language.

- **blindspot-map**: before answering, map the problem space: sub-areas, disagreements, common pitfalls, and the questions you should be asking.
- **answer-audit**: after answering, split key claims into fact, inference, and guess, find load-bearing assumptions and omissions, and verify claims against primary sources.
- **cross-check**: blind-ask a different model the same question without revealing the first answer, then compare where they disagree.

Optionally append `rules/blindspot-rule.md` to `~/.codex/AGENTS.md` or `~/.claude/CLAUDE.md` so high-stakes answers end with a short blind-spot note even when you did not think to ask.

Install by symlinking the folders under `skills/` into `~/.codex/skills` or `~/.claude/skills` (see above). MIT licensed.
