# Konbini Sky

## Identity

A city poster turned into a design system: a bright daytime sky over white paper, one giant white word,
cobalt captions and a single pixel-art street scene standing on the horizon line. It feels sunny,
ordinary and a little nostalgic, while the grid stays as strict as a Swiss poster.

It grew out of Japanese city posters, but it is not only for Japan. For other content the big word and
the street follow the content's own place: a minimarket in Bandung, a commuter station in Jakarta.

Fits city and travel guides, food and local shops, transit and maps, magazines and editorial pages, and
event pages. Avoid it for dense dashboards, luxury products, enterprise and finance, and content that
needs a serious or grieving tone.

Two themes: daylight by default, a lit-up night for evening use.

Dial: ENERGY 2 / RHYTHM 2 / MOTION 1

## Visual vocabulary

- **Two zones.** Sky on top, paper below, split by the horizon. The sky is a gradient: `--sky-top` held to
  28% of its height, then `--sky-mid` at 68% and `--horizon` at the bottom. It is the only gradient.
- **Color.** Paper `#F7F7F4` and white cards. Cobalt `--ink` `#1D5BD8` for captions, numbers, rules, the
  big word and buttons; navy `--text` `#1E2B4A` for paragraphs. Orange `#EE6A2B` lives in the scene plus
  at most one highlight per page, and never carries text on paper. Text on the sky is always white.
- **Night.** The sky turns deep night blue (`#0B1733` to `#2F4C80`), the paper becomes night ink `#0E1526`,
  `--ink` brightens to `#7EA6FF` and paragraphs turn pale blue. Buttons keep the cobalt fill. The scene
  lights up: bright windows, a brighter orange stripe, platform lamps, single-pixel stars and light
  spilling onto the ground in front of the building. Distant buildings go dark navy with a few warm
  windows. Every scene has a night twin; never leave a day scene under a night sky.
- **Type.** Public Sans 900 for one giant word per page on the sky, tracked tight (-0.05em) at 0.82 line
  height, filling about 90% of the width on one line. Public Sans 700 for captions and UI, 500 for body.
  Noto Sans JP 900 for Japanese words.
- **The trio.** Right under the horizon, three short cobalt captions spread left, center and right.
- **The big word.** One big word per page on the paper, or white and vertical beside the title on the sky.
  For Japanese content it is kanji or kana whose meaning fits the page (駅前 "in front of the station",
  報告 "report"). For other content it is one or two short words in the content's own language, 900
  cobalt, stacked one word per line. Never Japanese glyphs as decoration on non-Japanese content, never
  random characters.
- **Numbered blocks.** A big 900 number under a 2px cobalt rule; list rows split by hairlines. A small
  page number sits in the bottom-right corner.
- **The scene.** One pixel-art street scene per page, standing on the horizon: an SVG on a small integer
  grid (about 120 by 48 units) with crisp edges, scaled to the width. One main building (a corner store,
  a platform with a train, a row of shophouses); things further away fade into sky blue; overhead wires
  are thin lines; the ground strip is `--page`, so the building stands on the paper. Signs carry abstract
  pixel letters or the product's own name, never a real brand. The street follows the content's place. A
  landing hero may set two scenes side by side as one street.
- **White text on the sky.** The smallest white text (nav, captions, info lines) sits as high on the sky as
  it can; the giant word and bold subtitles may sit lower.
- **Shape.** Square corners everywhere and no shadows. Buttons are solid cobalt blocks with white text, or
  1.5px cobalt lines; on the sky the line button is white.
- **Motion.** None, or fades of 300 to 500ms. Nothing moves under `prefers-reduced-motion`.

## Reasons

- **Color:** a bright sky over white paper is the whole mood of a sunny city poster; cobalt is the one ink
  that reads on paper, and orange stays rare so the scene owns it.
- **Typography:** Public Sans 900 stands in for the Helvetica Bold of printed posters without falling back
  on the usual AI default; one giant word gives every page its poster headline.
- **Layout:** the sky and paper split, the trio and the page number give every medium the same poster grid,
  so even a screen without a scene still reads as this style.
- **Shape:** square corners and flat blocks keep the printed feel and leave the detail to the scene.
- **Depth:** no shadows; depth comes from the sky fading behind the scene. The sky is the only gradient and
  the scene is the only patterned surface on a page, because together they are the identity.
- **Motion:** a poster does not move; at most a slow fade when content changes.
- **Theme:** a corner store lit up at night is as much a part of the street as the daytime sky, so the
  night theme keeps the same zones and lights the scene instead of inventing a new look.
- **Contrast:** white on the top of the day sky is 2.20:1, below WCAG AA, and lower where the sky fades.
  This is a deliberate choice for the look, so small white text stays bold and essential information
  stays off the sky.

## Token usage

| Token | Role |
| --- | --- |
| `--page` | paper, the lower zone and the scene's ground |
| `--panel`, `--card` | white tab bars and cards on the paper |
| `--rule` | hairlines between rows |
| `--text`, `--text-muted` | navy paragraphs and secondary text |
| `--ink` | cobalt captions, numbers, the big word, line buttons, focus ring on paper |
| `--accent`, `--on-accent` | button fill and its white text |
| `--link`, `--danger` | links and errors |
| `--sky-top`, `--sky-mid`, `--horizon` | the stops of the sky gradient |
| `--on-sky` | all text on the sky |
| `--focus-on-sky` | focus ring on the sky |
| `--orange` | the scene and one highlight per page |
| `--tracking-display`, `--leading-display` | the giant word |
| `--font-sans`, `--font-jp` | Public Sans and Noto Sans JP |

## Components

```css
body { font: 500 var(--type-body)/1.6 var(--font-sans); color: var(--text); background: var(--page); }

.sky { background: linear-gradient(180deg, var(--sky-top) 0%, var(--sky-top) 28%, var(--sky-mid) 68%, var(--horizon) 100%);
  color: var(--on-sky); container-type: inline-size; }
.giant { margin: 0; color: var(--on-sky); white-space: nowrap; letter-spacing: var(--tracking-display);
  font: 900 min(var(--type-display), calc(128cqw / var(--chars, 6)))/var(--leading-display) var(--font-sans); }
.trio { display: flex; justify-content: space-between; gap: var(--space-md); color: var(--ink);
  font: 700 var(--type-caption)/1.2 var(--font-sans); }
.bigword { margin: 0; color: var(--ink); font: 900 clamp(64px, 14vw, 180px)/1 var(--font-sans); }
.bigword:lang(ja) { font-family: var(--font-jp); }
.numbered { border-top: 2px solid var(--ink); padding-top: var(--space-md); }
.numbered .num { display: block; color: var(--ink); font: 900 var(--type-h2)/1 var(--font-sans); }
.row { display: grid; grid-template-columns: 3ch 1fr auto; gap: var(--space-md); align-items: baseline;
  padding: 14px 0; border-bottom: 1px solid var(--rule); }
.pageno { color: var(--ink); font: 700 var(--type-label)/1 var(--font-sans); }

.btn { display: inline-flex; align-items: center; justify-content: center; min-height: 48px; padding: 0 var(--space-lg);
  border: 1.5px solid var(--accent); border-radius: var(--radius-control); background: var(--accent);
  color: var(--on-accent); font: 700 16px/1 var(--font-sans); cursor: pointer; transition: filter 300ms ease; }
.btn:hover { filter: brightness(0.88); }
.btn.line { background: transparent; border-color: var(--ink); color: var(--ink); }
.btn.line:hover, .sky .btn.line:hover { filter: none; text-decoration: underline; text-underline-offset: 4px; }
.sky .btn.line { border-color: var(--on-sky); color: var(--on-sky); }
.btn:disabled { opacity: 0.45; cursor: not-allowed; filter: none; }

.lbl { display: block; margin-bottom: var(--space-xs); color: var(--ink); font: 700 var(--type-caption)/1.2 var(--font-sans); }
.field { width: 100%; min-height: 48px; padding: 0 var(--space-md); border: 1.5px solid var(--ink);
  border-radius: var(--radius-control); background: var(--card); color: var(--text); font: 500 var(--type-body)/1 var(--font-sans); }
.field[aria-invalid="true"] { border-color: var(--danger); }
.err { color: var(--danger); font: 700 var(--type-caption)/1.3 var(--font-sans); }

:focus-visible { outline: 2px solid var(--ink); outline-offset: 2px; }
.sky :focus-visible { outline-color: var(--focus-on-sky); }

.scene { display: block; width: 100%; height: auto; shape-rendering: crispEdges; }

@media (prefers-reduced-motion: reduce) { .btn { transition: none; } }
```

Give every giant word `style="--chars: N"`, where N is its number of letters, and keep it inside a `.sky`
container. Most words then fill 78 to 92% of the width; words full of wide letters (M, W, O) reach about
97%. If a word still runs past the edge, raise `--chars` by one.

The gradient and the 2px rule read the theme tokens where they are used, so the night theme works on
`<html>` or on a single canvas (`data-theme="dark"` on one post or slide).

## Recipes

### UI

- **Landing page.** Sky hero: white nav (wordmark left; links and a white line button right), the giant
  word, a subtitle and a short lede on one row, then one or two scenes standing on the horizon. On the
  paper: the trio right under the horizon, three numbered blocks in a row, a row with the big word beside a
  call to action and two buttons (solid and line), and a footer with the page number. Sections 96px apart.
- **List or shop page.** A short sky with the giant word and one scene, then rows on the paper: number,
  name with a muted detail line, and a cobalt value on the right (minutes, price, opening time). Prices and
  times live here, never only on the sky.
- **Forms.** Always on the paper: labels above 48px fields with 1.5px cobalt lines, errors in `--danger`
  below the field.

### Slides

- **Title slide.** Sky over the top 66%, paper below. The giant word top left, sized
  `min(13cqw, calc(96cqw / var(--chars)))`, with a short white kicker under it, the scene about 62% wide on the right, standing on the horizon. The trio on the paper, the big
  word bottom left, the page number bottom right.
- **Data slide.** A 24% sky band at the top with a white headline. One big cobalt number with a caption,
  cobalt bars with a single orange bar for the value that matters, a vertical big word on the right edge
  and the page number.
- **Content slides.** Paper only, with a thin sky band on top; one idea per slide, numbered blocks for
  lists of three.
- Cuts or 400ms fades between slides; the scene never animates.

### Social

- **Post, 1080 × 1350.** Sky over the top 60% with the giant word and a bold subtitle, the scene on the
  horizon, then on the paper the trio, the big word, one short sentence bottom right and the page number.
- Keep the composition your own: move the big word and the sentence, change the scene. The post should
  read as this style, not as a copy of any one poster.
- **Story, 1080 × 1920.** The same zones stacked taller, with all text outside the top 250px and bottom
  340px.

### App

- **Header.** The sky as a header: status bar, a short white greeting, the place name as the giant word
  with its big word set vertically in white beside it, one white info line, and the scene at the bottom of
  the header. Size the name with `min(16cqw, calc(112cqw / var(--chars)))` and `min-width: 0`, so a long
  name still leaves room for the vertical word.
- **Body.** On the paper: the trio, a section title in cobalt, numbered rows (number, name with a muted
  detail, a cobalt value), and one full-width solid button.
- **Tab bar.** `--card` with a hairline on top; the active item in `--ink`, the others in `--text-muted`
  at full opacity.
- Times, prices and errors sit in the body, never only in the header.

## Outside CSS

| CSS effect | Replacement |
| --- | --- |
| The sky gradient | a linear gradient with stops at 0, 28, 68 and 100%, the top color held to 28% |
| `cqw` and `--chars` | size the giant word from the frame width: about 1.28 × width ÷ letters, capped at the display size |
| `cqw` inside slides and posts | fixed canvases (slides 1920 × 1080, posts 1080 × 1350) with sizes in pixels, for example a 6-letter giant word at about 250px on a slide |
| SVG pixel scene | vector rectangles on the same grid, or a PNG at a whole-number scale with nearest-neighbor resampling |
| `shape-rendering: crispEdges` | antialiasing off for the scene layer |
| Vertical kanji | one glyph per line, not a vertical text mode |
| `filter: brightness()` hover | a fill about 12% darker |

## Contrast rules (checked)

| Text | On | Theme | Ratio | Rule |
| --- | --- | --- | --- | --- |
| `--text` | `--page` | light | 13.05 | Body text in navy on paper. |
| `--text-muted` | `--page` | light | 6.64 | Secondary text. |
| `--ink` | `--page` | light | 5.53 | Captions, numbers, the big word. |
| `--ink` | `--card` | light | 5.93 | Ink on white cards and tab bars. |
| `--on-accent` | `--accent` | light | 5.93 | Button text. |
| `--link` | `--page` | light | 5.53 | Links. |
| `--danger` | `--page` | light | 5.17 | Error text. |
| `--on-sky` | `--sky-top` | light | 2.20 | White on the top of the sky, a deliberate exception: small text 14px and 700 or more, no essential information. |
| `--on-sky` | `--sky-mid` | light | 1.63 | White text lower on the sky drops toward this; keep only the giant word and bold subtitles there. |
| `--orange` | `--page` | light | 2.91 | Orange never carries text on paper. |
| `--ink` | `--page` | light | 5.53 | Focus ring on paper. |
| `--focus-on-sky` | `--sky-top` | light | 6.37 | Focus ring on the sky, navy because white would be 2.20. |
| `--ink` | `--card` | light | 5.93 | Field border, a 1.5px cobalt line. |
| `--text-muted` | `--card` | light | 7.12 | Inactive tab labels, at full opacity. |
| `--text` | `--page` | dark | 14.23 | Body text at night. |
| `--text-muted` | `--page` | dark | 8.03 | Secondary text. |
| `--ink` | `--page` | dark | 7.61 | Captions, numbers, the big word. |
| `--ink` | `--card` | dark | 6.68 | Ink on night cards. |
| `--ink` | `--panel` | dark | 7.16 | Ink on the tab bar. |
| `--on-accent` | `--accent` | dark | 5.93 | Button text. |
| `--link` | `--page` | dark | 7.61 | Links. |
| `--danger` | `--page` | dark | 8.25 | Error text. |
| `--on-sky` | `--sky-top` | dark | 17.73 | White on the night sky. |
| `--on-sky` | `--horizon` | dark | 8.51 | White near the horizon. |
| `--orange` | `--page` | dark | 7.01 | Orange highlight at night. |
| `--accent` | `--page` | dark | 3.07 | Button fill against the night page (non-text). |
| `--ink` | `--page` | dark | 7.61 | Focus ring on the night page. |
| `--focus-on-sky` | `--sky-top` | dark | 17.73 | Focus ring on the night sky, white. |
| `--ink` | `--panel` | dark | 7.16 | Field border at night. |
| `--text-muted` | `--card` | dark | 7.05 | Inactive tab labels at night. |

## Pitfalls

- Pixels creeping into the interface: pixel fonts, stepped corners, banded skies. Pixels belong to the scene.
- A real brand name or logo on a sign in the scene.
- Japanese glyphs on non-Japanese content, or kanji picked for looks without a fitting meaning.
- Prices, times, errors, form labels or instructions written only in white on the sky.
- Small white text under 14px or lighter than 700 on the sky.
- Orange text on paper; it fails contrast.
- More than one scene on a page (a landing hero may join two into one street).
- Shadows, rounded corners, or a second gradient anywhere besides the sky.
- A scene that floats above the horizon instead of standing on it.
- A giant word that breaks onto two lines or runs past the edge; set `--chars` to its letter count.

## Checklist

- [ ] Sky on top, paper below, one scene standing on the horizon with its ground in `--page`.
- [ ] One giant white word on one line, sized with `--chars`, and the trio right under the horizon.
- [ ] One big word on the paper with a fitting meaning, in the content's own language or script.
- [ ] Scenes are crisp pixel art with no brand on the signs; pixels appear nowhere else.
- [ ] White text on the sky is 14px and 700 or more, and essential information sits on the paper.
- [ ] Orange appears in the scene and at most once more, never as text on paper.
- [ ] Square corners, no shadows, no gradient besides the sky.
- [ ] Buttons and fields are at least 48px tall; focus shows a 2px outline (navy on the sky).
- [ ] Motion is a fade of 500ms or less, off under reduced motion.
- [ ] Both themes are complete; night scenes replace day scenes.
