#!/usr/bin/env python3
"""DESIGN.md 的共用解析器。零依赖。

为什么要单独抽出来：
    加一个风格时，lint / build-index / build-preview 三个脚本都要读同一份 front matter。
    解析逻辑写三遍 = 三处会漂。（这是"可扩展性"的具体含义：加东西时不该改老代码。）
"""

import re


# ------------------------------------------------------------------ 切 front matter

def split_front_matter(text):
    """返回 (yaml_text, body_text)。文件必须以 --- 开头，否则 yaml_text 为 None。"""
    if not text.startswith("---"):
        return None, text
    lines = text.split("\n")
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None, text
    return "\n".join(lines[1:end]), "\n".join(lines[end + 1:])


# ------------------------------------------------------------------ 顶层标量

_FOLD = (">-", ">", "|", "|-")


def flat_fields(yaml_text):
    """只读顶层，把标量和折叠块都拉平成 { 'name': '...', 'cues': '...' }。

    加新字段不用改这里 —— 任何没见过的顶层 key 都会被原样收进来。
    """
    out = {}
    lines = yaml_text.split("\n")
    i = 0
    while i < len(lines):
        raw = lines[i]
        line = raw.strip()
        i += 1
        if not line or line.startswith("#") or raw.startswith(" "):
            continue
        m = re.match(r"^([\w-]+):\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if val in _FOLD:
            # 折叠块：吃掉后面所有缩进行
            buf = []
            while i < len(lines) and (lines[i].startswith(" ") or not lines[i].strip()):
                buf.append(lines[i].strip())
                i += 1
            out[key] = " ".join(x for x in buf if x)
            continue
        if val.startswith('"') and val.endswith('"') and len(val) > 1:
            val = val[1:-1]
        elif val.startswith("'") and val.endswith("'") and len(val) > 1:
            val = val[1:-1]
        else:
            val = re.sub(r"\s+#\s.*$", "", val)
        out[key] = val
    return out


def split_list(value):
    """把 `a、b、c` 或 `a, b, c` 拆成列表。中英文分隔符都吃。"""
    if not value:
        return []
    parts = re.split(r"[、,，;；]", value)
    return [p.strip() for p in parts if p.strip()]


# ------------------------------------------------------------------ 嵌套 token

def parse_tokens(yaml_text):
    """两级映射 + 标量。够覆盖 DESIGN.md 的 token 段。

    返回 { 'colors': {'primary': '#123456'}, 'typography': {'h1': {'fontSize': '48px'}} }
    """
    tokens = {}
    top = None
    group = None
    for raw in yaml_text.split("\n"):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        line = raw.strip()

        if indent >= 4 and top == "_foldblock":
            continue

        if indent == 0:
            m = re.match(r"^([\w-]+):\s*(.*)$", line)
            if not m:
                continue
            key, val = m.group(1), m.group(2).strip()
            if val in _FOLD:
                top = "_foldblock"
                tokens.setdefault(key, "")
                continue
            if val == "":
                top = key
                group = None
                tokens.setdefault(key, {})
            else:
                top = None
                tokens[key] = _scalar(val)
        elif indent == 2 and isinstance(tokens.get(top), dict):
            m = re.match(r"^([\w.-]+):\s*(.*)$", line)
            if not m:
                continue
            key, val = m.group(1), m.group(2).strip()
            if val == "":
                group = key
                tokens[top][key] = {}
            else:
                group = None
                tokens[top][key] = _scalar(val)
        elif indent == 4 and group and isinstance(tokens.get(top, {}).get(group), dict):
            m = re.match(r"^([\w.-]+):\s*(.*)$", line)
            if m:
                tokens[top][group][m.group(1)] = _scalar(m.group(2).strip())
    tokens.pop("_foldblock", None)
    return tokens


def _scalar(v):
    v = v.strip()
    if v.startswith('"') and v.endswith('"') and len(v) > 1:
        return v[1:-1]
    if v.startswith("'") and v.endswith("'") and len(v) > 1:
        return v[1:-1]
    return re.sub(r"\s+#\s.*$", "", v)


# ------------------------------------------------------------------ 通用小工具

HEX_RE = re.compile(r"#[0-9A-Fa-f]{6}\b")


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def rel_luminance(rgb):
    def ch(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (ch(x) for x in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(c1, c2):
    l1, l2 = rel_luminance(hex_to_rgb(c1)), rel_luminance(hex_to_rgb(c2))
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def load_design(path):
    """→ (flat 顶层字段 dict, tokens dict, body 正文)"""
    text = path.read_text(encoding="utf-8")
    yml, body = split_front_matter(text)
    if yml is None:
        return None, None, text
    return flat_fields(yml), parse_tokens(yml), body
