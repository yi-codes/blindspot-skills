#!/usr/bin/env bash
# 新建一个风格目录，生成三个待填文件。
# 用法: ./scripts/new-style.sh <slug> "<中文名>"
#   例: ./scripts/new-style.sh brutalist "粗野主义"

set -euo pipefail

cd "$(dirname "$0")/.."

slug="${1:-}"
name="${2:-}"

if [ -z "$slug" ] || [ -z "$name" ]; then
  echo "用法: ./scripts/new-style.sh <slug> \"<中文名>\""
  echo "  例: ./scripts/new-style.sh brutalist \"粗野主义\""
  exit 1
fi

if ! printf '%s' "$slug" | grep -Eq '^[a-z][a-z0-9-]*$'; then
  echo "错误: slug 只能用小写字母、数字和短横线，且以字母开头（当前: $slug）"
  exit 1
fi

dir="styles/$slug"
if [ -d "$dir" ]; then
  echo "错误: $dir 已存在，不覆盖。"
  exit 1
fi

# 变量前缀取 slug 前两段首字母，冲突时手动改
prefix=$(printf '%s' "$slug" | awk -F- '{print substr($1,1,2)}')

mkdir -p "$dir"

cp scripts/templates/DESIGN.md "$dir/DESIGN.md"
STYLE_NAME="$name" STYLE_SLUG="$slug" perl -pi -e \
  's/__NAME__/$ENV{STYLE_NAME}/g; s/__SLUG__/$ENV{STYLE_SLUG}/g' "$dir/DESIGN.md"

cat > "$dir/tokens.css" <<EOF
/* ============================================================
   ${name} · 待填
   用法：给任意容器加 class="ds-${slug}"
   ------------------------------------------------------------
   变量前缀 --${prefix}-
   ============================================================ */

:where(.ds-${slug}) {
  /* ---- 颜色 ---- */
  --${prefix}-bg:          #FFFFFF;
  --${prefix}-surface:     #FFFFFF;
  --${prefix}-surface-alt: #F5F5F5;
  --${prefix}-ink:         #111111;
  --${prefix}-ink-muted:   #666666;
  --${prefix}-ink-faint:   #8F8F8F;
  --${prefix}-line:        #E0E0E0;
  --${prefix}-accent:      #2557D6;
  --${prefix}-accent-weak: #EAF0FD;

  /* ---- 字体 ---- */
  --${prefix}-font-display: system-ui, sans-serif;
  --${prefix}-font-body:    system-ui, sans-serif;
  --${prefix}-font-mono:    ui-monospace, monospace;

  /* ---- 字号阶（模数至少 1.25，只跳不渐进） ---- */
  --${prefix}-text-xs:  0.75rem;
  --${prefix}-text-sm:  0.875rem;
  --${prefix}-text-md:  1rem;
  --${prefix}-text-lg:  1.25rem;
  --${prefix}-text-xl:  1.5625rem;
  --${prefix}-text-2xl: 1.953rem;

  --${prefix}-leading-tight: 1.2;
  --${prefix}-leading-body:  1.75;  /* 中文正文 ≥ 1.7 */
  --${prefix}-tracking-display: -0.01em;
  --${prefix}-tracking-body:    0;

  /* ---- 间距（8 的倍数） ---- */
  --${prefix}-space-1: 0.5rem;
  --${prefix}-space-2: 1rem;
  --${prefix}-space-3: 1.5rem;
  --${prefix}-space-4: 2rem;
  --${prefix}-space-5: 3rem;
  --${prefix}-space-6: 4rem;

  /* ---- 形状 ---- */
  --${prefix}-radius: 0;
  --${prefix}-border: 1px solid var(--${prefix}-line);
  --${prefix}-border-strong: 1px solid var(--${prefix}-ink);

  /* ---- 动效 ---- */
  --${prefix}-duration: 160ms;
  --${prefix}-ease: cubic-bezier(0.2, 0, 0.2, 1);
}

:where(.ds-${slug}) {
  background: var(--${prefix}-bg);
  color: var(--${prefix}-ink);
  font-family: var(--${prefix}-font-body);
  font-size: var(--${prefix}-text-md);
  line-height: var(--${prefix}-leading-body);
  letter-spacing: var(--${prefix}-tracking-body);
  -webkit-font-smoothing: antialiased;
}

:where(.ds-${slug}) :where(h1, h2, h3, h4) {
  font-family: var(--${prefix}-font-display);
  font-weight: 700;
  line-height: var(--${prefix}-leading-tight);
  letter-spacing: var(--${prefix}-tracking-display);
  margin: 0 0 var(--${prefix}-space-2);
  text-wrap: balance;
}
:where(.ds-${slug}) :where(h1) { font-size: var(--${prefix}-text-2xl); }
:where(.ds-${slug}) :where(h2) { font-size: var(--${prefix}-text-xl); }
:where(.ds-${slug}) :where(h3) { font-size: var(--${prefix}-text-lg); }

:where(.ds-${slug}) :where(p) { margin: 0 0 var(--${prefix}-space-2); max-width: 34em; }
:where(.ds-${slug}) :where(a) { color: var(--${prefix}-accent); }
:where(.ds-${slug}) :where(hr) { border: 0; border-top: var(--${prefix}-border); margin: var(--${prefix}-space-3) 0; }

:where(.ds-${slug}) :where(button, .ds-btn) {
  font-family: var(--${prefix}-font-body);
  font-size: var(--${prefix}-text-sm);
  padding: 0.7em 1.4em;
  border-radius: var(--${prefix}-radius);
  border: var(--${prefix}-border-strong);
  background: var(--${prefix}-ink);
  color: var(--${prefix}-bg);
  cursor: pointer;
}

:where(.ds-${slug}) :where(.ds-card) {
  background: var(--${prefix}-surface);
  border: var(--${prefix}-border);
  border-radius: var(--${prefix}-radius);
  padding: var(--${prefix}-space-3);
}

:where(.ds-${slug}) :where(.ds-tag) {
  display: inline-block;
  font-size: var(--${prefix}-text-xs);
  padding: 0.25em 0.6em;
  border-radius: var(--${prefix}-radius);
  background: var(--${prefix}-accent-weak);
  color: var(--${prefix}-accent);
}

:where(.ds-${slug}) :where(.ds-eyebrow) {
  font-size: var(--${prefix}-text-xs);
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--${prefix}-accent);
}

:where(.ds-${slug}) :where(.ds-stat-value) {
  font-size: var(--${prefix}-text-xl);
  line-height: var(--${prefix}-leading-tight);
  font-variant-numeric: tabular-nums;
}
:where(.ds-${slug}) :where(.ds-stat-label) {
  font-size: var(--${prefix}-text-xs);
  color: var(--${prefix}-ink-faint);
}
EOF

cat > "$dir/prompt.md" <<EOF
# ${name} · 生图 Prompt 模板

## 主模板（可直接用）

\`\`\`
[材质/主体], [光线], [构图], [色彩与后期]
\`\`\`

四段式：材质 → 光线 → 构图 → 色彩后期。每段最多两个词，总数不超过 8 个。

## 中文说明

-

## 变体

**变体一（用途）**
\`\`\`
...
\`\`\`

## 负向词

见 \`../../prompts/negative.md\` 通用清单，本风格额外加：

\`\`\`
...
\`\`\`

## 参数建议

| 项 | 建议 |
|---|---|
| 画幅 | |
| 光线 | |
| 色温 | |
| 后期 | |
| 禁忌 | |
EOF

echo "已创建 $dir/"
echo "  变量前缀 --${prefix}-"
echo "  class 名 .ds-${slug}"
echo ""
echo "下一步："
echo "  1. 填 $dir/DESIGN.md（先写 Overview 和 Colors，那是这个风格的定义）"
echo "  2. 填 $dir/tokens.css"
echo "  3. 填 $dir/prompt.md"
echo "  4. ./scripts/build-preview.py 重新生成预览"
