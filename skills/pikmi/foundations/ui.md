# Foundation: web UI

Rules that hold for every style. A style's Recipes section only adds what is specific to it.

## Layout

- Breakpoints: 640px, 1024px, 1280px. Design the 375px phone layout first.
- No horizontal scroll at 375px. Text never escapes its container; cards never clip off-screen.
- Body text lines stay between 60 and 75 characters.
- One focal point per screen: one element is clearly the most important, the rest defer to it.

## Interaction

- Every control works or does not exist. Links point at real sections or pages.
- Click and tap targets are at least 44px in both directions.
- Keyboard: every control is reachable with Tab in visual order and works with Enter or Space. Dialogs
  close with Escape.
- Focus is always visible: a 2px outline at a 2px offset, in a color that passes 3:1 against its
  background. Never remove the outline without a stronger replacement.

## States

Any view that shows data has an empty state, a loading state and an error state, drawn in the style.

## Motion

- Every animation has a purpose: feedback, orientation or attention.
- Wrap non-essential motion in `@media (prefers-reduced-motion: no-preference)`, or turn it off under
  `prefers-reduced-motion: reduce`.
- No endless loops or pulses, except an indicator of a real live state.

## Themes

If a style ships two themes and the product has no strong reason for one, build a working toggle that sets
`data-theme` on `<html>`, and check contrast in both.

## Tokens

Link the style's `tokens.css` and read every color, radius, size and shadow from its variables. Do not
hard-code values the tokens already name.
