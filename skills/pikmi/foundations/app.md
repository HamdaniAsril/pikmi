# Foundation: apps

Rules that hold for every style. A style's Recipes section only adds what is specific to it.

## Platform

- Respect safe areas: notch, status bar, home indicator and rounded corners.
- Tap targets: at least 44 x 44pt on iOS, 48 x 48dp on Android.
- Body text 16pt or larger; support the system text size setting without clipping.
- Bottom navigation holds at most 5 items, each with a label.
- If the style ships two themes, follow the system light or dark setting. If it ships one, keep that theme
  and say so in the Reasons you hand over.

## Translating tokens

- Colors, radii and sizes come from `tokens.json`. Map role tokens to the platform's color roles
  (background, surface, primary, on-primary, error) instead of hard-coding hex values in views.
- CSS-only effects (backdrop blur, clip-path, layered inset shadows, repeating gradients) use the style's
  Outside CSS replacements. On native platforms prefer the system material or a flat fill.
- Motion follows the platform's reduce-motion setting.

## Structure

- One primary action per screen.
- Every list has empty, loading and error states drawn in the style.
- Use real content or clearly marked placeholders; no invented names, avatars or numbers.
