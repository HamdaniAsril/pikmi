---
name: teenage-engineering
description: Visual style for UI and graphics that look like a teenage engineering instrument (OP-1, OP-Z, OP-XY, EP-133 K.O. II, TX-6, pocket operators). Grey panels, numbered keys, encoders, small black screens with dot-matrix numbers, printed uppercase labels and one signal orange, in light or black edition. Use when the request names teenage engineering, one of its products, a synth or instrument-panel look, or "ala teenage engineering" / "kayak OP-1" / "desain seperti synthesizer"; works for dashboards, landing pages, apps and social posts.
---

# Teenage Engineering / instrument panel UI

A Stockholm studio (founded 2005) whose OP–1, field system, pocket operators and EP–133 K.O. II treat
electronics as playful instruments: few controls with one job each, a small screen, honest materials and one
joke. Translate the object, not the music: any product can be a panel.

Tokens live in `tokens.css` (CSS variables, `[data-theme="dark"]` for the black edition) and `tokens.json` (the
same values for other platforms). Use the role tokens (`--key`, `--screen`, `--on-screen`...) rather than raw
colors, so switching theme never turns a dark key white.

## Visual vocabulary

- **Material.** 90% greys (aluminium `#E5E5E5`, black `#0F0E12`, graphite `#272727`), under 10% signal color.
  Orange `#F05A24` is the voice. Blue, green and yellow appear only as encoder caps and status lights.
- **Type in three voices.** Thin lowercase sans for speech (Noto Sans JP 200 to 300); uppercase tracked labels
  like print on a panel (500, 1.5px tracking); dot-matrix numbers on small screens (Doto 700 to 900, 18px and
  up). Orange katakana is a second accent, one or two words beside a label: on black, or on light grey only when
  large and only on `--card`.
- **Details.** Model numbers with an en dash (TP–01), numbered sections and keys (01, 02), registration crosses
  and small technical labels in corners, one starburst sticker rotated about -8 degrees.
- **Depth.** A hard 2px key-travel shadow (`0 2px 0`) and flat tones. No soft shadows, gloss, gradients or
  textures.

## Hardware to UI

| Hardware | UI |
| --- | --- |
| Numbered key (number bottom-left, label top-right) | segmented control, tab, nav item, filter |
| Two-function key (action on top, shift action in orange on a black lower half) | action plus secondary action |
| Encoder (ring plus colored cap) | slider or stepper; the cap color names the parameter |
| Big round orange button | the one primary action (record, send, export) |
| Small black screen | readout, hero number, status |
| Slide switch plus LED | toggle and live state |
| Black pill plus blue text link | the web CTA pair |
| Starburst sticker | one surprise per screen (new, beta, sale) |

## Components

```css
.key {
  display: flex; flex-direction: column; justify-content: space-between;
  padding: 6px 8px; border-radius: var(--radius-key);
  background: var(--key); box-shadow: 0 2px 0 var(--key-shadow);
}
.key .label { align-self: flex-end; font: 500 11px/1 var(--font-sans);
  letter-spacing: var(--label-tracking); text-transform: uppercase; color: var(--key-label); }
.key .number { font: 300 16px/1 var(--font-sans); color: var(--key-number); }
.key[aria-pressed="true"] { background: var(--key-active); box-shadow: 0 2px 0 var(--key-active-shadow); }
.key[aria-pressed="true"] * { color: var(--key-active-ink); }
.key.alt { background: var(--key-alt); box-shadow: 0 2px 0 var(--key-alt-shadow); }
.key.alt .label { color: var(--key-alt-label); } .key.alt .number { color: var(--key-alt-number); }

.panel { background: var(--panel); border-radius: var(--radius-panel); padding: var(--space-sm); }

.screen {
  background: var(--screen); color: var(--on-screen); border-radius: var(--radius-key);
  box-shadow: inset 0 0 0 2px #1c1b20;
}
.screen .value { font: 900 64px/1 var(--font-dot); }
.screen .unit { font: 700 20px/1 var(--font-dot); color: var(--accent); }

.encoder { width: 40px; aspect-ratio: 1; border-radius: 50%; display: grid; place-items: center;
  background: repeating-conic-gradient(#d4d4d4 0 5deg, #bfbfbf 5deg 10deg); }
.encoder::after { content: ""; width: 24px; aspect-ratio: 1; border-radius: 50%;
  background: var(--cap, var(--signal-blue)); box-shadow: inset 0 -2px 3px #0003; }

.cta { background: var(--text); color: var(--page); border-radius: 999px; padding: 12px 26px;
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

Nesting: a panel with keys at its corners uses 8px padding so `radius-key + padding = radius-panel` (4 + 8 = 12).
Content panels without corner keys can use 12 to 24px. A round button is a circle, not a pill-radius box at a
panel corner.

## Black edition

The dark direction (OP–XY, TX–6 black): set `data-theme="dark"` on the root. Roles: page `#0F0E12`, body and
panels `#272727`, keys `#3B3B3D` with a `#000000` key shadow, active key orange, screens `#0F0E12` with `#F5F5F5`
numbers. Use it when the request asks for dark or black, and for social posts by default. Links in dark are
underlined light text (blue fails on graphite). If one file holds both light and dark designs, scope the theme
to each design's root instead of the whole document.

## Recipes

- **Dashboard.** A side panel with numbered nav keys and a live switch; a thin lowercase title with an
  uppercase section label (`01 · OVERVIEW`); time range as a row of keys (the active one an alt key); one screen
  with the main number and a bar chart (plain bars, the highlighted one orange); small readouts on cards; a
  table with uppercase 12px headers, 1px rule rows, right-aligned numbers, status as an LED plus a word.
  Orange goes to one control group (the active nav key) plus the highlighted bar.
- **Landing page.** Lowercase nav with a small black pill; a technical label with a model number and an
  optional katakana tag (orange on a black chip); a thin centered headline (display 88px, weight 200); one body
  line in `--text-muted`; black pill plus text link; the product's own UI drawn as a device as the hero image,
  with one sticker; a spec row of Doto numbers over uppercase labels, below a 1px rule.
- **Social post (1080x1350, black edition).** One giant Doto number, one thin sentence, two or three keys as
  ornament, technical labels (28 to 32px) and registration crosses in the corners, an optional sticker.

## Contrast rules (checked)

- Orange is a fill with black text (5.67:1); white on orange fails (3.39:1).
- Orange text: fine on black (5.67:1); on light grey only large and only on `--card` (3.11:1); never on
  `--page` (2.97:1) or `--panel` (2.69:1). On the dark panel it is 4.41:1, so large only.
- Blue links pass on light `--page` and `--card` (4.5 to 4.7:1), not on graphite.
- Dark `--danger` on a dark key is 4.39:1: keep error text on panels and cards.

## Pitfalls

- Orange creep: a second orange control group, orange text on light grey, orange backgrounds.
- Texture, gloss, gradients or soft shadows instead of flat tones and key travel.
- Doto for body text or numbers under 18px; labels under 11px (12px in dense dashboards, 28px on 1080-wide
  posts).
- Copying the brand: no logo, wordmark, product names or photos of their products in the design.

## Checklist

- [ ] Orange marks one control group per screen, as a fill with black text.
- [ ] Controls are objects: numbered keys for choices and navigation, encoders for values, one round button for
      the main action.
- [ ] The main number sits on a small black screen in Doto at 18px or larger, its unit in orange.
- [ ] Labels are uppercase, tracked and at the minimum size for the medium.
- [ ] Depth comes only from the 2px key shadow and flat tones.
- [ ] Two families only: Noto Sans JP and Doto.
- [ ] Keys at a panel corner nest: key radius + panel padding = panel radius.
- [ ] At most one playful element; no logo, wordmark or product name of the brand.

Sources: teenage.engineering product and guide pages (palette and fonts read from the site's CSS `--te-*`
variables; the site's own fonts, Univers TE and TechnoType, are not public, so Noto Sans JP and Doto stand in).
