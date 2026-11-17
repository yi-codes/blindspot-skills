#!/usr/bin/env python3
"""扫描 styles/*/DESIGN.md，生成唯一风格索引。

产物：
    styles/INDEX.md
    styles/index.json

索引是纯生成物。新增或修改风格只改风格目录，然后运行本脚本。
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _designmd import load_design, split_list  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
STYLES = ROOT / "styles"

FIELDS = [
    ("register", "职守"),
    ("surface", "明暗"),
    ("density", "密度"),
    ("cues", "什么时候用"),
    ("avoid", "什么时候别用"),
]

REQUIRED = ("name", "register", "surface", "density", "cues", "avoid")

REGISTER_ZH = {
    "story": "讲故事",
    "professional": "讲专业",
    "technical": "讲技术",
    "tool": "讲工具",
}
SURFACE_ZH = {"light": "浅色", "dark": "深色", "mixed": "双模"}
DENSITY_ZH = {"tight": "紧", "medium": "中", "roomy": "松"}


def guess_prefix(style_dir: Path) -> str:
    css = style_dir / "tokens.css"
    if not css.exists():
        return ""
    found = re.findall(r"--([a-z]{2,4})-", css.read_text(encoding="utf-8"))
    if not found:
        return ""
    best = max(set(found), key=found.count)
    return f"--{best}-*"


def guess_class(style_dir: Path, slug: str) -> str:
    css = style_dir / "tokens.css"
    if not css.exists():
        return f"ds-{slug}"
    text = css.read_text(encoding="utf-8")
    match = re.search(r":where\(\.(ds-[\w-]+)(?:\[[^]]+\])?\)", text)
    return match.group(1) if match else f"ds-{slug}"


def collect() -> tuple[list[dict], list[str]]:
    rows, problems = [], []

    for style_dir in sorted(path for path in STYLES.iterdir() if path.is_dir()):
        design = style_dir / "DESIGN.md"
        css = style_dir / "tokens.css"
        prompt = style_dir / "prompt.md"
        if not design.exists():
            problems.append(f"{style_dir.name}: 没有 DESIGN.md")
            continue

        flat, tokens, _ = load_design(design)
        if flat is None:
            problems.append(f"{style_dir.name}: front matter 解析失败")
            continue

        missing = [key for key in REQUIRED if not flat.get(key, "").strip()]
        if missing:
            problems.append(f"{style_dir.name}: 缺少选择字段 {', '.join(missing)}")

        colors = (tokens or {}).get("colors", {})
        accent = (
            colors.get("primary")
            or colors.get("accent")
            or colors.get("main")
            or colors.get("link")
            or colors.get("ink")
        )
        rows.append({
            "slug": style_dir.name,
            "name": flat.get("name", style_dir.name),
            "description": flat.get("description", "").strip(),
            "version": flat.get("version", "alpha"),
            "status": flat.get("status", "stable"),
            "register": flat.get("register", ""),
            "surface": flat.get("surface", ""),
            "density": flat.get("density", ""),
            "cues": split_list(flat.get("cues", "")),
            "avoid": split_list(flat.get("avoid", "")),
            "prefix": guess_prefix(style_dir),
            "className": guess_class(style_dir, style_dir.name),
            "canvas": colors.get("canvas") or colors.get("bg") or colors.get("background") or "",
            "ink": colors.get("ink") or colors.get("text") or "",
            "accent": accent or "",
            "previewUrl": f"preview/{style_dir.name}.html",
            "designPath": f"styles/{style_dir.name}/DESIGN.md",
            "tokensPath": f"styles/{style_dir.name}/tokens.css",
            "promptPath": f"styles/{style_dir.name}/prompt.md",
            "has_prompt": prompt.exists(),
            "has_css": css.exists(),
        })

    return rows, problems


def render_markdown(rows: list[dict], problems: list[str]) -> str:
    out = [
        "# 风格索引",
        "",
        "> 这个文件是脚本生成的，不要手改。改风格选择条件，去改该风格 `DESIGN.md` 的 front matter。",
        ">",
        "> 重建：`python3 scripts/designlib.py build`",
        "",
        f"当前 **{len(rows)}** 个风格。",
        "",
        "## 决定表",
        "",
        "先定**这篇东西要让读者确认什么**，再在那一组里挑。",
        "",
        "| 读者要确认的 | 职守 | 风格 |",
        "|---|---|---|",
    ]

    labels = {
        "story": "「这东西有品 / 值得读」",
        "professional": "「这东西专业 / 可以信任」",
        "technical": "「这人懂技术 / 内容可信」",
        "tool": "「这是给高频工作的人做的」",
    }
    for register in ("story", "professional", "technical", "tool", "未分类"):
        items = [row for row in rows if (row["register"] or "未分类") == register]
        if not items:
            continue
        cells = "、".join(f"`{item['slug']}`" for item in items)
        out.append(f"| {labels.get(register, '—')} | {REGISTER_ZH.get(register, register)} | {cells} |")

    out.extend([
        "",
        "## 交叉表（职守 × 密度）",
        "",
        "**密度是「这一屏要塞多少东西」，不是「留白多少」**。紧表示信息密度优先，松表示阅读节奏优先。",
        "",
        "| 职守 | 紧 | 中 | 松 |",
        "|---|---|---|---|",
    ])
    for register in ("story", "professional", "technical", "tool", "未分类"):
        items = [row for row in rows if (row["register"] or "未分类") == register]
        if not items:
            continue
        line = [REGISTER_ZH.get(register, register)]
        for density in ("tight", "medium", "roomy"):
            cell = [f"`{item['slug']}`" for item in items if item["density"] == density]
            line.append("、".join(cell) or "—")
        out.append("| " + " | ".join(line) + " |")

    out.extend([
        "",
        "## 全表",
        "",
        "| 风格 | 状态 | 职守 | 明暗 | 密度 | 什么时候用 | 什么时候别用 | 画布 |",
        "|---|---|---|---|---|---|---|---|",
    ])
    for row in rows:
        swatch = f"`{row['canvas']}`" if row["canvas"] else "—"
        out.append(
            f"| **{row['name']}** `{row['slug']}` | {row['status']} | "
            f"{REGISTER_ZH.get(row['register'], row['register'] or '—')} | "
            f"{SURFACE_ZH.get(row['surface'], row['surface'] or '—')} | "
            f"{DENSITY_ZH.get(row['density'], row['density'] or '—')} | "
            f"{'、'.join(row['cues']) or '—'} | {'、'.join(row['avoid']) or '—'} | {swatch} |"
        )

    out.extend([
        "",
        "## 用法速查",
        "",
        "```html",
        '<link rel="stylesheet" href="styles/<slug>/tokens.css">',
        '<div class="ds-<slug>">…</div>',
        "```",
        "",
        "更快的入口：",
        "",
        "```bash",
        'python3 scripts/designlib.py recommend "<你要做什么>"',
        "python3 scripts/designlib.py show <slug>",
        "```",
        "",
        "## 排他说明",
        "",
        "`avoid` 不是「不太推荐」，是「别用」。命中排他条件的风格，通常没有为那个场景建立必要的约束。",
        "",
    ])

    if problems:
        out.extend(["## 生成时的问题", ""])
        out.extend(f"- {problem}" for problem in problems)
        out.append("")
    return "\n".join(out)


def main() -> int:
    rows, problems = collect()
    payload = {
        "generatedFrom": "styles/*/DESIGN.md",
        "count": len(rows),
        "styles": rows,
    }
    (STYLES / "index.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (STYLES / "INDEX.md").write_text(render_markdown(rows, problems), encoding="utf-8")

    print(f"已生成 styles/INDEX.md 和 styles/index.json，共 {len(rows)} 个风格。")
    if problems:
        for problem in problems:
            print(f"  ! {problem}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
