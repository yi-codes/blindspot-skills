# 从旧入口迁移

## 路径映射

| 旧路径或名称 | 新路径 |
|---|---|
| `skills/style-library/` | `skills/design-library/` |
| `ui-styles/styles/codex-workbench.md` | `styles/codex-workbench/DESIGN.md` |
| `ui-styles/styles/liquid-glass.md` | `styles/liquid-glass/DESIGN.md` |
| `ui-styles/styles/ops-console.md` 的日常观测 | `styles/signal-console/DESIGN.md` |
| `ui-styles/styles/ops-console.md` 的事故响应 | `styles/incident-room/DESIGN.md` |

## 命令映射

| 旧命令 | 新命令 |
|---|---|
| `python3 scripts/lint.py` | `python3 scripts/designlib.py check` |
| `python3 scripts/build-index.py` | `python3 scripts/designlib.py build` |
| `python3 scripts/build-preview.py` | `python3 scripts/designlib.py build` |
| `./scripts/new-style.sh <slug> "<名称>"` | `python3 scripts/designlib.py new <slug> "<名称>"` |

`lint.py`、`slop.py` 等底层脚本仍保留，方便调试；日常入口统一为 `designlib.py`。

## Agent 安装

```bash
ln -sfn "$PWD/skills/design-library" ~/.codex/skills/design-library
```

不要继续保留两份 Skill 正本。旧目录可以在确认不再使用后移到备份位置。

