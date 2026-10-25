# pikmi: desain skill pemilih style

Tanggal: 2026-10-23 · Status: menunggu persetujuan

## 1. Intent

pikmi adalah skill agent (sekelas better-ui, impeccable, superpowers) yang membantu memilih dan menerapkan
style desain visual. Skill ini otomatis aktif saat user membuat desain baru atau minta mengganti tampilan,
memahami kata
suasana yang user ucapkan ("rubah tampilan web ini jadi modern industrial"), lalu **menawarkan** beberapa
style yang cocok. **User yang memilih.** Kalau user bingung atau bilang "terserah", agent merekomendasikan
satu style beserta alasannya.

Satu style harus bisa dipakai di empat medium: **UI web, slides, social media, dan app**. Ini pembeda utama
dari proyek sejenis, yang umumnya hanya mengurus UI web.

Nama `pikmi` dibaca "pick me": setiap style seolah berseru "pick me!". Lapis sarkasnya adalah slang
*pick-me*. Tagline: **"Not like other UIs."**

## 2. Goals, non-goals, anti-goals

**Goals**
- User memilih sendiri dari 2–4 tawaran; agent hanya merekomendasikan kalau diminta atau user ragu.
- Pencocokan kata suasana dalam bahasa Inggris dan Indonesia, termasuk sinonim dan slang.
- Satu style, empat medium, satu set token.
- Hemat konteks: yang selalu dimuat hanya `SKILL.md` pengarah yang pendek.
- Kualitas terjaga saat style bertambah (skrip pemeriksa dan daftar eval).

**Non-goals versi pertama**
- Server MCP, CLI npm, API online, update otomatis.
- Linter yang memeriksa kode hasil generate.
- Plugin Figma atau integrasi alat desain lain.

**Anti-goals** (gagal walaupun secara teknis jalan)
- Agent langsung memakai satu style tanpa menawarkan pilihan, padahal user tidak menyebut nama style dan
  proyeknya belum punya penanda pikmi.
- pikmi menawarkan style baru untuk proyek yang sudah punya tampilan, padahal user tidak minta ganti tampilan.
- Teks hard prompt referensi tersalin mentah ke dalam style pikmi.
- Nama, logo, atau produk brand muncul di desain yang dihasilkan.
- Style yang hanya berupa daftar class Tailwind dan tidak bisa dipakai di slides atau app.
- Hasil yang tetap terlihat seperti tampilan bawaan AI yang seragam.

## 3. Constraints

- Nama skill `pikmi`. Nama ini hanya muncul di `plugin.json`, `marketplace.json`, folder `skills/pikmi/`,
  baris `name:` di `SKILL.md`, dan README, supaya mudah diganti.
- Isi skill (SKILL.md, STYLE.md, katalog, foundations) ditulis dalam bahasa Inggris. Kata kunci ditulis dalam
  bahasa Inggris dan Indonesia.
- `SKILL.md` pengarah di bawah ±150 baris.
- File di folder style bernama `STYLE.md`, bukan `SKILL.md`, supaya installer tidak mendaftarkannya sebagai
  skill terpisah.
- Font hanya dari Google Fonts (gratis, bisa dimuat di web, slides, dan aplikasi desain).
- Setiap pasangan warna teks/latar yang disebut di STYLE.md punya angka kontras WCAG yang sudah dihitung, seperti
  di teenage-engineering sekarang.
- **Folder `hard prompt/` (materi dari luar) hanya referensi.** Keputusan user: tidak perlu file lisensi.
  Konsekuensinya: semua teks ditulis ulang dengan kata-kata sendiri, tidak ada kalimat, template HTML, atau
  checklist yang disalin, dan folder `hard prompt/` tidak ikut di-commit (masuk `.gitignore`).

## 4. Struktur repo

Sudah disetujui user.

```
style-lib/                      (folder repo; nama folder boleh tetap)
├─ .claude-plugin/
│  ├─ plugin.json
│  └─ marketplace.json          (source "./")
├─ skills/
│  └─ pikmi/
│     ├─ SKILL.md               pengarah: trigger + alur, satu-satunya yang auto-load
│     ├─ catalog.json           semua style + kata kunci + medium + tema
│     ├─ foundations/
│     │  ├─ ui.md
│     │  ├─ slides.md
│     │  ├─ social.md
│     │  └─ app.md
│     └─ styles/<id>/
│        ├─ STYLE.md
│        ├─ tokens.css
│        ├─ tokens.json
│        └─ preview.html
├─ scripts/check.py             pemeriksa untuk pembuat, tidak dipakai agent
├─ evals/prompts.md
├─ docs/superpowers/specs/      dokumen ini
├─ README.md                    galeri untuk manusia
└─ .gitignore                   .DS_Store, hard prompt/
```

## 5. Alur pengarah (SKILL.md)

**Kapan pikmi menawarkan style** (keputusan user): hanya untuk desain baru, atau saat user minta mengganti
tampilan. Kalau proyek sudah punya tampilan dan user hanya menambah atau mengubah bagian ("tambah halaman
pricing"), pikmi diam.

0. **Cek tampilan yang sudah ada.** Kalau proyek berisi `tokens.css` dengan baris penanda
   `/* pikmi: <id> */` di paling atas, lanjutkan style itu tanpa tawaran. Kalau proyek punya design system
   sendiri tanpa penanda, dan permintaan tidak meminta tampilan baru, jangan menawarkan apa pun.
1. **Kenali permintaan.** Medium apa (UI, slides, social, app; bisa lebih dari satu) dan kata suasana apa yang
   disebut. Kalau medium tidak jelas, tebak dari konteks (file yang dibuka, kata "slide", "post", "app").
2. **User menyebut nama style** (atau kata kunci brand yang memetakan ke tepat satu style): langsung pakai
   style itu, tanpa tawaran.
3. **Selain itu:** baca `catalog.json`, cocokkan kata kunci, tawarkan 2–4 style. Setiap tawaran: nama, satu
   kalimat kenapa cocok, dan path `preview.html`. Hanya style yang mendukung medium yang diminta.
4. **Tidak ada yang cocok:** katakan terus terang, lalu tawarkan yang paling mendekati.
5. **User memilih**, atau bilang "terserah": rekomendasikan satu dengan alasan, lalu lanjut kecuali user menolak.
6. **Muat hanya yang perlu:** `styles/<id>/STYLE.md`, `tokens.css` (hasil berbasis CSS) atau `tokens.json`
   (hasil lain), dan `foundations/<medium>.md` untuk medium yang dikerjakan.
7. **Bangun dalam format yang dipakai tugasnya** (keputusan user): HTML, .pptx lewat skill pptx, kode app
   native, atau alat desain. pikmi hanya menentukan tampilan, bukan format file. Untuk efek yang hanya ada
   di CSS, pakai pengganti dari bagian "Outside CSS" di STYLE.md.
8. **Tulis penanda** untuk proyek web: salin `tokens.css` ke proyek dengan baris pertama
   `/* pikmi: <id> */`. Hasil di luar web (slides, post, file desain) tidak diberi penanda.
9. **Periksa** dengan checklist STYLE.md sebelum menyerahkan hasil.

Kalau user meminta tema gelap untuk style yang hanya punya tema terang (atau sebaliknya), agent bilang
style itu tidak punya tema tersebut dan menawarkan style lain yang punya.

## 6. Format `catalog.json`

```json
{
  "version": 1,
  "styles": [
    {
      "id": "instrument-panel",
      "name": "Instrument Panel",
      "summary": "Grey hardware panels, numbered keys, a small black screen and one signal orange.",
      "keywords": {
        "en": ["industrial", "hardware", "synth", "instrument", "minimal", "playful", "teenage engineering", "op-1"],
        "id": ["industri", "mesin", "alat musik", "synthesizer", "kayak op-1"]
      },
      "media": ["ui", "slides", "social", "app"],
      "themes": ["light", "dark"],
      "preview": "styles/instrument-panel/preview.html",
      "brand_terms": ["teenage engineering", "op-1", "op-z", "ep-133"]
    }
  ]
}
```

- `keywords` untuk pencocokan; kata kunci brand boleh ada di sini.
- `brand_terms` adalah kata yang **tidak boleh** muncul di STYLE.md bagian aturan desain atau di
  `preview.html`; dipakai `check.py`.
- `summary` harus membedakan style ini dari style lain yang kata kuncinya mirip.

## 7. Format folder style

**STYLE.md** (bahasa Inggris), urutan bagian:
1. Identity: rasa, inspirasi (tanpa nama brand), kapan cocok, kapan tidak. Ditutup satu baris
   `Dial: ENERGY n / RHYTHM n / MOTION n` (bawaan style, format antislop).
2. Visual vocabulary: warna, tipografi, bentuk, kedalaman, gerak, dekorasi.
3. Reasons: satu baris alasan untuk warna, tipografi, tata letak, bentuk, kedalaman, dan gerak (antislop R-31).
4. Token usage: role token yang dipakai dan artinya.
5. Components: tombol, kartu, input, navigasi, layar/angka utama; contoh CSS memakai `var(--…)`.
6. Recipes per medium: UI, slides, social, app; masing-masing 3–6 baris konkret.
7. Outside CSS: pengganti untuk efek yang tidak ada di .pptx, app native, atau alat desain (misalnya blur
   kaca menjadi isian semi-transparan datar, clip-path menjadi bentuk vektor).
8. Contrast rules (checked): pasangan warna + rasio.
9. Pitfalls.
10. Checklist.

**tokens.css**: `:root` untuk tema utama; `[data-theme="dark"]` (atau `"light"`) untuk tema kedua bila ada.
Role token mengikuti pola teenage-engineering (`--page`, `--panel`, `--card`, `--text`, `--text-muted`,
`--accent`, `--on-accent`, `--rule`, `--link`, `--danger`, plus token khas style).

**tokens.json**: nilai yang sama persis dengan tokens.css, untuk platform selain web. Bentuknya mengikuti
tokens.json teenage-engineering yang sekarang (dibaca agent), bukan format W3C design tokens. Ekspor ke format
W3C untuk Figma atau Style Dictionary bisa ditambahkan nanti lewat skrip (keputusan builder).

**preview.html**: satu halaman mandiri yang memuat `tokens.css` dan font. Isinya komponen utama ditambah satu
contoh kecil per medium yang didukung (potongan UI, satu slide 16:9, satu post 4:5, satu layar app).
Fungsinya dua: dilihat user saat memilih, dan dipelajari agent sebagai acuan.

## 8. Foundations per medium

Aturan yang berlaku untuk semua style, ditulis sekali:
- **ui.md**: breakpoint, lebar baris teks, fokus terlihat, `prefers-reduced-motion`, ukuran klik minimum.
- **slides.md**: kanvas 1920×1080 (16:9), ukuran teks minimum, satu ide per slide, margin aman.
- **social.md**: 1080×1350 (4:5), 1080×1080, 1080×1920 (story); zona aman untuk teks; ukuran label minimum.
- **app.md**: safe area, tap target 44pt/48dp, navigasi bawah, mode gelap sistem.

Style hanya menulis yang khas untuknya di bagian Recipes.

## 9. Mengolah hard prompt menjadi style

**Diambil:** identitas dan rasa, palet warna, karakter tipografi, bentuk (radius, garis), kedalaman (bayangan),
karakter gerak, dekorasi khas, dan larangan yang benar-benar mendefinisikan style.

**Dibuang:** pemetaan class Tailwind dan regex class terlarang, template HTML generik, instruksi "salin prompt
ini", checklist yang berulang, dan daftar anti-slop generik yang ditempel di akhir setiap file.

**Diperbaiki:** kontradiksi di dalam sumber. Contoh di cyberpunk: radius `rounded-lg` vs "rounded-sm atau
none"; durasi 300ms vs 100–150ms; `active:scale-95` vs "glitch offset, bukan scale"; semua teks mono vs
heading non-mono; hero teks putih di atas cyan (kontras gagal). Pilih satu yang paling setia pada identitas
style, catat pilihannya di STYLE.md.

**Ditambahkan:** nama umum, font Google Fonts yang konkret, tokens.css/json, pasangan kontras yang dihitung,
resep empat medium, kata kunci EN+ID, `preview.html`.

## 10. Daftar style versi pertama

| id | Nama | Sumber | Tema | Catatan |
| --- | --- | --- | --- | --- |
| `instrument-panel` | Instrument Panel | teenage-engineering (sudah ada) | light, dark | ganti id; tambah resep slides & app |
| `cyberpunk-neon` | Cyberpunk Neon | cyberpunk.md | dark | |
| `anti-design` | Anti-Design | brutalism.md | light | kata kunci: brutalism, neo-brutalism |
| `corporate-clean` | Corporate Clean | corporate.md | light | |
| `pastoral-storybook` | Pastoral Storybook | ghibli.md | light | kata kunci brand: ghibli |
| `islamic-geometric` | Islamic Geometric | islamic.md | light (ivory), dark (biru tua) | lihat catatan budaya |
| `ukiyo-e-print` | Ukiyo-e Print | japanese-flat.md | light | |
| `japanese-minimal` | Japanese Minimal | japanese-minimalist.md | light | sumbernya "Japanese Fresh" |
| `mecha` | Mecha | sci-fi.md | dark | kata kunci brand: gundam, evangelion |
| `watercolor` | Watercolor | watercolor.md | light | |
| `nocturne-glass` | Nocturne Glass | glassmorphism.md | dark | dua sistem di file sumber digabung |
| `bento` | Bento | bento.md (Bento Grid) | light, dark | lihat catatan Bento |
| `dark-dev` | Dark Dev | dark_dev.md (Dark Mode) | dark | untuk alat developer dan dashboard malam |

**Catatan Bento (keputusan builder):** sumbernya terutama pola tata letak (kartu beragam ukuran di grid),
dan satu-satunya identitas warnanya adalah gradien biru-ungu, yaitu tampilan AI generik yang justru dihindari.
Bento di pikmi memakai permukaan netral (zinc) dengan kartu berwarna lembut dan satu aksen; identitasnya
datang dari grid, ukuran kartu yang bervariasi, dan rasa "widget". Gradien biru-ungu dibuang.

**Catatan budaya, islamic-geometric:** pakai pola geometri, bintang, dan bingkai lengkung. Jangan pakai
kaligrafi ayat atau teks keagamaan sebagai hiasan, dan jangan pakai gambar masjid sebagai dekorasi produk
yang tidak berhubungan.

## 11. Kompatibilitas antislop

Keputusan user: **setiap style harus lolos aturan antislop** (skill `antislop` yang terpasang di mesin user).
antislop adalah filter, bukan larangan teknik: teknik boleh dipakai kalau tujuannya ditulis dan dosisnya
dibatasi. Style pikmi berperan sebagai "design direction" yang diminta antislop (R-37), dan bagian Reasons serta
baris Dial di STYLE.md memenuhi R-31 dan Part 3.

**Aturan umum untuk semua style**
- Tidak ada em dash (—) di teks UI, termasuk di `preview.html` (R-02). En dash di nomor model boleh.
- Palet aktif per halaman: maksimal 2–3 warna inti + 1 aksen; netral tidak dihitung (R-29). Style yang
  sumbernya punya lebih banyak warna menulis kombinasi mana yang dipakai bersama.
- Glow hanya di 1–2 elemen fokus (R-13). Blur kaca hanya di 1–2 elemen (R-10).
- Bayangan hanya untuk penanda elevasi, bukan di semua komponen (R-12).
- Radius konsisten dan bertingkat; tidak semua elemen berbentuk pil (R-11).
- Pola latar (grid, scanline, garis) hanya kalau menjadi identitas style, ditulis alasannya, dan dibatasi
  pada satu permukaan (R-07).
- Monospace besar dan label huruf besar berjarak lebar hanya dengan alasan identitas yang ditulis (R-06).
- Font bukan pilihan bawaan AI (Inter, Geist, Space Grotesk, JetBrains Mono, Fira Code, dan sejenisnya)
  kecuali ada alasan yang ditulis (R-06).
- Animasi punya tujuan dan jalur `prefers-reduced-motion`; tidak ada loop atau pulse tanpa akhir kecuali
  indikator status yang nyata (R-19).
- Tema gelap tetap butuh alasan; untuk style yang hanya punya satu tema, alasannya ditulis di Reasons (R-21).
- Kontras WCAG AA untuk semua teks (R-25).

**Penyesuaian per style** (yang berubah dari sumbernya)

| Style | Penyesuaian |
| --- | --- |
| `instrument-panel` | Label cetak tetap (identitas panel), tidak dibuat sebagai badge di atas judul. |
| `cyberpunk-neon` | Neon lewat warna dan garis 1px; glow hanya pada CTA utama dan satu indikator langsung. Scanline hanya di satu permukaan hero. Mono untuk data dan label; judul memakai font display. |
| `anti-design` | Per halaman pilih 2–3 warna primer + 1 aksen dari set sumber. Rotasi dan "tata letak rusak" tidak boleh memindahkan target klik atau mengganggu urutan fokus. |
| `corporate-clean` | Wajib punya identitas (aksen dan font yang dipilih dengan alasan) supaya tidak jatuh ke "sterile default"; tidak meniru produk terkenal (R-30). |
| `pastoral-storybook` | Radius bertingkat (pil hanya untuk tombol dan tag); bayangan selektif; palet dikurangi per halaman; dekorasi alam harus berhubungan dengan konten. |
| `islamic-geometric` | Tiga warna inti; emerald dan merah tua hanya untuk status atau satu aksen. |
| `japanese-minimal` | Satu aksen pastel per halaman. |
| `mecha` | Judul memakai sans condensed, mono untuk anotasi; grid teknis hanya di satu permukaan; garis bahaya hanya untuk peringatan nyata. |
| `watercolor` | Maksimal dua noda warna per tampilan; italic untuk judul, teks isi tegak supaya mudah dibaca. |
| `nocturne-glass` | Kaca hanya di 1–2 elemen utama; permukaan lain memakai warna malam yang solid. Satu aksen champagne. |
| `bento` | Mosaik bento hanya untuk satu bagian yang isinya memang punya bobot berbeda (R-05, R-14); ukuran kartu mengikuti hierarki isi; bagian lain memakai komposisi lain. |
| `dark-dev` | Tidak memakai jendela terminal palsu sebagai visual hero (R-05); mono hanya untuk kode. |

## 12. Pemeriksaan kualitas

**scripts/check.py** (Python 3, tanpa dependensi):
- Setiap entri katalog punya folder dan empat file wajib; setiap folder punya entri katalog.
- Tidak ada file bernama `SKILL.md` di dalam `styles/`.
- Nilai tokens.css sama dengan tokens.json, untuk semua tema.
- Setiap angka kontras di bagian "Contrast rules" STYLE.md cocok dengan hasil hitung dari token (toleransi 0.01).
- `brand_terms` tidak muncul di `preview.html` maupun di bagian aturan desain STYLE.md.
- `SKILL.md` pengarah di bawah 150 baris.
- Tidak ada em dash di `preview.html`.
- Setiap STYLE.md punya baris `Dial:` dan bagian Reasons serta Outside CSS.

**evals/prompts.md**: sekitar 25 permintaan (campuran EN/ID, empat medium) beserta style yang seharusnya
muncul di tawaran. Contoh: "rubah tampilan web ini jadi modern industrial" → `instrument-panel` ada di
tawaran. Termasuk kasus di mana pikmi **harus diam**, misalnya "tambah halaman pricing" di proyek yang sudah
punya penanda pikmi atau design system sendiri. Dijalankan manual saat style ditambah.

## 13. Migrasi teenage-engineering

- `teenage-engineering/` → `skills/pikmi/styles/instrument-panel/`.
- Description di frontmatter SKILL.md lama → kata kunci di `catalog.json`.
- Isi SKILL.md lama (tanpa frontmatter) → STYLE.md, ditambah resep slides & app, sesuai format bagian 7.
- tokens.css dan tokens.json tidak berubah nilainya.
- Tambah `preview.html`.

## 14. Diserahkan ke builder

- Kata-kata di STYLE.md, resep per medium, dan isi foundations.
- Pilihan font Google Fonts per style (harus masuk akal untuk karakter style dan mendukung huruf Latin).
- Tata letak `preview.html`.
- Detail implementasi `check.py`.
- Isi README dan galeri.

## 15. Keputusan yang diambil builder (perlu dicek user)

- Nama umum tiap style di tabel bagian 10.
- Bento memakai permukaan netral dan membuang gradien biru-ungu.
- tokens.json tetap memakai bentuk yang sekarang, bukan format W3C.
- Penanda hanya ditulis untuk proyek web.
- Penyesuaian antislop per style di bagian 11.
- Folder `hard prompt/` masuk `.gitignore`.
