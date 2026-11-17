# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

delegated: 零依赖静态 HTML、CSS、JavaScript 与 Python；可直接打开、离线使用，也可由 GitHub Pages 或任意静态服务器托管。

## Users

主要用户是需要在具体产物中快速选择并执行视觉语言的个人开发者、设计工程使用者和 Coding Agent。Coding Agent 读取结构化规范；人通过浏览器目录比较和预览。

## Product Purpose

把分散在 `style-library` 与 `ui-styles` 中的个人视觉资产收成一个可执行正本。用户可以描述任务、筛选风格、比较真实渲染、拿到 token 和组件骨架，并在交付前运行统一检查。

## Positioning

它不是灵感画廊。每个风格都同时具备选择条件、排他条件、可直接引用的 CSS token、页面结构、生图模板、真实预览和自动校验。没有实现或没有明确边界的“风格”不能进入索引。

## Operating Context

在页面设计、重设计、控制台改版、文档版式、生图风格选择和 Agent Skill 调用中使用。高频动作是选一个风格、读两类文件、交付前检查；低频动作是收集参考和新增风格。

## Capabilities and Constraints

- 单页只使用一种风格。
- 推荐基于用户任务，不追求把全部风格塞进一个页面。
- 风格新增只动独立目录，索引、目录数据和预览由脚本生成。
- 浏览器目录必须离线可运行，不依赖第三方 CDN。
- 现有旧入口必须迁移，不能长期保留第二份规则。

## Evidence on Hand

- 17 套可执行风格及其 token、提示词和预览。
- 核心、变体、技法三层，全部保留，默认优先推荐核心风格。
- 从 GOV.UK、Carbon、Primer、Radix、Material、Fluent、Geist 等开源来源提炼的可追溯说明。
- 文档 lint、AI 味儿检查、预览生成器和外部参考提炼流程。

## Product Principles

- 全部保留，但必须分层、可排除、可追溯。
- 选择先看任务和排他条件，再看审美偏好。
- 规范、实现和预览必须同源。
- 新增能力通过生成器扩展，不通过复制规则扩展。
- Agent 的最小读数路径必须足够短。

## Accessibility & Inclusion

目录与预览至少满足 WCAG AA 文本对比度；所有筛选、比较、复制操作支持键盘，并提供清晰的焦点状态。动效只表达状态，并尊重 reduced-motion。

