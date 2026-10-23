#!/usr/bin/env python3
"""Check the pikmi skill: catalog, style folders, token parity, contrast claims and copy rules.

Usage: python3 scripts/check.py [repo_root]
"""
from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

MEDIA = {"ui": "UI", "slides": "Slides", "social": "Social", "app": "App"}
THEMES = ("light", "dark")
ROLES = ("page", "panel", "card", "rule", "text", "text-muted", "accent", "on-accent", "link", "danger")
SECTIONS = (
    "Identity", "Visual vocabulary", "Reasons", "Token usage", "Components",
    "Recipes", "Outside CSS", "Contrast rules (checked)", "Pitfalls", "Checklist",
)
STYLE_FILES = ("STYLE.md", "tokens.css", "tokens.json", "preview.html")
BRAND_FILES = ("STYLE.md", "preview.html", "tokens.css", "tokens.json")
EM_DASH_STYLE_FILES = ("STYLE.md", "preview.html")
ROUTER_LINE_LIMIT = 149
DESCRIPTION_LIMIT = 1024
EM_DASH = "—"

PX_GROUPS = {"typeScale": "type-", "tracking": "tracking-", "radius": "radius-", "space": "space-"}
BARE_GROUPS = ("colors", "effects")

ID_RE = re.compile(r"^[a-z0-9-]+$")
DIAL_RE = re.compile(r"^Dial: ENERGY [123] / RHYTHM [123] / MOTION [123]\s*$", re.M)
COMMENT_RE = re.compile(r"/\*.*?\*/", re.S)
BLOCK_RE = re.compile(r"([^{}]+)\{([^{}]*)\}")
DECL_RE = re.compile(r"(--[\w-]+)\s*:\s*([^;]+);")
THEME_SELECTOR_RE = re.compile(r"""^\[data-theme=["']([\w-]+)["']\]$""")
HEX_RE = re.compile(r"^#([0-9a-f]{3,4}|[0-9a-f]{6}|[0-9a-f]{8})$", re.I)
RGB_RE = re.compile(r"^rgba?\(\s*([\d.]+)[\s,]+([\d.]+)[\s,]+([\d.]+)(?:[\s,/]+([\d.]+%?))?\s*\)$", re.I)


@dataclass
class ContrastRow:
    text: str
    on: str
    theme: str
    ratio: float


def norm(value: str) -> str:
    return re.sub(r"\s+", " ", str(value)).strip().lower()


def parse_css_blocks(css: str) -> dict[str, dict[str, str]]:
    blocks: dict[str, dict[str, str]] = {}
    for selector, body in BLOCK_RE.findall(COMMENT_RE.sub("", css)):
        selector = selector.strip()
        if selector == ":root":
            key = "root"
        else:
            match = THEME_SELECTOR_RE.match(selector)
            if not match:
                continue
            key = match.group(1)
        blocks.setdefault(key, {}).update({name: value.strip() for name, value in DECL_RE.findall(body)})
    return blocks


def expected_css_vars(tokens: dict, themes: list[str]) -> tuple[dict[str, str], dict[str, dict[str, str]]]:
    base: dict[str, str] = {}
    for role, font in tokens.get("fonts", {}).items():
        base[f"--font-{role}"] = f'"{font["family"]}"'
    for group, prefix in PX_GROUPS.items():
        for key, value in tokens.get(group, {}).items():
            base[f"--{prefix}{key}"] = f"{value}px" if isinstance(value, (int, float)) else str(value)
    for group in BARE_GROUPS:
        for key, value in tokens.get(group, {}).items():
            base[f"--{key}"] = str(value)
    theme_roles = {
        theme: {f"--{role}": str(value) for role, value in tokens["themes"][theme].items()}
        for theme in themes
        if theme in tokens.get("themes", {})
    }
    return base, theme_roles


def parse_color(value: str) -> tuple[float, float, float, float] | None:
    value = value.strip()
    match = HEX_RE.match(value)
    if match:
        digits = match.group(1)
        if len(digits) in (3, 4):
            digits = "".join(ch * 2 for ch in digits)
        r, g, b = (int(digits[i:i + 2], 16) for i in (0, 2, 4))
        a = int(digits[6:8], 16) / 255 if len(digits) == 8 else 1.0
        return float(r), float(g), float(b), a
    match = RGB_RE.match(value)
    if match:
        r, g, b = (float(match.group(i)) for i in (1, 2, 3))
        alpha = match.group(4)
        if alpha is None:
            a = 1.0
        elif alpha.endswith("%"):
            a = float(alpha[:-1]) / 100
        else:
            a = float(alpha)
        return r, g, b, a
    return None


def _over(top: tuple[float, float, float, float], bottom: tuple[float, float, float, float]) -> tuple[float, float, float, float]:
    a = top[3]
    return tuple(top[i] * a + bottom[i] * (1 - a) for i in range(3)) + (1.0,)


def _luminance(color: tuple[float, float, float, float]) -> float:
    def channel(c: float) -> float:
        c /= 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = (channel(c) for c in color[:3])
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(text: str, on: str, under: str | None = None) -> float:
    fg, bg = parse_color(text), parse_color(on)
    if fg is None or bg is None:
        raise ValueError(f"not a color: {text if fg is None else on}")
    if bg[3] < 1:
        base = parse_color(under) if under else None
        bg = _over(bg, base or (255.0, 255.0, 255.0, 1.0))
    if fg[3] < 1:
        fg = _over(fg, bg)
    light, dark = sorted((_luminance(fg), _luminance(bg)), reverse=True)
    return (light + 0.05) / (dark + 0.05)


def _section(md: str, title: str) -> str | None:
    match = re.search(rf"^## {re.escape(title)}\s*$", md, re.M)
    if not match:
        return None
    rest = md[match.end():]
    end = re.search(r"^## ", rest, re.M)
    return rest[:end.start()] if end else rest


def parse_contrast_table(style_md: str) -> list[ContrastRow]:
    section = _section(style_md, "Contrast rules (checked)") or ""
    rows = []
    for line in section.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [cell.strip().strip("`").strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        try:
            ratio = float(cells[3])
        except ValueError:
            continue
        rows.append(ContrastRow(text=cells[0], on=cells[1], theme=cells[2], ratio=ratio))
    return rows


def _read_frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep:
            fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields


def _check_tokens(sid: str, style: Path, themes: list[str]) -> list[str]:
    errors = []
    css = (style / "tokens.css").read_text()
    marker = f"/* pikmi: {sid} */"
    if css.splitlines()[:1] != [marker]:
        errors.append(f"{sid}: tokens.css must start with {marker}")
    try:
        tokens = json.loads((style / "tokens.json").read_text())
    except json.JSONDecodeError as exc:
        return errors + [f"{sid}: tokens.json is not valid JSON ({exc})"]

    blocks = parse_css_blocks(css)
    root = blocks.get("root", {})
    base, theme_roles = expected_css_vars(tokens, themes)

    for var, want in base.items():
        have = root.get(var)
        if have is None:
            errors.append(f"{sid}: {var} missing in tokens.css")
        elif var.startswith("--font-"):
            if not norm(have).startswith(norm(want)):
                errors.append(f"{sid}: {var} is {have} in tokens.css but family {want} in tokens.json")
        elif norm(have) != norm(want):
            errors.append(f"{sid}: {var} is {have} in tokens.css but {want} in tokens.json")

    for name in tokens.get("themes", {}):
        if name not in themes:
            errors.append(f"{sid}: tokens.json has theme '{name}' not listed in catalog")
    for name in blocks:
        if name != "root" and name not in themes:
            errors.append(f"{sid}: tokens.css has theme '{name}' not listed in catalog")

    default = themes[0] if themes else None
    for theme in themes:
        roles = theme_roles.get(theme)
        if roles is None:
            errors.append(f"{sid}: theme '{theme}' missing in tokens.json")
            continue
        for role in ROLES:
            if f"--{role}" not in roles:
                errors.append(f"{sid}: theme '{theme}' lacks role '{role}'")
        if theme == default:
            block = {}
        elif theme in blocks:
            block = blocks[theme]
        else:
            errors.append(f"{sid}: theme '{theme}' missing in tokens.css")
            continue
        for var, want in roles.items():
            have = block.get(var, root.get(var))
            if have is None:
                errors.append(f"{sid}: {var} ({theme}) missing in tokens.css")
            elif norm(have) != norm(want):
                errors.append(f"{sid}: {var} ({theme}) is {have} in tokens.css but {want} in tokens.json")
        for var in block:
            if var not in roles:
                errors.append(f"{sid}: {var} in tokens.css theme '{theme}' has no value in tokens.json")

    known_root = set(base) | set(theme_roles.get(default, {}))
    for var in root:
        if var not in known_root:
            errors.append(f"{sid}: {var} in tokens.css has no value in tokens.json")

    return errors + _check_contrast(sid, style, tokens, themes)


def _resolve(cell: str, theme: str, tokens: dict) -> str | None:
    if not cell.startswith("--"):
        return cell
    name = cell[2:]
    return tokens.get("themes", {}).get(theme, {}).get(name) or tokens.get("colors", {}).get(name)


def _check_contrast(sid: str, style: Path, tokens: dict, themes: list[str]) -> list[str]:
    errors = []
    for row in parse_contrast_table((style / "STYLE.md").read_text()):
        if row.theme not in themes:
            errors.append(f"{sid}: contrast row uses theme '{row.theme}' not listed in catalog")
            continue
        text, on = _resolve(row.text, row.theme, tokens), _resolve(row.on, row.theme, tokens)
        page = tokens.get("themes", {}).get(row.theme, {}).get("page")
        if text is None or on is None:
            missing = row.text if text is None else row.on
            errors.append(f"{sid}: contrast token {missing} unknown in theme '{row.theme}'")
            continue
        try:
            actual = round(contrast_ratio(text, on, page), 2)
        except ValueError as exc:
            errors.append(f"{sid}: contrast {row.text} on {row.on} ({row.theme}): {exc}")
            continue
        if abs(actual - row.ratio) > 0.01 + 1e-9:
            errors.append(
                f"{sid}: contrast {row.text} on {row.on} ({row.theme}) is {actual:.2f}, STYLE.md says {row.ratio:.2f}"
            )
    return errors


def _check_style_md(sid: str, style: Path, media: list[str]) -> list[str]:
    errors = []
    md = (style / "STYLE.md").read_text()
    for title in SECTIONS:
        if _section(md, title) is None:
            errors.append(f"{sid}: missing section '{title}'")
    if not DIAL_RE.search(md):
        errors.append(f"{sid}: Dial line missing or malformed (Dial: ENERGY n / RHYTHM n / MOTION n)")
    recipes = _section(md, "Recipes") or ""
    for medium in media:
        heading = MEDIA.get(medium)
        if heading and not re.search(rf"^### {heading}\s*$", recipes, re.M):
            errors.append(f"{sid}: missing recipe '{heading}'")
    return errors


def _check_preview(sid: str, style: Path, media: list[str]) -> list[str]:
    errors = []
    html = (style / "preview.html").read_text()
    if not re.search(r"""href=["']tokens\.css["']""", html):
        errors.append(f"{sid}: preview.html must link tokens.css")
    for element in ["components"] + [m for m in media if m in MEDIA]:
        if not re.search(rf"""id=["']{element}["']""", html):
            errors.append(f'{sid}: preview.html missing id="{element}"')
    return errors


def _check_copy(sid: str, style: Path, brand_terms: list[str]) -> list[str]:
    errors = []
    for name in BRAND_FILES:
        text = (style / name).read_text()
        for term in brand_terms:
            if re.search(rf"(?<![\w]){re.escape(term)}(?![\w])", text, re.I):
                errors.append(f"{sid}: brand term '{term}' in {name}")
    for name in EM_DASH_STYLE_FILES:
        if EM_DASH in (style / name).read_text():
            errors.append(f"{sid}: em dash in {name}")
    return errors


def _check_entry(entry: dict) -> list[str]:
    sid = entry.get("id", "?")
    errors = []
    if not isinstance(sid, str) or not ID_RE.match(sid):
        errors.append(f"{sid}: id must match {ID_RE.pattern}")
    for field in ("name", "summary"):
        if not entry.get(field):
            errors.append(f"{sid}: catalog field '{field}' is empty")
    keywords = entry.get("keywords", {})
    for lang in ("en", "id"):
        if not keywords.get(lang):
            errors.append(f"{sid}: keywords.{lang} is empty")
    media = entry.get("media") or []
    if not media:
        errors.append(f"{sid}: media is empty")
    for medium in media:
        if medium not in MEDIA:
            errors.append(f"{sid}: unknown medium '{medium}'")
    themes = entry.get("themes") or []
    if not themes or len(set(themes)) != len(themes):
        errors.append(f"{sid}: themes must be a non-empty list without duplicates")
    for theme in themes:
        if theme not in THEMES:
            errors.append(f"{sid}: unknown theme '{theme}'")
    if entry.get("preview") != f"styles/{sid}/preview.html":
        errors.append(f"{sid}: preview must be styles/{sid}/preview.html")
    if not isinstance(entry.get("brand_terms"), list):
        errors.append(f"{sid}: brand_terms must be a list")
    return errors


def check_style(root: Path, entry: dict) -> list[str]:
    sid = entry["id"]
    style = root / "skills" / "pikmi" / "styles" / sid
    if not style.is_dir():
        return [f"{sid}: missing folder styles/{sid}"]
    missing = [name for name in STYLE_FILES if not (style / name).is_file()]
    if missing:
        return [f"{sid}: missing {name}" for name in missing]
    media = entry.get("media") or []
    themes = [t for t in entry.get("themes") or [] if t in THEMES]
    return (
        _check_tokens(sid, style, themes)
        + _check_style_md(sid, style, media)
        + _check_preview(sid, style, media)
        + _check_copy(sid, style, entry.get("brand_terms") or [])
    )


def _check_router(skill: Path) -> list[str]:
    router = skill / "SKILL.md"
    if not router.is_file():
        return ["skills/pikmi/SKILL.md missing"]
    errors = []
    text = router.read_text()
    lines = len(text.splitlines())
    if lines > ROUTER_LINE_LIMIT:
        errors.append(f"SKILL.md has {lines} lines (limit {ROUTER_LINE_LIMIT})")
    fields = _read_frontmatter(text)
    if fields.get("name") != "pikmi":
        errors.append("SKILL.md frontmatter name must be pikmi")
    description = fields.get("description", "")
    if not description:
        errors.append("SKILL.md frontmatter description is missing")
    elif len(description) > DESCRIPTION_LIMIT:
        errors.append(f"description is {len(description)} characters (limit {DESCRIPTION_LIMIT})")
    return errors


def _load_catalog(skill: Path) -> dict | None:
    path = skill / "catalog.json"
    if not path.is_file():
        return None
    return json.loads(path.read_text())


def check_repo(root: Path) -> list[str]:
    skill = root / "skills" / "pikmi"
    errors = _check_router(skill)
    for medium in MEDIA:
        if not (skill / "foundations" / f"{medium}.md").is_file():
            errors.append(f"foundations/{medium}.md missing")

    shared_copy = [skill / "SKILL.md", skill / "catalog.json", *sorted((skill / "foundations").glob("*.md"))]
    for path in shared_copy:
        if path.is_file() and EM_DASH in path.read_text():
            errors.append(f"{path.relative_to(skill)}: em dash")

    try:
        catalog = _load_catalog(skill)
    except json.JSONDecodeError as exc:
        return errors + [f"catalog.json is not valid JSON ({exc})"]
    if catalog is None:
        return errors + ["skills/pikmi/catalog.json missing"]

    entries = catalog.get("styles", [])
    ids = [entry.get("id") for entry in entries]
    for sid in sorted({i for i in ids if ids.count(i) > 1}):
        errors.append(f"{sid}: duplicate catalog id")
    for entry in entries:
        errors += _check_entry(entry)
        if isinstance(entry.get("id"), str):
            errors += check_style(root, entry)

    styles_dir = skill / "styles"
    if styles_dir.is_dir():
        for folder in sorted(p for p in styles_dir.iterdir() if p.is_dir()):
            if folder.name not in ids:
                errors.append(f"{folder.name}: folder has no catalog entry")
        for stray in sorted(styles_dir.rglob("SKILL.md")):
            errors.append(f"{stray.relative_to(skill)}: SKILL.md not allowed inside styles/")
    return errors


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    root = Path(argv[0]) if argv else Path(__file__).resolve().parent.parent
    errors = check_repo(root)
    if errors:
        for error in errors:
            print(error)
        return 1
    catalog = _load_catalog(root / "skills" / "pikmi") or {}
    print(f"OK: {len(catalog.get('styles', []))} styles checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
