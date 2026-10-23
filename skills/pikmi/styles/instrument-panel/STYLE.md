# Instrument Panel

## Identity

Pocket electronic instruments treated as playful tools: few controls with one job each, a small screen,
honest materials and one joke. Translate the object, not the music: any product can become a panel.

Fits tools, dashboards, product launches, audio and maker brands, and playful technology. Avoid it for
long-form reading, luxury or organic brands, and anything that needs softness and warmth.

Two editions: light (aluminium) by default, black for dark requests and social posts.

Dial: ENERGY 2 / RHYTHM 2 / MOTION 1

## Visual vocabulary

- **Material.** 90% greys (aluminium `#E5E5E5`, black `#0F0E12`, graphite `#272727`), under 10% signal
  color. Orange `#F05A24` is the voice. Blue, green and yellow appear only as encoder caps and status
  lights.
- **Type in three voices.** Thin lowercase sans for speech (Noto Sans JP 200 to 300); uppercase tracked
  labels like print on a panel (500, 1.5px tracking); dot-matrix numbers on small screens (Doto 700 to
  900, 18px and up). Orange katakana is a second accent, one or two words beside a label: on black, or on
  light grey only when large and only on `--card`.
- **Details.** Model numbers with an en dash (TP–01), numbered sections and keys (01, 02), registration
  crosses and small technical labels in corners, one starburst sticker rotated about -8 degrees.
- **Depth.** A hard 2px key travel (`--key-travel`) and flat tones. No soft shadows, gloss, gradients or
  textures. The knurled encoder ring is the one drawn pattern.

## Reasons

- **Color:** greys let one orange carry every decision; signal colors name parameters, so they stay on
  encoders and lights.
- **Typography:** three voices keep speech, printed labels and readouts apart, the way a device separates
  its casing, its print and its screen.
- **Layout:** controls grouped on panels, keys tucked into the corners, so each panel reads as one device
  doing one task.
- **Shape:** 4px keys inside 12px panels read as machined parts; circles are reserved for the one main
  button and the encoders.
- **Depth:** the 2px key travel marks what can be pressed; nothing else is raised.
- **Motion:** a press moves the key down 2px and nothing more, so the interface feels mechanical rather
  than animated.
- **Theme:** the light edition is the product's default look; the black edition exists for dark contexts
  and posts, and both are complete.

## Token usage

Use the role tokens, never raw colors, so switching edition never turns a dark key white.

| Token | Role |
| --- | --- |
| `--page`, `--panel`, `--card`, `--rule` | page, device body, inset cards, 1px rules |
| `--text`, `--text-muted`, `--link`, `--danger` | text roles |
| `--accent`, `--on-accent` | signal orange and the black ink that sits on it |
| `--key`, `--key-label`, `--key-number`, `--key-shadow` | a resting key |
| `--key-alt*` | the black alt key (shift functions, the active range) |
| `--key-active*` | the pressed or selected key |
| `--screen`, `--on-screen`, `--screen-bezel` | the small black screen |
| `--signal-blue`, `--signal-green`, `--signal-yellow`, `--led` | encoder caps and status lights only |
| `--key-travel`, `--tracking-label`, `--radius-*`, `--space-*`, `--type-*` | shape, spacing and type |

## Components

| Hardware | UI |
| --- | --- |
| Numbered key (number bottom-left, label top-right) | segmented control, tab, nav item, filter |
| Two-function key (action on top, shift action in orange on a black lower half) | action plus secondary action |
| Encoder (ring plus colored cap) | slider or stepper; the cap color names the parameter |
| Big round orange button | the one primary action (record, send, export) |
| Small black screen | readout, hero number, status |
| Slide switch plus LED | toggle and live state |
| Black pill plus text link | the web CTA pair |
| Starburst sticker | one surprise per screen (new, beta, sale) |

```css
.key {
  display: flex; flex-direction: column; justify-content: space-between;
  min-height: 44px; padding: 6px 8px; border-radius: var(--radius-key);
  background: var(--key); box-shadow: var(--key-travel) var(--key-shadow);
}
.key .label { align-self: flex-end; font: 500 var(--type-label)/1 var(--font-sans);
  letter-spacing: var(--tracking-label); text-transform: uppercase; color: var(--key-label); }
.key .number { font: 300 16px/1 var(--font-sans); color: var(--key-number); }
.key:active { transform: translateY(2px); box-shadow: none; }
.key[aria-pressed="true"] { background: var(--key-active); box-shadow: var(--key-travel) var(--key-active-shadow); }
.key[aria-pressed="true"] * { color: var(--key-active-ink); }
.key.alt { background: var(--key-alt); box-shadow: var(--key-travel) var(--key-alt-shadow); }
.key.alt .label { color: var(--key-alt-label); } .key.alt .number { color: var(--key-alt-number); }
.key:focus-visible { outline: 2px solid var(--text); outline-offset: 2px; }

.panel { background: var(--panel); border-radius: var(--radius-panel); padding: var(--space-sm); }

.screen {
  background: var(--screen); color: var(--on-screen); border-radius: var(--radius-key);
  box-shadow: inset 0 0 0 2px var(--screen-bezel);
}
.screen .value { font: 900 64px/1 var(--font-dot); }
.screen .unit { font: 700 20px/1 var(--font-dot); color: var(--accent); }

.encoder { width: 40px; aspect-ratio: 1; border-radius: 50%; display: grid; place-items: center;
  background: repeating-conic-gradient(var(--encoder-ring) 0 5deg, var(--encoder-groove) 5deg 10deg); }
.encoder::after { content: ""; width: 24px; aspect-ratio: 1; border-radius: 50%;
  background: var(--cap, var(--signal-blue)); box-shadow: inset 0 -2px 3px var(--encoder-cap-shade); }

.cta { background: var(--text); color: var(--page); border-radius: var(--radius-pill); padding: 12px 26px;
  font: 300 16px var(--font-sans); }
.link { color: var(--link); }
[data-theme="dark"] .link { text-decoration: underline; }

.sticker { width: 96px; aspect-ratio: 1; display: grid; place-items: center; rotate: -8deg;
  background: var(--accent); color: var(--on-accent); font: 900 18px/1 var(--font-dot); text-align: center;
  clip-path: polygon(50% 0, 57.8% 10.8%, 69.1% 3.8%, 72.2% 16.7%, 85.4% 14.6%, 83.3% 27.8%, 96.2% 30.9%,
    89.2% 42.2%, 100% 50%, 89.2% 57.8%, 96.2% 69.1%, 83.3% 72.2%, 85.4% 85.4%, 72.2% 83.3%, 69.1% 96.2%,
    57.8% 89.2%, 50% 100%, 42.2% 89.2%, 30.9% 96.2%, 27.8% 83.3%, 14.6% 85.4%, 16.7% 72.2%, 3.8% 69.1%,
    10.8% 57.8%, 0 50%, 10.8% 42.2%, 3.8% 30.9%, 16.7% 27.8%, 14.6% 14.6%, 27.8% 16.7%, 30.9% 3.8%, 42.2% 10.8%); }
```

Nesting: a panel with keys at its corners uses 8px padding so `radius-key + padding = radius-panel`
(4 + 8 = 12). Content panels without corner keys can use 12 to 24px. A round button is a circle, not a
pill-radius box at a panel corner.

## Recipes

### UI

- **Dashboard.** A side panel with numbered nav keys and a live switch; a thin lowercase title with an
  inline section label (`01 · overview` in label type, on the same line or the panel edge); time range as
  a row of keys, the active one an alt key; one screen with the main number and a bar chart (plain bars,
  the highlighted one orange); small readouts on cards; a table with uppercase 12px headers, 1px rule
  rows, right-aligned numbers, status as an LED plus a word. Orange goes to one control group (the active
  nav key) plus the highlighted bar.
- **Landing page.** Lowercase nav with a small black pill; a technical label with a model number and an
  optional katakana tag (orange on a black chip); a thin centered headline (display 88px, weight 200); one
  body line in `--text-muted`; black pill plus text link; the product's own UI drawn as a device as the
  hero image, with one sticker; a spec row of Doto numbers over uppercase labels, below a 1px rule.

### Slides

- `--panel` as the slide background, one screen per slide holding the key number in Doto at 160px or
  more, its unit in orange.
- Titles thin lowercase at 64px; a numbered key (01, 02) in the top-left corner as the section marker.
- One orange element per slide: the highlighted bar, the unit, or one sticker on the opening slide.
- No transitions; a cut between slides is the panel's own rhythm.

### Social

- 1080 x 1350, black edition by default.
- One giant Doto number, one thin sentence, two or three keys as ornament.
- Technical labels (28 to 32px) and registration crosses in the corners, an optional sticker.

### App

- Bottom navigation as up to five numbered keys at least 44pt tall; the current one is the active key.
- The one primary action is the round orange button; choices are a row of keys; values sit on a small
  screen; toggles are a slide switch plus LED.
- Follow the system theme with the light and black editions.

## Outside CSS

| CSS effect | Replacement |
| --- | --- |
| Starburst `clip-path` | a 32-point star vector shape, rotated -8 degrees |
| Encoder `repeating-conic-gradient` | a grey circle with 36 thin radial tick lines in `--encoder-groove` |
| Key travel `box-shadow` | a flat offset shadow (distance 2pt, blur 0, straight down) or a 2px darker bottom edge |
| Screen inset bezel | a 2px inner stroke in `--screen-bezel` |
| Encoder cap inner shade | a subtle darker lower crescent, or omit |

## Contrast rules (checked)

| Text | On | Theme | Ratio | Rule |
| --- | --- | --- | --- | --- |
| `--on-accent` | `--accent` | light | 5.67 | Orange is a fill with black text. |
| `#FFFFFF` | `--accent` | light | 3.39 | White on orange fails; never use it. |
| `--accent` | `--screen` | light | 5.67 | Orange text is fine on black. |
| `--accent` | `--card` | light | 3.11 | Orange text on light grey: large text only, and only on `--card`. |
| `--accent` | `--page` | light | 2.97 | Never orange text on `--page`. |
| `--accent` | `--panel` | light | 2.69 | Never orange text on `--panel`. |
| `--accent` | `--panel` | dark | 4.41 | On the dark panel orange text is large only. |
| `--link` | `--page` | light | 4.51 | Blue links pass on the light page. |
| `--link` | `--card` | light | 4.72 | Blue links pass on light cards; not on graphite, so dark links are underlined light text. |
| `--danger` | `--key` | dark | 4.39 | Keep dark error text on panels and cards, not on keys. |

## Pitfalls

- Orange creep: a second orange control group, orange text on light grey, orange backgrounds.
- Texture, gloss, gradients or soft shadows instead of flat tones and key travel.
- Doto for body text or numbers under 18px; labels under 11px (12px in dense dashboards, 28px on
  1080-wide posts).
- Copying a real device: no logo, wordmark, product names or photos of real hardware.
- Turning the section label into a pill badge above the headline. It is print on the panel, inline.
- A readout with invented numbers. The screen shows real values or a marked placeholder.

## Checklist

- [ ] Orange marks one control group per screen, as a fill with black text.
- [ ] Controls are objects: numbered keys for choices and navigation, encoders for values, one round
      button for the main action.
- [ ] The main number sits on a small black screen in Doto at 18px or larger, its unit in orange.
- [ ] Labels are uppercase, tracked and at the minimum size for the medium.
- [ ] Depth comes only from the 2px key travel and flat tones.
- [ ] Two families only: Noto Sans JP and Doto.
- [ ] Keys at a panel corner nest: key radius + panel padding = panel radius.
- [ ] At most one playful element; no logo, wordmark or product name.
- [ ] Keyboard focus is visible on every key, and keys are at least 44px tall.
