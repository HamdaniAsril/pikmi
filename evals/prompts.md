# pikmi router evals

Each row is a request plus the project context. A fresh agent that has read only
`skills/pikmi/SKILL.md` and `skills/pikmi/catalog.json` says what it would offer or do, without
building anything. The row passes when that answer matches "Expected".

Every offer must also list at most 3 styles, end with a "Continue without pikmi" option and open the
offered previews before asking; an offer that breaks this fails its row.

Run these by hand whenever a style is added, removed or renamed, or keywords change.

| ID | Prompt | Project context | Expected | Result |
| --- | --- | --- | --- | --- |
| E01 | rubah tampilan web ini jadi modern industrial | web project, no marker | offers include `instrument-panel` | PASS · asked instrument-panel, armor-plate + "Lanjut tanpa pikmi" |
| E02 | bikin slide pitch deck yang terasa mewah dan malam | new | offers include `nocturne-glass` | PASS · asked nocturne-glass, lapis-lattice + "Lanjut tanpa pikmi" |
| E03 | design a landing page for a meditation app, calm and airy | new | offers include `japanese-minimal` | PASS · asked japanese-minimal, soft-wash + "Continue without pikmi" |
| E04 | bikin poster instagram ramadan | new | offers include `lapis-lattice` | PASS · asked lapis-lattice, nocturne-glass, soft-wash + "Lanjut tanpa pikmi" |
| E05 | make it look like a Ghibli movie | new | offers 2 to 4 styles, no direct apply (no style lists Ghibli) | PASS · asked soft-wash, japanese-minimal, indigo-woodblock + "Continue without pikmi"; said nothing matches a Ghibli look exactly |
| E06 | dashboard buat tim devops, gelap | new | offers include `dark-dev` | PASS · asked dark-dev, armor-plate, night-circuit + "Lanjut tanpa pikmi" |
| E07 | bikin kayak game sci-fi jadul | new | offers include `armor-plate` or `night-circuit`, and says nothing matches exactly | PASS · asked night-circuit, armor-plate, instrument-panel + "Lanjut tanpa pikmi"; said no style is literally a retro sci-fi game |
| E08 | terserah, yang penting keren | new | recommends exactly one style with a reason | PASS · recommended instrument-panel with a reason |
| E09 | tambah halaman pricing | web project with `/* pikmi: instrument-panel */` | no offer, continues `instrument-panel` | PASS · continued instrument-panel, no offer |
| E10 | add a settings screen | app with its own design system, no marker | stays quiet, no offer | PASS · stayed quiet |
| E11 | post linkedin untuk laporan kuartal | new | offers include `ledger-blue` | PASS · asked ledger-blue, japanese-minimal, nocturne-glass + "Lanjut tanpa pikmi" |
| E12 | watercolor tapi dark mode | new | says `soft-wash` (the watercolor style) has no dark theme and offers styles that do | PASS · said soft-wash has no dark theme; asked nocturne-glass, lapis-lattice + "Lanjut tanpa pikmi" |
| E13 | bikin undangan nikah yang lembut dan artistik | new | offers include `soft-wash` | PASS · asked soft-wash, japanese-minimal, lapis-lattice + "Lanjut tanpa pikmi" |
| E14 | poster gig punk yang norak tapi keren | new | offers include `primary-riot` | PASS · asked primary-riot, night-circuit, indigo-woodblock + "Lanjut tanpa pikmi" |
| E15 | neon HUD screens for an esports tournament app | new | offers include `night-circuit` | PASS · asked night-circuit, armor-plate + "Continue without pikmi" |
| E16 | halaman menu restoran jepang tradisional | new | offers include `indigo-woodblock` | PASS · asked indigo-woodblock, japanese-minimal, konbini-sky + "Lanjut tanpa pikmi" |
| E17 | portfolio with widget-style cards for my projects | new | offers 2 or 3 styles, no direct apply (no style is a widget grid) | PASS · asked instrument-panel, nocturne-glass, primary-riot + "Continue without pikmi"; said no style is a widget grid |
| E18 | demo day slides for a robotics startup, tactical military feel | new | offers include `armor-plate` | PASS · asked armor-plate, night-circuit, instrument-panel + "Continue without pikmi" |
| E19 | ganti tampilan jadi cyberpunk | web project with `/* pikmi: soft-wash */` | offers with `night-circuit` first, no direct apply ("cyberpunk" is a mood word now, not a style name) | PASS · asked night-circuit, armor-plate, dark-dev + "Continue without pikmi" |
| E20 | use the teenage engineering style for my synth plugin site | new | applies `instrument-panel` directly, no offer | PASS · applied instrument-panel via brand_terms |
| E21 | onboarding screens for a kids' reading app, warm and friendly | new | offers include `soft-wash` | PASS · asked soft-wash, instrument-panel, primary-riot + "Continue without pikmi"; said no style is made for kids |
| E22 | fix the padding on this button | web project with `/* pikmi: ledger-blue */` | no offer, continues `ledger-blue` | PASS · continued ledger-blue, no offer |
| E23 | bikin dokumentasi API yang enak dibaca malam hari | new | offers include `dark-dev` | PASS · asked dark-dev, nocturne-glass, instrument-panel + "Lanjut tanpa pikmi" |
| E24 | landing page hotel mewah dengan efek kaca | new | offers include `nocturne-glass` | PASS · asked nocturne-glass, lapis-lattice, japanese-minimal + "Lanjut tanpa pikmi" |
| E25 | eid greeting card for WhatsApp, elegant | new | offers include `lapis-lattice` | PASS · asked lapis-lattice, nocturne-glass, soft-wash + "Continue without pikmi" |
| E26 | bikin landing page kayak apple | new | offers include `nocturne-glass`, no direct apply ("apple" is a keyword, not a brand term) | PASS · asked nocturne-glass, japanese-minimal, ledger-blue + "Lanjut tanpa pikmi" |
| E27 | build a settings screen with a bottom tab bar in the bento style | new app | says there is no bento style and offers 2 or 3 styles, no direct apply | PASS · said no style matches bento; asked ledger-blue, instrument-panel, japanese-minimal + "Continue without pikmi" |
| E28 | bikin landing page kayak iphone | new | offers 2 or 3 styles, no direct apply | PASS · asked nocturne-glass, japanese-minimal, ledger-blue + "Lanjut tanpa pikmi" |
| E29 | bikin landing page untuk kafe kopi | new | offers 2 or 3 styles plus "Continue without pikmi", each style with a palette and font card from its `tokens.json` | PASS · asked soft-wash, japanese-minimal, nocturne-glass + "Lanjut tanpa pikmi"; each card matched its tokens.json |
| E30 | sekarang bikin halaman about | same conversation; the user earlier picked "Continue without pikmi" | stays quiet, no offer | PASS · stayed quiet |
| E31 | pakai style ledger blue aja | same conversation; the user earlier picked "Continue without pikmi" | applies `ledger-blue` directly | PASS · applied ledger-blue as a named style |
| E32 | Lanjut tanpa pikmi | web project whose tokens.css starts with `/* pikmi: soft-wash */`; the user asked "ganti tampilan jadi cyberpunk", was offered styles, and gave this answer | builds without pikmi, loads no style files and deletes the `/* pikmi: soft-wash */` line | PASS · would load no style files, delete the soft-wash marker line and add no new marker |
| E33 | tambah halaman pricing | web project with `/* pikmi: bento */` (bento was removed) | no offer; says bento is no longer in pikmi and follows the project's own look | PASS · stayed quiet; said bento is no longer in the catalog and followed the project's own look |
| E34 | bikin landing page panduan wisata jepang yang cerah, kayak poster kota | new | offers include `konbini-sky` | PASS · asked konbini-sky, indigo-woodblock, japanese-minimal + "Lanjut tanpa pikmi" |
| E35 | app jadwal kereta dengan gambar pixel jalanan | new app | offers include `konbini-sky` | PASS · asked konbini-sky, instrument-panel, ledger-blue + "Lanjut tanpa pikmi"; said only konbini-sky has a pixel street scene |
| E36 | bikin landing page minimarket kayak lawson | new | applies `konbini-sky` directly (brand term) | PASS · applied konbini-sky via brand_terms, light theme, no brand in the design |
| E37 | slide perjalanan kereta komuter jakarta, cerah dan rame | new | offers include `konbini-sky` | PASS · asked konbini-sky, primary-riot + "Lanjut tanpa pikmi"; said no one style covers both "cerah" and "rame" |
| E38 | pakai konbini sky tapi mode gelap | new | applies `konbini-sky` with its dark theme | PASS · applied konbini-sky as a named style, dark theme |

## Last run

2026-10-25, after `konbini-sky` was added (light and dark, all four media, `brand_terms` 7-eleven,
seven-eleven, lawson and familymart). New rows E34 to E38 and the rows the new style could change (E07,
E16, E29) were run with two fresh Claude Sonnet routers, four rows each, and all pass. Konbini Sky joined
the E16 offer in third place without pushing out `indigo-woodblock`, and stayed out of E07 and E29. In
E29 two previews would not open in the shared browser pane, so the router gave their paths instead, which
SKILL.md allows ("when you can").

## Earlier runs

2026-10-24, after `bento` was removed. "apple" stayed a keyword of `nocturne-glass` but left its
`brand_terms`, so "kayak apple" still gets an offer instead of applying a dark-only style; step 0 now
says a marker whose id is not in the catalog means the project keeps its own look. E09 now uses an
`instrument-panel` marker, E31 names `ledger-blue`, and E33 covers a `bento` marker. The twelve rows
that involved bento or its removal (E06, E09, E11, E17, E21, E23, E26 to E29, E31, E33) were rerun with
two fresh Claude Sonnet routers and all pass.

2026-10-24, after the offer became one question with up to 3 styles, a palette and font card per
style, and "Continue without pikmi" last. All 31 rows were rerun with Claude Sonnet as the router, four
fresh agents of seven or eight rows each, and all pass; every offer opened its previews first and read
only the offered styles' `tokens.json`. Two gaps found in that run were fixed: the card's font line
assumed a `display` font, and declining in a marked project left the old marker behind. E29 and the new
E32 were rerun with one fresh agent after the fix and pass.

2026-10-24, after seven styles were renamed away from their old genre names: `anti-design` →
`primary-riot`, `corporate-clean` → `ledger-blue`, `cyberpunk-neon` → `night-circuit`,
`islamic-geometric` → `lapis-lattice`, `ukiyo-e-print` → `indigo-woodblock`, `mecha` → `armor-plate`,
`watercolor` → `soft-wash`. All 28 rows were rerun with Claude Sonnet as the router, four fresh agents of
seven rows each, and all pass. E19 now expects an offer instead of a direct apply, because "cyberpunk"
is a keyword of `night-circuit`, not its name. E07 is the weakest pass: the router noted that no style
is retro sci-fi but followed step 3, not step 4.

2026-10-23, Claude Sonnet as the router, five fresh agents of five rows each. The first run failed eight
rows (E02, E04, E06, E14, E15, E17, E18, E24): step 2 of SKILL.md let any keyword that matched a single
style skip the offer. Step 2 now skips the offer only for a style's name, id, short form or
`brand_terms`; the eight rows and the four direct-apply rows (E05, E12, E19, E20) were rerun and all
pass.

E26 to E28 were added after the final review. E27 failed before step 6 told the agent to read
`preview.html` for components STYLE.md does not spell out; it passed after the change. E26 passed before
and after the brand-term rule was made explicit.

2026-10-24: `pastoral-storybook` was removed. E05 now expects an offer instead of a direct apply, and
E21 expects `watercolor`. E03, E05, E13 and E21 were rerun with one fresh Claude Sonnet router and all
pass.
