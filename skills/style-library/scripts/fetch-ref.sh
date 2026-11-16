#!/usr/bin/env bash
# 抓一份外部 DESIGN.md 到 references/ 存档。
# 用法:
#   ./scripts/fetch-ref.sh <owner/repo> <path/in/repo> <短名>
# 例:
#   ./scripts/fetch-ref.sh VoltAgent/awesome-design-md design-md/linear/DESIGN.md linear
#
# 说明: 走 raw.githubusercontent.com，不受 GitHub API 限额影响。
#       默认走 Clash 代理 127.0.0.1:7897（本机直连 raw 会 reset）；
#       想直连就设 PROXY=""。

set -euo pipefail
cd "$(dirname "$0")/.."

owner_repo="${1:-}"
path="${2:-}"
name="${3:-}"
PROXY="${PROXY-http://127.0.0.1:7897}"

if [ -z "$owner_repo" ] || [ -z "$path" ] || [ -z "$name" ]; then
  echo "用法: ./scripts/fetch-ref.sh <owner/repo> <path/in/repo> <短名>"
  echo "  例: ./scripts/fetch-ref.sh VoltAgent/awesome-design-md design-md/linear/DESIGN.md linear"
  exit 1
fi

url="https://raw.githubusercontent.com/${owner_repo}/main/${path}"
dir="references/${name}"

if [ -f "$dir/DESIGN.md" ]; then
  echo "已存在 $dir/DESIGN.md，不覆盖。要更新先手动删。"
  exit 1
fi

mkdir -p "$dir"

proxy_args=()
[ -n "$PROXY" ] && proxy_args=(-x "$PROXY")

echo "GET $url"
code=$(curl -s "${proxy_args[@]}" --max-time 30 -w "%{http_code}" -o "$dir/DESIGN.md" "$url")

if [ "$code" != "200" ]; then
  rm -f "$dir/DESIGN.md"
  echo "失败: HTTP $code"
  echo "  可能是路径不对（分支不是 main？），或网络不通。"
  exit 1
fi

lines=$(wc -l < "$dir/DESIGN.md" | tr -d ' ')
echo "已保存 $dir/DESIGN.md（${lines} 行）"

if [ ! -f "$dir/NOTES.md" ]; then
  cat > "$dir/NOTES.md" <<EOF
# ${name}

## 来源

- 仓库：\`${owner_repo}\`
- 路径：\`${path}\`
- 抓取：$(date +%Y-%m-%d)
- star：（填）

## 取（吸收了什么，落到哪）

-

## 弃（明确不吸收，为什么）

-

## 待观察

-
EOF
  echo "已生成 $dir/NOTES.md 模板，去填「取 / 弃 / 待观察」。"
fi

echo ""
echo "下一步：读一遍 $dir/DESIGN.md，按 references/README.md 的三步拆解。"
