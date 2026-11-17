#!/usr/bin/env python3
"""为每个风格生成独立预览页，并生成总览页。

预览使用同一份内容骨架，但加载每个风格自己的 tokens.css。
这样比较的是真实 token 与基础组件，不是截图或手绘 mock。
"""

from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "styles" / "index.json"
OUT_DIR = ROOT / "preview"

REGISTER_ZH = {
    "story": "讲故事",
    "professional": "讲专业",
    "technical": "讲技术",
    "tool": "讲工具",
}


def story_sample() -> str:
    return """
      <nav class="frame-nav">
        <strong>North Line</strong>
        <span>Issue 04</span>
        <a href="#sample-main">阅读全文</a>
      </nav>
      <main id="sample-main" class="frame-story">
        <p class="frame-context"><time datetime="2026-11-17">2026 年 11 月 17 日</time></p>
        <h1>把复杂的事情，留给一段安静的文字</h1>
        <p class="frame-lede">真正耐读的页面不靠装饰争夺注意力。它先给出清楚的结构，再让材质、字号和留白承担节奏。</p>
        <div class="frame-actions">
          <button type="button">开始阅读</button>
          <a href="#sample-cards">查看目录</a>
        </div>
        <section id="sample-cards" class="frame-grid">
          <article class="ds-card">
            <h2>层级来自落差</h2>
            <p>标题与正文之间要拉开足够距离，相近字号只会制造犹豫。</p>
          </article>
          <article class="ds-card">
            <h2>一个信号色</h2>
            <p>强调色只指向操作和当前状态，不承担装饰。</p>
          </article>
          <article class="ds-card">
            <h2>让内容先说话</h2>
            <p>先确定这一屏最该被看见的内容，再决定容器和边界。</p>
          </article>
        </section>
      </main>
    """


def professional_sample() -> str:
    return """
      <nav class="frame-nav">
        <strong>Atlas Studio</strong>
        <span>产品方案</span>
        <a href="#sample-main">查看结论</a>
      </nav>
      <main id="sample-main" class="frame-professional">
        <header class="frame-split">
          <div>
            <h1>把分散的工作，收进一个清楚的决策面</h1>
            <p class="frame-lede">用户不需要先理解系统结构，只需要知道现在发生了什么、下一步做什么。</p>
            <div class="frame-actions"><button type="button">查看方案</button></div>
          </div>
          <dl class="frame-stats">
            <div><dt>开放事项</dt><dd><span class="ds-stat-value">12</span></dd></div>
            <div><dt>本周完成</dt><dd><span class="ds-stat-value">31</span></dd></div>
            <div><dt>待确认</dt><dd><span class="ds-stat-value">4</span></dd></div>
          </dl>
        </header>
        <section class="frame-grid">
          <article class="ds-card">
            <h2>先给结论</h2>
            <p>将最重要的判断放在章节顶部，再用证据支持它。</p>
          </article>
          <article class="ds-card">
            <h2>统一时间窗</h2>
            <p>每个数字都带时间范围，避免把不同口径放在一起比较。</p>
          </article>
          <article class="ds-card">
            <h2>下一步可见</h2>
            <p>主操作与当前状态保持相邻，不让用户自己拼线索。</p>
          </article>
        </section>
      </main>
    """


def technical_sample() -> str:
    return """
      <nav class="frame-nav">
        <strong>runtime-kit</strong>
        <span>Guide</span>
        <a href="#sample-main">API reference</a>
      </nav>
      <main id="sample-main" class="frame-technical">
        <header>
          <h1>从一个可验证的最小任务开始</h1>
          <p class="frame-lede">技术页面的首要任务不是显得复杂，而是让读者能复现结果、定位失败并继续前进。</p>
        </header>
        <section class="frame-grid">
          <article class="ds-card">
            <h2>安装</h2>
            <pre><code>npm install runtime-kit</code></pre>
            <p>列出唯一需要的命令，不混入可选步骤。</p>
          </article>
          <article class="ds-card">
            <h2>运行</h2>
            <pre><code>runtime-kit check --strict</code></pre>
            <p>成功与失败都要给出下一步，而不是只抛错误。</p>
          </article>
          <article class="ds-card">
            <h2>验证</h2>
            <pre><code>0 errors, 0 warnings</code></pre>
            <p>用可观察结果结束，不写“配置完成”却无法验证。</p>
          </article>
        </section>
      </main>
    """


def tool_sample() -> str:
    return """
      <div class="frame-app">
        <aside class="frame-side">
          <strong>Workbench</strong>
          <nav>
            <a href="#sample-main" aria-current="page">当前任务</a>
            <a href="#sample-cards">运行记录</a>
            <a href="#sample-actions">连接</a>
          </nav>
          <p class="frame-muted">最近同步 2 分钟前</p>
        </aside>
        <main id="sample-main" class="frame-workspace">
          <header class="frame-toolbar">
            <div>
              <h1>整理发布前检查</h1>
              <p class="frame-muted">有 3 个检查通过，1 个需要确认。</p>
            </div>
            <button type="button">继续执行</button>
          </header>
          <section class="frame-grid" id="sample-cards">
            <article class="ds-card">
              <h2>代码检查</h2>
              <p>全部通过。最近一次运行于 14:32。</p>
              <span class="ds-tag">通过</span>
            </article>
            <article class="ds-card">
              <h2>预览构建</h2>
              <p>产物已生成，等待人工确认移动端布局。</p>
              <span class="ds-tag">待确认</span>
            </article>
            <article class="ds-card">
              <h2>发布说明</h2>
              <p>已从本次变更生成，没有发现未登记卡片。</p>
              <span class="ds-tag">通过</span>
            </article>
          </section>
          <section class="frame-task" id="sample-actions">
            <div>
              <h2>当前需要你决定</h2>
              <p>预览中的移动端筛选栏可以折叠为按钮。批准后将进入发布步骤。</p>
            </div>
            <div class="frame-actions">
              <button type="button">批准并继续</button>
              <button type="button">查看差异</button>
            </div>
          </section>
        </main>
      </div>
    """


def docs_sample() -> str:
    return """
      <div class="frame-docs">
        <aside class="frame-docs-nav">
          <strong>runtime-kit</strong>
          <nav>
            <a href="#sample-main" aria-current="page">快速开始</a>
            <a href="#sample-cards">核心概念</a>
            <a href="#sample-cards">API 参考</a>
          </nav>
          <p class="frame-muted">v2.4 · 当前版本</p>
        </aside>
        <main id="sample-main" class="frame-docs-main">
          <h1>从一个可验证的最小任务开始</h1>
          <p class="frame-lede">安装依赖、运行检查、读取结果。每一步都能独立验证，失败时给出下一步。</p>
          <h2>安装</h2>
          <pre><code>npm install runtime-kit</code></pre>
          <h2>运行</h2>
          <pre><code>runtime-kit check --strict</code></pre>
          <div class="frame-grid" id="sample-cards">
            <article class="ds-card">
              <h3>版本</h3>
              <p>v2.4 与上一版保持配置兼容。</p>
            </article>
            <article class="ds-card">
              <h3>结果</h3>
              <p>检查通过后返回可复制的摘要。</p>
            </article>
            <article class="ds-card">
              <h3>失败</h3>
              <p>错误信息包含位置和恢复命令。</p>
            </article>
          </div>
        </main>
        <aside class="frame-docs-toc">
          <strong>本页</strong>
          <a href="#sample-cards">安装</a>
          <a href="#sample-cards">运行</a>
          <a href="#sample-cards">结果</a>
        </aside>
      </div>
    """


def table_sample() -> str:
    return """
      <div class="frame-data-shell">
        <aside class="frame-data-side">
          <strong>Operations</strong>
          <nav>
            <a href="#sample-main" aria-current="page">订单</a>
            <a href="#sample-main">客户</a>
            <a href="#sample-main">权限</a>
            <a href="#sample-main">审计</a>
          </nav>
        </aside>
        <main id="sample-main" class="frame-data-main">
          <header class="frame-toolbar">
            <div>
              <h1>订单</h1>
              <p class="frame-muted">12,480 条记录，当前筛选 24 条。</p>
            </div>
            <button type="button">新建订单</button>
          </header>
          <div class="frame-filterbar">
            <span>状态：待处理</span>
            <span>区域：华东</span>
            <span>时间：最近 7 天</span>
          </div>
          <table>
            <thead><tr><th>订单</th><th>客户</th><th>金额</th><th>状态</th><th>负责人</th></tr></thead>
            <tbody>
              <tr><td>ORD-1842</td><td>North Studio</td><td>¥ 8,400</td><td>待处理</td><td>Lin</td></tr>
              <tr><td>ORD-1841</td><td>Ming Labs</td><td>¥ 12,900</td><td>已审核</td><td>Wei</td></tr>
              <tr><td>ORD-1840</td><td>Field Notes</td><td>¥ 3,240</td><td>待发货</td><td>Chen</td></tr>
              <tr><td>ORD-1839</td><td>Atlas Works</td><td>¥ 21,760</td><td>已完成</td><td>Lin</td></tr>
            </tbody>
          </table>
          <div class="frame-task">
            <div><h2>已选择 2 条记录</h2><p>批量操作会写入审计日志，并在执行前再次确认。</p></div>
            <button type="button">批量更新</button>
          </div>
        </main>
      </div>
    """


def adaptive_sample() -> str:
    return """
      <main class="frame-adaptive" id="sample-main">
        <header>
          <p class="frame-muted">今天，星期二</p>
          <h1>把今天收成一个清楚的下一步</h1>
          <p class="frame-lede">三个任务已完成，一个决定需要你确认。重要信息保持在拇指可达的位置。</p>
        </header>
        <section class="frame-grid" id="sample-cards">
          <article class="ds-card">
            <span class="ds-tag">下一步</span>
            <h2>确认明天的行程</h2>
            <p>地点与出发时间已经整理好，只差你的确认。</p>
            <button type="button">查看并确认</button>
          </article>
          <article class="ds-card">
            <h2>今日回顾</h2>
            <p>2 条笔记已归档，1 条等待补充。</p>
          </article>
        </section>
        <nav class="frame-mobile-nav" aria-label="应用导航">
          <a href="#sample-main" aria-current="page">今天</a>
          <a href="#sample-cards">任务</a>
          <a href="#sample-cards">笔记</a>
          <a href="#sample-cards">设置</a>
        </nav>
      </main>
    """


SAMPLES = {
    "story": story_sample,
    "professional": professional_sample,
    "technical": technical_sample,
    "tool": tool_sample,
    "docs": docs_sample,
    "table": table_sample,
    "adaptive": adaptive_sample,
}


def clean_html(value: str) -> str:
    return "\n".join(line.rstrip() for line in value.strip().splitlines()) + "\n"


def single_page(style: dict) -> str:
    slug = html.escape(style["slug"])
    class_name = html.escape(style.get("className") or f"ds-{style['slug']}")
    title = html.escape(style["name"])
    preview_variant = style.get("previewVariant") or style.get("register", "professional")
    sample = SAMPLES.get(preview_variant, professional_sample)()
    return clean_html(f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{title} 的真实 token 渲染预览。">
  <title>{title} · Design Library Preview</title>
  <link rel="stylesheet" href="_frame.css">
  <link rel="stylesheet" href="../styles/{slug}/tokens.css">
</head>
<body>
  <div class="{class_name} preview-root">
    {sample}
  </div>
</body>
</html>
""")


def overview_page(styles: list[dict]) -> str:
    rows = []
    for style in styles:
        rows.append(f"""
        <article class="overview-row">
          <header>
            <div>
              <h2>{html.escape(style['name'])}</h2>
              <p><code>{html.escape(style['slug'])}</code>，{html.escape(REGISTER_ZH.get(style.get('register'), style.get('register', '')))}，{html.escape(style.get('status', 'stable'))}</p>
            </div>
            <a href="{html.escape(style['slug'])}.html">单独打开</a>
          </header>
          <iframe title="{html.escape(style['name'])} 预览" src="{html.escape(style['slug'])}.html" loading="lazy"></iframe>
        </article>
        """)

    return clean_html(f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="设计风格库全部风格的真实 token 渲染总览。">
  <title>Design Library · 全部预览</title>
  <link rel="stylesheet" href="_frame.css">
  <style>
    .overview {{
      width: min(94rem, calc(100% - 2rem));
      margin: 0 auto;
      padding: 2rem 0 5rem;
    }}
    .overview-head {{ display: grid; grid-template-columns: minmax(0, 1fr) minmax(16rem, 28rem); gap: 2rem; padding: 1rem 0 2rem; }}
    .overview-head h1 {{ margin: 0 0 0.5rem; font-size: 1.75rem; line-height: 1.15; }}
    .overview-head p {{ margin: 0; color: var(--frame-muted); line-height: 1.65; }}
    .overview-row {{ margin: 0 0 2.5rem; border-top: 1px solid var(--frame-line-strong); }}
    .overview-row header {{ display: flex; align-items: end; justify-content: space-between; gap: 1rem; padding: 0.85rem 0; }}
    .overview-row h2 {{ margin: 0; font-size: 1rem; }}
    .overview-row p {{ margin: 0.25rem 0 0; color: var(--frame-muted); font-size: 0.8125rem; }}
    .overview-row iframe {{ display: block; width: 100%; height: 42rem; border: 1px solid var(--frame-line); border-radius: 8px; background: var(--frame-panel); }}
    @media (max-width: 52rem) {{
      .overview-head {{ grid-template-columns: 1fr; }}
      .overview-row iframe {{ height: 34rem; }}
    }}
  </style>
</head>
<body>
  <main class="overview">
    <header class="overview-head">
      <div>
        <h1>全部风格，同一份内容</h1>
        <p>每块样张都加载该风格自己的 <code>tokens.css</code>。先看层级、密度与对比度是否适合任务，再回到目录读排他条件。</p>
      </div>
      <p>这个页面由 <code>scripts/build-preview.py</code> 生成，不作为风格索引。选择请打开 <a href="../catalog/index.html">catalog</a>。</p>
    </header>
    {''.join(rows)}
  </main>
</body>
</html>
""")


def main() -> int:
    payload = json.loads(INDEX.read_text(encoding="utf-8"))
    styles = payload.get("styles", [])
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    for style in styles:
        path = OUT_DIR / f"{style['slug']}.html"
        path.write_text(single_page(style), encoding="utf-8")

    (OUT_DIR / "index.html").write_text(overview_page(styles), encoding="utf-8")
    print(f"已生成 preview/index.html 与 {len(styles)} 个单风格预览。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
