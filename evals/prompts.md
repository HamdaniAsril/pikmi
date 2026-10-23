# pikmi router evals

Each row is a request plus the project context. A fresh agent that has read only
`skills/pikmi/SKILL.md` and `skills/pikmi/catalog.json` says what it would offer or do, without
building anything. The row passes when that answer matches "Expected".

Run these by hand whenever a style is added or keywords change.

| ID | Prompt | Project context | Expected | Result |
| --- | --- | --- | --- | --- |
| E01 | rubah tampilan web ini jadi modern industrial | web project, no marker | offers include `instrument-panel` | PASS · offered instrument-panel, mecha |
| E02 | bikin slide pitch deck yang terasa mewah dan malam | new | offers include `nocturne-glass` | PASS (rerun) · offered nocturne-glass, cyberpunk-neon, dark-dev |
| E03 | design a landing page for a meditation app, calm and airy | new | offers include `japanese-minimal` | PASS · offered japanese-minimal, watercolor, pastoral-storybook |
| E04 | bikin poster instagram ramadan | new | offers include `islamic-geometric` | PASS (rerun) · offered islamic-geometric, nocturne-glass, watercolor |
| E05 | make it look like a Ghibli movie | new | applies `pastoral-storybook` directly, no offer | PASS · applied pastoral-storybook via brand_terms |
| E06 | dashboard buat tim devops, gelap | new | offers include `dark-dev` | PASS (rerun) · offered dark-dev, bento, mecha |
| E07 | bikin kayak game sci-fi jadul | new | offers include `mecha` or `cyberpunk-neon`, and says nothing matches exactly | PASS · offered cyberpunk-neon, mecha, instrument-panel; said nothing is retro sci-fi exactly |
| E08 | terserah, yang penting keren | new | recommends exactly one style with a reason | PASS · recommended bento with a reason |
| E09 | tambah halaman pricing | web project with `/* pikmi: bento */` | no offer, continues `bento` | PASS · continued bento, no offer |
| E10 | add a settings screen | app with its own design system, no marker | stays quiet, no offer | PASS · stayed quiet |
| E11 | post linkedin untuk laporan kuartal | new | offers include `corporate-clean` | PASS · offered corporate-clean, bento, japanese-minimal |
| E12 | watercolor tapi dark mode | new | says watercolor has no dark theme and offers styles that do | PASS · said watercolor is light-only; offered nocturne-glass, islamic-geometric, bento |
| E13 | bikin undangan nikah yang lembut dan artistik | new | offers include `watercolor` | PASS · offered watercolor, pastoral-storybook, islamic-geometric |
| E14 | poster gig punk yang norak tapi keren | new | offers include `anti-design` | PASS (rerun) · offered anti-design, cyberpunk-neon, mecha |
| E15 | neon HUD screens for an esports tournament app | new | offers include `cyberpunk-neon` | PASS (rerun) · offered cyberpunk-neon, mecha |
| E16 | halaman menu restoran jepang tradisional | new | offers include `ukiyo-e-print` | PASS · offered ukiyo-e-print, japanese-minimal |
| E17 | portfolio with widget-style cards for my projects | new | offers include `bento` | PASS (rerun) · offered bento, instrument-panel, japanese-minimal |
| E18 | demo day slides for a robotics startup, tactical military feel | new | offers include `mecha` | PASS (rerun) · offered mecha, cyberpunk-neon, instrument-panel |
| E19 | ganti tampilan jadi cyberpunk | web project with `/* pikmi: watercolor */` | applies `cyberpunk-neon` and replaces the marker | PASS · applied cyberpunk-neon, replaces the marker, warns it is dark-only |
| E20 | use the teenage engineering style for my synth plugin site | new | applies `instrument-panel` directly, no offer | PASS · applied instrument-panel via brand_terms |
| E21 | onboarding screens for a kids' reading app, warm and friendly | new | offers include `pastoral-storybook` | PASS · offered pastoral-storybook, watercolor |
| E22 | fix the padding on this button | web project with `/* pikmi: corporate-clean */` | no offer, continues `corporate-clean` | PASS · continued corporate-clean, no offer |
| E23 | bikin dokumentasi API yang enak dibaca malam hari | new | offers include `dark-dev` | PASS · offered dark-dev, nocturne-glass |
| E24 | landing page hotel mewah dengan efek kaca | new | offers include `nocturne-glass` | PASS (rerun) · offered nocturne-glass, japanese-minimal, islamic-geometric |
| E25 | eid greeting card for WhatsApp, elegant | new | offers include `islamic-geometric` | PASS · offered islamic-geometric, nocturne-glass |
| E26 | bikin landing page kayak apple | new | offers include `nocturne-glass` and `bento` (brand listed under two styles) | PASS · offered nocturne-glass, bento, japanese-minimal |
| E27 | build a settings screen with a bottom tab bar in the bento style | new app | applies `bento` and opens its `preview.html` for the tab bar | PASS · applied bento; opened STYLE.md, tokens.json, foundations/app.md, preview.html |
| E28 | bikin landing page kayak iphone | new | offers include `bento`, no direct apply | PASS · offered bento, nocturne-glass, japanese-minimal |

## Last run

2026-10-23, Claude Sonnet as the router, five fresh agents of five rows each. The first run failed eight
rows (E02, E04, E06, E14, E15, E17, E18, E24): step 2 of SKILL.md let any keyword that matched a single
style skip the offer. Step 2 now skips the offer only for a style's name, id, short form or
`brand_terms`; the eight rows and the four direct-apply rows (E05, E12, E19, E20) were rerun and all
pass.

E26 to E28 were added after the final review. E27 failed before step 6 told the agent to read
`preview.html` for components STYLE.md does not spell out; it passed after the change. E26 passed before
and after the brand-term rule was made explicit.
