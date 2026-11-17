from __future__ import annotations

import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

spec = importlib.util.spec_from_file_location("designlib", ROOT / "scripts" / "designlib.py")
designlib = importlib.util.module_from_spec(spec)
assert spec and spec.loader
spec.loader.exec_module(designlib)


class DesignLibraryTests(unittest.TestCase):
    def test_library_has_expected_styles(self):
        rows = designlib.load_rows()
        self.assertGreaterEqual(len(rows), 17)
        slugs = {row["slug"] for row in rows}
        self.assertIn("liquid-glass", slugs)
        self.assertIn("codex-workbench", slugs)
        self.assertIn("signal-console", slugs)
        self.assertIn("incident-room", slugs)
        self.assertIn("developer-docs", slugs)
        self.assertIn("enterprise-data", slugs)
        self.assertIn("adaptive-companion", slugs)

    def test_every_style_has_three_artifacts(self):
        for row in designlib.load_rows():
            style_dir = ROOT / "styles" / row["slug"]
            for filename in ("DESIGN.md", "tokens.css", "prompt.md"):
                with self.subTest(slug=row["slug"], filename=filename):
                    self.assertTrue((style_dir / filename).is_file())

    def test_selection_fields_are_valid(self):
        valid_registers = {"story", "professional", "technical", "tool"}
        valid_surfaces = {"light", "dark", "mixed"}
        valid_densities = {"tight", "medium", "roomy"}
        valid_tiers = {"core", "variant", "technique"}
        for row in designlib.load_rows():
            with self.subTest(slug=row["slug"]):
                self.assertIn(row["register"], valid_registers)
                self.assertIn(row["surface"], valid_surfaces)
                self.assertIn(row["density"], valid_densities)
                self.assertIn(row["tier"], valid_tiers)
                self.assertTrue(row["family"])
                self.assertTrue(row["cues"])
                self.assertTrue(row["avoid"])

    def test_incident_recommendation_promotes_incident_room(self):
        rows = designlib.load_rows()
        best = max(
            rows,
            key=lambda row: designlib.score_style(
                row,
                "正在发生重大事故，需要值班交接和时间线",
            )[0],
        )
        self.assertEqual(best["slug"], "incident-room")

    def test_catalog_matches_generated_data(self):
        actual = [row["slug"] for row in designlib.load_rows()]
        payload = json.loads((ROOT / "styles" / "index.json").read_text(encoding="utf-8"))
        self.assertEqual([row["slug"] for row in payload["styles"]], actual)

        source = (ROOT / "catalog" / "data.js").read_text(encoding="utf-8").strip()
        prefix = "window.DESIGN_DATA = "
        self.assertTrue(source.startswith(prefix))
        self.assertTrue(source.endswith(";"))
        data = json.loads(source[len(prefix):-1])
        self.assertEqual([row["slug"] for row in data["styles"]], actual)


if __name__ == "__main__":
    unittest.main()

