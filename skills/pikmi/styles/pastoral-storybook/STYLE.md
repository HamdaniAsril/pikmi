# Pastoral Storybook

## Identity

The calm of a hand-drawn animated film set in the countryside: cream paper, sage fields, a wide sky, soft
rounded shapes and small details from nature. It is warm and unhurried, and it feels made by a person
with a brush rather than generated.

Fits children's and family products, wellbeing and slow-living brands, cafes and bakeries, travel and
outdoor stories, picture books, community projects and gentle onboarding. Avoid it for finance, security,
developer tools, high-density dashboards and anything that must feel fast or technical.

Light only.

Dial: ENERGY 2 / RHYTHM 2 / MOTION 2

## Visual vocabulary

- **Color.** Cream paper `#F4E4BC`, lighter cream panels and cards, warm brown ink `#5A4A3A`. Sage
  `#7CB9A8` and sky `#85CDCA` are the core pair; coral `#E8A87C` is the accent (rose `#C38D94` can replace
  it). Text on colored fills uses the dark bark brown `#2F2A22`.
- **Shape.** Generous radii: 24px cards, 32px panels, pill shapes only for buttons and tags.
- **Type.** Kaisei Decol for headings, a warm serif with brush-like terminals; Zen Maru Gothic for body,
  a rounded sans that stays readable at small sizes.
- **Nature details.** Clouds, leaves, hills and small creatures drawn as simple soft shapes, in the
  background layer, related to the content (a leaf beside "garden", a cloud near "weather").
- **Depth.** A soft warm shadow on raised cards only; gentle vertical gradients in skies and hills.

## Reasons

- **Color:** cream and brown read as paper and ink, sage and sky as fields and air; one warm accent keeps
  the page from turning into a pastel sampler.
- **Typography:** a brush-flavored serif for headings gives the storybook voice; a rounded sans keeps
  body text easy for every age.
- **Layout:** wide margins and few elements per section let the scene breathe, like a frame in a picture
  book.
- **Shape:** large radii feel safe and hand-made; reserving pills for buttons and tags keeps hierarchy.
- **Depth:** soft shadows mark the few things you can pick up; the rest lies flat on the paper.
- **Motion:** slow, small movements (500 to 700ms, up to 2px and 1 degree) feel like a breeze rather
  than an interface reacting.
- **Theme:** the style is daylight on paper; a dark version would lose its warmth.

## Token usage

| Token | Role |
| --- | --- |
| `--page`, `--panel`, `--card`, `--rule` | paper, lighter paper, cards, soft rules |
| `--text`, `--text-muted` | brown ink and secondary ink |
| `--accent`, `--on-accent` | sage buttons and the bark text on them |
| `--sky`, `--coral`, `--rose` | scenery, illustrations and one accent |
| `--bark` | text on any colored fill |
| `--link`, `--danger` | deep sage links, earthy red errors |
| `--soft-shadow` | raised cards only |
| `--radius-pill`, `--radius-card`, `--radius-panel` | buttons and tags, cards, panels |

## Components

```css
.btn { min-height: 48px; padding: 0 var(--space-lg); border: 0; border-radius: var(--radius-pill);
  background: var(--accent); color: var(--on-accent); font: 700 17px/1 var(--font-body);
  transition: transform 600ms ease-in-out; }
.btn:hover { transform: translateY(-2px) rotate(-1deg); }
.btn:active { transform: scale(0.98); }
.btn.warm { background: var(--coral); color: var(--bark); }
.btn:focus-visible, .field:focus-visible { outline: 3px solid var(--link); outline-offset: 3px; }

.card { background: var(--card); border-radius: var(--radius-card); padding: var(--space-lg); box-shadow: var(--soft-shadow); }
.panel { background: var(--panel); border-radius: var(--radius-panel); padding: var(--space-lg); }
.tag { display: inline-block; padding: 4px 12px; border-radius: var(--radius-pill); background: var(--sky);
  color: var(--bark); font: 500 var(--type-label)/1.4 var(--font-body); }

h1, h2, h3 { font-family: var(--font-display); font-weight: 700; color: var(--text); }
.field { min-height: 48px; width: 100%; padding: 0 var(--space-md); border: 2px solid var(--rule);
  border-radius: 16px; background: var(--card); color: var(--text); font: 400 17px var(--font-body); }

.hill { background: linear-gradient(180deg, var(--accent), #5E9E8C); border-radius: 50% 50% 0 0 / 100% 100% 0 0; }
.cloud { background: var(--card); border-radius: var(--radius-pill); opacity: 0.9; }
@media (prefers-reduced-motion: reduce) { .btn { transition: none; } }
```

## Recipes

### UI

- **Landing page.** A sky band (`--sky` fading into `--panel`) with two soft clouds and a line of sage
  hills at the bottom; the headline in Kaisei Decol sits in the sky in `--text`, one sentence below, a
  sage pill button and a text link in `--bark` (sage links fail on the sky). Sections below alternate: a story paragraph beside a single illustration, a row
  of three cards with small nature icons, a quote on a lighter panel.
- **App-like screens.** Lists on `--card` with 24px corners and generous padding; one sage primary
  button; illustrations only in empty states and onboarding.

### Slides

- Cream background with a low band of hills along the bottom 15% and one cloud.
- Headings in Kaisei Decol at 64px, one short paragraph at 30px, or one illustration with a caption.
- Use sky and sage for scenery, coral for the one highlighted word or figure.
- Slow fade transitions (600ms) at most.

### Social

- 1080 x 1350: a scene (sky, hills, one creature or object), a heading at 72px and one sentence at 40px
  on a cream card with 32px corners.
- Keep body text on a flat cream card; only a short heading in `--text` or `--bark` may sit on the sky.
- A carousel walks through the scene: morning, noon, evening, using the same frame.

### App

- Cream background, cards with 24px corners, pill buttons at least 48pt tall.
- Bottom navigation with simple rounded icons and labels in Zen Maru Gothic.
- Empty states carry the illustrations; working screens stay light and readable.

## Outside CSS

| CSS effect | Replacement |
| --- | --- |
| Hill gradient and elliptical `border-radius` | a vector hill shape with a two-stop vertical gradient, or flat sage |
| `--soft-shadow` | a soft drop shadow (8pt down, 30pt blur, 10% brown), or none on native lists |
| Hover rotate and float | omit on touch; keep the 0.98 press |
| Cloud shapes | simple rounded vector blobs at 90% opacity |

## Contrast rules (checked)

| Text | On | Theme | Ratio | Rule |
| --- | --- | --- | --- | --- |
| `--text` | `--page` | light | 6.73 | Body text on paper. |
| `--text` | `--card` | light | 8.15 | Body text on cards. |
| `--text-muted` | `--page` | light | 5.37 | Secondary text. |
| `--on-accent` | `--accent` | light | 6.35 | Sage buttons carry bark text. |
| `--link` | `--page` | light | 5.04 | Links. |
| `--danger` | `--page` | light | 4.58 | Error text. |
| `--bark` | `--coral` | light | 7.00 | Text on coral. |
| `--bark` | `--sky` | light | 7.85 | Text and links on sky. |
| `--text` | `--sky` | light | 4.68 | Brown ink passes even on the darkest stop of the sky. |
| `--link` | `--sky` | light | 3.50 | Sage links fail on the sky; use `--bark` there. |

## Pitfalls

- Every element pill-shaped. Pills are for buttons and tags only.
- Soft shadows on everything. Only raised cards get one.
- A pastel rainbow. Sage and sky plus one accent per page.
- Decoration unrelated to the content, or illustrations that cover text.
- Body text, muted text or sage links over the sky or busy scenery; they fail contrast in parts. Only
  `--text` and `--bark` pass across the whole sky.
- Copying characters, scenes or logos from real films. Draw your own simple shapes.
- Fast, springy or bouncing motion.

## Checklist

- [ ] The page is cream paper with brown ink; sage and sky are the core pair, one accent at most.
- [ ] Headings use Kaisei Decol, body uses Zen Maru Gothic.
- [ ] Only buttons and tags are pill-shaped; cards 24px, panels 32px.
- [ ] Shadows appear only on raised cards.
- [ ] Every nature detail relates to the content and sits behind text.
- [ ] Only headings in `--text` or `--bark` sit on the sky; body text stays on flat cream.
- [ ] Motion is slow and small, and stops under reduced motion.
- [ ] No characters, scenes or names from real films.
