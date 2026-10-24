# Primary Riot

## Identity

A protest poster that learned to be an interface. Thick black borders, hard shadows, pure primary colors
that clash on purpose, square corners and type sizes that collide. It refuses the polished look of every
other site, but it still works: you can read it, click it and navigate it by keyboard.

Fits zines, music and art events, indie products with attitude, portfolios, campaigns and anything that
wants to be remembered for being loud. Avoid it for healthcare, finance, government, enterprise tools and
any audience that needs calm.

Light only.

Dial: ENERGY 3 / RHYTHM 3 / MOTION 1

## Visual vocabulary

- **Color.** White page, black ink, and pure primaries at full saturation: red `#FF0000`, blue `#0000FF`,
  yellow `#FFFF00`, with magenta, cyan and green in reserve. Per page, pick red, blue and yellow as the
  core three plus one reserve color as the accent. Never grey: hierarchy comes from size and weight.
- **Borders.** 4 to 8px solid black on every block; heavier on the right and bottom to fake depth.
- **Shadows.** Hard offset only: `8px 8px 0` black, no blur.
- **Shape.** Square corners everywhere. Nothing is ever rounded.
- **Type.** Archivo Black for display, Archivo 400 to 900 for everything else. Mix sizes dramatically
  inside one block: a 128px word next to a 17px sentence. Uppercase for shouting, sentence case for
  reading.
- **Composition.** Blocks of color alternate between sections; headlines and stickers tilt between -3 and
  5 degrees; the decorative layer breaks the grid while content columns stay aligned.

## Reasons

- **Color:** pure primaries at full strength are the opposite of a curated palette, which is the point;
  limiting a page to three of them plus one accent keeps the clash readable.
- **Typography:** an ultra-black grotesk at extreme sizes creates tension that a balanced type scale
  would erase; Archivo keeps body text readable underneath the noise.
- **Layout:** tilted headlines and off-grid stickers make the page feel made by hand, while the content
  grid underneath keeps reading order and tap targets predictable.
- **Shape:** zero radius and heavy borders read as cut paper and photocopies.
- **Depth:** hard offset shadows are depth without polish.
- **Motion:** instant state changes (no easing) feel like a switch, not an animation.
- **Theme:** the look is ink and paper; a dark version would lose the white that makes primaries scream.

## Token usage

| Token | Role |
| --- | --- |
| `--page`, `--card` | white paper |
| `--panel` | yellow section blocks |
| `--rule`, `--text`, `--text-muted` | black ink (muted is black on purpose) |
| `--accent`, `--on-accent` | red buttons with black text |
| `--link` | blue links, underlined |
| `--danger` | darker red for error text |
| `--clash-blue`, `--clash-yellow`, `--clash-magenta`, `--clash-cyan`, `--clash-green` | section colors and the accent pick |
| `--border-heavy`, `--hard-shadow`, `--hard-shadow-sm`, `--border-focus` | borders, shadows and focus |

## Components

```css
.block { background: var(--card); border: var(--border-heavy); border-right-width: 10px; border-bottom-width: 10px;
  box-shadow: var(--hard-shadow); padding: var(--space-lg); }
.block.yellow { background: var(--panel); }
.block.blue { background: var(--clash-blue); color: #FFFFFF; }

.btn { min-height: 48px; padding: 0 var(--space-lg); border: var(--border-heavy); border-radius: 0;
  background: var(--accent); color: var(--on-accent); box-shadow: var(--hard-shadow-sm);
  font: 900 18px/1 var(--font-body); text-transform: uppercase; cursor: pointer; transition: none; }
.btn:hover { background: var(--clash-yellow); }
.btn:active { box-shadow: none; transform: translate(4px, 4px); }
.btn:focus-visible, .field:focus-visible { outline: var(--border-focus); outline-offset: 2px; }
.btn.blue { background: var(--clash-blue); color: #FFFFFF; }
.block.blue :focus-visible { outline-color: var(--clash-yellow); }

.field { min-height: 48px; width: 100%; border: var(--border-heavy); border-radius: 0; padding: 0 var(--space-md);
  background: var(--card); color: var(--text); font: 700 18px var(--font-body); }

.shout { font: 400 var(--type-display)/0.85 var(--font-display); text-transform: uppercase; rotate: -3deg; }
.sticker { display: inline-block; padding: var(--space-sm) var(--space-md); background: var(--clash-magenta);
  border: 4px solid var(--text); rotate: 5deg; font: 900 16px/1 var(--font-body); text-transform: uppercase; }
.link { color: var(--link); text-decoration: underline; text-decoration-thickness: 3px; }
```

Rotation goes on headlines, stickers and decorative blocks only. Buttons, links and inputs stay straight
and never move on hover, so the cursor and the keyboard focus always find them where they were.

## Recipes

### UI

- **Landing page.** A white hero with a tilted 128px headline breaking out of its block, one sentence of
  body at 22px, a red button and a blue link. Below, alternate full-width bands: yellow, white, blue (white
  text). Each band uses a different composition: one huge word, a three-column list with numbered
  heavy-bordered blocks, a single quote in a magenta sticker.
- **Dashboard or app screen.** Keep the noise in the header and empty states; tables stay calm: 2px black
  rules, bold column headers, numbers right-aligned. One clash color marks the active filter.

### Slides

- White or yellow full-bleed slides with one 6px black frame inset 96px.
- One word or number per slide at 200px or more, tilted -3 degrees, plus one line of body at 32px.
- Switch the background color every few slides (white, yellow, blue) to mark sections.
- Pick the page's three colors at the start of the deck and keep them.

### Social

- 1080 x 1350: one shouted phrase in Archivo Black filling the canvas, one sticker, one hard-shadowed
  block holding the details at 32px or more.
- Background in one core color; black text on red, yellow, magenta, cyan or green; white text only on
  blue.
- A carousel keeps the frame and moves the sticker to a new corner each frame.

### App

- White screens, black 4px borders around list rows and cards, a red primary button at the bottom.
- Tab bar with square 4px-bordered tabs; the active tab is filled yellow.
- Empty and error states get the loud treatment (a tilted shouted word); working screens stay readable.
- Press feedback is the 4px shadow collapse, instant.

## Outside CSS

| CSS effect | Replacement |
| --- | --- |
| Hard offset `box-shadow` | a black duplicate of the shape offset 8px right and down, behind it |
| Uneven borders (heavier right and bottom) | a second black rectangle offset 4px, or a thicker stroke on two sides |
| `rotate` on headlines | rotate the text box -3 degrees in the layout tool |
| `transform` on press | swap to a version without the shadow |

## Contrast rules (checked)

| Text | On | Theme | Ratio | Rule |
| --- | --- | --- | --- | --- |
| `--on-accent` | `--accent` | light | 5.25 | Red buttons carry black text. |
| `#FFFFFF` | `--accent` | light | 4.00 | White on red fails for normal text; never use it. |
| `#FFFFFF` | `--clash-blue` | light | 8.59 | Blue is the only color that takes white text. |
| `--link` | `--page` | light | 8.59 | Blue links on white. |
| `--text` | `--panel` | light | 19.56 | Black on yellow. |
| `--danger` | `--panel` | light | 5.48 | Error text holds even on yellow. |
| `#000000` | `--clash-magenta` | light | 6.70 | Black on magenta. |
| `#000000` | `--clash-cyan` | light | 16.75 | Black on cyan. |
| `#000000` | `--clash-green` | light | 15.30 | Black on green. |
| `--clash-blue` | `--page` | light | 8.59 | Focus ring (8px blue) on white and yellow. |
| `--clash-yellow` | `--clash-blue` | light | 8.00 | Focus ring on blue bands switches to yellow. |
| `--rule` | `--card` | light | 21.00 | Field border (6px black). |

## Pitfalls

- All six primaries on one page. Three core colors plus one accent.
- Grey text or grey borders. This style has no grey.
- Rounded corners, soft shadows, gradients or blur: any polish breaks it.
- Tilting buttons or moving them on hover. Controls stay where the user expects them.
- Breaking the reading order. The decoration can collide; the content column cannot.
- White text on red, yellow, magenta, cyan or green.
- Overlaps that hide text on a phone. Below 640px, tilt at most 2 degrees and stack blocks.

## Checklist

- [ ] The page uses three core primaries plus one accent, all at full saturation, and no grey.
- [ ] Every block has a 4 to 8px black border and a hard shadow with no blur.
- [ ] No element has rounded corners.
- [ ] At least one huge shouted word sits next to small readable text.
- [ ] Rotation appears only on headlines, stickers and decoration.
- [ ] Focus is an 8px blue outline, louder than the default state.
- [ ] State changes are instant (no easing).
- [ ] Every text pair passes the contrast table; white text only on blue.
