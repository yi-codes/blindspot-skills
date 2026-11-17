#!/usr/bin/env python3
"""从 styles/index.json 生成静态目录数据。"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "styles" / "index.json"
OUT = ROOT / "catalog" / "data.js"


def main() -> int:
    payload = json.loads(INDEX.read_text(encoding="utf-8"))
    data = {
        "generatedAt": datetime.now().astimezone().strftime("%Y-%m-%d %H:%M"),
        "count": payload.get("count", len(payload.get("styles", []))),
        "styles": payload.get("styles", []),
    }
    OUT.write_text(
        "window.DESIGN_DATA = "
        + json.dumps(data, ensure_ascii=False, separators=(",", ":"))
        + ";\n",
        encoding="utf-8",
    )
    print(f"已生成 {OUT.relative_to(ROOT)}，共 {data['count']} 个风格。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

