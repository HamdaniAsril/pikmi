from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import check  # noqa: E402

CHECK_PY = Path(__file__).resolve().parent / "check.py"

ROUTER = """---
name: pikmi
description: Pick a visual style.
---

# pikmi
"""

CATALOG = {
    "version": 1,
    "styles": [
        {
            "id": "demo",
            "name": "Demo",
            "summary": "A demo style.",
            "keywords": {"en": ["demo"], "id": ["contoh"]},
            "media": ["ui", "slides"],
            "themes": ["light", "dark"],
            "preview": "styles/demo/preview.html",
            "brand_terms": ["eva"],
        }
    ],
}

TOKENS_CSS = """/* pikmi: demo */
/* Demo. Fonts: https://fonts.googleapis.com/css2?family=Archivo */
:root {
  --font-body: "Archivo", system-ui, sans-serif;
  --radius-key: 4px;
  --signal: #ff0000;
  --lift: 0 2px 0;
  --page: #ffffff;
  --panel: #f2f2f2;
  --card: #ffffff;
  --rule: #cccccc;
  --text: #000000;
  --text-muted: #444444;
  --accent: #0000ff;
  --on-accent: #ffffff;
  --link: #0000ff;
  --danger: #b00020;
}

[data-theme="dark"] {
  --page: #000000;
  --text: #ffffff;
}
"""

LIGHT = {
    "page": "#FFFFFF", "panel": "#F2F2F2", "card": "#FFFFFF", "rule": "#CCCCCC",
    "text": "#000000", "text-muted": "#444444", "accent": "#0000FF",
    "on-accent": "#FFFFFF", "link": "#0000FF", "danger": "#B00020",
}

TOKENS_JSON = {
    "name": "demo",
    "title": "Demo",
    "fonts": {"body": {"family": "Archivo", "weights": [400]}},
    "radius": {"key": 4},
    "colors": {"signal": "#FF0000"},
    "effects": {"lift": "0 2px 0"},
    "themes": {"light": LIGHT, "dark": {**LIGHT, "page": "#000000", "text": "#FFFFFF"}},
}

STYLE_MD = """# Demo

## Identity

A demo.

Dial: ENERGY 1 / RHYTHM 1 / MOTION 1

## Visual vocabulary

Plain.

## Reasons

- Color: contrast.

## Token usage

Roles.

## Components

None.

## Recipes

### UI

Use it.

### Slides

Use it big.

## Outside CSS

Nothing special.

## Contrast rules (checked)

| Text | On | Theme | Ratio | Rule |
| --- | --- | --- | --- | --- |
| `--text` | `--page` | light | 21.00 | Body text. |
| `--text` | `--page` | light | 21.00 | Focus ring on the page. |
| `--text` | `--page` | dark | 21.00 | Focus ring on the dark page. |
| `--text-muted` | `--card` | light | 9.74 | Field border on cards. |
| `--text-muted` | `--card` | dark | 9.74 | Field border on dark cards. |

## Pitfalls

None.

## Checklist

- [ ] Done.
"""

PREVIEW = """<!doctype html>
<html lang="en">
<head>
<link rel="stylesheet" href="tokens.css">
</head>
<body>
<section id="components"></section>
<section id="ui"></section>
<section id="slides"></section>
</body>
</html>
"""


def make_repo(tmp: Path) -> Path:
    root = tmp / "repo"
    skill = root / "skills" / "pikmi"
    (skill / "foundations").mkdir(parents=True)
    (skill / "SKILL.md").write_text(ROUTER)
    for medium in ("ui", "slides", "social", "app"):
        (skill / "foundations" / f"{medium}.md").write_text(f"# {medium}\n")
    (skill / "catalog.json").write_text(json.dumps(CATALOG, indent=2))
    style = skill / "styles" / "demo"
    style.mkdir(parents=True)
    (style / "tokens.css").write_text(TOKENS_CSS)
    (style / "tokens.json").write_text(json.dumps(TOKENS_JSON, indent=2))
    (style / "STYLE.md").write_text(STYLE_MD)
    (style / "preview.html").write_text(PREVIEW)
    return root


def style_dir(root: Path) -> Path:
    return root / "skills" / "pikmi" / "styles" / "demo"


def edit(path: Path, old: str, new: str) -> None:
    text = path.read_text()
    assert old in text, f"fixture does not contain {old!r}"
    path.write_text(text.replace(old, new, 1))


def edit_json(path: Path, mutate) -> None:
    data = json.loads(path.read_text())
    mutate(data)
    path.write_text(json.dumps(data, indent=2))


class CheckRepoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = Path(tempfile.mkdtemp())
        self.root = make_repo(self.tmp)
        self.style = style_dir(self.root)
        self.skill = self.root / "skills" / "pikmi"

    def tearDown(self) -> None:
        shutil.rmtree(self.tmp)

    def assertError(self, fragment: str) -> None:
        errors = check.check_repo(self.root)
        self.assertTrue(
            any(fragment in e for e in errors),
            f"expected an error containing {fragment!r}, got {errors!r}",
        )

    def test_valid_repo_passes(self) -> None:
        self.assertEqual(check.check_repo(self.root), [])

    def test_missing_style_folder(self) -> None:
        shutil.rmtree(self.style)
        self.assertError("demo: missing folder")

    def test_orphan_style_folder(self) -> None:
        (self.skill / "styles" / "ghost").mkdir()
        self.assertError("ghost: folder has no catalog entry")

    def test_skill_md_inside_styles(self) -> None:
        (self.style / "SKILL.md").write_text("---\nname: demo\n---\n")
        self.assertError("SKILL.md not allowed")

    def test_css_json_mismatch(self) -> None:
        edit_json(self.style / "tokens.json", lambda d: d["themes"]["light"].update(accent="#00FF00"))
        self.assertError("demo: --accent (light)")

    def test_dark_override_parity(self) -> None:
        edit(self.style / "tokens.css", "  --text: #ffffff;", "  --text: #eeeeee;")
        self.assertError("demo: --text (dark)")

    def test_px_group(self) -> None:
        edit_json(self.style / "tokens.json", lambda d: d["radius"].update(key=5))
        self.assertError("demo: --radius-key")

    def test_tokens_marker(self) -> None:
        edit(self.style / "tokens.css", "/* pikmi: demo */\n", "")
        self.assertError("demo: tokens.css must start with /* pikmi: demo */")

    def test_missing_theme_block(self) -> None:
        css = self.style / "tokens.css"
        css.write_text(css.read_text().split('[data-theme="dark"]')[0])
        self.assertError("demo: theme 'dark' missing in tokens.css")

    def test_contrast_claim_wrong(self) -> None:
        edit(self.style / "STYLE.md", "| light | 21.00 |", "| light | 9.99 |")
        self.assertError("demo: contrast --text on --page (light) is 21.00, STYLE.md says 9.99")

    def test_contrast_translucent(self) -> None:
        self.assertEqual(round(check.contrast_ratio("rgba(255,255,255,0.6)", "#0B1322"), 2), 7.14)

    def test_brand_term_word_boundary(self) -> None:
        edit(self.style / "STYLE.md", "A demo.", "A demo to evaluate.")
        self.assertFalse(any("brand term" in e for e in check.check_repo(self.root)))
        edit(self.style / "STYLE.md", "to evaluate.", "like an EVA unit.")
        self.assertError("demo: brand term 'eva'")

    def test_em_dash(self) -> None:
        edit(self.style / "preview.html", '<section id="ui"></section>', '<section id="ui">a — b</section>')
        self.assertError("demo: em dash in preview.html")

    def test_missing_dial(self) -> None:
        edit(self.style / "STYLE.md", "Dial: ENERGY 1 / RHYTHM 1 / MOTION 1\n", "")
        self.assertError("demo: Dial line")

    def test_missing_section(self) -> None:
        edit(self.style / "STYLE.md", "## Outside CSS\n", "")
        self.assertError("demo: missing section 'Outside CSS'")

    def test_missing_medium_recipe(self) -> None:
        edit(self.style / "STYLE.md", "### Slides\n", "")
        self.assertError("demo: missing recipe 'Slides'")

    def test_preview_missing_medium_id(self) -> None:
        edit(self.style / "preview.html", ' id="slides"', "")
        self.assertError('demo: preview.html missing id="slides"')

    def test_preview_missing_tokens_link(self) -> None:
        edit(self.style / "preview.html", '<link rel="stylesheet" href="tokens.css">\n', "")
        self.assertError("demo: preview.html must link tokens.css")

    def test_catalog_bad_medium(self) -> None:
        edit_json(self.skill / "catalog.json", lambda d: d["styles"][0].update(media=["print"]))
        self.assertError("demo: unknown medium 'print'")

    def test_router_too_long(self) -> None:
        lines = ROUTER.splitlines()
        lines += ["filler"] * (150 - len(lines))
        (self.skill / "SKILL.md").write_text("\n".join(lines) + "\n")
        self.assertError("SKILL.md has 150 lines (limit 149)")

    def test_description_too_long(self) -> None:
        (self.skill / "SKILL.md").write_text(ROUTER.replace("Pick a visual style.", "x" * 1025))
        self.assertError("description is 1025 characters (limit 1024)")

    def test_ratio_cell_not_a_number(self) -> None:
        edit(self.style / "STYLE.md", "| light | 21.00 | Body text. |", "| light | 21:1 | Body text. |")
        self.assertError("demo: contrast ratio '21:1' is not a number")

    def test_focus_row_required(self) -> None:
        edit(self.style / "STYLE.md", "| `--text` | `--page` | light | 21.00 | Focus ring on the page. |\n", "")
        self.assertError("demo: contrast table needs a 'Focus ring' row for theme 'light'")

    def test_focus_row_below_three(self) -> None:
        edit(self.style / "STYLE.md", "| `--text` | `--page` | light | 21.00 | Focus ring on the page. |",
             "| `--rule` | `--card` | light | 1.61 | Focus ring on the page. |")
        self.assertError("demo: Focus ring row --rule on --card (light) is 1.61, below 3.0")

    def test_field_border_row_required(self) -> None:
        edit(self.style / "STYLE.md", "| `--text-muted` | `--card` | dark | 9.74 | Field border on dark cards. |\n", "")
        self.assertError("demo: contrast table needs a 'Field border' row for theme 'dark'")

    def test_tap_target_too_small(self) -> None:
        edit(self.style / "preview.html", "</head>", "<style>.btn { min-height: 40px; }</style>\n</head>")
        self.assertError("demo: .btn min-height 40px is below 44px in preview.html")

    def test_tap_target_ignores_scaled_canvas(self) -> None:
        edit(self.style / "preview.html", "</head>",
             "<style>.slide .key { min-height: 0; } .post .btn { min-height: 20px; }</style>\n</head>")
        self.assertFalse(any("min-height" in e for e in check.check_repo(self.root)))

    def test_cli_ok(self) -> None:
        result = subprocess.run(
            [sys.executable, str(CHECK_PY), str(self.root)],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(result.stdout.strip(), "OK: 1 styles checked")


if __name__ == "__main__":
    unittest.main()
