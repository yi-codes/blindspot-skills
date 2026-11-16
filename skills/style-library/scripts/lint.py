#!/usr/bin/env python3
"""校验 styles/*/DESIGN.md 的结构完整性、token 引用、WCAG 对比度、与 CSS 的一致性。

零依赖（不装 PyYAML / npm 包），只做针对本库所需的子集检查。

用法:
    ./scripts/lint.py              # 检查全部
    ./scripts/lint.py <slug>       # 只查一个

严重级别:
    E  错误 —— 会让 agent 读错，必须修
    W  警告 —— 会让风格走偏，建议修
    I  提示 —— 信息，可以不处理
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STYLES = ROOT / "styles"

sys.path.insert(0, str(Path(__file__).parent))
from _designmd import (  # noqa: E402
    split_front_matter, parse_tokens, flat_fields,
    HEX_RE, hex_to_rgb, rel_luminance, contrast,
)

# 选择条件：build-index.py 靠这几个字段把风格摆进索引。缺一个 = 这个风格选不出来。
SELECTION_FIELDS = ("cues", "avoid", "surface", "register")
REGISTERS = {"story", "professional", "technical", "tool"}
SURFACES = {"light", "dark", "mixed"}

LEN_RE = re.compile(r"^\s*(-?[\d.]+)\s*(px|rem)?\s*$")


def to_px(v):
    """把长度折成整数 px，用于比对字号/圆角/间距。

    - '28px' → 28
    - '1.75rem' → 28
    - '1.953rem' → 31（取整吸收模块化字阶的取整误差，31.248 就是 31）
    - '0' → 0
    - em / % / clamp() / 关键字 → None（相对单位折 px 没有意义，比了就是假警报）
    """
    m = LEN_RE.match(str(v or ""))
    if not m:
        return None
    n = float(m.group(1))
    unit = m.group(2) or ("px" if n == 0 else None)
    if unit == "rem":
        n *= 16
    elif unit != "px":
        return None
    return int(round(n))

REQUIRED_SECTIONS = [
    "Overview",
    "Colors",
    "Typography",
    "Layout",
    "Elevation & Depth",
    "Shapes",
    "Components",
    "Do's and Don'ts",
]

# 章节别名，允许写成这些
SECTION_ALIASES = {
    "Brand & Style": "Overview",
    "Layout & Spacing": "Layout",
    "Elevation": "Elevation & Depth",
    "Do's and Don'ts": "Do's and Don'ts",
    "Do’s and Don’ts": "Do's and Don'ts",
}


# ------------------------------------------------------------------- 颜色



# ------------------------------------------------------------------- 检查

def lint_style(design_md: Path):
    findings = []

    def add(level, msg, where=""):
        findings.append((level, msg, where))

    text = design_md.read_text(encoding="utf-8")
    yaml_text, body = split_front_matter(text)

    if yaml_text is None:
        add("E", "缺少 YAML front matter（文件必须以 --- 开头，并以 --- 结束）")
        return findings, {}

    tokens = parse_tokens(yaml_text)

    # --- 必填字段 ---
    if not tokens.get("name"):
        add("E", "front matter 缺 name")
    if not isinstance(tokens.get("colors"), dict) or not tokens.get("colors"):
        add("E", "缺 colors 或 colors 为空")

    # --- 选择条件（build-index.py / SKILL.md 靠它把风格摆进索引）---
    flat = flat_fields(yaml_text)
    for k in SELECTION_FIELDS:
        if not flat.get(k, "").strip():
            add("E", f"缺少选择字段 `{k}` —— 这个风格在 styles/INDEX.md 里选不出来，SKILL.md 也不会推荐它")
    for k in ("register", "surface"):
        if "|" in flat.get(k, ""):
            add("E", f"`{k}` 还是脚手架占位符（`{flat[k]}`）—— 没改成实际值，索引会把它归到「未分类」")
    if flat.get("register") and "|" not in flat["register"] and flat["register"] not in REGISTERS:
        add("W", f"register 的值 `{flat['register']}` 不在 {sorted(REGISTERS)} 里，索引会把它归到「未分类」")
    if flat.get("surface") and "|" not in flat["surface"] and flat["surface"] not in SURFACES:
        add("W", f"surface 的值 `{flat['surface']}` 不在 {sorted(SURFACES)} 里")

    colors = tokens.get("colors", {}) if isinstance(tokens.get("colors"), dict) else {}
    typo = tokens.get("typography", {}) if isinstance(tokens.get("typography"), dict) else {}
    rounded = tokens.get("rounded", {}) if isinstance(tokens.get("rounded"), dict) else {}
    spacing = tokens.get("spacing", {}) if isinstance(tokens.get("spacing"), dict) else {}

    # --- 颜色值合法性 ---
    for k, v in colors.items():
        if isinstance(v, str) and v.startswith("#") and not re.fullmatch(r"#[0-9A-Fa-f]{3,8}", v):
            add("E", f"colors.{k} 的十六进制格式非法: {v}")
        elif isinstance(v, str) and not v.startswith("#") and not re.match(
            r"^(rgb|hsl|oklch|oklab|color-mix|transparent)", v
        ):
            add("W", f"colors.{k} 的值不是常见 CSS 颜色: {v}")

    # --- token 引用完整性 ---
    components = tokens.get("components", {}) if isinstance(tokens.get("components"), dict) else {}
    groups = {
        "colors": colors,
        "typography": typo,
        "rounded": rounded,
        "spacing": spacing,
        "components": components,
    }
    # Iteration Guide / Known Gaps 里出现的 {xxx.yyy} 是元引用（在讲"怎么用引用"），不是真引用
    checkable = re.split(r"^##\s+(?:Iteration Guide|Known Gaps)\s*$", body, flags=re.MULTILINE)[0]
    for m in re.finditer(r"\{([\w-]+)\.([\w.-]+)\}", checkable):
        g, t = m.group(1), m.group(2)
        if g not in groups:
            add("E", f"引用了未知 token 组: {{{g}.{t}}}")
            continue
        if t not in groups[g]:
            add("E", f"引用了不存在的 token: {{{g}.{t}}}")

    # --- 章节 ---
    heads = [h.strip() for h in re.findall(r"^##\s+(.+?)\s*$", body, re.MULTILINE)]
    normalized = [SECTION_ALIASES.get(h, h) for h in heads]
    missing = [s for s in REQUIRED_SECTIONS if s not in normalized]
    if missing:
        add("W", "缺少规范章节: " + "、".join(missing))

    present = [s for s in normalized if s in REQUIRED_SECTIONS]
    expected = [s for s in REQUIRED_SECTIONS if s in present]
    if present != expected:
        add("W", "规范章节顺序不对。当前: " + " → ".join(present))

    if len(heads) != len(set(heads)):
        dup = [h for h in set(heads) if heads.count(h) > 1]
        add("E", "章节标题重复（规范要求报错）: " + "、".join(dup))

    # --- 中文排版章节（本库的差异化要求）---
    if "Chinese Typography" not in heads:
        add("W", "缺少 ## Chinese Typography 章节。这是本库相对上游样本的核心增量，不要省。")

    # --- WCAG 对比度 ---
    def c(name):
        v = colors.get(name)
        return v if isinstance(v, str) and HEX_RE.fullmatch(v) else None

    bg = c("canvas")
    pairs = [
        ("ink", "canvas", "正文 / 画布", 4.5),
        ("ink", "surface", "正文 / 卡片", 4.5),
        ("ink-muted", "canvas", "次要文字 / 画布", 4.5),
        ("ink-faint", "canvas", "最弱文字 / 画布", 3.0),
        ("primary", "canvas", "强调色 / 画布", 3.0),
    ]
    for fg, bgn, label, need in pairs:
        fg_v, bg_v = c(fg), c(bgn)
        if fg_v and bg_v:
            ratio = contrast(fg_v, bg_v)
            if ratio < need:
                add("W", f"对比度不足 {label}: {ratio:.2f}:1（需 ≥{need}）", f"{fg} on {bgn}")
            elif ratio > 21:
                add("I", f"{label} 对比度异常: {ratio:.2f}:1")

    # --- 与 CSS 实现的一致性 ---
    for css_name in ("tokens.css", "theme.css"):
        css_path = design_md.parent / css_name
        if not css_path.exists():
            continue
        css_text = css_path.read_text(encoding="utf-8")
        css_colors = {h.upper() for h in HEX_RE.findall(css_text)}
        doc_colors = {v.upper() for v in colors.values()
                      if isinstance(v, str) and HEX_RE.fullmatch(v)}
        only_doc = doc_colors - css_colors
        only_css = css_colors - doc_colors
        if only_doc:
            add("E", f"{css_name} 缺少这些颜色（DESIGN.md 有、CSS 没实现）: "
                     + "、".join(sorted(only_doc)))
        if only_css:
            add("E", f"{css_name} 有 DESIGN.md 未声明的颜色（会产生漂移）: "
                     + "、".join(sorted(only_css)))

        # --- 数值阶的对齐：字号 / 圆角 / 间距 ---
        css_vars = re.findall(r"(--[\w-]+)\s*:\s*([^;{}]+);", css_text)
        css_nums = {to_px(v) for _, v in css_vars}
        css_nums.discard(None)
        css_names = {n for n, _ in css_vars}

        doc_sets = {
            "typography.fontSize": {to_px(spec.get("fontSize"))
                                    for spec in typo.values() if isinstance(spec, dict)},
            "rounded": {to_px(v) for v in rounded.values()},
            "spacing": {to_px(v) for v in spacing.values()},
        }
        for label, vals in doc_sets.items():
            vals = {v for v in vals if v is not None}
            missing = sorted(vals - css_nums)
            if missing:
                shown = "、".join(f"{v}px" for v in missing)
                add("E", f"{css_name} 没有实现 {label} 里的这些值: {shown}"
                         "（DESIGN.md 说有、CSS 里找不到对应变量，等于这个档位不存在）")

        # 反向：CSS 里 radius 命名的变量，值必须出现在 rounded 阶里
        doc_radius = {v for v in doc_sets["rounded"] if v is not None}
        for n, v in css_vars:
            if "radius" not in n and "rounded" not in n:
                continue
            px = to_px(v)
            if px is not None and doc_radius and px not in doc_radius:
                add("W", f"{css_name} 里 `{n}: {v.strip()}` = {px}px，不在 rounded 阶上（会悄悄长出一档圆角）")
        break


    # --- 生图侧出口 ---
    if not (design_md.parent / "prompt.md").exists():
        add("W", "缺 prompt.md（生图出口）。没有它这个风格只能用于网页，不能用于配图。")

    return findings, tokens


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    dirs = sorted([d for d in STYLES.iterdir() if d.is_dir()]) if STYLES.exists() else []
    if only:
        dirs = [d for d in dirs if d.name == only]
        if not dirs:
            sys.exit(f"找不到风格: {only}")

    total = {"E": 0, "W": 0, "I": 0}
    print()
    for d in dirs:
        dm = d / "DESIGN.md"
        if not dm.exists():
            print(f"\033[31m✗ {d.name}\033[0m: 缺 DESIGN.md")
            total["E"] += 1
            continue
        findings, tokens = lint_style(dm)
        name = tokens.get("name", d.name)
        n_e = sum(1 for f in findings if f[0] == "E")
        n_w = sum(1 for f in findings if f[0] == "W")
        n_i = sum(1 for f in findings if f[0] == "I")
        total["E"] += n_e
        total["W"] += n_w
        total["I"] += n_i

        mark = "\033[32m✓\033[0m" if n_e == 0 and n_w == 0 else (
            "\033[31m✗\033[0m" if n_e else "\033[33m!\033[0m")
        print(f"{mark} {name}  ({d.name})   E{n_e} W{n_w} I{n_i}")
        for level, msg, where in findings:
            color = {"E": "31", "W": "33", "I": "36"}[level]
            w = f"  [{where}]" if where else ""
            print(f"    \033[{color}m{level}\033[0m {msg}{w}")
    print(f"\n合计: {total['E']} 错误 / {total['W']} 警告 / {total['I']} 提示\n")
    sys.exit(1 if total["E"] else 0)


if __name__ == "__main__":
    main()
