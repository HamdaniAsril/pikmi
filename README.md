# pikmi

**Not like other UIs.**

pikmi (read it as "pick me") is an agent skill that picks and applies a visual design style for web UI,
slides, social media posts and apps. Tell your agent the mood you want ("make it modern industrial",
"bikin kayak poster punk", "calm and airy"), and pikmi offers two to four matching styles with previews.
You pick one, and the agent builds with only that style loaded.

## Install

In Claude Code:

```
/plugin marketplace add HamdaniAsril/pikmi
/plugin install pikmi@pikmi
```

The repository is private for now, so installing needs a GitHub account with access to it.

## How it works

1. You ask for a new design, or ask to change how something looks.
2. pikmi reads its catalog and matches your mood words, in English or Indonesian.
3. It offers two to four styles, each with a one-line reason and a preview page.
4. You pick one (or say "terserah" and it recommends one).
5. The agent loads that style's rules and tokens plus the rules for your medium, builds, and checks the
   result against the style's checklist.

pikmi stays quiet when a project already has its own look and you are only adding or fixing a part of
it. Web projects built with a pikmi style carry a marker (`/* pikmi: <id> */`) at the top of their
`tokens.css`, so later sessions continue the same style.

## Styles

| Style | What it looks like | Themes |
| --- | --- | --- |
| [Instrument Panel](skills/pikmi/styles/instrument-panel/preview.html) | Grey hardware panels, numbered keys, a small black screen and one signal orange: a pocket synthesizer turned into an interface. | light, dark |
| [Cyberpunk Neon](skills/pikmi/styles/cyberpunk-neon/preview.html) | Near-black night surfaces, cyan and magenta neon, hard thin strokes and HUD readouts; louder and more electric than Mecha. | dark |
| [Anti-Design](skills/pikmi/styles/anti-design/preview.html) | Loud neo-brutalism: thick black borders, hard offset shadows, clashing primary colors, square corners and type sizes that collide on purpose. | light |
| [Corporate Clean](skills/pikmi/styles/corporate-clean/preview.html) | Trustworthy enterprise UI with an identity: ledger hairlines, tabular numbers, ink-blue headings and one confident blue for actions. | light |
| [Pastoral Storybook](skills/pikmi/styles/pastoral-storybook/preview.html) | Warm cream paper, sage and sky, soft rounded shapes and gentle hand-drawn nature: the calm of an animated countryside film. | light |
| [Islamic Geometric](skills/pikmi/styles/islamic-geometric/preview.html) | Lapis blue, ivory and gold with eight-point star patterns used as frames and dividers, symmetrical and calm; ivory by day, deep blue by night. | light, dark |
| [Ukiyo-e Print](skills/pikmi/styles/ukiyo-e-print/preview.html) | Japanese woodblock print as an interface: indigo outlines on rice paper, flat color blocks, vermilion stamps, wave motifs and hard print shadows. | light |
| [Japanese Minimal](skills/pikmi/styles/japanese-minimal/preview.html) | Extreme whitespace, hairline rules, light-weight type and a single soft pastel: quiet, airy and unhurried, built on the idea of ma. | light |
| [Mecha](skills/pikmi/styles/mecha/preview.html) | Armored control panels in navy and military green, cut corners, hazard yellow and red, unit numbers in mono; heavier and more military than Cyberpunk Neon, with no glow. | dark |
| [Watercolor](skills/pikmi/styles/watercolor/preview.html) | Soft washes of peach, teal and rose bleeding into warm paper, blue-grey ink, italic serif headings and slow, painterly motion. | light |
| [Nocturne Glass](skills/pikmi/styles/nocturne-glass/preview.html) | A deep ink night scene with soft moonlit light wells, solid night-steel surfaces and one or two pieces of colorless frosted glass, lit by a single champagne accent. | dark |
| [Bento](skills/pikmi/styles/bento/preview.html) | A modular grid of widget-like cards in different sizes, sized by importance, on neutral zinc surfaces with soft tints and one tangerine accent. | light, dark |
| [Dark Dev](skills/pikmi/styles/dark-dev/preview.html) | Calm slate dark mode for developer tools: low-contrast layers, borders that light up on hover, one blue for actions and mono only for code. | dark |

Open any preview in a browser through a local server (for example `python3 -m http.server` from
`skills/pikmi`), so each page can load its `tokens.css`.

## Add a style

1. Add an entry to `skills/pikmi/catalog.json` (id, name, summary, keywords in English and Indonesian,
   media, themes, preview path, brand terms).
2. Create `skills/pikmi/styles/<id>/` with `STYLE.md`, `tokens.css`, `tokens.json` and `preview.html`.
   Follow an existing style for the section order and token names.
3. Run the checker until it passes:

```
python3 scripts/check.py
```

4. Open the preview at 1280px and 375px, check both themes, and add a row to `evals/prompts.md` for the
   new style's keywords.

The checker verifies the catalog against the folders, keeps `tokens.css` and `tokens.json` identical,
recomputes every contrast ratio claimed in `STYLE.md`, and blocks brand names and em dashes in the
style files. Its tests run with:

```
python3 -m unittest discover -s scripts -p 'test_*.py'
```

## Layout

```
.claude-plugin/          plugin and marketplace manifests
skills/pikmi/SKILL.md    the router skill (the only file that loads automatically)
skills/pikmi/catalog.json
skills/pikmi/foundations/  rules per medium: ui, slides, social, app
skills/pikmi/styles/<id>/  STYLE.md, tokens.css, tokens.json, preview.html
scripts/check.py         the repo checker
evals/prompts.md         router evals
docs/superpowers/        design spec and implementation plan
```
