# Islamic Geometric

## Identity

The order of geometric tilework: lapis blue, ivory and gold, eight-point stars repeating into patterns,
content framed the way a courtyard frames the sky. Ornament lives on the edges (frames, dividers, arches)
so the center stays calm and readable. Symmetry and rhythm carry the mood, not decoration piled on top.

Fits Ramadan and Eid campaigns, Islamic finance and education, travel and culture in North Africa, the
Middle East and Southeast Asia, events, invitations, hospitality and premium heritage brands. Avoid it
for playful tech, children's games, or any context unrelated to the culture it draws from.

Two themes: ivory (light) by default, deep blue (dark) for evening and night use.

Dial: ENERGY 2 / RHYTHM 1 / MOTION 1

## Visual vocabulary

- **Color.** Three core colors: lapis blue `#1A3A5C`, ivory `#F5ECD7` and gold `#C9A74E`. Emerald
  `#25693B` and deep red `#8B2332` are for status or a single accent, never both on one page.
- **Pattern.** The eight-point star (two overlapping squares) and its tessellation. Use it as a frame
  border, a divider band, a corner piece, or a background at 8% opacity or less on one surface.
- **Arches.** Images and feature cards can take the arch shape (`--arch-radius`), one or two per screen.
- **Gold rules.** Dividers fade in from both ends (`--gold-rule`); 2px gold borders frame important
  panels.
- **Type.** El Messiri for headings (its Latin was drawn alongside Arabic letterforms), Noto Sans for
  body, which also covers Arabic script through Noto Sans Arabic. Headings get slight tracking; body
  stays relaxed at 1.7 line height.
- **Layout.** Centered, symmetrical compositions; content blocks mirror each other across the axis.

## Reasons

- **Color:** blue, ivory and gold come from the classic tile and manuscript palette; keeping emerald and
  red as rare accents preserves the calm.
- **Typography:** El Messiri bridges Latin and Arabic shapes, so bilingual layouts feel like one voice;
  Noto Sans keeps long text readable in both scripts.
- **Layout:** symmetry reflects the geometry the style is built on and gives every page a clear center.
- **Shape:** arches and framed panels echo architecture without imitating a specific building.
- **Depth:** depth comes from framing and pattern, not shadows; a soft shadow only lifts a modal.
- **Motion:** slow, symmetric transitions (400 to 500ms) keep the dignified rhythm; ornaments may brighten
  gently on hover, never flash.
- **Theme:** ivory reads like paper and daylight; the deep blue theme suits evening use, such as the hours
  after iftar, and both are complete.

## Token usage

| Token | Role |
| --- | --- |
| `--page`, `--panel`, `--card` | ivory or deep-blue surfaces |
| `--rule` | gold frames and dividers |
| `--text`, `--text-muted` | blue ink (light) or ivory ink (dark) |
| `--accent`, `--on-accent` | blue buttons with ivory text (light); gold buttons with deep-blue text (dark) |
| `--link`, `--danger` | links and errors per theme |
| `--gold`, `--emerald`, `--deep-red` | ornament, status, the single accent |
| `--gold-rule`, `--arch-radius` | divider gradient and arch shape |

## Components

```css
.btn { min-height: 48px; padding: 0 var(--space-lg); border: 2px solid var(--rule); border-radius: var(--radius-control);
  background: var(--accent); color: var(--on-accent); font: 600 16px/1 var(--font-display);
  letter-spacing: var(--tracking-heading); transition: box-shadow 450ms ease-out; }
.btn:hover { box-shadow: 0 0 0 4px color-mix(in srgb, var(--gold) 35%, transparent); }
.btn:active { transform: scale(0.98); }
.btn.quiet { background: transparent; color: var(--text); }
.btn:focus-visible, .field:focus-visible { outline: 2px solid var(--gold); outline-offset: 3px; }

.frame { position: relative; background: var(--card); border: 2px solid var(--rule); border-radius: var(--radius-card);
  padding: var(--space-xl) var(--space-lg); text-align: center; }
.frame::before, .frame::after { content: ""; position: absolute; width: 28px; height: 28px; background: var(--gold);
  clip-path: polygon(50% 0, 61% 25%, 85% 15%, 75% 39%, 100% 50%, 75% 61%, 85% 85%, 61% 75%, 50% 100%, 39% 75%, 15% 85%, 25% 61%, 0 50%, 25% 39%, 15% 15%, 39% 25%); }
.frame::before { top: -15px; left: 50%; translate: -50% 0; }
.frame::after { bottom: -15px; left: 50%; translate: -50% 0; }

.divider { height: 2px; border: 0; background: var(--gold-rule); margin: var(--space-xl) auto; width: min(480px, 80%); }
.arch { border-radius: var(--arch-radius); overflow: hidden; border: 2px solid var(--rule); }
.pattern { background-color: var(--panel); background-size: 48px;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='48' height='48' viewBox='0 0 48 48'%3E%3Cg fill='%23C9A74E' opacity='0.08'%3E%3Crect x='15' y='15' width='18' height='18'/%3E%3Crect x='15' y='15' width='18' height='18' transform='rotate(45 24 24)'/%3E%3C/g%3E%3C/svg%3E"); }

h1, h2, h3 { font-family: var(--font-display); font-weight: 700; letter-spacing: var(--tracking-heading); color: var(--text); }
.field { min-height: 48px; width: 100%; padding: 0 var(--space-md); border: 1px solid var(--rule); border-radius: var(--radius-control);
  background: var(--card); color: var(--text); font: 400 17px var(--font-body); }
@media (prefers-reduced-motion: reduce) { .btn { transition: none; } }
```

The star tile is one eight-point star (two overlapping squares) in gold, drawn as a group at 8% opacity
so the overlap does not darken, repeating every 48px.

## Recipes

### UI

- **Campaign landing page.** A centered hero inside a gold-framed panel with stars at the top and bottom
  of the frame; heading in El Messiri, one paragraph, a primary and a quiet button. Below, a band of the
  star pattern as a divider, then three cards mirrored around the center, one with an arch-shaped image.
- **Information pages.** Plain ivory text column at 65 characters, gold dividers between sections, a
  framed callout for the one key fact (prayer times, schedule, donation details).

### Slides

- Ivory slides framed by a thin gold border 96px inside the edge, with a star at the top center.
- Centered titles at 64px in El Messiri; body at 30px; one framed fact or an arch-shaped image per slide.
- Section openers use the deep blue theme with a pattern band across the bottom 20%.

### Social

- 1080 x 1350, centered: an arch or framed panel holding the greeting or message, a gold divider, the
  details at 36px or more.
- Deep blue theme for evening posts, ivory for daytime announcements.
- Bilingual posts put the Latin and Arabic lines on the same axis, the same size and weight.

### App

- Follow the system theme with ivory and deep blue.
- Lists on cards with gold 1px separators; one primary button per screen in `--accent`.
- Pattern only on the header or an empty state, never behind list text.

## Outside CSS

| CSS effect | Replacement |
| --- | --- |
| Star `clip-path` corner pieces | an eight-point star vector (two squares rotated 45 degrees) |
| `--gold-rule` gradient | a gold line with tapered ends, or a plain 2px gold line |
| `--arch-radius` | an arch vector mask (semicircle on top of a rectangle) |
| Pattern background tile | a repeating pattern fill at 6 to 8% opacity |
| `color-mix()` hover halo | a 4px gold outer stroke at 35% opacity |

## Contrast rules (checked)

| Text | On | Theme | Ratio | Rule |
| --- | --- | --- | --- | --- |
| `--text` | `--page` | light | 9.90 | Blue ink on ivory. |
| `--text-muted` | `--card` | light | 6.83 | Secondary text. |
| `--on-accent` | `--accent` | light | 9.90 | Ivory on blue buttons. |
| `--gold` | `--page` | light | 1.96 | Gold is never text on ivory; ornament only. |
| `--gold` | `--accent` | light | 5.06 | Gold text is fine on lapis blue. |
| `--emerald` | `--page` | light | 5.65 | Emerald status text, light theme only. |
| `--danger` | `--page` | light | 7.49 | Error text. |
| `--text` | `--page` | dark | 12.40 | Ivory ink on deep blue. |
| `--text-muted` | `--card` | dark | 5.52 | Secondary text on dark cards. |
| `--on-accent` | `--accent` | dark | 6.33 | Deep blue on gold buttons. |
| `--link` | `--page` | dark | 9.48 | Light gold links. |
| `--danger` | `--card` | dark | 4.73 | Error text on dark cards. |

## Pitfalls

- Religious text (verses, sacred names, calligraphy of scripture) used as decoration. Never.
- Mosque photos or domes as decoration for unrelated products.
- Pattern everywhere. One patterned surface per screen, at 8% opacity or less, never behind body text.
- Gold text on ivory; it fails contrast.
- Neon or saturated modern colors, pure black backgrounds, cartoon or handwritten fonts.
- Asymmetric, scattered layouts; this style needs a clear center.
- Emerald and deep red together on one page; pick one as the accent.

## Checklist

- [ ] The page uses lapis blue, ivory and gold, plus at most one of emerald or deep red.
- [ ] Ornament sits on frames, dividers, corners or one background surface, never behind body text.
- [ ] Layouts are centered and symmetrical.
- [ ] Headings use El Messiri; body uses Noto Sans at a relaxed line height.
- [ ] No gold text on ivory.
- [ ] No sacred text, verses or mosque imagery used as decoration.
- [ ] Both themes are complete and pass the contrast table.
- [ ] Focus shows a gold outline; transitions are slow and symmetric.
