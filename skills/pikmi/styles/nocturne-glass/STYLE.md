# Nocturne Glass

## Identity

A city at night seen through a rain-washed window. A deep ink scene with two or three soft wells of
moonlight carries all the color; most surfaces are solid night steel; and one or two pieces of
colorless frosted glass catch the light where it matters. A single champagne accent marks the action.
Quiet luxury: composed, cinematic and believable, never the generic purple glass of AI templates.

Fits premium consumer products, hospitality and hotels, fashion and jewelry, audio and film, finance
products that want to feel high-end, event invitations and launch pages. Avoid it for children's
products, dense data tools, accessibility-first public services and anything playful.

Dark only.

Dial: ENERGY 2 / RHYTHM 2 / MOTION 2

## Visual vocabulary

- **Scene.** Page `#0B1322` (deep ink) with two or three large radial light wells in moonlight `#7C9CC4`
  and moon steel `#33517A`, plus an optional faint warm well of champagne. Edges fade to night deep
  `#060A13`. A film grain at 2.5% removes the plastic look.
- **Surfaces.** Most panels are solid night steel `#16233A` with a 1px rule. Glass is reserved for one or
  two focal elements per screen: colorless white at 8% (`--glass-fill`), a 40px blur with a saturation
  boost, a lit top edge and a shaded bottom edge (`--glass-shadow`).
- **Accent.** Champagne `#E4B863` on the primary action and key numbers; champagne bright `#F3DCA8` for
  links and highlighted words. Nothing else is colored.
- **Type.** Bodoni Moda 500 for headings and big numbers, with hairline contrast like engraved glass;
  Albert Sans for body and interface text.
- **Shape.** 16px controls, 24px cards and glass.

## Reasons

- **Color:** the scene owns the color and the glass stays neutral, which is how real glass behaves; a
  single champagne accent keeps it luxurious instead of colorful.
- **Typography:** a high-contrast didone reads as premium and editorial; a clean geometric sans keeps
  the interface quiet.
- **Layout:** solid panels hold most content so the one or two glass elements become the focal point.
- **Shape:** generous radii make glass feel like a polished pane; sharp corners would read as a cut
  sheet.
- **Depth:** real depth comes from blur over the scene and a lit edge, used sparingly, plus a deep
  shadow under glass only.
- **Motion:** slow, decelerating transitions (500ms, `--ease-glass`) feel like heavy glass settling.
- **Theme:** the style depends on light wells in darkness; a light version would have nothing to
  refract.

## Token usage

| Token | Role |
| --- | --- |
| `--page`, `--night-deep` | the night scene and its edges |
| `--moonlight`, `--moon-steel` | light well colors only |
| `--panel`, `--card`, `--rule` | solid night-steel surfaces and their rules |
| `--text`, `--text-muted` | white text and secondary text (secondary only on solid surfaces) |
| `--accent`, `--on-accent` | champagne primary action with ink text |
| `--link`, `--champagne-bright` | links and highlighted words |
| `--glass-fill`, `--glass-border`, `--glass-blur`, `--glass-shadow` | the one or two glass elements |
| `--ease-glass`, `--grain-opacity` | motion curve and film grain |
| `--danger` | error text |

## Components

```css
.scene { background:
  radial-gradient(560px circle at 85% 10%, rgba(124, 156, 196, 0.28), transparent 65%),
  radial-gradient(520px circle at 10% 90%, rgba(51, 81, 122, 0.35), transparent 65%),
  var(--page); }

.panel { background: var(--panel); border: 1px solid var(--rule); border-radius: var(--radius-card); padding: var(--space-lg); }

.glass { position: relative; background: var(--glass-fill); border: 1px solid var(--glass-border); border-radius: var(--radius-card);
  backdrop-filter: blur(var(--glass-blur)) saturate(180%); -webkit-backdrop-filter: blur(var(--glass-blur)) saturate(180%);
  box-shadow: var(--glass-shadow); padding: var(--space-lg); color: var(--text);
  transition: transform 500ms var(--ease-glass), border-color 500ms var(--ease-glass); }
.glass::before { content: ""; position: absolute; inset: 0; border-radius: inherit; pointer-events: none;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.12), transparent 40%); }
.glass:hover { transform: translateY(-4px); border-color: rgba(255, 255, 255, 0.3); }

.btn { min-height: 48px; padding: 0 var(--space-lg); border: 0; border-radius: var(--radius-control);
  background: var(--accent); color: var(--on-accent); font: 500 16px/1 var(--font-body);
  transition: transform 500ms var(--ease-glass); }
.btn:hover { transform: translateY(-2px); }
.btn:active { transform: scale(0.97); transition-duration: 150ms; }
.btn.quiet { background: transparent; color: var(--text); box-shadow: inset 0 0 0 1px var(--glass-border); }
.btn:focus-visible, .field:focus-visible { outline: 2px solid var(--champagne-bright); outline-offset: 3px; }

.figure { font: 500 var(--type-h1)/1 var(--font-display); color: var(--accent); }
.field { min-height: 48px; width: 100%; padding: 0 var(--space-md); border: 1px solid var(--text-muted); border-radius: var(--radius-control);
  background: var(--panel); color: var(--text); font: 400 16px var(--font-body); }
.grain { position: fixed; inset: 0; pointer-events: none; opacity: var(--grain-opacity);
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E"); }
@media (prefers-reduced-motion: reduce) { .glass, .btn { transition: none; } }
```

Text on glass is always white (`--text`). Secondary text belongs on solid panels: over the brightest
light well, glass drops secondary text below 4.5:1.

## Recipes

### UI

- **Landing page.** The night scene fills the hero; a large Bodoni headline in white, one line of body,
  a champagne button and a quiet button. One glass card floats over the brightest light well holding the
  key detail (price, date, availability). Sections below sit on solid panels: features as plain text
  blocks with champagne numerals, an image strip, a final call to action.
- **App-like pages.** Solid panels for every list and form; one glass element at most, such as the
  sticky checkout dock or a now-playing bar.

### Slides

- Every slide sits on the night scene with the light wells in different positions per section.
- Bodoni titles at 72px, body at 28px in Albert Sans; key numbers in champagne at 160px.
- One glass card per slide at most, holding a quote or a key figure.
- Slow 600ms fades.

### Social

- 1080 x 1350: the night scene, one glass pane centered over a light well, a Bodoni headline inside it
  and one champagne detail.
- Keep the copy short; white text only on the glass.

### App

- Night-steel screens; native blur material for the one glass element (tab bar or player bar).
- One champagne primary action per screen.
- Respect reduced transparency: replace glass with a solid `--panel` when the system asks.

## Outside CSS

| CSS effect | Replacement |
| --- | --- |
| `backdrop-filter` glass | a flat white fill at 8% over the scene, plus a 1px lighter top edge; on native, the system thin material |
| `--glass-shadow` layered insets | an outer shadow (16pt down, 40pt blur, 50% ink) and a 1px light top stroke |
| Radial light wells | radial gradient fills, or a blurred background image |
| Film grain | a noise texture at 2 to 3% opacity, or omit |
| `--ease-glass` | the platform's decelerate easing |

## Contrast rules (checked)

| Text | On | Theme | Ratio | Rule |
| --- | --- | --- | --- | --- |
| `--text` | `--page` | dark | 18.58 | White on the night scene. |
| `--text-muted` | `--panel` | dark | 6.79 | Secondary text on solid panels. |
| `--on-accent` | `--accent` | dark | 10.03 | Ink text on champagne buttons. |
| `--accent` | `--panel` | dark | 8.49 | Champagne numbers and words on panels. |
| `--link` | `--page` | dark | 13.81 | Champagne-bright links. |
| `--danger` | `--panel` | dark | 6.58 | Error text. |
| `rgba(255,255,255,0.6)` | `--page` | dark | 7.14 | 60% white text still passes on the plain scene. |
| `--text-muted` | `rgba(124, 156, 196, 0.32)` | dark | 4.62 | Keep moonlight wells at 32% or less so secondary text on the bare scene passes. |
| `--text` | `#3C495D` | dark | 9.12 | White on glass over the brightest light well. |
| `--text-muted` | `#3C495D` | dark | 3.94 | Secondary text fails on glass over a light well; keep it on panels. |

## Pitfalls

- Glass everywhere: navbar, cards, modals and sidebar all frosted. One or two glass elements per screen.
- Tinted glass (purple, blue, pink fills). Glass is colorless; color comes from the scene.
- Purple-to-pink or blue-to-purple gradients. The scene is ink and moonlight.
- Glass on a flat background; with nothing behind it, it reads as a grey box.
- Glass opacity above 15%; it turns into a solid block.
- More than one accent color, or champagne on everything.
- Secondary or small text on glass.
- Fast, snappy transitions.

## Checklist

- [ ] The background is a deep ink scene with two or three soft light wells, no purple.
- [ ] Glass appears on one or two focal elements only; other surfaces are solid panels.
- [ ] Glass is colorless (white at 5 to 12%), blurred and has a lit top edge.
- [ ] Champagne marks only the primary action, key numbers and links.
- [ ] Text on glass is white; secondary text stays on panels.
- [ ] Headings and figures use Bodoni Moda; interface text uses Albert Sans.
- [ ] Transitions use the slow glass curve and stop under reduced motion.
- [ ] Reduced transparency falls back to solid panels.
