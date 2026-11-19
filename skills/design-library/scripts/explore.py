#!/usr/bin/env python3
"""发散起点：从模型外部注入一次随机性，产出结构不同的候选方向。

用法:
    python3 scripts/explore.py
    python3 scripts/explore.py --task "独立开发者的作品集首页"
    python3 scripts/explore.py --count 5 --json
    python3 scripts/explore.py --seed <hex>   # 复现同一轮

它只做一件事：给一个**模型自己生成不出来**的变化源。
模型说"随机一点"没用——它填的仍是高概率 token，于是换皮不换结构。
随机串必须来自 shell / secrets 这类外部源。

输出的是一段可复制的探索提示词，不是风格定义。
候选只有经过 REVIEW.md 的评审、并能写成六层字段，才允许进 references 候选池；
种子本身是一次性燃料，不进 DESIGN.md front matter，不进长期记忆。

边界：借自 Sakana AI《String Seed of Thought》(arXiv:2510.21150) 的思路，
但论文验证的是概率采样忠实度与输出多样性，**没有验证网页设计质量**。
详见 docs/EXPLORING.md。
"""

from __future__ import annotations

import argparse
import json
import secrets
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 候选之间必须在这些轴上不同。只换颜色不算不同方向。
STRUCTURE_AXES = (
    "构图骨架（首屏主体占比、栏数、对称或不对称）",
    "信息组织（列表 / 详情 / 引导流程 / 单一决策视图）",
    "字体类别与层级（衬线、无衬线、等宽各承担什么）",
    "交互隐喻（这个界面让人联想到什么实物或场景）",
)

PROMPT = """\
【探索任务】{task}

先读这串由外部随机源生成的十六进制字符。它只是燃料，不是答案：

{seed}

按下面的步骤做，不要跳步：

1. 从字符串里找可以转成设计规则的结构：重复模式、字符形状、特殊数字、
   段落节奏、明暗联想。不要把它当密码解读，也不要把它写进界面。
2. 给出 {count} 个**结构上真正不同**的方向。每个方向用 2-3 句话写清：
   - 视觉隐喻 / 目标感受
   - 构图骨架与信息层级
   - 字体类别、明暗关系、色彩家族
   - 一个只能属于这个产品、换到别的产品就不成立的决定
3. 差异必须落在这些轴上：{axes}
   只换主色、圆角或插图，不算不同方向——那是换皮。
4. 每个方向自检一遍 principles.md §11.2 的「一眼假 12 条」和 §11.1 的
   Specificity。命中 3 条以上或遮住产品名仍站得住的方向，直接划掉并说明原因。
5. 本轮只输出方向说明和自检结果，**不要实现页面，不要写 DESIGN.md**。
   等我选方向。种子不要出现在任何产物里。

约束（发散也不能越过的下限）：
- 颜色、字体、字号、间距、圆角仍只走所选风格的 tokens.css，不写裸值
- 一个页面只用一种风格（The Floor 第 9 条）
- 不用紫到蓝/紫到粉渐变，不用 background-clip: text（第 3 条）
- 中文正文行高不低于 1.7，界面类不低于 1.5（第 6 条）
- 标题前不放宣布型装饰小字（第 4 条）
- 每个交互元素有 :focus-visible，动效有 reduced-motion 降级（第 10 条）

大胆要落在清晰的设计选择上，不能牺牲可读性、导航或关键操作。
如果某个方向让你怀疑「这能做成网页吗」，它才真的在拓展边界；
如果一个方向听起来很安全，它大概率会退回训练分布里的平均答案。
"""

OUTPUT_NOTE = """\
---
下一步：把选中的方向写成 brief，再走 docs/REVIEW.md 的独立截图评审。
发散产物仍受六层契约管：能写成 {token} 或可检查规则的，才允许沉淀；
只是氛围的留在 references 当灵感，不进 styles/。
种子属于一次性判断燃料，不进 DESIGN.md front matter，不进长期记忆。
"""


def build_seed(seed: str | None, length: int) -> str:
    if seed:
        stripped = seed.strip().lower()
        if not stripped or any(c not in "0123456789abcdef" for c in stripped):
            raise ValueError("--seed 必须是十六进制字符串")
        return stripped
    # token_hex(48) = 96 个十六进制字符，足够从里面取出结构线索
    return secrets.token_hex(length)


def build_prompt(seed: str, task: str, count: int) -> str:
    return PROMPT.format(
        task=task,
        seed=seed,
        count=count,
        axes="；".join(STRUCTURE_AXES),
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="从外部随机源生成结构不同的设计方向探索提示词"
    )
    parser.add_argument(
        "--task", default="一个还没定视觉方向的产品页面",
        help="页面任务描述（越具体越好）",
    )
    parser.add_argument("--count", type=int, default=3, help="候选方向数量，默认 3")
    parser.add_argument("--seed", default=None, help="复现用的十六进制种子")
    parser.add_argument("--length", type=int, default=48, help="随机字节数，默认 48")
    parser.add_argument("--json", action="store_true", help="输出 JSON 便于脚本消费")
    args = parser.parse_args()

    if args.count < 2 or args.count > 8:
        print("错误：--count 需在 2 到 8 之间", file=sys.stderr)
        return 2
    if args.length < 8 or args.length > 256:
        print("错误：--length 需在 8 到 256 之间", file=sys.stderr)
        return 2

    try:
        seed = build_seed(args.seed, args.length)
    except ValueError as error:
        print(f"错误：{error}", file=sys.stderr)
        return 2

    prompt = build_prompt(seed, args.task, args.count)

    if args.json:
        print(json.dumps({
            "seed": seed,
            "task": args.task,
            "count": args.count,
            "axes": list(STRUCTURE_AXES),
            "prompt": prompt,
            "source": "secrets.token_hex (external)",
            "ephemeral": True,
        }, ensure_ascii=False, indent=2))
    else:
        print(prompt)
        print(OUTPUT_NOTE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
