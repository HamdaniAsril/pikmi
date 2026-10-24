---
name: pikmi
description: Pick and apply a visual design style for web UI, slides, social media posts and apps. Use when the user starts a new design or asks to change how something looks, names a mood or aesthetic (industrial, cyberpunk, brutalist, glassmorphism, watercolor, Japanese minimal, bento, dark developer, corporate, Islamic geometric, ukiyo-e, mecha), asks to "make it look like ...", or says it in Indonesian ("ganti tampilan", "bikin desain", "ala ...", "kayak ..."). Offers 2 to 4 matching styles with previews and lets the user choose; continues a style already marked in the project. Not for small edits to a project that already has its own look.
---

# pikmi

pikmi ("pick me") is a catalog of visual styles. Every style works across four media: web UI, slides,
social posts and apps. Find the styles that fit the request, let the user pick, then build with only the
chosen style loaded.

Paths below are relative to this file's folder.

## When to offer, when to stay quiet

Offer styles only when the user starts a new design or asks to change how something looks.

Stay quiet when the project already has a look and the request only adds or edits a part of it ("add a
pricing page", "fix this button"). Do not offer styles then.

## Flow

### 0. Check for an existing look

- Look for a `tokens.css` in the project whose first line is `/* pikmi: <id> */`. If it exists and the
  user is not asking for a new look, continue with that style: go to step 6.
- If the project has its own design system or stylesheet without that marker, and the user is not asking
  for a new look, do not use pikmi. Follow the project's own look.
- If the user asks to change the look ("ganti tampilan jadi ...", "restyle this"), go on to step 1 even
  when a marker exists.

### 1. Read the request

- Medium: `ui`, `slides`, `social` or `app`; a request can need more than one. When it is unsaid, infer it
  from context: open files, or words like "slide", "deck", "post", "story", "feed", "screen", "app".
- Mood words: every adjective, aesthetic name or reference ("like a synthesizer", "kayak game", "ala
  Muji"), plus any theme wish (dark, light).

### 2. A named style

Skip the offer only when the user names a style directly:

- by its catalog `name` or `id`, or a clear short form of it ("woodblock", "lattice", "bento"), or
- by a brand, product or work listed in that style's `brand_terms` and in no other style's `brand_terms`
  ("ala teenage engineering", "like a Blade Runner movie"). A brand listed under two styles goes to step 3
  with both styles first.

Then use that style and say in one line which one you picked. Mood words, topics and occasions
("ramadan", "luxury", "dark", "devops", "military", "widgets") never skip the offer, even when only one
style matches them: go to step 3 and put that style first.

### 3. Offer 2 to 4 styles

- Read `catalog.json`. Match the mood words against `keywords.en`, `keywords.id` and `summary` by
  meaning, not only by exact word. Indonesian and slang count.
- Keep only styles whose `media` include the requested medium and whose `themes` include a requested
  theme.
- Offer 2 to 4, best first, even when one style clearly leads. For each give the name, one sentence on
  why it fits this request, its themes, and the preview `styles/<id>/preview.html` (open it in a
  browser for the user when you can).
- Ask the user to pick. Do not build before they answer.

### 4. Nothing fits

Say plainly that no style matches exactly, then offer the closest 2 or 3 and say what each one misses.

If the user wants a theme a style does not have, such as a dark version of a light-only style, say that
style has no such theme and offer styles that do.

### 5. No preference

If the user says "terserah", "up to you", or cannot decide, recommend one style with a one-line reason,
then continue unless they object.

### 6. Load only what you need

- `styles/<id>/STYLE.md`, always.
- `styles/<id>/tokens.css` for anything built with CSS (web pages, HTML slides or posts), or
  `styles/<id>/tokens.json` for everything else (.pptx, native app code, design tools).
- `foundations/<medium>.md` for each medium you build.
- `styles/<id>/preview.html` as the reference for any component STYLE.md does not spell out
  (navigation, tab bars, the main number, slide and post layouts). Copy its patterns, not its sample
  text.

Do not open other styles' folders.

### 7. Build in the format the task needs

pikmi decides the look, not the file format. Build HTML, a .pptx through a slides skill, SwiftUI or
Compose, or a design file: whatever the task calls for. When an effect only exists in CSS, use the
replacement from the style's "Outside CSS" section.

### 8. Mark web projects

For a web project, copy the style's `tokens.css` into the project unchanged, so its first line
`/* pikmi: <id> */` travels with it. When you restyle a marked project, replace that file. Slides, posts
and design files get no marker.

### 9. Check before you deliver

Run the style's Checklist and Contrast rules against what you built, and fix anything that fails.

## Working with other design skills

The chosen STYLE.md is the design direction for what you build. When antislop or a similar filter is
active:

- Use the style's `Dial:` line as the dial setting.
- Use its Reasons section as the written reason for each technique.
- Its limits on glow, glass, palette size and shadows already follow antislop. Keep them.

## Rules for every style

- Never put a brand's name, logo or product into the design. Catalog keywords may name a brand so users
  can find a style; the output never does.
- Use real content or clearly marked placeholders. No invented statistics, testimonials or logos.
- Keep the active palette to 2 or 3 core colors plus 1 accent per page.
- Respect `prefers-reduced-motion`, and keep keyboard focus visible.
