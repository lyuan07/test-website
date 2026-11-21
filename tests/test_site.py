import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "site/index.html").read_text(encoding="utf-8")
CSS = (ROOT / "site/styles.css").read_text(encoding="utf-8")


class TestWebsiteTests(unittest.TestCase):
    def test_page_has_product_identity(self):
        self.assertIn("Test Website", HTML)
        self.assertNotIn("YuanFlow", HTML)
        self.assertIn('href="styles.css"', HTML)

    def test_theme_contract_is_complete(self):
        for token in ("--brand", "--brand-dark", "--brand-soft", "--brand-ink"):
            self.assertRegex(CSS, rf"{re.escape(token)}:\s*#[0-9A-Fa-f]{{6}};")

    def test_theme_uses_pink_palette(self):
        palette = {
            "--brand": "#BE185D",
            "--brand-dark": "#9D174D",
            "--brand-soft": "#FCE7F3",
            "--brand-ink": "#831843",
            "--line": "#FBCFE8",
            "--canvas": "#FFF1F7",
        }
        for token, color in palette.items():
            with self.subTest(token=token):
                self.assertRegex(CSS, rf"{re.escape(token)}:\s*{color};")

    def test_page_has_accessible_structure(self):
        self.assertIn("<nav", HTML)
        self.assertIn("<main", HTML)
        self.assertIn("<h1", HTML)
        self.assertIn("<footer", HTML)


if __name__ == "__main__":
    unittest.main()
