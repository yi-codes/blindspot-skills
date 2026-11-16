#!/usr/bin/env python3
"""重建 preview/index.html —— 把 styles/ 下所有风格渲染成同内容对照页。

用法:
    ./scripts/build-preview.py

规则:
  - 扫描 styles/*/tokens.css
  - 风格名从 style.md 的首个标题取（形如 `# Swiss Grid · 瑞士网格`）
  - 若存在 styles/<slug>/demo.html，用它替换默认演示内容
  - status: draft 的风格会标注 draft
"""

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STYLES_DIR = ROOT / "styles"
OUT = ROOT / "preview" / "index.html"

# ---- 默认演示内容：三种风格用同一份，差异才可比 ----
DEFAULT_DEMO = """
      <span class="ds-eyebrow">Case Study · 案例</span>
      <h1>把复杂的事说清楚</h1>
      <p>好的排版不负责让人惊艳，它负责让人读下去。当一段话值得被认真读完的时候，界面应该退到后面去，只留下纸、墨，和恰到好处的空白。</p>
      <h2>留白是一种语气</h2>
      <p>行高从 1.5 加到 1.85，字数从每行 60 收到 34，同样的文字会产生完全不同的阅读速度。慢下来，是设计出来的。</p>
      <div class="row">
        <button>开始阅读</button>
        <span class="ds-tag">2026 · Q4</span>
      </div>
      <div class="grid3">
        <div class="ds-card">
          <h3>层级靠落差</h3>
          <p class="muted">字号要么同级，要么跳一大截。17 → 18 → 19 是最难看的中间状态。</p>
        </div>
        <div class="ds-card">
          <h3>一个强调色</h3>
          <p class="muted">颜色收敛到三个家族以内。强调色只出现在可点击的东西上，它指路，不装饰。</p>
        </div>
        <div class="ds-card">
          <div class="ds-stat-label">阅读时长</div>
          <div class="ds-stat-value">12 分钟</div>
          <div class="ds-stat-label">全文 3,400 字</div>
        </div>
      </div>
"""

SHELL = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>风格库 · 对照预览</title>
{links}
<style>
  /* 页面外壳：中性化，不干扰三个风格的展示 */
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    padding: 48px 24px 96px;
    background: #ECEBE8;
    font-family: -apple-system, "PingFang SC", system-ui, sans-serif;
    color: #2B2B2B;
  }}
  .wrap {{ max-width: 1100px; margin: 0 auto; }}

  .hd {{ margin-bottom: 56px; }}
  .hd h1 {{ font-size: 30px; font-weight: 650; margin: 0 0 10px; letter-spacing: -0.01em; }}
  .hd p {{ font-size: 14px; line-height: 1.8; color: #5F5F5F; max-width: 46em; margin: 0; }}
  .hd code {{
    font-family: "SF Mono", ui-monospace, monospace;
    font-size: 12.5px; background: #DFDEDA; padding: 1px 5px; border-radius: 3px;
  }}

  .demo-block {{ margin-bottom: 72px; }}

  .demo-meta {{
    display: flex; align-items: baseline; gap: 12px;
    margin-bottom: 12px; padding-left: 2px; flex-wrap: wrap;
  }}
  .demo-name {{ font-size: 15px; font-weight: 650; }}
  .demo-slug {{
    font-family: "SF Mono", ui-monospace, monospace;
    font-size: 11.5px; color: #86847E;
    border: 1px solid #D5D3CE; border-radius: 3px; padding: 1px 6px;
  }}
  .demo-draft {{
    font-size: 11px; letter-spacing: 0.08em; text-transform: uppercase;
    color: #9A6B00; background: #F6E7C8; border-radius: 3px; padding: 1px 6px;
  }}
  .demo-note {{ font-size: 12.5px; color: #86847E; margin-left: auto; }}

  .stage {{ padding: 56px 5% 48px; border-radius: 3px; overflow: hidden; }}

  .row {{ display: flex; flex-wrap: wrap; gap: 14px; align-items: center; margin-top: 28px; }}
  .grid3 {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
    gap: 20px;
    margin-top: 32px;
  }}
  .muted {{ font-size: 13px; line-height: 1.7; margin: 0; }}
</style>
</head>
<body>
<div class="wrap">

  <div class="hd">
    <h1>风格库 · 对照预览</h1>
    <p>
      同一份内容，{count} 种风格。每块都是一份真实的 DOM，只靠容器上的一个 class 切换。
      新增风格后重跑 <code>scripts/build-preview.py</code> 就会多一块。
      本页由脚本生成，不要手改。
    </p>
  </div>
{blocks}
</div>
</body>
</html>
"""


def parse_meta(design_md: Path):
    """从 DESIGN.md 的 YAML front matter 取 (名称, 一句话描述, 是否 draft)。"""
    if not design_md.exists():
        return None, "", False
    text = design_md.read_text(encoding="utf-8")

    name = None
    m = re.search(r"^name:\s*(.+?)\s*$", text, re.MULTILINE)
    if m:
        name = m.group(1).strip().strip('"').strip("'")

    # description 可能是单行、或 >- / | 折叠块
    note = ""
    m2 = re.search(r"^description:\s*(>-?|\|-?)\s*\n((?:[ \t]+.*\n?)+)", text, re.MULTILINE)
    if m2:
        block = " ".join(line.strip() for line in m2.group(2).split("\n") if line.strip())
        note = block
    else:
        m3 = re.search(r"^description:\s*(.+?)\s*$", text, re.MULTILINE)
        if m3:
            note = m3.group(1).strip().strip('"').strip("'")

    # 只取第一句，预览页放不下整段
    if note:
        note = re.split(r"(?<=[。！？\.])\s", note)[0]
        if len(note) > 42:
            note = note[:42] + "…"

    draft = bool(re.search(r"status:\s*draft", text, re.IGNORECASE))
    return name, note, draft


def collect():
    styles = []
    for d in sorted(STYLES_DIR.iterdir()):
        if not d.is_dir():
            continue
        css = d / "tokens.css"
        if not css.exists():
            print(f"  [跳过] {d.name}: 缺 tokens.css")
            continue
        name, note, draft = parse_meta(d / "DESIGN.md")
        demo_file = d / "demo.html"
        demo = demo_file.read_text(encoding="utf-8") if demo_file.exists() else DEFAULT_DEMO
        styles.append({
            "slug": d.name,
            "name": name or d.name,
            "note": note,
            "draft": draft,
            "demo": demo,
        })
    return styles


def render(styles):
    links = "\n".join(
        f'<link rel="stylesheet" href="../styles/{s["slug"]}/tokens.css">' for s in styles
    )
    blocks = []
    for s in styles:
        badge = '<span class="demo-draft">draft</span>' if s["draft"] else ""
        note = f'<span class="demo-note">{html.escape(s["note"])}</span>' if s["note"] else ""
        blocks.append(f"""
  <section class="demo-block">
    <div class="demo-meta">
      <span class="demo-name">{html.escape(s["name"])}</span>
      <span class="demo-slug">{s["slug"]}</span>
      {badge}{note}
    </div>
    <div class="stage ds-{s["slug"]}">{s["demo"]}    </div>
  </section>""")

    return SHELL.format(links=links, blocks="\n".join(blocks), count=len(styles))


def main():
    if not STYLES_DIR.exists():
        sys.exit(f"找不到 {STYLES_DIR}")
    styles = collect()
    if not styles:
        sys.exit("styles/ 下没有任何风格")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(styles), encoding="utf-8")
    print(f"已生成 {OUT.relative_to(ROOT)}，共 {len(styles)} 个风格：")
    for s in styles:
        flag = " (draft)" if s["draft"] else ""
        print(f"  - {s['slug']}  {s['name']}{flag}")


if __name__ == "__main__":
    main()
