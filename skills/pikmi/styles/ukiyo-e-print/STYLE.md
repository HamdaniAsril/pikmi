# Ukiyo-e Print

## Identity

A Japanese woodblock print turned into an interface. Indigo outlines on rice paper, large flat blocks of
color, a vermilion seal stamped where it matters, waves and clouds as patterns, and a hard print shadow
that looks like a second block printed slightly off register. No depth, no blur, no gloss: everything is
pressed flat onto paper.

Fits culture and travel, restaurants and tea houses, craft and heritage brands, museums and exhibitions,
editorial features, festivals and posters. Avoid it for fintech, developer tools, healthcare and any
product that must feel modern-neutral.

Light only.

Dial: ENERGY 2 / RHYTHM 2 / MOTION 1

## Visual vocabulary

- **Color.** Rice paper `#F5F0E1`, indigo `#1A3055` for ink and outlines, deep vermilion `#B8402A` for
  actions, bright vermilion `#D4553A` for seals and large accents, gold leaf `#C9A227` only on indigo.
  Four colors in all; nothing outside them.
- **Outlines.** 2px indigo borders around blocks and controls, like the key block of a print.
- **Print shadow.** A hard 4px offset in indigo (`--print-shadow`), never blurred.
- **Shape.** Corners 0 to 2px. No pills, no circles except the seal.
- **Type.** Shippori Mincho B1 for headings, a mincho with sharp brush-cut serifs; Zen Kaku Gothic New for
  body text.
- **Motifs.** One wave, cloud or mountain pattern per view, drawn as flat indigo or vermilion shapes on
  paper.
- **Seal.** A small vermilion square stamp with one or two characters or initials marks the key item.

## Reasons

- **Color:** four inks match how a woodblock print is made, one block per color, and keep the palette
  inside the antislop limit by design.
- **Typography:** a mincho heading carries the brush and the period; a quiet gothic body keeps reading
  easy.
- **Layout:** flat color blocks with bold outlines make sections obvious without any shadows or
  gradients.
- **Shape:** sharp corners read as cut wood and paper; rounding would read as plastic.
- **Depth:** the off-register print shadow is the only depth, which keeps the page flat as paper.
- **Motion:** a hard cut (75ms or none) matches the stamp-and-lift of printing; smooth easing would feel
  digital.
- **Theme:** rice paper is the material; a dark version would be a different style.

## Token usage

| Token | Role |
| --- | --- |
| `--page`, `--panel`, `--card` | rice paper in three tones |
| `--rule`, `--text`, `--link` | indigo ink, outlines and links |
| `--text-muted` | softer indigo for secondary text |
| `--accent`, `--on-accent` | deep vermilion buttons with paper-colored text |
| `--vermilion` | seals, large accents, decoration |
| `--indigo`, `--gold-leaf` | indigo blocks and the gold that only sits on them |
| `--danger` | error text |
| `--print-shadow`, `--print-shadow-hover`, `--outline` | print shadow and outlines |

## Components

```css
.btn { min-height: 48px; padding: 0 var(--space-lg); border: var(--outline); border-radius: var(--radius-key);
  background: var(--accent); color: var(--on-accent); box-shadow: var(--print-shadow);
  font: 700 17px/1 var(--font-display); letter-spacing: 1px; transition: transform 75ms linear, box-shadow 75ms linear; }
.btn:hover { transform: translate(-2px, -2px); box-shadow: var(--print-shadow-hover); }
.btn:active { transform: translate(4px, 4px); box-shadow: none; border-color: var(--vermilion); }
.btn.paper { background: var(--card); color: var(--text); }
.btn:focus-visible, .field:focus-visible { outline: 3px solid var(--vermilion); outline-offset: 3px; }

.block { background: var(--card); border: var(--outline); border-radius: var(--radius-card); padding: var(--space-lg);
  box-shadow: var(--print-shadow); }
.block.indigo { background: var(--indigo); color: var(--page); }
.block.indigo .gold { color: var(--gold-leaf); }

.seal { display: inline-grid; place-items: center; width: 56px; height: 56px; background: var(--vermilion);
  color: #FFFFFF; font: 800 22px/1 var(--font-display); rotate: -4deg; }
.label { font: 500 var(--type-label)/1 var(--font-body); letter-spacing: var(--tracking-label); color: var(--text-muted); }
.field { min-height: 48px; width: 100%; padding: 0 var(--space-md); border: var(--outline); border-radius: var(--radius-key);
  background: var(--card); color: var(--text); font: 400 17px var(--font-body); }

.waves { height: 64px; background:
  radial-gradient(circle at 50% 100%, transparent 18px, var(--indigo) 19px 21px, transparent 22px) 0 0 / 48px 32px repeat-x,
  radial-gradient(circle at 50% 100%, transparent 18px, var(--indigo) 19px 21px, transparent 22px) 24px 32px / 48px 32px repeat-x; }
@media (prefers-reduced-motion: reduce) { .btn { transition: none; } }
```

The seal's white text on bright vermilion is 4.07:1, so seal text must be 22px or larger and bold.

## Recipes

### UI

- **Landing page.** A paper hero with a mincho headline at 56 to 84px, a wave band along the bottom,
  one vermilion seal next to the product name and a deep vermilion button. Sections are flat blocks:
  an indigo block with paper text and a gold detail, a row of outlined paper cards with print shadows,
  a menu or schedule as an outlined table.
- **Content pages.** A single paper column, mincho subheads, indigo rules between sections, one seal
  marking the featured item.

### Slides

- Paper slides with a 2px indigo frame inset 96px, a wave band across the bottom 15%.
- Mincho titles at 72px, body at 30px; one flat illustration or one large vermilion figure per slide.
- Section slides flip to an indigo background with paper text and a gold-leaf title.
- Cut transitions only.

### Social

- 1080 x 1350: a big flat composition (a wave, a mountain, a sun disc) in indigo and vermilion on
  paper, a mincho headline at 72px or more, a seal in a corner.
- Details in an outlined paper block with the print shadow.
- Carousels keep the wave band and the seal in the same place.

### App

- Paper screens, outlined list rows, a deep vermilion primary button with the print shadow.
- Tab bar: outlined square tabs, the active one filled indigo with paper text.
- Press feedback removes the print shadow instantly, like lifting a stamp.

## Outside CSS

| CSS effect | Replacement |
| --- | --- |
| `--print-shadow` | an indigo duplicate of the shape offset 4px right and down, no blur |
| `.waves` radial-gradient pattern | a repeating wave vector pattern, or a single drawn wave |
| Hover offset | none on touch; keep the press state |
| Seal `rotate` | rotate the seal shape -4 degrees |

## Contrast rules (checked)

| Text | On | Theme | Ratio | Rule |
| --- | --- | --- | --- | --- |
| `--text` | `--page` | light | 11.54 | Indigo ink on paper. |
| `--text-muted` | `--panel` | light | 6.56 | Secondary text on darker paper. |
| `--on-accent` | `--accent` | light | 4.84 | Paper text on deep vermilion buttons. |
| `--vermilion` | `--page` | light | 3.57 | Bright vermilion text only at 24px or larger. |
| `#FFFFFF` | `--vermilion` | light | 4.07 | Seal text only, 22px bold or larger. |
| `--gold-leaf` | `--indigo` | light | 5.43 | Gold only ever on indigo. |
| `--page` | `--indigo` | light | 11.54 | Paper text on indigo blocks. |
| `--danger` | `--page` | light | 6.57 | Error text. |
| `--vermilion` | `--page` | light | 3.57 | Focus ring (3px vermilion). |
| `--rule` | `--card` | light | 12.37 | Field border (2px indigo). |

## Pitfalls

- Gradients, blur, soft shadows or glass; the print is flat.
- Large rounded corners or pill buttons.
- Neon or modern saturated colors outside the four inks.
- Bright vermilion for small text; use deep vermilion or indigo.
- Gold on paper; it only works on indigo.
- Patterns on every block. One motif per view.
- Copying a famous print. Draw your own waves, clouds and mountains in the same flat manner.

## Checklist

- [ ] Only rice paper, indigo, vermilion and gold leaf appear.
- [ ] Blocks and controls have 2px indigo outlines and 0 to 2px corners.
- [ ] Depth comes only from the hard 4px print shadow.
- [ ] Headings use Shippori Mincho B1; body uses Zen Kaku Gothic New.
- [ ] One motif and at most one seal per view.
- [ ] Transitions are 75ms linear or none; press removes the shadow.
- [ ] Every text pair passes the contrast table at its size.
