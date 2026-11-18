# The Broad

## 来源

- 类型：① 二手网站设计分析（OpenDesign，含页面截图索引）
- 页面：https://opendesign.cc/en?open=the-broad
- 原站：https://thebroad.org
- 抓取：2026-11-17
- star：不适用

## 取（吸收了什么，落到哪）

- `#D6001C` 单一行动红、`#333F48` 墨色 → `gallery-wall` 的 primary 与 ink。
- 12 列、24px 槽沟、作品图优先和简洁展签 → `styles/gallery-wall/`。
- 直角主面板、清晰导航、不遮挡艺术品 → Shapes、Components 与 Don't。

## 弃（明确不吸收，为什么）

- 纯白大面积背景 → 改为 `#F3F3F0`，遵守本库底色规则。
- 大写导航与标题 → 中文无对应语义，且不作为默认装饰。
- 原站卡片阴影 → 展陈作品不需要，只有悬浮功能层保留有限投影。

## 待观察

- 红色行动点在摄影作品展中的抢眼程度。
- 预约购票与藏品筛选尚未进入组件范围。
