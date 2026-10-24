# Armor Plate

## Identity

The cockpit and hangar of a giant robot: armored panels in navy and military green, corners cut at 45
degrees, warning yellow and danger red, unit numbers and technical notes in mono. It is heavy,
mechanical and serious. Where Night Circuit glows, Armor Plate is painted steel: no glow, no blur, just hard
edges and paint.

Fits games and esports, robotics and hardware startups, defense-flavored and tactical tools, monitoring
and operations dashboards, model kits, anime and sci-fi fan events. Avoid it for wellness, children's
education, food, fashion and anything that should feel soft or friendly.

Dark only.

Dial: ENERGY 3 / RHYTHM 2 / MOTION 1

## Visual vocabulary

- **Color.** Navy steel `#141E33` page, `#1A2744` panels, `#1F2D4D` cards; military green `#4A5C3A` for
  rules and secondary plates. Hazard yellow `#FBBF24` is the accent (actions, selection). Hazard red
  `#EF4444` marks danger fills; error text uses the lighter `--danger`.
- **Plates.** Panels have one or two corners cut at 45 degrees (`--plate-cut`) and a hard offset shadow
  in near-black (`--plate-shadow`). Radius is always 0.
- **Type.** Saira Condensed 600 to 700 uppercase for headings and buttons; Saira for body; IBM Plex Mono
  for unit numbers, coordinates and technical annotations (`UNIT-07`, `SEC 3 / BAY 2`).
- **Markings.** Unit numbers in plate corners, thin rules with tick marks, square status dots, diagonal
  hazard stripes on real warnings only.
- **Texture.** A faint technical grid (`--tech-grid`) on one surface per screen, such as the hero or the
  status screen.

## Reasons

- **Color:** navy and military green read as painted armor; one warning yellow makes every action
  findable, and red is kept for real danger.
- **Typography:** a condensed sans fits long uppercase labels into narrow plates like stenciled markings;
  mono annotations separate data from speech.
- **Layout:** plates with cut corners and unit numbers make each block feel like a removable part of a
  machine, so sections have obvious edges.
- **Shape:** zero radius and 45 degree cuts are what machined armor looks like.
- **Depth:** a hard offset shadow stacks plates without any soft light.
- **Motion:** short linear moves (100 to 150ms) feel hydraulic and mechanical, never springy.
- **Theme:** painted steel in a hangar is dark by nature; a light version would lose the weight.

## Token usage

| Token | Role |
| --- | --- |
| `--page`, `--panel`, `--card` | hangar, armor plates, inset plates |
| `--rule`, `--armor-green` | rules, secondary plates |
| `--text`, `--text-muted` | body and annotation text |
| `--accent`, `--on-accent`, `--link` | hazard-yellow actions with navy text, yellow links |
| `--hazard-yellow`, `--hazard-red` | warnings and danger fills |
| `--danger` | error text |
| `--plate-cut`, `--plate-shadow`, `--hazard-stripes`, `--tech-grid` | plate shape, depth, warnings, one grid surface |

## Components

```css
.plate { background: var(--panel); clip-path: var(--plate-cut); padding: var(--space-lg); position: relative; }
.plate-wrap { filter: drop-shadow(var(--plate-shadow)); }
/* clip-path cuts box-shadow, so the shadow sits on a wrapper as a drop-shadow */
.plate .unit { position: absolute; top: var(--space-sm); right: var(--space-lg); font: 500 var(--type-label)/1 var(--font-mono);
  letter-spacing: var(--tracking-label); color: var(--text-muted); }

.btn { min-height: 48px; padding: 0 var(--space-lg); border: 0; border-radius: 0; clip-path: var(--plate-cut);
  background: var(--accent); color: var(--on-accent); font: 700 16px/1 var(--font-display); letter-spacing: var(--tracking-label);
  text-transform: uppercase; transition: transform 120ms linear; }
.btn:hover { transform: translateX(2px); }
.btn:active { transform: translate(3px, 3px); }
.btn.ghost { background: transparent; color: var(--accent); box-shadow: inset 0 0 0 2px var(--accent); clip-path: none; }
.btn:focus-visible, .field:focus-visible { outline: 3px solid var(--text); outline-offset: 3px; }
.btn:focus-visible { clip-path: none; }
/* clip-path also clips the outline, so a focused button drops its cut corners */

.field { min-height: 48px; width: 100%; padding: 0 var(--space-md); border: 2px solid var(--text-muted); border-radius: 0;
  background: var(--card); color: var(--text); font: 400 16px var(--font-mono); }
.field:focus { border-color: var(--accent); }

.status { display: inline-flex; align-items: center; gap: var(--space-sm); font: 500 13px/1 var(--font-mono); text-transform: uppercase; }
.status::before { content: ""; width: 10px; height: 10px; background: currentColor; }
.status.ok { color: var(--text); } .status.warn { color: var(--hazard-yellow); } .status.bad { color: var(--danger); }

.hazard { height: 12px; background: var(--hazard-stripes); }
.grid-surface { background: var(--tech-grid), var(--card); }
@media (prefers-reduced-motion: reduce) { .btn { transition: none; } }
```

Field borders use `--text-muted` because the green rule is too faint to mark an input. `--tech-grid` carries
its own position and size, so it goes in the `background` shorthand; `background-image` rejects it.

## Recipes

### UI

- **Landing page.** A hero plate on the tech-grid surface with a unit number in the corner, an uppercase
  condensed headline at 60 to 104px, one line of body, a yellow cut-corner button and a ghost button.
  Below, a row of plates with spec readouts (mono numbers over uppercase labels), and one hazard strip only
  above a real warning or limited-stock notice.
- **Dashboard.** Plates on a strict grid, each with a unit number; status as square dots plus words; one
  status screen with the tech grid; yellow marks the selected item; red only for faults.

### Slides

- Navy slides with a plate frame inset 96px and a unit number in the top-right corner.
- Uppercase condensed titles at 72px; one spec readout or one diagram drawn in 2px lines per slide.
- Section slides use a military-green plate across the full width.
- Hazard stripes only on the risk or safety slide.

### Social

- 1080 x 1350: one big condensed word or number, a plate with the details, unit numbers and tick marks
  in the corners at 28px.
- Yellow for the one call to action or highlight; no glow.
- Carousels number frames like units (`01 / 05`).

### App

- Navy screens with plates for groups, list rows separated by green rules.
- The one primary action is a yellow cut-corner button; destructive actions use a red fill with white
  text only at 18px bold or larger, or a red outline with `--danger` text.
- Tab bar with square indicators; the active tab gets a yellow bar on top.

## Outside CSS

| CSS effect | Replacement |
| --- | --- |
| `--plate-cut` clip-path | a vector shape with one or two 45 degree corner cuts (12px) |
| `--plate-shadow` drop-shadow | a near-black duplicate of the plate offset 4px right and down |
| `--hazard-stripes` | a striped pattern fill, yellow and navy at -45 degrees |
| `--tech-grid` | a 24px grid pattern at 8% opacity, or omit |

## Contrast rules (checked)

| Text | On | Theme | Ratio | Rule |
| --- | --- | --- | --- | --- |
| `--text` | `--page` | dark | 13.67 | Body text. |
| `--text` | `--panel` | dark | 12.18 | Text on plates. |
| `--text-muted` | `--card` | dark | 6.45 | Annotations and field borders. |
| `--on-accent` | `--accent` | dark | 9.96 | Navy text on yellow buttons. |
| `--accent` | `--card` | dark | 8.16 | Yellow text and links. |
| `--danger` | `--card` | dark | 4.93 | Error text. |
| `--hazard-red` | `--page` | dark | 4.42 | Hazard red only as a fill or large text. |
| `--text` | `--armor-green` | dark | 5.99 | Text on green plates. |
| `--text` | `--page` | dark | 13.67 | Focus ring (3px light outline). |
| `--text-muted` | `--card` | dark | 6.45 | Field border (2px). |

## Pitfalls

- Neon glow, gradients or blur; that is Night Circuit, not Armor Plate.
- Rounded corners or soft pastel colors.
- Hazard stripes as decoration; they mean a real warning.
- The tech grid on every plate; one surface per screen.
- All-mono pages; mono is for annotations and numbers.
- Red for anything but danger.
- Copying a real robot design, logo or show title.

## Checklist

- [ ] Surfaces are navy and military green; yellow is the only accent; red means danger.
- [ ] Plates have cut corners, zero radius and a hard offset shadow.
- [ ] Headings and buttons are uppercase Saira Condensed; annotations are IBM Plex Mono.
- [ ] Every plate group carries a unit number or annotation.
- [ ] Hazard stripes appear only next to real warnings.
- [ ] The tech grid sits on one surface only.
- [ ] Motion is 100 to 150ms linear; nothing glows.
- [ ] Focus is a 3px light outline; fields have visible borders.
