"""发散脚本与两块新流程文档的契约测试。

这里只验证"能被机器检查的部分"：外部随机源、结构轴约束、一次性声明、
文档互相引用不断链。不验证设计质量——那属于 REVIEW.md 的职责。
"""

from __future__ import annotations

import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"

spec = importlib.util.spec_from_file_location("explore", SCRIPTS / "explore.py")
explore = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(explore)


class ExploreScriptTests(unittest.TestCase):
    def test_seed_is_external_and_long_enough(self):
        seed = explore.build_seed(None, 48)
        self.assertEqual(len(seed), 96)
        self.assertTrue(all(c in "0123456789abcdef" for c in seed))
        self.assertNotEqual(seed, explore.build_seed(None, 48))

    def test_explicit_seed_reproduces(self):
        given = "ab" * 48
        self.assertEqual(explore.build_seed(given, 48), given)

    def test_rejects_non_hex_seed(self):
        with self.assertRaises(ValueError):
            explore.build_seed("not-hex-zz", 48)

    def test_prompt_forbids_color_only_variation(self):
        prompt = explore.build_prompt("ab" * 48, "一个作品集首页", 3)
        for needle in (
            "构图骨架", "信息组织", "字体类别", "交互隐喻",
            "只换主色", "不要实现页面", "种子不要出现在任何产物里",
            "一眼假", "focus-visible", "reduced-motion",
        ):
            with self.subTest(needle=needle):
                self.assertIn(needle, prompt)

    def test_cli_runs_and_json_is_parseable(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPTS / "explore.py"), "--json", "--task", "测试"],
            cwd=ROOT, capture_output=True, text=True, check=True,
        )
        import json
        payload = json.loads(result.stdout)
        self.assertEqual(payload["task"], "测试")
        self.assertTrue(payload["ephemeral"])
        self.assertEqual(payload["source"], "secrets.token_hex (external)")
        self.assertEqual(len(payload["axes"]), 4)

    def test_cli_rejects_invalid_count(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPTS / "explore.py"), "--count", "1"],
            cwd=ROOT, capture_output=True, text=True,
        )
        self.assertNotEqual(result.returncode, 0)


class WorkflowDocTests(unittest.TestCase):
    def test_new_docs_exist(self):
        for relative in (
            "docs/EXPLORING.md", "docs/REVIEW.md",
            "references/ai-design-workflow/NOTES.md",
        ):
            with self.subTest(relative=relative):
                self.assertTrue((ROOT / relative).is_file(), relative)

    def test_review_keeps_score_out_of_lint(self):
        text = (ROOT / "docs" / "REVIEW.md").read_text(encoding="utf-8")
        for needle in (
            "只给四样东西", "绝对不给", "最多两轮", "不进 `lint.py`",
            "审美评价", "功能验证", "降级",
        ):
            with self.subTest(needle=needle):
                self.assertIn(needle, text)

    def test_layer5_has_media_discipline(self):
        text = (ROOT / "LAYERS.md").read_text(encoding="utf-8")
        for needle in ("删除测试", "不可替代性", "降级齐备", "不让生图模型画字"):
            with self.subTest(needle=needle):
                self.assertIn(needle, text)

    def test_skill_wires_both_workflows(self):
        text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        for needle in ("docs/EXPLORING.md", "docs/REVIEW.md", "六个动作", "2.2.0"):
            with self.subTest(needle=needle):
                self.assertIn(needle, text)

    def test_notes_records_rejections(self):
        text = (ROOT / "references/ai-design-workflow/NOTES.md").read_text(encoding="utf-8")
        for needle in ("## 弃", "9/10", "随机种子写进", "没有验证网页设计质量"):
            with self.subTest(needle=needle):
                self.assertIn(needle, text)


if __name__ == "__main__":
    unittest.main()
