# Dark Dev

## Identity

The calm dark interface of a good developer tool: slate layers that differ only slightly, borders that
light up when you hover a card, text in three quiet levels, one blue for actions and mono only where code
lives. Nothing glows or shouts; the work on screen is the brightest thing.

Fits developer tools, API docs and dashboards, DevOps and observability, admin consoles, internal tools,
technical blogs and changelogs. Avoid it for consumer brands, food, fashion, children and anything that
should feel warm or playful.

Dark only, because developer tools are used for long sessions in low light and next to dark editors.

Dial: ENERGY 1 / RHYTHM 2 / MOTION 1

## Visual vocabulary

- **Color.** Slate page `#0F172A`, panels and cards `#1E293B`, rules `#334155` brightening to `#64748B`
  on hover. Text in three levels: headings `#F1F5F9`, body `#CBD5E1`, secondary `#94A3B8`. One blue
  `#2563EB` for actions with white text; links in light blue `#60A5FA`. Green `#22C55E` and red
  `#F87171` for status only.
- **Light.** Primary buttons have a faint lit top edge (`--inset-glow`). Cards rise 2px on hover with a
  deep black shadow; borders brighten as if a light passed nearby.
- **Type.** Red Hat Display 600 for headings, Red Hat Text for interface and body, Red Hat Mono for code,
  IDs, versions and command lines.
- **Shape.** 8px controls, 12px cards.

## Reasons

- **Color:** close slate layers reduce glare over long sessions; three text levels give hierarchy
  without extra colors; a single blue keeps actions findable.
- **Typography:** the Red Hat families were drawn as one system for technical documentation, so sans and
  mono sit together naturally.
- **Layout:** panels and cards on a calm grid let dense information breathe without decoration.
- **Shape:** modest radii keep the interface precise but not harsh.
- **Depth:** border illumination and a deep shadow mark interactive cards; nothing else is raised.
- **Motion:** 200ms for controls and 300ms for cards, ease-out: fast enough for tools, never springy.
- **Theme:** dark is the reason for the style (R-21: developer tools have a legitimate dark default).

## Token usage

| Token | Role |
| --- | --- |
| `--page`, `--panel`, `--card` | slate layers |
| `--rule`, `--rule-hover` | borders at rest and on hover |
| `--text`, `--body-text`, `--text-muted` | headings, body, secondary |
| `--accent`, `--on-accent` | blue actions with white text |
| `--link` | light blue links |
| `--success`, `--danger` | status |
| `--inset-glow`, `--card-shadow` | button top edge and card hover depth |
| `--font-mono` | code, IDs, versions |

## Components

```css
.btn { min-height: 40px; padding: 0 var(--space-md); border: 0; border-radius: var(--radius-control);
  background: var(--accent); color: var(--on-accent); box-shadow: var(--inset-glow);
  font: 500 14px/1 var(--font-body); transition: background-color 200ms ease-out, box-shadow 200ms ease-out; }
.btn:hover { background: #1D4ED8; box-shadow: var(--inset-glow), 0 0 0 1px var(--link); }
.btn:active { transform: scale(0.98); box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.3); }
.btn.secondary { background: var(--panel); color: var(--text); box-shadow: inset 0 0 0 1px var(--rule); }
.btn:focus-visible, .field:focus-visible { outline: 2px solid var(--link); outline-offset: 2px; }

.card { background: var(--card); border: 1px solid var(--rule); border-radius: var(--radius-card); padding: var(--space-lg);
  transition: border-color 300ms ease-out, transform 300ms ease-out, box-shadow 300ms ease-out; }
a.card:hover { border-color: var(--rule-hover); transform: translateY(-2px); box-shadow: var(--card-shadow); }
a.card .title { color: var(--text); } a.card .desc { color: var(--text-muted); transition: color 200ms ease-out; }
a.card:hover .desc { color: var(--body-text); }

code, .mono { font-family: var(--font-mono); font-size: 0.92em; }
.code { background: var(--page); border: 1px solid var(--rule); border-radius: var(--radius-control); padding: var(--space-md);
  font: 400 13px/1.7 var(--font-mono); color: var(--body-text); overflow-x: auto; }
.field { min-height: 40px; width: 100%; padding: 0 var(--space-md); border: 1px solid var(--rule-hover); border-radius: var(--radius-control);
  background: var(--page); color: var(--text); font: 400 14px var(--font-body); }
.badge { display: inline-flex; align-items: center; gap: 6px; font: 500 12px/1 var(--font-body); }
.badge::before { content: ""; width: 8px; height: 8px; border-radius: 50%; background: currentColor; }
.badge.ok { color: var(--success); } .badge.bad { color: var(--danger); }
@media (prefers-reduced-motion: reduce) { .btn, .card, a.card .desc { transition: none; } }
```

Inputs use `--rule-hover` as their border (3.75:1) so the field edge stays visible; the resting
`--rule` is for decorative dividers only.

## Recipes

### UI

- **Developer landing page.** A headline that says what the tool does in one sentence, one paragraph,
  a blue button and a secondary button, then a real code sample in a `.code` block. Sections: a three-card
  row of capabilities (cards light up on hover), a short changelog list with version numbers in mono, a
  docs link list.
- **Dashboard.** Left nav on `--panel`, content on `--page`, metric cards with real values, a table with
  mono IDs and status badges, empty, loading and error states drawn in the same slate.

### Slides

- Slate slides, white headings at 56px, body at 28px in `--body-text`.
- Code slides: one `.code` block at 28px mono, at most 12 lines, with the key line highlighted by a blue
  left marker inside the code block.
- One chart per slide in blue and slate greys.

### Social

- 1080 x 1350: release notes as a card on the slate page, version in mono, three short bullets at 36px,
  the docs link at the bottom.
- No fake terminal windows; show a real snippet or the product UI.

### App

- Slate screens, list rows on `--card` with 1px rules, mono for IDs.
- One blue primary action per screen; destructive actions in a red outline with `--danger` text.
- Notifications use badges with a dot plus a word.

## Outside CSS

| CSS effect | Replacement |
| --- | --- |
| `--inset-glow` | a 1px lighter line along the top edge of the button |
| `--card-shadow` hover | none on touch; on desktop, a deep shadow (8pt down, 30pt blur, 50% black) |
| Border illumination | switch the stroke color from `--rule` to `--rule-hover` on hover or focus |

## Contrast rules (checked)

| Text | On | Theme | Ratio | Rule |
| --- | --- | --- | --- | --- |
| `--text` | `--page` | dark | 16.30 | Headings. |
| `--body-text` | `--panel` | dark | 9.85 | Body text on panels. |
| `--text-muted` | `--panel` | dark | 5.71 | Secondary text on panels. |
| `--text-muted` | `--page` | dark | 6.96 | Secondary text on the page. |
| `--on-accent` | `--accent` | dark | 5.17 | White on the action blue. |
| `--link` | `--panel` | dark | 5.75 | Links. |
| `--success` | `--panel` | dark | 6.42 | Success badges. |
| `--danger` | `--panel` | dark | 5.29 | Errors. |
| `--rule-hover` | `--page` | dark | 3.75 | Input borders pass the 3:1 non-text minimum. |

## Pitfalls

- Pure white text or pure black backgrounds; they glare. Use the slate levels.
- A fake terminal window as the hero visual. Show real code or the real product.
- Mono for headings or body text. Mono is for code.
- Neon accents or glows; this is a calm tool, not a cockpit.
- More than one accent color.
- Focus rings that disappear on dark; keep the light blue outline with an offset.
- Invented metrics, uptime numbers or customer logos.

## Checklist

- [ ] Surfaces use the slate layers; text uses the three levels.
- [ ] Blue is the only accent; green and red appear only as status.
- [ ] Cards light their border and rise 2px on hover, in 300ms.
- [ ] Mono appears only for code, IDs and versions.
- [ ] Inputs have visible `--rule-hover` borders; focus is a light blue outline.
- [ ] No fake terminal visuals and no invented numbers.
- [ ] Empty, loading and error states exist for data views.
