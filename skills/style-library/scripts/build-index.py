#!/usr/bin/env python3
"""扫描 styles/*/DESIGN.md，生成可被机器读的选择索引。

用法：
    python3 scripts/build-index.py

产物：
    styles/INDEX.md     ← 人和 AI 都读这个（SKILL.md 指向它，不指向任何具体风格）
    styles/index.json   ← 给脚本用（showcase 生成、未来的推荐器）

为什么要有这个脚本：
    在这之前，"怎么选风格"是 SKILL.md 里一张手写的表。
    加第 5 个风格就要手改 SKILL.md，加第 12 个风格那张表就没法看了。
    现在风格自己声明 cues / avoid / surface / register，
    索引、预览、lint 全部从声明里长出来 —— 加风格只动 styles/ 一个目录。
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _designmd import load_design, split_list  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
STYLES = ROOT / "styles"

# 加字段时只改这张表：字段名 → 中文标题。build-index 自动多一列。
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


def main():
    rows, problems = [], []

    for d in sorted(STYLES.iterdir()):
        if not d.is_dir():
            continue
        design = d / "DESIGN.md"
        if not design.exists():
            problems.append(f"{d.name}: 没有 DESIGN.md")
            continue

        flat, tokens, body = load_design(design)
        if flat is None:
            problems.append(f"{d.name}: front matter 解析失败")
            continue

        missing = [k for k in REQUIRED if not flat.get(k, "").strip()]
        if missing:
            problems.append(f"{d.name}: 缺少选择字段 {', '.join(missing)}（这个风格选不出来）")

        colors = (tokens or {}).get("colors", {})
        rows.append({
            "slug": d.name,
            "name": flat.get("name", d.name),
            "description": flat.get("description", "").strip(),
            "register": flat.get("register", ""),
            "surface": flat.get("surface", ""),
            "density": flat.get("density", ""),
            "cues": split_list(flat.get("cues", "")),
            "avoid": split_list(flat.get("avoid", "")),
            "prefix": guess_prefix(d),
            "canvas": colors.get("canvas") or colors.get("bg") or colors.get("background") or "",
            "ink": colors.get("ink") or colors.get("text") or "",
            "has_prompt": (d / "prompt.md").exists(),
            "has_css": (d / "tokens.css").exists(),
        })

    # ---------------- index.json
    (STYLES / "index.json").write_text(
        json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # ---------------- INDEX.md
    out = []
    out.append("# 风格索引")
    out.append("")
    out.append("> 这个文件是**脚本生成的**，不要手改。")
    out.append("> 改风格的选择条件，去改那个风格 `DESIGN.md` 的 front matter，然后跑：")
    out.append(">")
    out.append("> ```bash")
    out.append("> python3 scripts/build-index.py")
    out.append("> ```")
    out.append("")
    out.append(f"当前 **{len(rows)}** 个风格。")
    out.append("")

    # 决定表：先按职守分组
    by_register = {}
    for r in rows:
        by_register.setdefault(r["register"] or "未分类", []).append(r)

    out.append("## 决定表")
    out.append("")
    out.append("先定**这篇东西要让读者确认什么**，再在那一组里挑。")
    out.append("")
    out.append("| 读者要确认的 | 职守 | 风格 |")
    out.append("|---|---|---|")
    for reg in ("story", "professional", "technical", "tool", "未分类"):
        if reg not in by_register:
            continue
        items = by_register[reg]
        label = {
            "story": "「这人靠谱 / 这东西有品」",
            "professional": "「这东西好用 / 这公司专业」",
            "technical": "「这人技术过硬」",
            "tool": "「这是给专业人做的」",
            "未分类": "—",
        }[reg]
        cells = "、".join(f"`{i['slug']}`" for i in items)
        out.append(f"| {label} | {REGISTER_ZH.get(reg, reg)} | {cells} |")
    out.append("")

    # 交叉表：职守 × 密度。8 个风格之后，单看职守已经挑不出来
    out.append("## 交叉表（职守 × 密度）")
    out.append("")
    out.append("定了职守还挑不出来时看这张。**密度是「这一屏要塞多少东西」，不是「留白多少」** ——")
    out.append("紧 = 信息密度优先，松 = 阅读节奏优先。")
    out.append("")
    out.append("| 职守 | 紧 | 中 | 松 |")
    out.append("|---|---|---|---|")
    filled = crowded = 0
    for reg in ("story", "professional", "technical", "tool", "未分类"):
        if reg not in by_register:
            continue
        cells = {k: [] for k in ("tight", "medium", "roomy")}
        other = []
        for i in by_register[reg]:
            d = i["density"]
            if d in cells:
                cells[d].append(f"`{i['slug']}`")
            else:
                other.append(f"`{i['slug']}`")
        row = [REGISTER_ZH.get(reg, reg)]
        for k in ("tight", "medium", "roomy"):
            row.append("、".join(cells[k]) or "—")
            if cells[k]:
                filled += 1
                if len(cells[k]) > 1:
                    crowded += 1
        out.append("| " + " | ".join(row) + " |")
        if other:
            out.append(f"| | 未标密度：{'、'.join(other)} | | |")
    out.append("")
    if crowded:
        # 有格子挤了 2 个以上，密度这个维度才算真的在起筛选作用
        out.append(f"有 {crowded} 个格子塞了不止一个风格 —— 那些格子还得往下看「明暗」，或者干脆各写各的场景。")
        out.append("")
    else:
        out.append("现在每个格子里最多一个风格，说明密度还没开始筛人；看不出来就用全表的「什么时候用」判。")
        out.append("")

    out.append("## 全表")
    out.append("")
    head = "| 风格 | " + " | ".join(t for _, t in FIELDS) + " | 画布 |"
    sep = "|---|" + "|".join(["---"] * len(FIELDS)) + "|---|"
    out.append(head)
    out.append(sep)
    for r in rows:
        cells = []
        for key, _ in FIELDS:
            if key == "register":
                cells.append(REGISTER_ZH.get(r[key], r[key] or "—"))
            elif key == "surface":
                cells.append(SURFACE_ZH.get(r[key], r[key] or "—"))
            elif key == "density":
                cells.append(DENSITY_ZH.get(r[key], r[key] or "—"))
            elif key in ("cues", "avoid"):
                cells.append("、".join(r[key]) or "—")
            else:
                cells.append(r.get(key) or "—")
        swatch = f"`{r['canvas']}`" if r["canvas"] else "—"
        out.append(f"| **{r['name']}** `{r['slug']}` | " + " | ".join(cells) + f" | {swatch} |")
    out.append("")

    out.append("## 用法速查")
    out.append("")
    out.append("```html")
    out.append('<!-- 引入某个风格 -->')
    out.append('<link rel="stylesheet" href="styles/<slug>/tokens.css">')
    out.append('<div class="ds-<slug>"> … </div>')
    out.append("```")
    out.append("")
    out.append("变量前缀见每个风格 `tokens.css` 顶部的注释（`--ed-*` / `--sw-*` …）。")
    out.append("")
    out.append("## 排他说明")
    out.append("")
    out.append("`avoid` 里列的不是「不推荐」，是「**别用**」。")
    out.append("一个风格用在它 avoid 的场景里，出来的东西一定像模板 —— 因为它没为那个场景做过约束。")
    out.append("")
    out.append("全都排除了，说明这里该开一个新风格（见 `principles.md` §8），而不是硬套。")
    out.append("")

    if problems:
        out.append("## ⚠ 生成时的问题")
        out.append("")
        for p in problems:
            out.append(f"- {p}")
        out.append("")

    (STYLES / "INDEX.md").write_text("\n".join(out) + "\n", encoding="utf-8")

    print(f"已生成 styles/INDEX.md 和 styles/index.json，共 {len(rows)} 个风格。")
    for r in rows:
        flag = "" if all(r.get(k) for k in ("register", "surface", "density", "cues", "avoid")) else "  ⚠ 选择字段不全"
        print(f"  - {r['slug']:<18} {r['name']:<16} {REGISTER_ZH.get(r['register'], r['register'] or '?'):<6}{flag}")
    if problems:
        print("\n问题：")
        for p in problems:
            print("  !", p)
        return 1
    return 0


def guess_prefix(style_dir):
    """从 tokens.css 里猜变量前缀（--xx- 里最长出现的那种），只用于展示。"""
    css = style_dir / "tokens.css"
    if not css.exists():
        return ""
    import re
    found = re.findall(r"--([a-z]{2,4})-", css.read_text(encoding="utf-8"))
    if not found:
        return ""
    best = max(set(found), key=found.count)
    return f"--{best}-*"


if __name__ == "__main__":
    sys.exit(main())
