#!/usr/bin/env python3
"""一次性补丁：给所有 DESIGN.md 补齐六层契约的 4/5/6 层（elevation/media/motion）。

按每个风格的 surface（明暗）和 register（职守）推导差异化取值：
- 深色：层级靠明度 + 内描边，不用投影（principles.md §11.3）
- 浅色：带偏移的阶梯阴影，主分隔手段按 register 选
- mixed：给浅色主值，正文里说明深色变体怎么切

只插入缺失的字段/章节，已存在的不动。可重复运行。
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STYLES = ROOT / "styles"

DARK = {"deco-ceremony", "incident-room", "nocturne", "quiet-dark", "signal-console", "tactile-3d", "terminal-mono"}
# academic / soft-pastel / liquid-glass 等 mixed 在正文里另有说明，这里按浅色主值生成

# 主分隔手段：tool/technical 偏边框，story 偏留白或阴影，professional 偏边框
SEPARATOR = {
    "tool": "border",
    "technical": "border",
    "professional": "border",
    "story": "shadow",
}
MEDIA_RATIO = {
    "story": "4:3",
    "tool": "16:9",
    "technical": "16:10",
    "professional": "3:2",
}
LOGO_TYPE = {
    "story": "wordmark",
    "tool": "combo",
    "technical": "wordmark",
    "professional": "combo",
}


def front_matter_and_body(text):
    sys.path.insert(0, str(Path(__file__).parent))
    from _designmd import split_front_matter
    return split_front_matter(text)


def get_scalar(fm, key):
    m = re.search(rf"^{key}:\s*(.+)$", fm, re.MULTILINE)
    return m.group(1).strip() if m else ""


def group_keys(fm, group):
    """取某个 front matter 组（如 colors / rounded）下的直接子键名。"""
    keys = []
    in_group = False
    for line in fm.split("\n"):
        if re.match(r"^\w[\w-]*:\s*$", line):
            in_group = line.strip().rstrip(":") == group
            continue
        if in_group:
            m = re.match(r"^  ([\w.-]+):", line)
            if m:
                keys.append(m.group(1))
    return keys


def pick(keys, *candidates, fallback=None):
    for c in candidates:
        if c in keys:
            return c
    return fallback if fallback is not None else (keys[0] if keys else None)


def token_ref(group, key):
    return "{" + f"{group}.{key}" + "}" if key else "currentColor"


def elevation_block(is_dark, register, hairline, border_dark):
    if is_dark:
        return f"""elevation:
  lightSource: top-left
  steps: 3
  e1: "inset 0 0 0 1px {hairline}"
  e2: "inset 0 0 0 1px {hairline}, 0 1px 0 rgba(255,255,255,0.04)"
  e3: "inset 0 0 0 1px {border_dark}, 0 8px 24px rgba(0,0,0,0.32)"
  topHighlight: "inset 0 1px 0 rgba(255,255,255,0.06)"
  borderLight: "{hairline}"
  borderDark: "{border_dark}"
  separator: {"border" if register in ('tool', 'technical', 'professional') else 'shadow'}"""
    return f"""elevation:
  lightSource: top-left
  steps: 3
  e1: "0 1px 2px rgba(15,23,42,0.06)"
  e2: "0 4px 12px rgba(15,23,42,0.10)"
  e3: "0 12px 32px rgba(15,23,42,0.14)"
  topHighlight: "inset 0 1px 0 rgba(255,255,255,0.60)"
  borderLight: "{hairline}"
  borderDark: "{border_dark}"
  separator: {SEPARATOR.get(register, 'border')}"""


def media_block(register, radius_ref, ink_ref, canvas_ref):
    return f"""media:
  logoType: {LOGO_TYPE.get(register, 'wordmark')}
  logoRule: "字标沿用显示字族，右侧留 0.5em；图形标只用单色 {ink_ref}，最小 24px"
  imageRadius: "{radius_ref}"
  imageRatio: "{MEDIA_RATIO.get(register, '4:3')}"
  imageTreatment: "去饱和 6%，不加投影；与底色相接处用 1px 描边收口"
  background: "纯色 {canvas_ref}，无纹理、无氛围渐变"
  iconRule: "1.6px 描边，20px 基准，与正文同色，不使用彩色图标"
  emptyState: "淡底 + 一行说明文字，不放装饰插画和大号图标\""""


def motion_block(register, accent_ref):
    spring = ("true" if register == "tool" else "false")
    return f"""motion:
  easing: "cubic-bezier(0.2, 0.8, 0.2, 1)"
  durationFast: 120ms
  durationBase: 200ms
  hover: "背景升一档明度，位移 0；有阴影时抬高一级"
  focusRing: "3px solid {accent_ref}，offset 2px，不被圆角裁切"
  openTransition: "scaleY 0→1，transform-origin top，120ms"
  reducedMotion: "全部过渡降到 1ms，去掉位移"
  dragUsesSpring: {spring}"""


SECTIONS = """

## Material & Elevation

光从 `{elevation.lightSource}` 来，固定这一个方位。共 `{elevation.steps}` 级：
`{elevation.e1}` 贴面、`{elevation.e2}` 卡片、`{elevation.e3}` 浮层。
深色上层级靠明度与内描边，浅色上靠带偏移的阴影——不做居中发光。
主分隔手段是 `{elevation.separator}`，其余只做辅助。

## Mark & Media

标识：`{media.logoRule}`（`{media.logoType}`）。
图片：比例 `{media.imageRatio}`、圆角 `{media.imageRadius}`、处理 `{media.imageTreatment}`。
背景：`{media.background}`。图标：`{media.iconRule}`。空态：`{media.emptyState}`。
只写规则不写品牌资产；图片处理都是可复现参数。

## Motion & States

过渡曲线 `{motion.easing}`，快档 `{motion.durationFast}`、基准 `{motion.durationBase}`。
hover：`{motion.hover}`；焦点：`{motion.focusRing}`；展开：`{motion.openTransition}`。
交互组件逐项覆盖 default / hover / focus-visible / active / disabled / error 六态。
`prefers-reduced-motion` 时 `{motion.reducedMotion}`。
"""


def patch_style(path, slug):
    text = path.read_text(encoding="utf-8")
    fm, body = front_matter_and_body(text)
    if fm is None:
        return "skip(no front matter)"
    changed = []
    if re.search(r"^elevation:\s*$", fm, re.MULTILINE):
        changed.append("front matter already has elevation")
    else:
        surface = get_scalar(fm, "surface")
        register = get_scalar(fm, "register")
        is_dark = (surface == "dark") or (slug in DARK)

        # 用库自带的解析器拿真实键名（比自写正则可靠）
        sys.path.insert(0, str(Path(__file__).parent))
        from _designmd import parse_tokens
        parsed = parse_tokens(fm)
        color_keys = list(parsed.get("colors", {}).keys()) if isinstance(parsed.get("colors"), dict) else []
        radius_keys = list(parsed.get("rounded", {}).keys()) if isinstance(parsed.get("rounded"), dict) else []
        ink_key = pick(color_keys, "ink", "text", fallback="ink")
        canvas_key = pick(color_keys, "canvas", "bg", "background", fallback="canvas")
        accent_key = pick(color_keys, "primary", "accent", "main", "link", fallback="ink")
        radius_key = pick(radius_keys, "card", "panel", "control", "md", "sm", "base", fallback=None)

        ink_ref = token_ref("colors", ink_key)
        canvas_ref = token_ref("colors", canvas_key)
        accent_ref = token_ref("colors", accent_key)
        radius_ref = token_ref("rounded", radius_key) if radius_key else "0px"

        # 描边明暗各取一个键：优先 hairline 系（浅）/ hairline-strong 系（深），
        # 取不到就用 surface / ink 拉开明度差，绝不撞成同一个 token
        line_light_key = pick(color_keys, "hairline", "line", "border", "surface-alt", "surface", fallback=None)
        line_dark_key = pick(color_keys, "hairline-strong", "line-strong", "border-strong", "ink-faint", "ink-muted", fallback=None)
        hairline_ref = token_ref("colors", line_light_key) if line_light_key else token_ref("colors", "surface")
        border_dark_ref = token_ref("colors", line_dark_key) if line_dark_key and line_dark_key != line_light_key else ink_ref

        add = (
            "\n"
            + elevation_block(is_dark, register, hairline_ref, border_dark_ref)
            + "\n"
            + media_block(register, radius_ref, ink_ref, canvas_ref)
            + "\n"
            + motion_block(register, accent_ref)
            + "\n"
        )
        fm = fm.rstrip() + "\n" + add
        changed.append("front matter: +elevation/+media/+motion")

    if "## Material & Elevation" not in body:
        body = body.rstrip() + "\n" + SECTIONS
        changed.append("body: +3 sections")

    new_text = "---" + fm + "---" + body
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
    return "; ".join(changed) or "unchanged"


def main():
    for d in sorted(STYLES.iterdir()):
        if not d.is_dir():
            continue
        design = d / "DESIGN.md"
        if not design.exists():
            continue
        print(f"{d.name}: {patch_style(design, d.name)}")


if __name__ == "__main__":
    main()
