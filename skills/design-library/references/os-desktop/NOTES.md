# OS Desktop / Windows 95 Interface — 来源提炼

## 来源

- 类型：① 网页风格卡 + ① 在线风格辞典 + ① 技能卡（含完整 CSS 变量模板）+ ① 开源 CSS 设计系统（引用 Microsoft 官方指南）；四份交叉验证，均为公开网页
- 页面一：https://aesthetic.fyi/os-desktop
  - 显式值：墙纸 Teal `#008080` 或渐变；标题栏灰渐变 `#DFDFDF → #C0C0C0`，活动窗口蓝标题栏、非活动灰；1px solid `#888` 边框与 outset/inset 3D 斜边；系统字体栈 `-apple-system, Segoe UI, Tahoma, sans-serif`；底部常驻任务栏含 Start 按钮、时钟与状态指示；图标对齐刚性网格、小尺寸带标签、32px 精度；768px / 480px 响应；Good For「复古计算展示与博物馆、开发者作品集、交互艺术与实验项目、怀旧产品活动、计算史教育」，Not For「企业 SaaS、移动优先消费 App、电商、极简品牌、内容型新闻媒体」
  - 抓取：2026-11-27
- 页面二：https://indexstyle.org/zh/styles/windows-95-interface
  - 显式规则：1995–2001 微软 UI；灰色面上外缘与内缘两道明暗线；屏幕下端带子 + 左端方按钮；深蓝纯色标题栏 + 右端三个小方块；无抗锯齿小号点阵字、只有分配的字母带下划线；字体「点阵黑体按原尺寸，字号只留一种，强调只用粗体」；版面「下端带子 + 工作区两层，部件间隙 4px 上下，确定/取消横排右下」；材料「只用四色：面灰、亮白、暗中灰、轮廓黑；外缘内缘两条线；按下明暗对调」；注意「只抄灰色和两道线却添圆角或柔和阴影，刻痕方向就读不出来」
  - 抓取：2026-11-27
- 页面三：http://skillsmd.top/skills/erichowens/some_claude_skills/windows-95-web-designer
  - 显式值：桌面青 `#008080`、系统灰 `#c0c0c0`、标题深蓝 `#000080`、标题浅蓝 `#1084d0`、按钮面 `#dfdfdf`、高光 `#ffffff`、阴影 `#808080`、深影 `#000000`、窗口底 `#ffffff`、选中蓝 `#000080`；标题栏 `linear-gradient(90deg,#000080 0%,#1084d0 100%)`、11px Tahoma Bold、padding `3px 4px`；非活动标题栏 `linear-gradient(90deg,#808080,#b5b5b5)`；控制按钮 `16×14px`、gap `2px`、四层 inset 斜边；字体 Tahoma / MS Sans Serif 11px、代码 Fixedsys 12px；开始菜单 `bottom:28px;width:200px`、侧栏 24px 竖排；任务栏 `height:28px`、padding `2px 4px`、gap `4px`、任务按钮 `min-width:140px;max-width:160px;height:22px;11px`；对话框 `min-width:340px`、padding `16px`、图标 `32×32`；主按钮 `min-width:75px;padding:4px 12px`、虚线焦点内缩 4px；间距 `2/4/8/16/24px` 的 4px 网格；反模式「汉堡菜单 / 悬浮操作按钮 / 圆角卡片布局 / 到处渐变背景 / 柔化阴影」；断点 `<640px` 袖珍 PC、`640–1024px` 笔记本、`>1024px` 完整桌面
  - 抓取：2026-11-27
- 页面四：https://jdan.github.io/98.css/ 与 https://github.com/jdan/98.css
  - 显式值（库文档引用 *Microsoft Windows User Experience*）：标准按钮 `75px × 23px`、默认 `12px` 水平 padding；凸起外框与内框，点击后斜边转内凹；禁用按钮保持凸起但标签淡化；焦点是「内容内缩 4px 的虚线边框」；复选框/单选配 `<label for>`；分组框外凹内凸；文本框用 input/textarea；滑块、下拉、树视图、标签页、进度条各有独立语义组件；库本身无 JavaScript，以语义 HTML + CSS 实现
  - 抓取：2026-11-27
- star：不适用（风格卡 / 风格辞典 / 技能卡 / CSS 设计系统，非风格模板仓库）

## 取（吸收了什么，落到哪）

- aesthetic.fyi 与技能卡双源的墙纸 `#008080` → 落到 `colors.desktop` 与 `.preview-root` 背景；窗口之外的青绿是唯一大面积彩色平面。
- 技能卡的 `#c0c0c0` / `#dfdfdf` / `#000080` / `#808080` / `#000000` / `#ffffff` → 落到 `colors.surface-alt` / `surface` / `primary` / `shadow` / `dark-shadow` / `highlight`；纯白与纯黑收进 1px 斜边 token，不作背景。
- 技能卡的标题栏 `linear-gradient(90deg,#000080,#1084d0)` → 落到 `--os-title-gradient`；浅端按本库对比度门槛调深到 `#0A5FA8`，落到 `colors.title-light`。
- IndexStyle 的「外缘内缘两条线 / 按下明暗对调 / 四色刻边」与技能卡的四层 inset → 落到 `elevation.e1`（凸起）与 `elevation.e2`（内凹），以及按钮 `:active` 的 `border-color` 反转。
- 技能卡的 `box-shadow: 2px 2px 0` 与 IndexStyle 禁柔影 → 落到 `elevation.e3`、`--os-shadow-window`；没有模糊、没有发光。
- 技能卡的 `height:28px` 任务栏与 `bottom:28px` 开始菜单定位 → 落到 `spacing.bar` 28px 与 `.preview-root::after` 固定底栏。
- 技能卡的 `32×32` 图标、`16×14` 控制按钮、`75×23` 标准按钮与 4px 网格 → 落到 `media.imageRatio`、`Shapes` 的方块规格、`spacing.micro/xs/sm/md` 与按钮 `min-width:75px`。
- 98.css 的「焦点虚线内缩 4px」→ 落到 `motion.focusRing` 与 `:focus-visible { outline-offset: -4px }`；不用外扩光环。
- aesthetic.fyi 的系统字体栈与 IndexStyle 的「只用一种字号、强调只用粗体」→ 落到 `typography` 的 Tahoma 一族、400/700 两档与 0 字距；中文正文按本库规则提到 18px/1.7。
- 技能卡的三大反模式（汉堡菜单 / FAB / 圆角卡片）与 aesthetic.fyi 的 Not For → 落到 `avoid`、`Do's and Don'ts` 与 `prompt.md` 负向词。
- aesthetic.fyi 的 Good For → 落到 `cues` 与 `When to Use`。

## 弃（明确不吸收，为什么）

- **窗口背景 `#FFFFFF` 与大面积纯黑** → 触犯 The Floor 第 2 条；暖化为 `#F4F2EA` 纸白与 `#1A1A1A` 墨色，纯白/纯黑仅留 1px 斜边与 2px 硬投影。
- **标题栏浅端 `#1084D0`** → 对纸白仅 3.58:1，11px 浅色标题不达 4.5:1；调深到 `#0A5FA8`（5.83:1）。原值保留在来源记录里，不进 token。
- **非活动标题栏渐变 `#808080 → #B5B5B5`** → 第二档灰渐变增加色值数量且预览只有单活动窗口；简化为 `#808080` 实色，非活动态仍可辨。
- **Plus! 暗色主题 `#1a1a2e` / 黄金时代 `#8b4513`** → 扩展主题包，不是 Win95 主语法；合进来会变成多主题拼贴。
- **黄/红/绿/蓝四色语义状态 `#ff0000` / `#ffff00` / `#00ff00` / `#0000ff`** → 来源清晰地把它们列为语义色，但本库 error/disabled 只用已有墨色与深蓝，避免新增色相破坏四色刻边。
- **Fixedsys / MS Sans Serif / Marlett 字形资产** → 字体只取系统无衬线家族与字重规则，中文回退黑体；不引入来源专属点阵字体文件。
- **真实 Windows 徽标、开始按钮图标、厂商字标** → 品牌资产不可迁移；`media.logoRule` 只写排字规则，图标用 1px 线稿重画。
- **汉堡菜单、悬浮操作按钮、圆角卡片布局、到处渐变、柔化阴影** → 技能卡逐条点名反模式；圆角与柔影同时被 IndexStyle 点名会抹掉刻痕方向。
- **Clippy 助手、黄色记事本与可拖拽窗口 JS** → 属于延伸资产/交互，本轮只沉淀桌面、窗口、任务栏、图标网格四条主干；预览用固定双栏与焦点表达层级。
- **「复古 / 怀旧 / 未来感」等形容词** → 不可写成 token；只保留 hex、28px/32px/75px、2px/4px 斜边、4px 网格与 0ms/100ms 这些可检查数值。

## 待观察

- aesthetic.fyi 说墙纸可用青绿或渐变，技能卡与 IndexStyle 只给青绿/灰色；本库取实色青绿，若要做渐变墙纸须另开风格而不是改 token。
- 标题栏浅端 `#0A5FA8` 是本库推断值，不是来源显式值；在真实 Win95 截图里 #1084D0 的亮蓝更具年代感，需要用真机评审确认调深后的气质损失是否可接受。
- 任务栏 28px 是显式值，但 14px 中文标签在其内偏紧；本库限制任务栏只放短词与数字，长导航仍需另开菜单。
- 来源界面字号 11px，本库中文正文 18px/1.7、界面标签 14px/1.5；这使页面不像原尺寸截图，是刻意的可访问性取舍。
- 98.css 的按钮高度 23px 与本库 14px 字 + `4px` padding 推出的高度接近但不完全相同；非像素级复刻，需实机比对。
- 截图环境缺 Tahoma 时中文回退到系统黑体，点阵字的「无抗锯齿」气质会减弱；`-webkit-font-smoothing` 在中文回退字上的效果尚未逐设备采样。
- 没有真实 JS 拖拽/层叠/最小化；`:focus-within` 只能模拟焦点，不能替代多窗口管理，交互实现仍需单独验证。
- 错误态、空态、弹窗文案来源未给出；本库按六态契约推断，属于 Known Gaps 而非来源事实。
