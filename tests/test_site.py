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

    def test_theme_uses_green_palette(self):
        expected = {
            "--brand": "#15803D",
            "--brand-dark": "#166534",
            "--brand-soft": "#DCFCE7",
            "--brand-ink": "#14532D",
            "--line": "#BBF7D0",
            "--canvas": "#F0FDF4",
        }
        for token, color in expected.items():
            with self.subTest(token=token):
                self.assertRegex(CSS, rf"{re.escape(token)}:\s*{color};")

    def test_page_has_accessible_structure(self):
        self.assertIn("<nav", HTML)
        self.assertIn("<main", HTML)
        self.assertIn("<h1", HTML)
        self.assertIn("<footer", HTML)


if __name__ == "__main__":
    unittest.main()
