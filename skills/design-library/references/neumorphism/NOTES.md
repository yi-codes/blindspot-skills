# Neumorphism

## 来源

- 类型：① 二手设计风格分析（三份 DESIGN.md 交叉验证）+ 一手 CSS 生成器参数
- 页面一（一手色值与字阶）：https://github.com/bergside/awesome-design-skills/blob/HEAD/skills/neumorphism/DESIGN.md
  （raw: https://raw.githubusercontent.com/bergside/awesome-design-skills/HEAD/skills/neumorphism/DESIGN.md）
- 页面二（中文风格卡、明暗定义、Good/Not Good）：https://stitchprompt.com/zh/gallery/neumorphism
- 页面三（圆角与字体分工、9 节约束）：https://opendesigner.io/uk/design-systems/neumorphism
- 页面四（双向阴影生成器，标定偏移—模糊关系）：https://neumorphism.io/
- 抓取：2026-11-28
- star：不适用

## 取（吸收了什么，落到哪）

- bergside 的显式色板 `primary #006666`、`surface #E7E5E4`、`text #1E2938`、`success #00A63D` → 落到 `styles/neumorphism` 的 `colors.primary / canvas+surface / ink / accent`，其中 canvas 与 surface 同值正是新拟态「控件与底同色」的定义。
- bergside 的字号 `h1 3rem / body 1rem / label 0.75rem` 与「100–900 权重声明」→ 折算成 44/18/11px 三档参照，权重在本库收敛到 700/400。
- stitchprompt 的定义「同色系底 #F1F2F5 上，左上高光与右下阴影的双向投影塑造凸起与凹陷，控件无边框，全靠光影暗示可点击」→ 落到 `elevation.e1/e2/e3` 与 Elevation & Depth 一节；这是本风格的核心语法。
- stitchprompt 的 Good For「趣味小工具界面、智能家居控制面板」与 Not Good For「信息密集后台、扁平极简产品」→ 落到 `cues / avoid`。
- stitchprompt 的圆角 `sm 4 / md 8 / lg 12px`、间距 `8/12/24px`、Inter 字族与标题 32 / 正文 16 / 标签 13px → 落到 `rounded / spacing / typography` 的基准，中文正文按本库下限上提。
- opendesigner 的默认圆角 `22px`、字体分工 `Inter 正文 / SF Mono 代码`、base `16px` → 卡片圆角取 22px、正文用 Inter、代码交回系统等宽栈。
- neumorphism.io 的默认参数 `background #e0e0e0`、`box-shadow: 20px 20px 60px #bebebe, -20px -20px 60px #ffffff` → 提炼出「偏移:模糊 ≈ 1:3、双向异色、有明确方向」的关系，本库按控件尺寸缩到 6/12px 与 12/24px 两档（e1/e2），凹陷用同值 inset（e3）。
- 三份来源一致的「单色、无边框、无彩渐变、柔和塑料感」→ 落到 `elevation.separator: shadow`、Do's and Don'ts 与 prompt.md 的负向词。

## 弃（明确不吸收，为什么）

- 来源的纯白高光 `#ffffff` 与 stitchprompt 的纯白 surface `#FFFFFF` → 不作任何背景或文字色；纯白只保留在 `--ne-shadow-light` 阴影变量里（The Floor 第 2 条：浅色底不用大面积纯白）。
- 来源 success `#00A63D`（stitchprompt 作主强调）对暖灰底仅 2.56:1 → 调深到 `#0B7A32`（4.35:1），且只走 ≥14px 图形与非正文状态点，不承载段落。
- bergside 的 `warning #FE9900`、`danger #FF2157` 与 8 档语义色 → 全部不用；为守住「一族中性 + 青 + 绿」三色族，error 态借墨色说明而非新增警示色。
- bergside 的 `Space Mono / JetBrains Mono` 作为正文与标题字族 → 等宽字体当正文是 slop S6 戏服，且中文不成立；正文统一 Inter，代码交回系统栈。
- bergside 的 `100–900` 九档字重 → 收敛到 700/400 两档；中文回退字体缺中间字重，写九档会在中文里失真。
- 来源 `surface #F1F2F5`（stitchprompt）与 `#E7E5E4`（bergside）冲突 → 取后者作画布；两者同为暖灰、都能承接双向阴影，冲突已记入 Known Gaps。
- 来源 `border #d7d8da` 的细边框分层（stitchprompt 推导）→ 弃用；新拟态的主分隔只有 shadow，加边框会把「浮起」读成「框起来」。
- 来源正文 16px、标签 13px → 中文正文提到 18px/1.7、标签提到 14px/1.5；这是可访问性改造，不是原尺寸。
- 真实 3D 触控、力反馈与设备振动 → 不可迁移；Web 只有阴影切换，不做伪弹簧动画。

## 待观察

- 双向投影在低对比暖灰底上可读性依赖设备校色；暗影 `#B9B6B3` 对底仅 1.61:1，暗光环境或低端屏上「浮起」读感会减弱，需在真机复核。
- 截图环境可能缺 Inter；中文回退到系统黑体后，柔软字腔会减弱。
- success 调深到 `#0B7A32` 后仍是 4.35:1，未达正文 4.5:1；含表单的页面若让绿色承载小字需再调深或换墨色。
- 本轮只做了 tool 模板预览；story / docs / table 模板下的凸起密度与凹槽读感尚未验证。
- 与 `tactile-3d` 的边界靠「静止 vs 随指针倾斜」划分；两者混用会破坏本风格的单光源约束，需在实际页面里复核。
