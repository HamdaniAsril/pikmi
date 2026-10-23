# Bento

## Identity

Content packed like compartments in a lunch box: a grid of independent cards, each one a small widget
with its own job, sized by how much it matters. One or two large cards hold the main story, a few medium
ones support it, and small ones carry a number, a tag or an icon. Surfaces are calm zinc neutrals with
soft tints; one tangerine accent marks the action. The grid is the identity, so it is used where content
really has different weights, not as the layout of every section.

Fits product showcases and launch pages, portfolios, personal dashboards, feature overviews,
year-in-review pages and app home screens. Avoid it for long reading, step-by-step flows, forms and any
section whose items are equal in importance.

Two themes: light by default, dark for dark-mode products, both complete.

Dial: ENERGY 2 / RHYTHM 3 / MOTION 1

## Visual vocabulary

- **Grid.** Four columns on desktop (1024px and up), two on tablet (640px and up), one on phones; 16px
  gaps everywhere. One or two large cards (2 x 2), two or three medium (2 x 1 or 1 x 2), the rest 1 x 1.
- **Color.** Zinc page `#F4F4F5`, white cards, near-black text `#18181B`, secondary `#52525B`. Cards may
  take a soft tint (orange `#FFF1E6`, green `#E9F7EF`, blue `#EAF2FF`) to group related widgets.
  Tangerine `#E4572E` is the single accent. Dark theme mirrors this with zinc darks and warmer tangerine
  `#F0714D`.
- **Type.** Schibsted Grotesk throughout: 700 for big numbers and titles, 500 for labels, 400 for text.
- **Shape.** Cards 20px radius; anything nested inside a card 12px (`--radius-inner`), so the inner radius
  plus padding visually matches the outer.
- **Depth.** Flat at rest; a soft lift (`--card-lift`) only on hover of interactive cards.

## Reasons

- **Color:** neutral surfaces let card size and position carry hierarchy; tints group related widgets
  without adding accents; one tangerine marks what to do.
- **Typography:** a sturdy grotesk keeps tiny widget labels legible and gives big numbers weight.
- **Layout:** card size follows importance, so the eye lands on the large card first; using the mosaic
  in one section only keeps it meaningful and avoids the default AI layout.
- **Shape:** consistent outer and inner radii make cards read as compartments of one box.
- **Depth:** flat cards keep the grid calm; lift appears only where a card is clickable.
- **Motion:** a small, quick hover (200 to 300ms, 2px lift, scale at most 1.01) confirms interactivity
  without bouncing.
- **Theme:** product UI often ships both modes, so both are designed and checked.

## Token usage

| Token | Role |
| --- | --- |
| `--page`, `--panel`, `--card`, `--rule` | page, raised areas, cards, hairlines |
| `--text`, `--text-muted` | primary and secondary text |
| `--accent`, `--on-accent` | tangerine actions with dark text |
| `--tint-orange`, `--tint-green`, `--tint-blue` | card tints for grouping (per theme) |
| `--link`, `--danger` | links and errors |
| `--radius-card`, `--radius-inner`, `--radius-control` | card, nested and control radii |
| `--card-lift` | hover elevation |

## Components

```css
.bento { display: grid; gap: 16px; grid-template-columns: 1fr; grid-auto-flow: dense; }
@media (min-width: 640px) { .bento { grid-template-columns: repeat(2, 1fr); } }
@media (min-width: 1024px) { .bento { grid-template-columns: repeat(4, 1fr); grid-auto-rows: minmax(160px, auto); } }
.tile { background: var(--card); border: 1px solid var(--rule); border-radius: var(--radius-card); padding: var(--space-lg);
  display: flex; flex-direction: column; gap: var(--space-sm); min-width: 0; }
@media (min-width: 640px) { .tile.wide { grid-column: span 2; } }
@media (min-width: 1024px) { .tile.big { grid-column: span 2; grid-row: span 2; } .tile.tall { grid-row: span 2; } }
.tile.orange { background: var(--tint-orange); } .tile.green { background: var(--tint-green); } .tile.blue { background: var(--tint-blue); }
a.tile { color: inherit; text-decoration: none; transition: transform 250ms ease-out, box-shadow 250ms ease-out; }
a.tile:hover { transform: translateY(-2px) scale(1.01); box-shadow: var(--card-lift); }

.tile .num { font: 700 48px/1 var(--font-body); font-variant-numeric: tabular-nums; }
.tile .label { font: 500 var(--type-label)/1 var(--font-body); color: var(--text-muted); }
.tile .icon { width: 40px; height: 40px; border-radius: var(--radius-inner); display: grid; place-items: center; background: var(--page);
  transition: background-color 200ms ease-out; }
a.tile:hover .icon { background: var(--accent); }

.btn { min-height: 44px; padding: 0 var(--space-md); border: 0; border-radius: var(--radius-control);
  background: var(--accent); color: var(--on-accent); font: 500 15px/1 var(--font-body); }
.btn:active { transform: scale(0.98); }
.btn:focus-visible, a.tile:focus-visible { outline: 2px solid var(--text); outline-offset: 2px; }
@media (prefers-reduced-motion: reduce) { a.tile, .tile .icon { transition: none; } }
```

## Recipes

### UI

- **Product page.** A normal hero (headline, one paragraph, one tangerine button) followed by one bento
  section: a big card with the product's main screen or photo, a tall card with a short testimonial only
  if real, wide cards for two features, small cards for one-number facts (battery, weight, price). Other
  sections use plain text and image layouts.
- **Dashboard home.** The bento grid is the home screen: the most-used widget big, two medium, four
  small; every widget opens its own page.

### Slides

- A single bento slide per deck as the summary or overview: one big card for the key result, three or
  four small cards for supporting facts, 24px gaps at 1920 x 1080.
- Other slides use one card at full width with one point each.

### Social

- 1080 x 1350: a 2 x 3 mini grid with one big card (the headline or product shot) and three to four
  small cards with numbers or tags; text at 32px or more.
- Year-in-review carousels: one bento grid per frame, the same structure each time.

### App

- The home screen is a two-column bento of widgets; the most important widget spans both columns.
- Detail screens are plain lists; the bento belongs to the overview.
- Follow the system theme with the light and dark tokens.

## Outside CSS

| CSS effect | Replacement |
| --- | --- |
| CSS Grid spans | a manual grid of frames: 4 columns, 16px gutters, cards spanning 1 or 2 cells |
| `--card-lift` hover | none on touch; on desktop, a soft shadow (8pt down, 30pt blur, 8%) |
| `grid-auto-flow: dense` | arrange cards by hand so no gaps remain |

## Contrast rules (checked)

| Text | On | Theme | Ratio | Rule |
| --- | --- | --- | --- | --- |
| `--text` | `--page` | light | 16.12 | Primary text. |
| `--text-muted` | `--tint-orange` | light | 6.99 | Secondary text holds on tinted cards. |
| `--text-muted` | `--tint-blue` | light | 6.86 | Secondary text on blue tint. |
| `--on-accent` | `--accent` | light | 4.81 | Tangerine buttons carry dark text. |
| `#FFFFFF` | `--accent` | light | 3.68 | White on tangerine fails; never use it. |
| `--link` | `--card` | light | 6.70 | Links. |
| `--danger` | `--card` | light | 6.57 | Error text. |
| `--text` | `--card` | dark | 14.94 | Primary text on dark cards. |
| `--text-muted` | `--card` | dark | 6.41 | Secondary text on dark cards. |
| `--text-muted` | `--tint-blue` | dark | 6.68 | Secondary text on dark tints. |
| `--on-accent` | `--accent` | dark | 6.54 | Dark text on the dark-theme tangerine. |
| `--link` | `--panel` | dark | 8.48 | Links in dark. |
| `--danger` | `--card` | dark | 5.90 | Error text in dark. |

## Pitfalls

- Every section as a bento grid. One bento section per page; the rest use other compositions.
- All cards the same size. Size follows importance.
- Blue-to-purple gradient cards. Use the neutral surfaces and soft tints.
- Overstuffed cards. One idea per card.
- Invented numbers in small cards. Real figures or marked placeholders only.
- Bouncy or springy hover effects.
- White text on tangerine.
- Uneven gaps or radii that differ from card to card.

## Checklist

- [ ] The bento mosaic appears in one section, where items truly differ in weight.
- [ ] Card sizes follow importance: one or two big, a few medium, the rest small.
- [ ] Gaps are 16px everywhere; card radius 20px, nested radius 12px.
- [ ] Surfaces are neutral; tints group related cards; tangerine is the only accent.
- [ ] Hover lift is 2px and scale at most 1.01, in 200 to 300ms, off under reduced motion.
- [ ] The grid collapses to two columns at 640px and one column on phones.
- [ ] Both themes pass the contrast table.
