#!/usr/bin/env python3
"""Design Library 统一命令行。

把选风格、查看最小读数路径、重建索引/预览和执行完整检查收在一个入口。
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _designmd import load_design, split_list  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
STYLES_DIR = ROOT / "styles"
INDEX = STYLES_DIR / "index.json"
CATALOG_DATA = ROOT / "catalog" / "data.js"
PSEUDO_SOURCES = {
    "native",
    "openai-codex-observed",
    "openai-desktop-client-observed",
    "ui-styles-liquid-glass",
    "ui-styles-ops-console",
}

REGISTER_ZH = {
    "story": "讲故事",
    "professional": "讲专业",
    "technical": "讲技术",
    "tool": "讲工具",
}
SURFACE_ZH = {"light": "浅色", "dark": "深色", "mixed": "双模"}
DENSITY_ZH = {"tight": "紧", "medium": "中", "roomy": "松"}
TIER_ZH = {"core": "核心", "variant": "变体", "technique": "技法"}

REGISTER_SIGNALS = {
    "story": ("品牌", "故事", "作品集", "活动", "营销", "发布", "叙事", "杂志", "创意"),
    "professional": ("产品页", "落地页", "案例", "数据看板", "b 端", "官网", "方案", "企业"),
    "technical": ("文档", "代码", "日志", "cli", "规范", "技术", "论文", "开发"),
    "tool": ("控制台", "工作台", "后台", "面板", "工具", "dashboard", "console", "admin", "任务", "设置", "运维", "监控", "告警"),
}


def load_rows() -> list[dict]:
    rows = []
    for style_dir in sorted(path for path in STYLES_DIR.iterdir() if path.is_dir()):
        design = style_dir / "DESIGN.md"
        if not design.exists():
            continue
        flat, tokens, _ = load_design(design)
        if flat is None:
            continue
        colors = (tokens or {}).get("colors", {})
        rows.append({
            "slug": style_dir.name,
            "name": flat.get("name", style_dir.name),
            "description": flat.get("description", ""),
            "version": flat.get("version", "alpha"),
            "status": flat.get("status", "stable"),
            "family": flat.get("family", ""),
            "tier": flat.get("tier", ""),
            "sourceRefs": split_list(flat.get("sourceRefs", "")),
            "register": flat.get("register", ""),
            "surface": flat.get("surface", ""),
            "density": flat.get("density", ""),
            "cues": split_list(flat.get("cues", "")),
            "avoid": split_list(flat.get("avoid", "")),
            "canvas": colors.get("canvas") or colors.get("bg") or "",
            "ink": colors.get("ink") or "",
            "accent": (
                colors.get("primary")
                or colors.get("accent")
                or colors.get("main")
                or colors.get("link")
                or colors.get("ink")
                or ""
            ),
        })
    return rows


def normalize(value: str) -> str:
    return re.sub(r"\s+", " ", value.casefold()).strip()


def semantic_fragments(value: str) -> set[str]:
    normalized = normalize(value)
    fragments = set()
    for run in re.findall(r"[\u4e00-\u9fff]+", normalized):
        for width in (2, 3, 4):
            fragments.update(run[index:index + width] for index in range(len(run) - width + 1))
    for word in re.findall(r"[a-z0-9][a-z0-9.+-]{1,}", normalized):
        fragments.add(word)
    return fragments - {"这个", "那个", "需要", "可以", "进行", "以及", "一个", "页面"}


def score_style(style: dict, query: str) -> tuple[int, list[str]]:
    if not query:
        return 0, []

    text = normalize(query)
    score = {"core": 1, "variant": 0, "technique": -1}.get(style.get("tier"), 0)
    reasons = []

    query_fragments = semantic_fragments(text)
    for cue in style["cues"]:
        cue_norm = normalize(cue)
        if cue_norm and (cue_norm in text or text in cue_norm):
            score += 5
            reasons.append(f"命中场景：{cue}")
            continue
        overlap = semantic_fragments(cue) & query_fragments
        if overlap:
            score += min(4, len(overlap))
            reasons.append(f"语义相关：{cue}")

    for register, signals in REGISTER_SIGNALS.items():
        if any(signal in text for signal in signals):
            if style["register"] == register:
                score += 3
                reasons.append(f"职责匹配：{REGISTER_ZH[register]}")
            else:
                score -= 1

    for avoid in style["avoid"]:
        avoid_norm = normalize(avoid)
        if avoid_norm and avoid_norm in text:
            score -= 8
            reasons.append(f"命中排他：{avoid}")

    if re.search(r"高密度|密集|大量|表格|值班|排障|监控", text) and style["density"] == "tight":
        score += 2
        reasons.append("密度匹配：紧")
    if re.search(r"长文|阅读|慢慢|报告|文章", text) and style["density"] == "roomy":
        score += 2
        reasons.append("密度匹配：松")
    if re.search(r"深色|夜间|暗色", text) and style["surface"] == "dark":
        score += 2
        reasons.append("明暗匹配：深色")
    if re.search(r"浅色|明亮|白天|打印", text) and style["surface"] == "light":
        score += 2
        reasons.append("明暗匹配：浅色")

    return score, list(dict.fromkeys(reasons))[:3]


def command_list(args: argparse.Namespace) -> int:
    rows = load_rows()
    if args.register:
        rows = [row for row in rows if row["register"] == args.register]
    if args.surface:
        rows = [row for row in rows if row["surface"] == args.surface]
    if args.density:
        rows = [row for row in rows if row["density"] == args.density]
    if args.tier:
        rows = [row for row in rows if row["tier"] == args.tier]

    for row in rows:
        print(
            f"{row['slug']:<18} {row['name']:<18} "
            f"{TIER_ZH.get(row['tier'], row['tier']):<2} "
            f"{REGISTER_ZH.get(row['register'], row['register']):<5} "
            f"{SURFACE_ZH.get(row['surface'], row['surface']):<4} "
            f"{DENSITY_ZH.get(row['density'], row['density']):<2} "
            f"{','.join(row['cues'][:2])}"
        )
    print(f"\n{len(rows)} 个风格")
    return 0


def command_recommend(args: argparse.Namespace) -> int:
    query = " ".join(args.query).strip()
    rows = load_rows()
    ranked = []
    for index, row in enumerate(rows):
        score, reasons = score_style(row, query)
        ranked.append((score, index, row, reasons))
    ranked.sort(key=lambda item: (-item[0], item[1]))
    ranked = [item for item in ranked if item[0] > 0] or ranked
    top = ranked[: args.limit]

    if args.json:
        print(json.dumps([
            {"slug": row["slug"], "name": row["name"], "score": score, "reasons": reasons}
            for score, _, row, reasons in top
        ], ensure_ascii=False, indent=2))
        return 0

    print(f"任务：{query or '未填写'}\n")
    for rank, (score, _, row, reasons) in enumerate(top, start=1):
        reason = "；".join(reasons) or "没有直接命中，按现有索引排序"
        print(f"{rank}. {row['name']} ({row['slug']})  score={score}  [{TIER_ZH.get(row['tier'], row['tier'])}]")
        print(f"   {reason}")
        print(f"   读：styles/{row['slug']}/DESIGN.md")
        print(f"       styles/{row['slug']}/tokens.css")
        print(f"   看：preview/{row['slug']}.html\n")
    return 0


def command_show(args: argparse.Namespace) -> int:
    row = next((item for item in load_rows() if item["slug"] == args.slug), None)
    if not row:
        print(f"找不到风格：{args.slug}", file=sys.stderr)
        return 1

    print(f"{row['name']} ({row['slug']})")
    print(f"状态：{row['status']} · v{row['version']}")
    print(f"家族：{row['family']} · 层级：{TIER_ZH.get(row['tier'], row['tier'])}")
    print(f"用途：{REGISTER_ZH.get(row['register'], row['register'])} · {SURFACE_ZH.get(row['surface'], row['surface'])} · {DENSITY_ZH.get(row['density'], row['density'])}")
    print(f"\n{row['description']}\n")
    print("最小读数路径：")
    print(f"  styles/{row['slug']}/DESIGN.md")
    print(f"  styles/{row['slug']}/tokens.css")
    print(f"  预览：preview/{row['slug']}.html")
    print("\n什么时候用：")
    for cue in row["cues"]:
        print(f"  - {cue}")
    print("\n绝对别用：")
    for avoid in row["avoid"]:
        print(f"  - {avoid}")
    return 0


def run_script(name: str, *args: str) -> None:
    command = [sys.executable, str(ROOT / "scripts" / name), *args]
    subprocess.run(command, cwd=ROOT, check=True)


def validate_catalog() -> list[str]:
    problems = []
    rows = load_rows()
    slugs = [row["slug"] for row in rows]
    if len(slugs) != len(set(slugs)):
        problems.append("存在重复 slug")

    if not INDEX.exists():
        return ["缺少 styles/index.json"]
    payload = json.loads(INDEX.read_text(encoding="utf-8"))
    index_slugs = [item.get("slug") for item in payload.get("styles", [])]
    if index_slugs != slugs:
        problems.append("styles/index.json 与实际风格目录不一致，运行 build")

    if not CATALOG_DATA.exists():
        problems.append("缺少 catalog/data.js")
    else:
        raw = CATALOG_DATA.read_text(encoding="utf-8").strip()
        prefix = "window.DESIGN_DATA = "
        if not raw.startswith(prefix) or not raw.endswith(";"):
            problems.append("catalog/data.js 不是生成的常量格式")
        else:
            try:
                catalog = json.loads(raw[len(prefix):-1])
            except json.JSONDecodeError as error:
                problems.append(f"catalog/data.js JSON 无法解析：{error}")
            else:
                data_slugs = [item.get("slug") for item in catalog.get("styles", [])]
                if data_slugs != slugs:
                    problems.append("catalog/data.js 与风格目录不一致，运行 build")

    index_md = (STYLES_DIR / "INDEX.md").read_text(encoding="utf-8") if (STYLES_DIR / "INDEX.md").exists() else ""
    if f"当前 **{len(slugs)}** 个风格" not in index_md:
        problems.append("styles/INDEX.md 数量未同步，运行 build")

    for slug in slugs:
        style_dir = STYLES_DIR / slug
        row = next((item for item in rows if item["slug"] == slug), {})
        for filename in ("DESIGN.md", "tokens.css", "prompt.md"):
            if not (style_dir / filename).exists():
                problems.append(f"{slug}: 缺少 {filename}")

        if row_tier := row.get("tier", ""):
            if row_tier not in TIER_ZH:
                problems.append(f"{slug}: tier `{row_tier}` 无效")
        for source in row.get("sourceRefs", []):
            if source not in PSEUDO_SOURCES and not (ROOT / "references" / source / "NOTES.md").exists():
                problems.append(f"{slug}: sourceRefs 指向不存在的提炼卡 references/{source}/NOTES.md")

        preview = ROOT / "preview" / f"{slug}.html"
        if not preview.exists():
            problems.append(f"{slug}: 缺少预览页，运行 build")
            continue
        preview_text = preview.read_text(encoding="utf-8")
        if f"../styles/{slug}/tokens.css" not in preview_text:
            problems.append(f"{slug}: 预览没有引用自己的 tokens.css")

        design_text = (style_dir / "DESIGN.md").read_text(encoding="utf-8")
        for broken in re.findall(r"(?:\.\./|\b)(?:styles|skills/style-library|skills/ui-styles)/[\w./-]+", design_text):
            target = ROOT / broken
            if broken.startswith(("styles/", "skills/")) and not target.exists():
                problems.append(f"{slug}: DESIGN.md 引用了不存在路径 {broken}")

    html_paths = [
        ROOT / "catalog" / "index.html",
        ROOT / "preview" / "index.html",
        *sorted((ROOT / "showcase").glob("ops-ai-console/*.html")),
    ]
    for html_path in html_paths:
        if not html_path.exists():
            problems.append(f"缺少 {html_path.relative_to(ROOT)}")
            continue
        text = html_path.read_text(encoding="utf-8")
        for href in re.findall(r'(?:href|src)="([^"]+)"', text):
            if href.startswith(("#", "http:", "https:", "mailto:", "data:")):
                continue
            clean = href.split("#", 1)[0]
            if clean and not (html_path.parent / clean).resolve().exists():
                problems.append(f"{html_path.relative_to(ROOT)}: 本地链接不存在 {href}")

    markdown_files = [ROOT / "SKILL.md", ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md"))]
    for markdown_path in markdown_files:
        if not markdown_path.exists():
            problems.append(f"缺少 {markdown_path.relative_to(ROOT)}")
            continue
        text = markdown_path.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            target = target.strip().strip("<>")
            if target.startswith(("http:", "https:", "mailto:", "#")):
                continue
            clean = target.split("#", 1)[0].split("?", 1)[0]
            if clean and not (markdown_path.parent / clean).resolve().exists():
                problems.append(f"{markdown_path.relative_to(ROOT)}: 本地链接不存在 {target}")

    if len(slugs) < 17:
        problems.append(f"当前只有 {len(slugs)} 个风格，预期至少 17 个")
    return list(dict.fromkeys(problems))


def command_build(_: argparse.Namespace) -> int:
    run_script("build-index.py")
    run_script("build-catalog.py")
    run_script("build-preview.py")
    problems = validate_catalog()
    if problems:
        for problem in problems:
            print(f"  ! {problem}", file=sys.stderr)
        return 1
    print("目录、预览与静态索引已同步。")
    return 0


def command_check(_: argparse.Namespace) -> int:
    print("1/4 重建生成物")
    if command_build(argparse.Namespace()) != 0:
        return 1

    print("\n2/4 文档层检查")
    run_script("lint.py")

    print("3/4 产物层检查")
    preview_files = sorted(str(path) for path in (ROOT / "preview").glob("*.html"))
    if preview_files:
        run_script("slop.py", *preview_files)
    run_script("slop.py", str(ROOT / "catalog" / "index.html"))
    showcase_files = sorted(str(path) for path in (ROOT / "showcase" / "ops-ai-console").glob("*.html"))
    if showcase_files:
        run_script("slop.py", *showcase_files)

    print("4/4 项目自洽与测试")
    problems = validate_catalog()
    test_result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        cwd=ROOT,
    )
    if problems:
        for problem in problems:
            print(f"  ! {problem}", file=sys.stderr)
    if problems or test_result.returncode != 0:
        return 1
    print("\n全部检查通过。")
    return 0


def command_new(args: argparse.Namespace) -> int:
    command = [str(ROOT / "scripts" / "new-style.sh"), args.slug, args.name]
    return subprocess.run(command, cwd=ROOT).returncode


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Design Library")
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="列出全部风格")
    list_parser.add_argument("--register", choices=tuple(REGISTER_ZH))
    list_parser.add_argument("--surface", choices=("light", "dark", "mixed"))
    list_parser.add_argument("--density", choices=("tight", "medium", "roomy"))
    list_parser.add_argument("--tier", choices=tuple(TIER_ZH))
    list_parser.set_defaults(func=command_list)

    recommend_parser = subparsers.add_parser("recommend", help="按任务描述推荐风格")
    recommend_parser.add_argument("query", nargs="+")
    recommend_parser.add_argument("--limit", type=int, default=5)
    recommend_parser.add_argument("--json", action="store_true")
    recommend_parser.set_defaults(func=command_recommend)

    show_parser = subparsers.add_parser("show", help="显示一个风格的读数路径")
    show_parser.add_argument("slug")
    show_parser.set_defaults(func=command_show)

    build_parser_cmd = subparsers.add_parser("build", help="重建索引、目录数据和预览")
    build_parser_cmd.set_defaults(func=command_build)

    check_parser = subparsers.add_parser("check", help="运行完整检查")
    check_parser.set_defaults(func=command_check)

    new_parser = subparsers.add_parser("new", help="创建新风格骨架")
    new_parser.add_argument("slug")
    new_parser.add_argument("name")
    new_parser.set_defaults(func=command_new)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

