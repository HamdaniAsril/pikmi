# Foundation: slides

Rules that hold for every style. A style's Recipes section only adds what is specific to it.

## Canvas

- 1920 x 1080 (16:9). Design at that size; scale the whole slide, never reflow it.
- Safe margin: 96px on every side. Nothing important touches the edge.

## Type

- Titles 56px or larger, body text 28px or larger, labels and captions 20px or larger.
- At most about 30 words of body text per slide. Long text goes to speaker notes.
- Use the style's display face for titles and its body face for text. Never more than two families.

## Structure

- One idea per slide. The title states the point, not the topic ("Signups doubled in March", not
  "Signups").
- One focal element per slide: a big number, one image, one diagram or one quote.
- A big number belongs on the style's screen or readout component when it has one.
- Use real data or a clearly marked `[REAL DATA]` placeholder. Never invent figures.

## Building

- HTML slides: one `<section>` per slide at a fixed 1920 x 1080, styled with the style's `tokens.css`.
- .pptx or Google Slides: take values from `tokens.json` and use the style's Outside CSS replacements for
  effects the format cannot draw.
- Check contrast at the projected size: text over images or gradients must pass across its whole area.
