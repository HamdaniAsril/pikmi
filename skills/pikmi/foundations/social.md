# Foundation: social media posts

Rules that hold for every style. A style's Recipes section only adds what is specific to it.

## Canvas

| Format | Size | Notes |
| --- | --- | --- |
| Feed portrait (default) | 1080 x 1350 (4:5) | Most room in the feed. |
| Feed square | 1080 x 1080 | When the platform or carousel needs it. |
| Story or reel cover | 1080 x 1920 (9:16) | Keep the top 250px and bottom 340px free of text; the app's own UI covers them. |

Keep a 64px margin on feed formats.

## Type

- Main text 48px or larger; labels 28px or larger on a 1080px-wide canvas.
- One core sentence per post. A carousel spreads a longer story over several frames, one idea each.
- Two families at most: the style's display face and its body face.

## Composition

- One focal element: a number, a phrase, a product shot or an illustration. Everything else supports it.
- The post must read at thumbnail size (about 300px wide). Test it scaled down.
- No invented numbers, quotes or logos. Mark placeholders as placeholders.

## Building

- HTML or SVG canvas at the exact pixel size, styled with `tokens.css`, exported as PNG.
- Design tools or image generators: take colors and sizes from `tokens.json`; use the style's Outside CSS
  replacements for effects.
