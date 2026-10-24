# Night Circuit

## Identity

A night city seen through a heads-up display: near-black surfaces, thin cyan strokes, a magenta second
voice and readouts in a narrow mono. The light comes from the interface itself, so the page stays dark and
the signals stay sharp.

Fits games, creative studios, music and event launches, hacker and security tools, and anything that
should feel electric at night. Avoid it for healthcare, finance, children, long-form reading, and any
brand that needs to feel calm or warm.

Dark only.

Dial: ENERGY 3 / RHYTHM 2 / MOTION 2

## Visual vocabulary

- **Color.** Near-black `#0A0A0F` page, slightly lifted panels and cards. Cyan `#00F0FF` is the primary
  signal (actions, focus, live data). Magenta `#FF2BD6` is the second voice (highlights, a selected
  state). Yellow `#FACC15` appears once, for warnings.
- **Strokes.** 1px lines in deep teal `--rule`, brightening to cyan on hover and focus. Corners are almost
  square: 2px on controls, 4px on panels.
- **Type.** Chakra Petch for headings, body and buttons: angular cuts, uppercase for headings and
  labels with wide tracking. Share Tech Mono only for numbers, codes, timestamps and data labels.
- **Light.** One glow on the primary call to action and one on a live indicator. Everything else is lit
  by color, not blur.
- **Texture.** A faint scanline on one surface per screen, usually the hero readout.

## Reasons

- **Color:** a dark page makes saturated cyan and magenta read as emitted light; two signals plus one
  warning color keep the palette within three hues.
- **Typography:** Chakra Petch's cut corners echo machined HUD frames while staying readable at body
  size; the narrow mono separates data from speech.
- **Layout:** framed panels with corner labels read as screens inside a cockpit, so each block has an
  obvious edge and purpose.
- **Shape:** near-square corners keep the look technical; soft rounding would read friendly.
- **Depth:** depth comes from light (stroke brightness and one glow), not from shadows, which vanish on
  black anyway.
- **Motion:** fast, raw transitions (100 to 150ms) and a glitch offset on press feel like hardware
  responding, not like a page animating.
- **Theme:** the style is defined by emitted light on darkness; a light version would lose its reason to
  exist.

## Token usage

| Token | Role |
| --- | --- |
| `--page`, `--panel`, `--card` | night background, framed panels, raised cards |
| `--rule` | 1px strokes at rest |
| `--text`, `--text-muted` | body text, secondary text and captions |
| `--accent`, `--on-accent` | cyan actions and the near-black ink on cyan fills |
| `--link` | cyan links, always underlined |
| `--neon-magenta` | highlights and the selected state |
| `--neon-yellow` | warnings only |
| `--danger` | errors |
| `--glow` | the one or two glowing elements per screen |
| `--scanline` | the scanline texture on one surface |
| `--font-display`, `--font-mono` | speech and data |

## Components

```css
.btn {
  min-height: 44px; padding: 0 var(--space-lg); border: 1px solid var(--accent); border-radius: var(--radius-key);
  background: transparent; color: var(--accent);
  font: 600 14px/1 var(--font-display); letter-spacing: var(--tracking-label); text-transform: uppercase;
  transition: background-color 120ms ease-out, color 120ms ease-out;
}
.btn:hover { background: var(--accent); color: var(--on-accent); }
.btn.primary { background: var(--accent); color: var(--on-accent); box-shadow: var(--glow); }
.btn:active { transform: translate(2px, -1px); background: var(--neon-magenta); color: var(--on-accent); border-color: var(--neon-magenta); }
.btn:focus-visible, .field:focus-visible { outline: 2px solid var(--neon-magenta); outline-offset: 2px; }

.frame {
  position: relative; background: var(--panel); border: 1px solid var(--rule); border-radius: var(--radius-panel);
  padding: var(--space-lg);
}
.frame:hover { border-color: var(--accent); }
.frame .corner { position: absolute; top: -0.6em; left: var(--space-md); padding: 0 var(--space-xs);
  background: var(--page); font: 400 var(--type-label)/1 var(--font-mono); letter-spacing: var(--tracking-label);
  text-transform: uppercase; color: var(--accent); }

.readout { background: var(--card); background-image: var(--scanline); border: 1px solid var(--rule);
  border-radius: var(--radius-panel); padding: var(--space-lg); font-family: var(--font-mono); }
.readout .value { font-size: 64px; line-height: 1; color: var(--text); font-variant-numeric: tabular-nums; }
.readout .unit { color: var(--accent); }

.field { min-height: 44px; width: 100%; background: var(--card); color: var(--text); border: 1px solid var(--text-muted);
  border-radius: var(--radius-key); padding: 0 var(--space-md); font: 400 16px var(--font-mono); }
.field:focus { border-color: var(--accent); }

.live { display: inline-flex; align-items: center; gap: var(--space-sm); font: 400 var(--type-label)/1 var(--font-mono);
  text-transform: uppercase; letter-spacing: var(--tracking-label); color: var(--text); }
.live::before { content: ""; width: 8px; height: 8px; background: var(--accent); box-shadow: var(--glow); }
@media (prefers-reduced-motion: no-preference) { .live::before { animation: pulse 2.4s ease-in-out infinite; } }
@keyframes pulse { 50% { opacity: 0.35; } }

.tag { display: inline-block; padding: 2px var(--space-sm); border: 1px solid var(--neon-magenta);
  color: var(--neon-magenta); font: 400 var(--type-label)/1.4 var(--font-mono); text-transform: uppercase; }
.warn { color: var(--neon-yellow); }
```

## Recipes

### UI

- **Landing page.** A full-width hero frame on `--page`; the headline in uppercase Chakra Petch 700
  (56 to 96px) with one word in cyan; one line of body in `--text-muted`; a primary button with the glow
  and a secondary outline button. Below it, a readout with the scanline showing one real product value,
  and a row of framed feature panels with mono corner labels (`SYS.01`).
- **Dashboard.** Framed panels on a 12-column grid; one readout panel as the focal point; tables with
  mono numbers right-aligned and 1px rules; the live indicator next to whatever updates in real time;
  magenta only for the selected row or filter.

### Slides

- Background `--page`, a 1px frame inset 96px from the edges with a mono label in its top-left corner.
- One idea per slide: an uppercase title at 72px and either one readout (number at 200px in mono) or one
  diagram drawn in 2px cyan lines.
- Magenta marks the single most important word or data point; yellow only on a slide about risks.
- The scanline only on the title slide.

### Social

- 1080 x 1350 on `--page`: one giant mono number or one uppercase phrase, a framed corner label at 28px,
  and a thin cyan crop-mark frame.
- One glow at most, on the key word or number.
- A carousel keeps the same frame and moves the corner label (`01/05`, `02/05`).

### App

- Dark app with `--panel` screens and `--card` list rows separated by 1px rules.
- The one primary action is a cyan filled button with the glow; everything else is outlined.
- Tab bar icons in 1.5px cyan strokes; the active tab adds a magenta underline.
- Haptic or visual feedback on press uses the glitch offset, never a bounce.

## Outside CSS

| CSS effect | Replacement |
| --- | --- |
| `--glow` box-shadow | an outer glow (cyan, 50% opacity, 20px), or a second 1px cyan stroke 3px outside the shape |
| Text glow | skip it; use cyan text on black instead |
| `--scanline` gradient | a tiled 1 x 3px pattern image at 4% white, or omit |
| Glitch press offset | move the element 2px right and 1px up for one frame, or a magenta color flash |
| Pulse animation | a static cyan dot; native apps follow reduce-motion |

## Contrast rules (checked)

| Text | On | Theme | Ratio | Rule |
| --- | --- | --- | --- | --- |
| `--text` | `--page` | dark | 18.30 | Body text. |
| `--text-muted` | `--card` | dark | 7.08 | Secondary text holds on cards. |
| `--on-accent` | `--accent` | dark | 14.02 | Cyan fills always carry near-black text, never white. |
| `--accent` | `--card` | dark | 12.76 | Cyan text and links on cards. |
| `--neon-magenta` | `--page` | dark | 6.18 | Magenta text passes on the page. |
| `--on-accent` | `--neon-magenta` | dark | 6.18 | The press flash is a magenta fill with near-black text; magenta text on a cyan fill is only 2.27. |
| `--neon-yellow` | `--page` | dark | 12.90 | Warnings. |
| `--danger` | `--card` | dark | 6.12 | Error text on cards. |
| `--neon-magenta` | `--page` | dark | 6.18 | Focus ring (magenta outline). |
| `--text-muted` | `--card` | dark | 7.08 | Field border at rest; it turns cyan on focus. |

## Pitfalls

- Glow on everything. Two glowing elements per screen at most: the primary action and a live indicator.
- White text on cyan. Cyan fills take `--on-accent`.
- All-mono pages. Mono is for data; headings and body stay in Chakra Petch.
- Purple-to-blue gradients or neon gradient backgrounds. Color lives in strokes, text and small fills.
- Endless flicker. Only a real live indicator pulses, and it stops under reduced motion.
- Scanlines or grids on every panel. One textured surface per screen.
- A fake terminal window as the hero. Show the real product or a real readout.
- Rounded corners above 4px; they turn the cockpit into a toy.

## Checklist

- [ ] The page is near-black and the palette is cyan, magenta and at most one yellow warning.
- [ ] Exactly one or two elements carry `--glow`.
- [ ] Cyan fills use `--on-accent` text.
- [ ] Mono appears only on numbers, codes and data labels.
- [ ] Corners are 2px on controls and 4px on panels.
- [ ] Transitions run 100 to 150ms; press uses the offset, not a scale.
- [ ] The scanline sits on one surface only.
- [ ] Focus is visible (magenta outline) and every control is at least 44px tall.
- [ ] No brand names, logos or game titles in the design.
