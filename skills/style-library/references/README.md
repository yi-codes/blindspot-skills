# references/ —— 外部样本层

这里放**别人的**设计，不是我的。作用是供给，不是收藏。

```
references/
├── README.md            ← 你正在读的（方法论）
├── claude/
│   ├── DESIGN.md        ← 原始存档，只读，不许改
│   └── NOTES.md         ← 我的提炼卡：吸收了什么、丢了什么
└── ollama/
    ├── DESIGN.md
    └── NOTES.md
```

## 为什么要单独一层

因为"喜欢的风格"和"我自己的风格"是两件事。

混在一起会有两个后果：库变成收藏夹（越多越没用），或者自己的东西被别人的规则污染（改着改着不知道哪个是自己的）。

分开之后，`references/` 可以无限膨胀而不影响 `styles/` 的一致性。**只有经过提炼、能写成数值的东西，才允许进入 `styles/`。**

## 怎么用这一层

### 第一步：拿到原始文件

上游主力是 [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)（127k★，84 个真实网站的 DESIGN.md）。
文件在 `design-md/<品牌>/DESIGN.md`。

```bash
./scripts/fetch-ref.sh <owner/repo> <path> <短名>
# 例：
./scripts/fetch-ref.sh VoltAgent/awesome-design-md design-md/linear/DESIGN.md linear
```

也可以从别处来：某个产品官网、自己截图分析、Figma 社区的规范文件。只要能落成 DESIGN.md 格式，就走同一套流程。

### 第二步：拆

拿到一份外部 DESIGN.md，先做一次二分：**哪些能变成数值，哪些只是氛围。**

| 能吸收（写进 NOTES 的"取"） | 不能吸收（写进"弃"） |
|---|---|
| 具体色值和它出现的比例 | "高级感""未来感"这类形容词 |
| 字号阶的比例关系（1.25 还是 1.333） | 只有该品牌有的字体授权 |
| 间距节奏（8 倍数 / 4 倍数） | 特定插画风格、吉祥物 |
| 圆角与阴影的选择逻辑 | 动效的具体曲线（除非有明确数值） |
| Do / Don't 里的硬规则 | 版权标识、logo 用法 |
| 一个风格怎么处理"层级" | 与品牌强绑定的文案语气 |

**判断标准：这一条能不能写成 `{token}` 或一条可检查的规则？**
不能，就是氛围，留在 REFERENCES 里当灵感，别往 styles 里搬。

### 第三步：落

提炼出的东西分三种去处：

1. **补进现有风格**——大部分情况。比如从 Claude 学到"墨色不用纯黑"，直接修 `editorial-serif` 的 `colors.ink`。
2. **成为通用原则**——跨风格都成立的，写进 `principles.md`。比如"颜色不超过三个家族"。
3. **促成新风格**——只有当它**必须违反现有风格的硬约束**时才新开。见 `principles.md` 第 8 节。

### 第四步：写 NOTES.md

每份样本必配一张卡，四个字段不能少：

```markdown
# <品牌>

## 来源
仓库 / 路径 / 抓取日期 / star 数

## 取（吸收了什么，落到哪）
- 具体一条 → 落到 styles/xxx 的哪个 token，或 principles.md 第几节

## 弃（明确不吸收，为什么）
- 具体一条 → 原因（授权 / 与风格冲突 / 只是装饰）

## 待观察
- 还看不懂或没验证的
```

**"弃"这一栏比"取"更重要。** 它记录的是判断力，半年后回头看，你能知道自己当时为什么没抄它。

## 三条纪律

1. **原始存档不改**。`references/<name>/DESIGN.md` 是证据，改了就失去参照价值。要标注批注写在 NOTES 里。
2. **不整份搬进 styles**。搬进来的是提炼结果，不是文件。库里不该出现两个长得一样的风格。
3. **吸收要能追溯**。`styles/x/DESIGN.md` 里如果有一条规则是从外面学来的，在 NOTES 里要能对上。追溯不了，说明是拍脑袋加的。

## 上游动态

- 格式规范：[google-labs-code/design.md](https://github.com/google-labs-code/design.md)（28.9k★），`docs/spec.md`
- 样本库：[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)（127.6k★）
- 官方校验：`npx @google/design.md lint DESIGN.md`（能查 WCAG 对比度、失效引用；不认识 `borderColor` 这类自定义属性，会告警——规范里组件属性只有 8 个）
