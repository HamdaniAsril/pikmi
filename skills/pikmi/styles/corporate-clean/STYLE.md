# Corporate Clean

## Identity

The quiet confidence of a well-kept ledger. Pale slate surfaces, white cards, hairline rules, numbers
that line up in columns, ink-blue headings and a single confident blue for actions. It is calm on
purpose, but it is not anonymous: the ledger rules, the tabular figures and the ink headings are its
signature.

Fits B2B SaaS, finance and operations tools, admin panels, reports, investor and board material, and
corporate sites. Avoid it for consumer brands that want personality first, entertainment, fashion or
anything that should feel playful.

Light only.

Dial: ENERGY 1 / RHYTHM 2 / MOTION 1

## Visual vocabulary

- **Color.** Page `#F8FAFC`, cards white, rules `#E5E7EB`. Text near-black `#111827`, secondary
  `#4B5563`. Headings in ink blue `#0F2A5C`. Actions and focus in blue `#1F4FD1`. Green, amber and red
  appear only as status.
- **Ledger motif.** 1px rules separate rows and sections like a printed ledger; key figures sit in
  tabular numerals, right-aligned, with their unit in the secondary color.
- **Type.** IBM Plex Sans 400 for text, 500 for interactive elements, 600 for headings. Tabular numbers
  everywhere data appears (`font-variant-numeric: tabular-nums`). Sentence case, never all caps except
  12px table headers.
- **Shape.** 8px radius on controls, 12px on cards. Never square, never pill.
- **Depth.** Cards rest on `--shadow-rest`; only the hovered card or an open menu rises to
  `--shadow-raised`.

## Reasons

- **Color:** one blue reserved for actions makes every clickable thing obvious; ink-blue headings give
  the page a recognizable voice without adding a second accent.
- **Typography:** IBM Plex Sans was drawn for an engineering company's corporate identity, so it reads as
  serious and precise; its tabular figures keep numbers comparable at a glance.
- **Layout:** ledger rules and aligned numeric columns turn dense information into something scannable.
- **Shape:** a medium radius is friendly without looking consumer; it stays consistent so hierarchy
  comes from size and weight.
- **Depth:** shadows mark elevation only (rest, hover, menu), so nothing floats without a reason.
- **Motion:** short (150 to 200ms) and functional: hover lift, press confirmation, focus ring.
- **Theme:** light keeps long working sessions readable in offices and on projectors; products that need
  a dark mode should pair this style with Dark Dev rather than inventing one.

## Token usage

| Token | Role |
| --- | --- |
| `--page`, `--panel`, `--card`, `--rule` | page, sidebars and headers, cards, hairline rules |
| `--text`, `--text-muted` | body and secondary text |
| `--ink` | headings and key figures |
| `--accent`, `--on-accent`, `--link`, `--focus` | actions, links and focus rings |
| `--field-border` | input borders (3:1 or more on cards) |
| `--success`, `--warning`, `--danger` | status text and badges only |
| `--shadow-rest`, `--shadow-raised` | elevation levels |

## Components

```css
.btn { min-height: 44px; padding: 0 var(--space-md); border: 1px solid transparent; border-radius: var(--radius-control);
  background: var(--accent); color: var(--on-accent); font: 500 15px/1 var(--font-body);
  box-shadow: var(--shadow-rest); transition: transform 150ms ease-out, box-shadow 150ms ease-out; }
.btn:hover { transform: translateY(-1px); box-shadow: var(--shadow-raised); }
.btn:active { transform: scale(0.98); box-shadow: var(--shadow-rest); }
.btn.secondary { background: var(--card); color: var(--text); border-color: var(--rule); }
.btn:focus-visible, .field:focus-visible { outline: 2px solid var(--focus); outline-offset: 2px; }

.card { background: var(--card); border: 1px solid var(--rule); border-radius: var(--radius-card); padding: var(--space-lg);
  box-shadow: var(--shadow-rest); transition: transform 200ms ease-out, box-shadow 200ms ease-out; }
a.card:hover { transform: translateY(-2px); box-shadow: var(--shadow-raised); }

.figure { font: 600 var(--type-h1)/1 var(--font-body); color: var(--ink); font-variant-numeric: tabular-nums; }
.figure .unit { font-size: var(--type-body); font-weight: 500; color: var(--text-muted); }

.ledger { width: 100%; border-collapse: collapse; font-variant-numeric: tabular-nums; }
.ledger th { font: 600 12px/1 var(--font-body); letter-spacing: var(--tracking-label); text-transform: uppercase;
  color: var(--text-muted); text-align: left; padding: 10px 12px; border-bottom: 1px solid var(--rule); }
.ledger td { padding: 12px; border-bottom: 1px solid var(--rule); }
.ledger td.num, .ledger th.num { text-align: right; }

.field { min-height: 44px; width: 100%; padding: 0 12px; border: 1px solid var(--field-border); border-radius: var(--radius-control);
  background: var(--card); color: var(--text); font: 400 16px var(--font-body); }
.badge { display: inline-flex; align-items: center; gap: 6px; font: 500 13px/1 var(--font-body); }
.badge::before { content: ""; width: 8px; height: 8px; border-radius: 50%; background: currentColor; }
.badge.ok { color: var(--success); } .badge.warn { color: var(--warning); } .badge.bad { color: var(--danger); }
```

## Recipes

### UI

- **Dashboard.** A white sidebar (`--panel`) with text navigation, a page header with an ink-blue title
  and the date range as a segmented control. One row of two to four cards, each holding one figure with
  its unit and a one-line comparison; the most important figure gets the widest card. Below, a ledger
  table. Real data or `[REAL DATA]` placeholders only.
- **Corporate site.** A plain headline in ink blue that states what the company does, one paragraph,
  a primary and a secondary button. Sections vary: a ledger-style comparison table, a two-column text and
  figure block, a short customer story only if it is real.

### Slides

- White slides with a 1px rule under the title and a small footer line (section name, page number).
- Titles state the finding in ink blue at 56px; one chart or one figure per slide.
- Charts: blue for the series that matters, greys for context, no 3D, no gradients; numbers labeled
  directly instead of a legend.
- Board-deck density is fine as long as each slide has one point.

### Social

- 1080 x 1350, white or `--page`, a 1px rule framing a single figure or a short statement in ink blue.
- Company and source in a small footer line; no stock photos of handshakes.
- LinkedIn-style carousels: one figure per frame, the same layout on every frame.

### App

- Native list rows with 1px separators, figures right-aligned in tabular numerals.
- One blue primary button per screen; everything else is secondary or text.
- Status shown with a colored dot plus a word, never color alone.

## Outside CSS

| CSS effect | Replacement |
| --- | --- |
| `--shadow-rest`, `--shadow-raised` | a 1px border in `--rule`, or the platform's elevation level 1 and 3 |
| `font-variant-numeric: tabular-nums` | the font's tabular figures setting, or a monospaced number style |
| Hover lift | none on touch platforms; use the pressed state only |

## Contrast rules (checked)

| Text | On | Theme | Ratio | Rule |
| --- | --- | --- | --- | --- |
| `--text` | `--page` | light | 16.96 | Body text. |
| `--text-muted` | `--card` | light | 7.56 | Secondary text and table headers. |
| `--ink` | `--page` | light | 13.33 | Headings and key figures. |
| `--on-accent` | `--accent` | light | 6.78 | White on the action blue. |
| `--accent` | `--page` | light | 6.48 | Blue text for active states. |
| `--link` | `--card` | light | 6.70 | Links. |
| `--danger` | `--card` | light | 4.83 | Error text. |
| `--success` | `--card` | light | 5.02 | Success text. |
| `--warning` | `--card` | light | 5.02 | Warning text. |
| `--focus` | `--page` | light | 3.52 | Focus ring (2px, offset 2px). |
| `--field-border` | `--card` | light | 4.83 | Field border on cards. |

## Pitfalls

- The sterile default: grey-on-white with no ink headings, no ledger rules and no tabular figures. That
  is a template, not this style.
- Copying a famous product's look. Use this vocabulary, not someone else's interface.
- Shadows on every element. Rest shadow on cards, raised only on hover or menus.
- A second accent color. Status colors are for status only.
- Invented metrics, logos or testimonials. Show real numbers or a marked placeholder.
- Generic calls to action. Name the action ("Export the March report").
- Transitions longer than 200ms; the interface should feel immediate.

## Checklist

- [ ] Headings are ink blue; actions are the one blue.
- [ ] Numbers use tabular figures and line up right in tables.
- [ ] Rows and sections are separated by 1px rules.
- [ ] Controls are 8px radius, cards 12px, nothing pill-shaped.
- [ ] Only cards rest on a shadow; only hover and menus rise.
- [ ] Every focusable element shows a 2px focus ring with a 2px offset.
- [ ] Status uses a dot plus a word.
- [ ] No invented data, logos or testimonials.
