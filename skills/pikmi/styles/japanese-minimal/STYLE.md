# Japanese Minimal

## Identity

Design built from what is left out. Ma, the meaningful space between things, is the main element:
sections float in wide whitespace, rules are hairlines, type is light, and one soft pastel appears once
per page like a single flower in a room. Slight asymmetry and a single drawn branch keep it human rather
than sterile.

Fits wellness and meditation, tea, stationery and home goods, architecture and interior studios,
portfolios, editorial and personal sites. Avoid it for dense dashboards, sales-heavy pages, games, and
anything that needs urgency or many calls to action.

Light only.

Dial: ENERGY 1 / RHYTHM 2 / MOTION 1

## Visual vocabulary

- **Color.** Rice white `#FAFAF8`, a slightly deeper panel `#F4F4F1`, white cards. Text in slate
  `#4A5568`, secondary `#5F6E82`. Hairlines `#D4D4CF`. One pastel per page: sky `#64B5F6`, mint
  `#98D8C8`, sakura `#FFB7C5` or powder `#B8D4E3`. Pastels never carry text.
- **Space.** Sections are 128px apart (`--space-section`); inside a section, elements sit 32 to 64px
  apart. A page should feel half empty.
- **Lines.** 1px hairlines in `--rule` divide sections. Inputs use only a bottom line, in `--text-muted`
  so it stays visible.
- **Type.** M PLUS 1 at 200 for headings and 300 for body, never bold, never uppercase. Body text at 17px
  or larger so the thin weight stays readable.
- **Accents.** One line-drawn botanical (a branch, a leaf) per section, 1px stroke, off-center.
- **Shape.** Small radii: 6px controls, 8px cards. No shadows at all.

## Reasons

- **Color:** neutral surfaces let a single pastel feel deliberate; using it once per page keeps the calm.
- **Typography:** thin, even strokes echo the hairlines; avoiding bold keeps the voice soft and lets space
  create hierarchy instead.
- **Layout:** large gaps between sections are the identity of the style (ma); slight asymmetry keeps it
  from looking like an empty template.
- **Shape:** small radii feel gentle without becoming rounded or cute.
- **Depth:** no shadows; elements rest in space by position and hairlines alone.
- **Motion:** slow, small changes (500ms, at most 1px of movement) feel like breath, not interaction.
- **Theme:** the style is daylight and paper; a dark version would lose the emptiness it relies on.

## Token usage

| Token | Role |
| --- | --- |
| `--page`, `--panel`, `--card` | rice white, quiet bands, white cards |
| `--rule`, `--hairline` | 1px section dividers |
| `--text`, `--text-muted` | slate text and secondary text (also input lines) |
| `--accent`, `--on-accent` | the sky pastel for focus, fills and lines; dark text on its fills |
| `--mint`, `--sakura`, `--powder` | alternative pastels, one per page |
| `--link`, `--danger` | links and errors |
| `--space-section` | the 128px gap between sections |

## Components

```css
body { font: 300 17px/1.9 var(--font-body); color: var(--text); background: var(--page); }
h1, h2, h3 { font-weight: 200; letter-spacing: var(--tracking-heading); color: var(--text); }

.btn { min-height: 48px; padding: 0 var(--space-lg); border: 1px solid var(--text-muted); border-radius: var(--radius-control);
  background: transparent; color: var(--text); font: 400 16px/1 var(--font-body);
  transition: background-color 500ms ease-in-out, transform 500ms ease-in-out; }
.btn:hover { background: var(--panel); transform: translateY(-1px); }
.btn:active { opacity: 0.8; }
.btn.fill { background: var(--accent); border-color: var(--accent); color: var(--on-accent); }
.btn:focus-visible, .line-field input:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }

.section { padding-block: var(--space-section); border-top: var(--hairline); }
.card { background: var(--card); border: var(--hairline); border-radius: var(--radius-card); padding: var(--space-lg); }

.line-field { position: relative; padding-top: 20px; }
.line-field input { width: 100%; min-height: 44px; border: 0; border-bottom: 1px solid var(--text-muted); background: transparent;
  color: var(--text); font: 300 17px var(--font-body); }
.line-field label { position: absolute; top: 0; left: 0; font: 400 13px/1 var(--font-body); color: var(--text-muted); }

.branch { width: 120px; height: 80px; stroke: var(--text-muted); stroke-width: 1; fill: none; }
@media (prefers-reduced-motion: reduce) { .btn { transition: none; } }
```

The floating label stays visible above the field at all times; it never disappears into the line.

## Recipes

### UI

- **Landing page.** One sentence as the headline at 44 to 64px weight 200, set slightly left of center;
  one paragraph; one outline button. 128px of space, a hairline, then the next section: a single image
  with a caption, then three short items in a row with a branch drawing beside them.
- **Shop or portfolio.** A grid of white cards with hairline borders and generous gaps (32px); text below
  each image, never on top of it; the price or detail in `--text-muted`.

### Slides

- Rice-white slides, a single sentence at 64px weight 200, set at the golden ratio point, nothing else.
- Data slides: one number at 160px weight 200 with a hairline under it and a caption.
- One pastel shape or branch per slide, off-center.
- Fades of 600ms between slides, or none.

### Social

- 1080 x 1350: one short sentence at 64px weight 200 in the upper third, a large empty middle, a branch
  drawing and a small caption at 28px near the bottom.
- One pastel field, if any, behind the branch, never behind the text.

### App

- White screens, hairline-separated rows, 48pt rows with generous side padding.
- One outline primary button; filled sky only for the single most important action.
- Bottom-line inputs with visible labels; focus shows the sky outline.

## Outside CSS

| CSS effect | Replacement |
| --- | --- |
| `--hairline` | a 1pt line in `--rule`; on high-density screens 0.5pt |
| Hover lift | none on touch platforms |
| Floating label | a small label above the field, always visible |
| Branch SVG | a 1pt stroked vector drawing |

## Contrast rules (checked)

| Text | On | Theme | Ratio | Rule |
| --- | --- | --- | --- | --- |
| `--text` | `--page` | light | 7.20 | Body text, which is thin, so keep it at 17px or larger. |
| `--text-muted` | `--page` | light | 4.97 | Secondary text and input lines. |
| `--text-muted` | `--panel` | light | 4.72 | Secondary text on quiet bands. |
| `--on-accent` | `--accent` | light | 6.56 | Dark text on sky fills. |
| `--link` | `--page` | light | 5.07 | Links. |
| `--danger` | `--page` | light | 4.97 | Error text. |
| `--accent` | `--page` | light | 2.12 | The sky pastel never carries text on the page. |
| `--text` | `--powder` | light | 4.86 | Slate text can sit on a powder field if it must. |

## Pitfalls

- Filling the space. If a section feels empty, that is the style working.
- Bold or uppercase text, heavy borders, shadows, dark backgrounds.
- More than one pastel on a page, or pastel text.
- Hairline input lines in `--rule`; they fail non-text contrast. Use `--text-muted`.
- Thin text below 16px; weight 300 at small sizes turns grey and faint.
- Focus shown only by a faint line color change; use the visible sky outline.
- A perfectly centered, symmetrical template layout with no branch or asymmetry; it reads as sterile.

## Checklist

- [ ] Sections are about 128px apart and the page feels half empty.
- [ ] All type is M PLUS 1 at 200 to 400, never bold or uppercase, body at 17px or larger.
- [ ] Only hairlines divide content; there are no shadows.
- [ ] Exactly one pastel appears, and never as text.
- [ ] Inputs show a bottom line in `--text-muted` and a label that stays visible.
- [ ] Focus is a 2px sky outline.
- [ ] One branch or leaf drawing per section, off-center.
- [ ] Motion is 500ms and at most 1px of movement, off under reduced motion.
