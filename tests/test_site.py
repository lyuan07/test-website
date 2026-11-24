import hashlib
import re
import struct
from html.parser import HTMLParser
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

    def test_header_describes_high_performing_teams(self):
        self.assertIn(
            '<div class="eyebrow"><span></span> Built for high-performing teams</div>',
            HTML,
        )

    def test_header_paragraph_describes_apex_solutions(self):
        self.assertIn(
            "<p>Apex Solutions gives growing teams one place to plan customer work, "
            "automate the busywork, and keep every promise.</p>",
            HTML,
        )

    def test_header_displays_supplied_image(self):
        class ImageParser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.images = []

            def handle_starttag(self, tag, attrs):
                if tag == "img":
                    self.images.append(dict(attrs))

        hero = re.search(r'<section class="hero shell">(.*?)</section>', HTML, re.S)
        self.assertIsNotNone(hero)
        parser = ImageParser()
        parser.feed(hero.group(1))
        self.assertEqual(len(parser.images), 1)
        image = parser.images[0]
        self.assertEqual(image.get("src"), "images/header.png")
        self.assertIn("alt", image)
        data = (ROOT / "site" / image["src"]).read_bytes()
        self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")
        width, height = struct.unpack(">II", data[16:24])
        self.assertEqual((image.get("width"), image.get("height")),
                         (str(width), str(height)))
        self.assertEqual(hashlib.sha256(data).hexdigest(),
                         "044bad4db856c52420a1625c97985abc4512177278854ef3420ca2915577082e")

    def test_header_image_preserves_responsive_aspect_ratio(self):
        rule = re.search(r"\.hero-image\s*\{([^}]+)\}", CSS)
        self.assertIsNotNone(rule)
        self.assertRegex(rule.group(1), r"(?:^|;)\s*width:\s*100%;")
        self.assertRegex(rule.group(1), r"(?:^|;)\s*height:\s*auto;")

    def test_page_has_accessible_structure(self):
        self.assertIn("<nav", HTML)
        self.assertIn("<main", HTML)
        self.assertIn("<h1", HTML)
        self.assertIn("<footer", HTML)


if __name__ == "__main__":
    unittest.main()
