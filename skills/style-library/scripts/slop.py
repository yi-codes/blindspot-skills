#!/usr/bin/env python3
"""产物层检查 —— 找 AI 味儿。

和 lint.py 的分工：
    lint.py  查**文档**：DESIGN.md 与 tokens.css 是否自洽、token 引用是否有效、对比度、章节。
    slop.py  查**产物**：真正做出来的 HTML 和它引用的 CSS 里，有没有 principles.md §11 的"一眼假"。

为什么必须分开：
    lint 全绿但产物很丑，是常态。因为 lint 从不读 HTML。

用法：
    python3 scripts/slop.py showcase/*.html
    python3 scripts/slop.py page.html --quiet

检查项（编号对应 principles.md §11.2）：
    S1  渐变文字 / 紫蓝渐变          (#1)
    S2  装饰性 eyebrow               (#3)
    S3  全大写或拉大字距的小标签       (#4)  ← 默认 W。编辑/瑞士/终端三种排版传统里
                                              这是原生语法，不算抄；--strict 才升成 E。
    S4  中点拼三个以上元信息          (#5)
    S5  裸纯黑 / 纯白                (#8)
    S6  等宽字体当戏服（提示级）       (#6)
    S7  氛围光 / 无偏移的发光投影      (#10)

豁免 —— 写在触发那一行，理由不少于 12 个字符：
    .label { text-transform: uppercase; }  /* slop-ok S3: 这是终端风格里真实的 ENV 名 */

理由是给自己看的。写不出像样的理由，通常说明它确实不该在那儿。
"""

import re
import sys
from pathlib import Path

MIN_REASON = 12

WAIVER_RE = re.compile(r"slop-ok\s+(S\d)(?:\s*[:：]\s*([^*]*))?")


# ------------------------------------------------------------------ 小工具

def to_lines(text):
    return text.split("\n")


def line_of(text, index):
    return text.count("\n", 0, index) + 1


def hex_hue(h):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    r, g, b = (int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    mx, mn = max(r, g, b), min(r, g, b)
    d = mx - mn
    if d == 0:
        return None
    if mx == r:
        hue = ((g - b) / d) % 6
    elif mx == g:
        hue = (b - r) / d + 2
    else:
        hue = (r - g) / d + 4
    return hue * 60


def px_value(v):
    """'15px' → 15 ; '0.9375rem' → 15 ; 其它 → None"""
    v = v.strip().lower()
    m = re.match(r"^(-?[\d.]+)px$", v)
    if m:
        return float(m.group(1))
    m = re.match(r"^(-?[\d.]+)rem$", v)
    if m:
        return float(m.group(1)) * 16
    m = re.match(r"^(-?[\d.]+)em$", v)
    if m:
        return float(m.group(1)) * 16
    return None


def em_value(v):
    v = v.strip().lower()
    m = re.match(r"^(-?[\d.]+)em$", v)
    if m:
        return float(m.group(1))
    m = re.match(r"^(-?[\d.]+)px$", v)
    if m:
        return float(m.group(1)) / 16
    return None


# ------------------------------------------------------------------ CSS 规则切分

RULE_RE = re.compile(r"([^{}@;]+)\{([^{}]*)\}")


def strip_comments(css):
    """把 /* */ 换成等长空白，保留换行。这样行号不变，注释也不会混进 selector。"""
    def blank(m):
        return re.sub(r"[^\n]", " ", m.group())
    return re.sub(r"/\*.*?\*/", blank, css, flags=re.S)


def iter_rules(css):
    """→ 生成 (selector, {prop: value}, 行号)。跳过 @media/@supports 的外壳。"""
    for m in RULE_RE.finditer(css):
        sel = m.group(1).strip()
        body = m.group(2)
        if not sel or sel.startswith("@") or "/*" in sel and "*/" not in sel:
            continue
        decls = {}
        for d in body.split(";"):
            if ":" not in d:
                continue
            k, v = d.split(":", 1)
            k = k.strip().lower()
            if k:
                decls[k] = v.strip()
        yield sel, decls, line_of(css, m.start())


# ------------------------------------------------------------------ 检查

class Report:
    def __init__(self, name):
        self.name = name
        self.items = []
        self.waived = []

    def add(self, level, code, msg, where=""):
        self.items.append((level, code, msg, where))

    def waiver(self, code, reason, where):
        self.waived.append((code, reason, where))

    def bump(self, count):
        self.items = self.items[count:]


def check_css(css, fname, rep, line_offset=0, strict=False):
    rules = list(iter_rules(strip_comments(css)))
    lines = to_lines(css)
    seen = set()

    def key(code, ln):
        return (code, ln)

    for sel, decls, ln_raw in rules:
        ln = ln_raw + line_offset
        raw_line = lines[ln_raw - 1] if ln_raw - 1 < len(lines) else ""
        # 豁免：规则起始行或带声明的那几行里的 slop-ok
        window = "\n".join(lines[max(0, ln_raw - 1):ln_raw + 6])
        waivers = {}
        for wm in WAIVER_RE.finditer(window):
            waivers[wm.group(1)] = (wm.group(2) or "").strip()

        hit = []

        # S1 渐变
        for prop in ("background", "background-image"):
            val = decls.get(prop, "")
            if "gradient(" in val:
                hues = [hex_hue(h) for h in re.findall(r"#[0-9A-Fa-f]{3,6}\b", val)]
                hues = [h for h in hues if h is not None]
                purple = any(248 <= h <= 305 for h in hues)
                if purple:
                    hit.append(("E", "S1", f"渐变里有紫色相（{val[:60]}），这是第一号 AI 特征", f"{fname}:{ln} {sel}"))
                elif len(hues) >= 2:
                    hit.append(("W", "S1", f"多色相渐变（{val[:60]}）—— 确认它是否承担了语义", f"{fname}:{ln} {sel}"))
        if "text" in decls.get("background-clip", "").lower() or "text" in decls.get("-webkit-background-clip", "").lower():
            hit.append(("E", "S1", "渐变文字（background-clip: text）", f"{fname}:{ln} {sel}"))

        # S2 eyebrow
        if re.search(r"eyebrow|kicker|overline|pretitle|pre-title", sel, re.I):
            hit.append(("W", "S2", f"装饰性 eyebrow：`{sel}` —— 删掉它，页面丢了什么？", f"{fname}:{ln}"))

        # S3 全大写 / 拉大字距
        tt = decls.get("text-transform", "").lower()
        ls = em_value(decls.get("letter-spacing", "")) if decls.get("letter-spacing") else None
        fs = px_value(decls.get("font-size", "")) if decls.get("font-size") else None
        if tt in ("uppercase", "full-width") or decls.get("font-variant-caps", "") in ("small-caps", "all-small-caps"):
            if fs is None:
                hit.append(("W", "S3", f"全大写标签，字号未知（`{sel}`）—— 确认它 ≤15px", f"{fname}:{ln}"))
            elif fs <= 15:
                lvl = "E" if strict else "W"
                hit.append((lvl, "S3", f"全大写 + {fs:g}px 小标签（`{sel}`）", f"{fname}:{ln}"))
        if ls is not None and ls > 0.03 and (fs is None or fs <= 16):
            lvl = "E" if strict else "W"
            hit.append((lvl, "S3", f"字距 {ls:g}em 超过 0.03（`{sel}`）—— 小标签不拉字距", f"{fname}:{ln}"))

        # S5 裸纯黑白
        for prop, val in decls.items():
            if prop.startswith("--"):
                continue
            v = val.strip().lower()
            if v in ("#fff", "#ffffff", "white", "#000", "#000000", "black"):
                lvl = "E"
                hit.append((lvl, "S5", f"`{prop}: {val}` 是绝对黑/白 —— 往主色偏一点", f"{fname}:{ln} {sel}"))
            m = re.match(r"^rgba?\(\s*(255\s*,\s*255\s*,\s*255|0\s*,\s*0\s*,\s*0)\s*(?:,\s*1(\.0+)?\s*)?\)$", v)
            if m and prop in ("color", "background", "background-color"):
                hit.append(("W", "S5", f"`{prop}: {val[:40]}` 用了绝对黑/白", f"{fname}:{ln} {sel}"))

        # S6 mono 当戏服
        ff = decls.get("font-family", "").lower()
        CODEISH = r"code|pre\b|kbd|samp|mono|diff|cmd|log|terminal|token|num|line|hunk|dline|d2|fhead|fchip|gutter|\bln\b"
        if ("mono" in ff) and not re.search(CODEISH, sel, re.I):
            if fs is not None and fs <= 13:
                hit.append(("I", "S6", f"等宽字体用在 {fs:g}px 的非代码元素（`{sel}`）", f"{fname}:{ln}"))

        # S7 发光
        sh = decls.get("box-shadow", "")
        if sh:
            for part in sh.split(","):
                nums = re.findall(r"-?[\d.]+px", part)
                if len(nums) >= 3:
                    try:
                        ox, oy = float(nums[0][:-2]), float(nums[1][:-2])
                        blur = float(nums[2][:-2])
                    except ValueError:
                        continue
                    color = re.search(r"#[0-9A-Fa-f]{3,6}|rgba?\([^)]*\)", part)
                    if ox == 0 and oy == 0 and blur > 0 and not (color and "0, 0, 0" in color.group() or color and color.group().lower().startswith("#0")):
                        hit.append(("W", "S7", f"无偏移的发光投影（{part.strip()[:44]}）—— 深色上的投影会变成光", f"{fname}:{ln} {sel}"))
        if re.search(r"filter:\s*blur", " ".join(f"{k}:{v}" for k, v in decls.items())):
            hit.append(("W", "S7", "filter: blur —— 模糊光斑是 AI 最爱的氛围手段", f"{fname}:{ln} {sel}"))

        for item in hit:
            code, where = item[1], item[3]
            if code in waivers:
                reason = waivers[code]
                if len(reason) >= MIN_REASON and code + where not in seen:
                    rep.waiver(code, reason, where)
                    seen.add(code + where)
                    continue
                if len(reason) < MIN_REASON:
                    rep.add("W", code, f"豁免理由太短（{len(reason)}<{MIN_REASON} 字符），不算数", where)
            if code + where in seen:
                continue
            seen.add(code + where)
            rep.add(*item)

    return rep


def check_markup(html, fname, rep):
    """S4：可见文本里的中点串。"""
    # 去掉 style/script，避免把 CSS 内容当文本
    stripped = re.sub(r"<(style|script)[^>]*>.*?</\1>", lambda m: " " * len(m.group()), html,
                      flags=re.S | re.I)
    for m in re.finditer(r">([^<>]{2,})<", stripped):
        text = m.group(1)
        if text.count("·") >= 2:
            ln = line_of(stripped, m.start())
            rep.add("E", "S4", f"中点拼了三段以上元信息：`{text.strip()[:48]}`", f"{fname}:{ln}")


# ------------------------------------------------------------------ 主流程

def scan(path, strict=False):
    html = path.read_text(encoding="utf-8", errors="replace")
    rep = Report(str(path))

    # 1) 内联 <style>
    for m in re.finditer(r"<style[^>]*>(.*?)</style>", html, re.S | re.I):
        check_css(m.group(1), path.name, rep, line_offset=line_of(html, m.start(1)) - 1, strict=strict)

    # 2) 外链 CSS
    for m in re.finditer(r"<link[^>]+href=[\"']([^\"']+\.css)[\"']", html, re.I):
        href = m.group(1)
        if href.startswith("http"):
            continue
        css_path = (path.parent / href).resolve()
        if not css_path.exists():
            rep.add("W", "S0", f"引用的 CSS 不存在：{href}", path.name)
            continue
        try:
            label = str(css_path.relative_to(path.parent.parent))
        except ValueError:
            label = css_path.name
        check_css(css_path.read_text(encoding="utf-8", errors="replace"), label, rep, strict=strict)

    # 3) 文本层
    check_markup(html, path.name, rep)
    return rep


def main(argv):
    quiet = "--quiet" in argv
    strict = "--strict" in argv
    files = [a for a in argv[1:] if not a.startswith("-")]
    if not files:
        print("用法: python3 scripts/slop.py <html...> [--quiet] [--strict]")
        return 2

    total = {"E": 0, "W": 0, "I": 0}
    n_waived = 0
    for f in files:
        p = Path(f)
        if not p.exists():
            print(f"跳过（不存在）: {f}")
            continue
        rep = scan(p, strict=strict)
        errs = [i for i in rep.items if i[0] == "E"]
        warns = [i for i in rep.items if i[0] == "W"]
        infos = [i for i in rep.items if i[0] == "I"]
        for k, v in (("E", len(errs)), ("W", len(warns)), ("I", len(infos))):
            total[k] += v
        n_waived += len(rep.waived)

        mark = "✓" if not errs else "✗"
        print(f"\n{mark} {p.name}   E{len(errs)} W{len(warns)} I{len(infos)}"
              + (f"  豁免{len(rep.waived)}" if rep.waived else ""))
        if quiet:
            continue
        for lvl, code, msg, where in errs + warns + infos:
            print(f"    {lvl} [{code}] {msg}")
            if where:
                print(f"           {where}")
        for code, reason, where in rep.waived:
            print(f"    · [{code}] 已豁免：{reason}   ({where})")

    print(f"\n合计: {total['E']} 错误 / {total['W']} 警告 / {total['I']} 提示"
          + (f" / {n_waived} 处豁免" if n_waived else ""))
    print("\nE 是 principles.md §11.2 里点名的特征，改掉或用 `slop-ok` 写明理由。")
    print("W 需要你自己确认；I 只是提示。")
    return 1 if total["E"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
