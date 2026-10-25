# pikmi

**Not like other UIs.**

pikmi (read it as "pick me") is an agent skill that picks and applies a visual design style for web UI,
slides, social media posts and apps. Tell your agent the mood you want ("make it modern industrial",
"bikin kayak poster punk", "calm and airy"), and pikmi offers up to three matching styles with previews.
You pick one and the agent builds with only that style loaded, or you carry on without pikmi.

## Install

### Claude Code

```
/plugin marketplace add HamdaniAsril/pikmi
/plugin install pikmi@pikmi
```

### OpenCode and other agents

pikmi is a plain Agent Skills folder (`skills/pikmi/SKILL.md`), so any agent that reads `SKILL.md`
skills can use it. The [skills CLI](https://github.com/vercel-labs/skills) installs it for the agents
you name:

```
npx skills add HamdaniAsril/pikmi -g -a opencode
```

`-g` installs it for your user instead of the current project. Add one `-a` per agent
(`-a opencode -a codex`), or leave `-a` out and pick from a list.

To install by hand, copy or symlink `skills/pikmi` into the agent's skills folder. For OpenCode that is
`~/.config/opencode/skills/pikmi` for every project, or `.opencode/skills/pikmi` for one project.

Install pikmi in one place per agent. OpenCode also reads `~/.claude/skills/` and `~/.agents/skills/`,
and two copies of the same skill name clash. The Claude Code plugin lives under `~/.claude/plugins/`,
which OpenCode does not read, so an OpenCode install next to the plugin is fine.

Agents without a question tool that shows previews still offer the same choice, with each style's
palette and fonts card under its option.

## How it works

1. You ask for a new design, or ask to change how something looks.
2. pikmi reads its catalog and matches your mood words, in English or Indonesian.
3. It opens the preview pages and asks one question: up to three styles, each with a one-line reason
   and a card of its palette and fonts, plus "Continue without pikmi".
4. You pick one (or say "terserah" and it recommends one). If you continue without pikmi, it stays quiet
   for the rest of the conversation unless you name a style.
5. The agent loads that style's rules and tokens plus the rules for your medium, builds, and checks the
   result against the style's checklist.

pikmi stays quiet when a project already has its own look and you are only adding or fixing a part of
it. Web projects built with a pikmi style carry a marker (`/* pikmi: <id> */`) at the top of their
`tokens.css`, so later sessions continue the same style.

## Styles

| Style | What it looks like | Themes |
| --- | --- | --- |
| [Instrument Panel](skills/pikmi/styles/instrument-panel/preview.html) | Grey hardware panels, numbered keys, a small black screen and one signal orange: a pocket synthesizer turned into an interface. | light, dark |
| [Night Circuit](skills/pikmi/styles/night-circuit/preview.html) | Near-black night surfaces, cyan and magenta neon, hard thin strokes and HUD readouts; louder and more electric than Armor Plate. | dark |
| [Primary Riot](skills/pikmi/styles/primary-riot/preview.html) | Loud neo-brutalism: thick black borders, hard offset shadows, clashing primary colors, square corners and type sizes that collide on purpose. | light |
| [Ledger Blue](skills/pikmi/styles/ledger-blue/preview.html) | Trustworthy enterprise UI with an identity: ledger hairlines, tabular numbers, ink-blue headings and one confident blue for actions. | light |
| [Lapis Lattice](skills/pikmi/styles/lapis-lattice/preview.html) | Lapis blue, ivory and gold with eight-point star patterns used as frames and dividers, symmetrical and calm; ivory by day, deep blue by night. | light, dark |
| [Indigo Woodblock](skills/pikmi/styles/indigo-woodblock/preview.html) | Japanese woodblock print as an interface: indigo outlines on rice paper, flat color blocks, vermilion stamps, wave motifs and hard print shadows. | light |
| [Japanese Minimal](skills/pikmi/styles/japanese-minimal/preview.html) | Extreme whitespace, hairline rules, light-weight type and a single soft pastel: quiet, airy and unhurried, built on the idea of ma. | light |
| [Armor Plate](skills/pikmi/styles/armor-plate/preview.html) | Armored control panels in navy and military green, cut corners, hazard yellow and red, unit numbers in mono; heavier and more military than Night Circuit, with no glow. | dark |
| [Soft Wash](skills/pikmi/styles/soft-wash/preview.html) | Soft washes of peach, teal and rose bleeding into warm paper, blue-grey ink, italic serif headings and slow, painterly motion. | light |
| [Nocturne Glass](skills/pikmi/styles/nocturne-glass/preview.html) | A deep ink night scene with soft moonlit light wells, solid night-steel surfaces and one or two pieces of colorless frosted glass, lit by a single champagne accent. | dark |
| [Dark Dev](skills/pikmi/styles/dark-dev/preview.html) | Calm slate dark mode for developer tools: low-contrast layers, borders that light up on hover, one blue for actions and mono only for code. | dark |
| [Konbini Sky](skills/pikmi/styles/konbini-sky/preview.html) | Bright daytime sky over white paper, giant white grotesk type, cobalt captions and one pixel-art street scene on the horizon; bolder and sunnier than Japanese Minimal, with a lit-up night theme. | light, dark |

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

## License

[MIT](LICENSE)
