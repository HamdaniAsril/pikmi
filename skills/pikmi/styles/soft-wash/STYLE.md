# Soft Wash

## Identity

A page that looks painted: soft washes of peach, teal and rose bleeding into warm paper, blue-grey ink
for text, italic serif headings like a calligrapher's hand, and motion as slow as pigment spreading on
wet paper. Edges are soft and colors overlap, but the reading surface stays calm and clear.

Fits weddings and invitations, artists and illustrators, florists and botanical brands, poetry and
literary projects, gentle wellness, and slow lifestyle content. Avoid it for data-heavy tools, finance,
technical products and anything that must feel crisp or urgent.

Light only.

Dial: ENERGY 2 / RHYTHM 2 / MOTION 2

## Visual vocabulary

- **Color.** Warm paper `#FAF8F5`, a deeper paper panel `#F3EEE7`, white cards. Ink in blue-grey
  `#3D5F91`, secondary `#586A89`. Washes in peach `#E8A87C`, teal `#85CDCA`, rose `#C38D94` and sand
  `#D4A373`, always translucent (`--wash-opacity`, 0.3). Per page, choose two washes as the core pair and
  one as the accent.
- **Washes.** Two soft, blurred blots per view at most, layered behind content, edges fading out.
- **Type.** Cormorant italic for headings (500 to 600), Crimson Pro upright for body at 19px. Italic is for
  headings and short emphasis only.
- **Shape.** Rounded but not pill: 16px controls, 28px cards.
- **Depth.** A blue-tinted bloom shadow (`--bloom-shadow`) on hover, like color spreading; no grey
  shadows.

## Reasons

- **Color:** translucent washes over warm paper are the medium itself; blue-grey ink is softer than black
  but still reads clearly.
- **Typography:** a calligraphic italic gives the hand-painted voice; an upright text face keeps long
  passages readable, which a page of italic would not.
- **Layout:** generous margins and few elements leave room for the washes to breathe without crowding
  text.
- **Shape:** soft radii echo brush edges; keeping pills out preserves hierarchy.
- **Depth:** a colored bloom instead of a lift feels like pigment, not plastic.
- **Motion:** slow 500ms ease-in-out transitions match the feeling of paint moving on wet paper.
- **Theme:** watercolor needs white paper to glow; on a dark ground the washes turn muddy.

## Token usage

| Token | Role |
| --- | --- |
| `--page`, `--panel`, `--card`, `--rule` | paper tones and soft rules |
| `--text`, `--text-muted`, `--link` | blue-grey ink |
| `--accent`, `--on-accent` | deep blue-grey buttons with white text |
| `--peach`, `--teal`, `--rose`, `--sand` | washes, always translucent |
| `--wash-opacity` | the strongest allowed wash behind text |
| `--bloom-shadow` | hover bloom |
| `--danger` | error text |

## Components

```css
.wash { position: absolute; width: 420px; aspect-ratio: 1; border-radius: 50%; filter: blur(48px);
  background: var(--peach); opacity: var(--wash-opacity); pointer-events: none; z-index: 0; }
.wash.teal { background: var(--teal); }

h1, h2, h3 { font-family: var(--font-display); font-style: italic; font-weight: 600; color: var(--text); }
body { font: 400 19px/1.75 var(--font-body); color: var(--text); background: var(--page); }

.btn { min-height: 48px; padding: 0 var(--space-lg); border: 0; border-radius: var(--radius-control);
  background: var(--accent); color: var(--on-accent); font: 500 18px/1 var(--font-body);
  transition: box-shadow 500ms ease-in-out, transform 500ms ease-in-out; }
.btn:hover { box-shadow: var(--bloom-shadow); }
.btn:active { transform: scale(0.98); }
.btn.soft { background: var(--card); color: var(--text); box-shadow: inset 0 0 0 1px var(--rule); }
.btn:focus-visible, .field:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px; }

.card { position: relative; z-index: 1; background: var(--card); border-radius: var(--radius-card); padding: var(--space-lg);
  border: 1px solid var(--rule); transition: box-shadow 500ms ease-in-out; }
a.card:hover { box-shadow: var(--bloom-shadow); }
.field { min-height: 48px; width: 100%; padding: 0 var(--space-md); border: 1px solid var(--text-muted); border-radius: var(--radius-control);
  background: var(--card); color: var(--text); font: 400 18px var(--font-body); }
@media (prefers-reduced-motion: reduce) { .btn, .card { transition: none; } }
```

Washes stay at 30% opacity or less wherever text crosses them, and never overlap behind text; at that
strength a single wash keeps body ink above 4.5:1, while two overlapping washes drop it to 4.09. Secondary
text never sits over a wash.

## Recipes

### UI

- **Landing page.** Paper background with one peach and one teal wash bleeding off the top corners; a
  centered italic headline at 60 to 88px, two lines of upright body, a blue-grey button and a soft
  button. Sections below: a story column with a single painted image, a row of white cards with 28px
  corners, a quote set in italic at 32px on a panel.
- **Invitation or event page.** One wash behind the names or the date, details on white cards, a map or
  RSVP form in plain upright type.

### Slides

- Paper slides with one wash entering from a corner; italic titles at 64px, upright body at 30px.
- Images as soft-edged vignettes; quotes in italic.
- Fade transitions of 600ms.

### Social

- 1080 x 1350: two washes overlapping behind a centered italic phrase at 80px, a small upright line
  below at 36px.
- Keep the text inside the lighter part of the washes or on a white card.

### App

- Paper screens, white cards with 28px corners, a blue-grey primary button.
- One wash only, in the header or an empty state, never behind lists.
- Italic only for screen titles.

## Outside CSS

| CSS effect | Replacement |
| --- | --- |
| Blurred `.wash` with `filter: blur` | a soft painted texture image, or a radial gradient fading to transparent |
| `--bloom-shadow` | a soft colored outer glow (blue-grey, 25%, 40pt), or none on native |
| `--wash-opacity` | set the layer opacity to 30% |

## Contrast rules (checked)

| Text | On | Theme | Ratio | Rule |
| --- | --- | --- | --- | --- |
| `--text` | `--page` | light | 6.11 | Ink on paper. |
| `--text` | `--panel` | light | 5.61 | Ink on panels. |
| `--text` | `--card` | light | 6.47 | Ink on cards. |
| `--text-muted` | `--page` | light | 5.16 | Secondary text on paper. |
| `--text-muted` | `--panel` | light | 4.74 | Secondary text on panels. |
| `--on-accent` | `--accent` | light | 5.11 | White on blue-grey buttons. |
| `--text` | `rgba(232, 168, 124, 0.35)` | light | 4.91 | Ink still passes over a peach wash at 35%. |
| `--text` | `rgba(195, 141, 148, 0.35)` | light | 4.50 | Rose is the limit; keep washes at 30% behind text. |
| `--text-muted` | `rgba(232, 168, 124, 0.35)` | light | 4.15 | Secondary text fails over washes; keep it on plain paper. |
| `--danger` | `--page` | light | 5.49 | Error text. |
| `--text` | `#E6C7BE` | light | 4.09 | Peach and rose washes overlapping behind text fail; keep washes apart. |
| `--accent` | `--page` | light | 4.82 | Focus ring (2px blue-grey). |
| `--text-muted` | `--card` | light | 5.47 | Field border on cards. |

## Pitfalls

- Washes stronger than 30% behind text, more than two washes in a view, or two washes overlapping
  behind text.
- All-italic body text; italic is for headings and short emphasis.
- Hard borders, sharp corners, black backgrounds or hard offset shadows.
- Saturated, fully opaque color blocks; color is always translucent here.
- Grey drop shadows; use the blue bloom.
- Fast or springy motion.
- Every element pill-shaped.

## Checklist

- [ ] Paper background; ink is blue-grey.
- [ ] Two washes at most per view, at 30% or less behind text, never overlapping behind text.
- [ ] Headings are Cormorant italic; body is Crimson Pro upright at 19px.
- [ ] Controls 16px radius, cards 28px, no pills.
- [ ] Hover shows the blue bloom; nothing else casts shadows.
- [ ] Secondary text never sits over a wash.
- [ ] Transitions are 500ms ease-in-out and stop under reduced motion.
