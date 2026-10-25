# Konbini Sky Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Menambahkan style `konbini-sky` ke pikmi: langit siang cerah di atas kertas putih, kata raksasa putih, caption kobalt, satu pemandangan pixel di garis cakrawala, dan tema malam yang menyala.

**Architecture:** Satu folder style baru (`STYLE.md`, `tokens.css`, `tokens.json`, `preview.html`) ditambah satu entri `catalog.json`, dibangun bertahap: siang untuk UI, lalu slides, social, dan app, lalu tema malam, lalu README dan eval. `scripts/check.py` yang sudah ada menjadi test otomatis. Pengecekan visual memakai server `pikmi-previews` dari `.claude/launch.json` dan satu skrip JS yang ditulis sekali di bawah.

**Tech Stack:** Markdown, JSON, CSS custom properties dan container query units, HTML statis dengan SVG inline, Google Fonts, Python 3 (`scripts/check.py`).

**Spec:** `docs/superpowers/specs/2026-10-25-konbini-sky-design.md`. Mockup acuan: `docs/superpowers/specs/2026-10-25-konbini-sky-mockups/day.html` dan `night.html`. Format file style: spec pikmi `docs/superpowers/specs/2026-10-23-pikmi-design.md` bagian 7 dan 11, plus bagian "Shared formats" di `docs/superpowers/plans/2026-10-23-pikmi.md`.

## Global Constraints

- Kerja langsung di `main`, satu commit per task, tidak di-push.
- STYLE.md, summary katalog, dan teks preview berbahasa Inggris. Pengecualiannya kata Jepang dan satu contoh berbahasa Indonesia (K9). Kata kunci katalog EN dan ID.
- Tidak ada em dash (—) di STYLE.md, preview.html, dan catalog.json.
- `brand_terms` (7-eleven, seven-eleven, lawson, familymart) tidak boleh muncul di keempat file style. Papan nama di pemandangan memakai huruf pixel abstrak atau nama produk fiktif ("EKIMAE").
- Font hanya Public Sans 500, 700, 900 (`--font-sans`) dan Noto Sans JP 900 (`--font-jp`). Public Sans dipilih saat menyusun rencana ini (K1), setelah dibandingkan dengan Inter Tight, Hanken Grotesk, Schibsted Grotesk, Archivo, dan Albert Sans. Public Sans paling dekat ke Helvetica Bold di referensi, dan belum dipakai style lain. Lebarnya sekitar 6% lebih lebar dari Inter Tight di mockup.
- Palet per halaman: langit, kertas, dan kobalt sebagai inti, ditambah jingga sebagai satu aksen. Navy dan `--text-muted` dihitung netral.
- Radius 0, tanpa bayangan, dan tanpa gradasi selain `--sky`.
- Pixel art hanya di pemandangan: tidak ada font pixel, sudut bertangga, atau langit bergradasi bertingkat. Satu adegan per halaman, kecuali hero landing yang boleh menjajarkan dua adegan.
- Teks di langit selalu putih (`--on-sky`) di kedua tema. Teks putih kecil di langit minimal 14px dan 700. Harga, jam, error, label form, dan instruksi tidak boleh hanya ditulis putih di langit.
- Kata besar di kertas: kanji atau kana yang artinya benar untuk konten Jepang. Untuk konten lain, satu atau dua kata dalam bahasa kontennya, 900 kobalt, ditumpuk per kata. Konten non-Jepang tidak memakai huruf Jepang.
- Tidak ada statistik karangan di preview. Angka yang dipakai harus berupa properti konten (menit jalan kaki, jam buka), bukan klaim.
- Target klik minimal 44px; `check.py` memeriksa `min-height` di selector `.btn`, `.field`, `.tab`, dan `button`. Fokus berupa outline 2px dengan offset 2px.
- `python3 scripts/check.py` mencetak `OK: 12 styles checked` di akhir setiap task.

## Review Focus

1. **Layar 375px.** Kata raksasa dengan tracking negatif dan `white-space: nowrap` gampang memicu scroll horizontal. Halaman harus tetap tanpa scroll horizontal, di kedua tema. Dites oleh skrip cek preview di Task 1, 2, dan 3.
2. **Kata raksasa yang panjang**, misalnya "YOGYAKARTA" (10 huruf). Kata itu harus tetap satu baris dan muat di lebarnya, tidak terpotong. Dites di Task 1, langkah 6.
3. **Teks putih kecil di langit.** Nav, caption, dan baris info cenderung dibuat 12 sampai 13px. Semua teks di langit selain kata raksasa harus minimal 14px dan 700. Dites oleh skrip cek preview.
4. **Ganti tema.** Saat malam, pemandangan siang tidak boleh tetap terlihat di langit malam, dan tombol ganti tema mengubah `aria-checked`. Dites di Task 3, langkah 6.
5. **Contoh non-Jepang.** Post Bandung tidak boleh berisi huruf Jepang, dan pemandangannya jalanan lokal. Dites di Task 2, langkah 6.

### Skrip cek preview (dipakai di Task 1 sampai 3)

Jalankan di halaman preview lewat `javascript_tool` Browser pane. Kalau semuanya lolos, hasilnya `[]`.

```js
(() => {
  const errs = [];
  // canvases are shown scaled down: judge text at its real size against that medium's minimum
  const canvas = { slide: [1920, 20], post: [1080, 28], phone: [375, 14] };
  const realSize = el => {
    const c = el.closest('.slide, .post, .phone');
    const [width, min] = c ? canvas[['slide', 'post', 'phone'].find(k => c.classList.contains(k))] : [0, 14];
    const scale = c ? width / c.getBoundingClientRect().width : 1;
    return [parseFloat(getComputedStyle(el).fontSize) * scale, min];
  };
  if (document.documentElement.scrollWidth > innerWidth) errs.push('horizontal scroll');
  document.querySelectorAll('.giant').forEach(g => {
    if (g.scrollWidth > g.clientWidth + 1) errs.push('giant overflows: ' + g.textContent.trim());
  });
  document.querySelectorAll('.sky *').forEach(el => {
    if (el.closest('svg') || el.closest('.giant')) return;
    const ownText = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
    if (!ownText || !el.getClientRects().length) return;
    const [size, min] = realSize(el);
    if (size < min || Number(getComputedStyle(el).fontWeight) < 700) errs.push('small sky text: ' + el.textContent.trim().slice(0, 30));
  });
  return errs;
})()
```

Batas minimumnya: 14px di halaman dan layar app, 20px di slide 1920×1080, dan 28px di post 1080×1350 (sesuai `foundations/slides.md` dan `social.md`).

Cara membuka: `preview_start` dengan `name: "pikmi-previews"`, lalu `navigate` ke `http://localhost:8765/styles/konbini-sky/preview.html`. Ukuran layar diatur dengan `resize_window` (`width: 1280, height: 900`, lalu preset `mobile`). Kembalikan ke preset `desktop` setelah selesai.

---

## File map

```
skills/pikmi/catalog.json                          Task 1 (entri baru), Task 2 (media), Task 3 (themes, summary)
skills/pikmi/styles/konbini-sky/tokens.css         Task 1 (light), Task 3 (dark)
skills/pikmi/styles/konbini-sky/tokens.json        Task 1 (light), Task 3 (dark)
skills/pikmi/styles/konbini-sky/STYLE.md           Task 1, 2, 3
skills/pikmi/styles/konbini-sky/preview.html       Task 1, 2, 3
README.md, evals/prompts.md                        Task 4
```

## Nilai token

Pemetaan JSON ke CSS mengikuti "Shared formats" di plan pikmi. Tema light ditulis di `:root`; `[data-theme="dark"]` hanya berisi role yang nilainya berbeda.

| Grup | Nilai |
| --- | --- |
| `name` / `title` | `konbini-sky` / `Konbini Sky` |
| `fonts` | `sans` Public Sans [500, 700, 900]; `jp` Noto Sans JP [900] |
| `typeScale` | label 13, caption 14, body 17, lead 20, h3 24, h2 34, h1 56, display 240 |
| `radius` | control 0, card 0 |
| `space` | xs 4, sm 8, md 16, lg 24, xl 48, section 96 |
| `colors` | `on-sky` #FFFFFF |
| `effects` | `sky` `linear-gradient(180deg, var(--sky-top) 0%, var(--sky-top) 28%, var(--sky-mid) 68%, var(--horizon) 100%)`; `tracking-display` `-0.05em`; `leading-display` `0.82`; `rule-strong` `2px solid var(--ink)` |

| Role | light | dark (Task 3) |
| --- | --- | --- |
| page | #F7F7F4 | #0E1526 |
| panel | #FFFFFF | #121B31 |
| card | #FFFFFF | #16213B |
| rule | rgba(29, 91, 216, 0.28) | rgba(126, 166, 255, 0.25) |
| text | #1E2B4A | #DCE4F2 |
| text-muted | #4A5876 | #9EADC8 |
| accent | #1D5BD8 | #1D5BD8 |
| on-accent | #FFFFFF | #FFFFFF |
| link | #1D5BD8 | #7EA6FF |
| danger | #C0352B | #FF8F85 |
| ink | #1D5BD8 | #7EA6FF |
| sky-top | #5CB9E8 | #0B1733 |
| sky-mid | #96D3F0 | #1B3263 |
| horizon | #E3F2FA | #2F4C80 |
| orange | #EE6A2B | #FF7A35 |
| focus-on-sky | #1E2B4A | #FFFFFF |

`--accent` adalah isian tombol (sama di kedua tema). `--ink` adalah warna teks kobalt: caption, angka, kata besar, garis tebal.

## Bentuk komponen (dipakai Task 1 sampai 3)

Nama class di bawah dipakai di STYLE.md Components dan di preview.html. Isi CSS-nya ditulis implementer dengan `var(--…)`.

- `.sky`: `background: var(--sky)`, `color: var(--on-sky)`, `container-type: inline-size`.
- `.giant`: `--font-sans` 900, `letter-spacing: var(--tracking-display)`, `line-height: var(--leading-display)`, `white-space: nowrap`, `font-size: min(var(--type-display), calc(150cqw / var(--chars, 6)))`. Setiap kata raksasa menulis `style="--chars: N"` sesuai jumlah hurufnya. Angka 150 dihitung dari lebar rata-rata huruf Public Sans 900 dengan tracking -0.05em (sekitar 0.6em) supaya kata memenuhi sekitar 90% lebar. Kalau di browser kata 6 huruf ternyata lebih dari 95% atau kurang dari 80% lebar wadah, sesuaikan angka 150 dan tulis angka barunya di STYLE.md.
- `.trio`: flex, `justify-content: space-between`, `--ink`, 700, ukuran caption.
- `.bigword`: kata besar di kertas, `--ink` 900. Isinya satu kata per baris (`<br>` atau blok). Font `--font-jp` untuk huruf Jepang, `--font-sans` untuk kata lain.
- `.numbered`: `border-top: var(--rule-strong)`, angka 900 di atas judul blok.
- `.btn`: `min-height: 48px`, isian `--accent`, teks `--on-accent` 700, radius 0. `.btn.line` transparan dengan garis 1.5px `--ink` dan teks `--ink`. Di dalam `.sky`, `.btn.line` memakai garis dan teks `--on-sky`.
- `.field`: `min-height: 48px`, latar `--card`, garis 1.5px `--ink`, radius 0. Label selalu terlihat di atasnya.
- Fokus: `outline: 2px solid var(--ink); outline-offset: 2px`. Di dalam `.sky`: `outline-color: var(--focus-on-sky)`.
- `.pageno`: nomor kecil 700 `--ink` di pojok kanan bawah.
- `.scene`: `<svg>` dengan `shape-rendering: crispEdges`, `display: block`, lebar 100%. Tanah di bagian bawah gambar diisi `var(--page)` lewat `style="fill: var(--page)"`, bukan warna tetap. Pemandangan siang memakai class `scene-day`, pemandangan malam `scene-night`.

---

### Task 1: Konbini Sky siang untuk UI

**Files:**
- Modify: `skills/pikmi/catalog.json` (entri baru di akhir array `styles`)
- Create: `skills/pikmi/styles/konbini-sky/tokens.css`, `tokens.json`, `STYLE.md`, `preview.html`

**Interfaces:**
- Consumes: nilai token dan bentuk komponen di atas; simbol SVG `konbini` dan `train` dari `mockups/day.html`.
- Produces: role token di atas (light); class komponen di atas; simbol SVG `scene-konbini-day` dan `scene-station-day` di preview.html; elemen `id="components"` dan `id="ui"`.

- [ ] **Step 1: Tambah entri katalog, pastikan check gagal**
  Entri: `id` `konbini-sky`; `name` `Konbini Sky`; `summary` "Bright daytime sky over white paper, giant white grotesk type, cobalt captions and one pixel-art street scene on the horizon; bolder and sunnier than Japanese Minimal."; `keywords` dan `brand_terms` persis seperti K7 di spec; `media` `["ui"]`; `themes` `["light"]`; `preview` `styles/konbini-sky/preview.html`.
  Run: `python3 scripts/check.py`
  Expected: exit 1, ada baris `konbini-sky: missing folder`.

- [ ] **Step 2: Tulis `tokens.css` dan `tokens.json` (light)**
  Pakai nilai di tabel token. Baris pertama `tokens.css` adalah `/* pikmi: konbini-sky */`, lalu komentar `Konbini Sky. Same values as tokens.json.` dan URL font `https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@900&family=Public+Sans:wght@500;700;900&display=swap`.

- [ ] **Step 3: Tulis `STYLE.md`**
  Semua heading wajib, urut. Resep cukup `### UI` dulu. Isi yang harus ada:
  - **Identity:** poster kota yang dijadikan sistem desain. Bukan hanya untuk Jepang; untuk konten lain, kata dan pemandangannya mengikuti tempat kontennya. Daftar cocok dan tidak cocok dari K5. Tulis "Light only for now" (diganti di Task 3). Baris `Dial: ENERGY 2 / RHYTHM 2 / MOTION 1`.
  - **Visual vocabulary:**
    - Warna dan tata letak dua zona dari spec bagian 4.
    - Aturan pemandangan pixel: grid bilangan bulat, viewBox kecil, satu bangunan utama di cakrawala, yang jauh memudar ke biru langit, kabel listrik garis tipis, tanah `--page`, tanpa brand, lokasi mengikuti konten.
    - Aturan kata besar (K2).
    - Teks putih yang paling kecil (nav, caption, baris info) sebisa mungkin di bagian atas langit. Kata raksasa dan subjudul tebal boleh lebih ke bawah.
    - Gerak: tanpa gerak atau fade 300 sampai 500ms, mati di `prefers-reduced-motion`.
  - **Reasons:** satu baris untuk warna, tipografi, tata letak, bentuk, kedalaman, dan gerak, ditambah:
    - Public Sans sebagai pengganti Helvetica.
    - Gradasi langit sebagai satu-satunya gradasi, karena itu identitasnya.
    - Pemandangan sebagai satu-satunya permukaan berpola (R-07).
    - Teks putih di langit di bawah AA sebagai keputusan sadar demi tampilan.
  - **Token usage:** tabel semua role dan token khas di atas.
  - **Components:** CSS untuk semua class di "Bentuk komponen".
  - **Recipes, `### UI`:** landing sesuai spec bagian 4 (nav di langit, kata raksasa, subjudul dan lede, dua adegan berdampingan; di kertas trio, tiga blok bernomor, baris kata besar dengan ajakan, footer dengan `.pageno`), plus satu baris untuk halaman daftar atau toko.
  - **Outside CSS:** baris untuk:
    - gradasi `--sky` (gradasi linear dengan stop 0, 28, 68, 100%);
    - `cqw`/`--chars` (hitung ukuran huruf dari lebar bingkai);
    - SVG pixel (vektor kotak, atau PNG skala bilangan bulat dengan nearest-neighbor);
    - kanji vertikal (satu huruf per baris, bukan `writing-mode`).
  - **Contrast rules (checked):** baris light dengan angka persis:

    | Text | On | Ratio | Rule (awal kalimat) |
    | --- | --- | --- | --- |
    | `--text` | `--page` | 13.05 | Body text |
    | `--text-muted` | `--page` | 6.64 | Secondary text |
    | `--ink` | `--page` | 5.53 | Captions, numbers, the big word |
    | `--ink` | `--card` | 5.93 | Ink on white cards |
    | `--on-accent` | `--accent` | 5.93 | Button text |
    | `--link` | `--page` | 5.53 | Links |
    | `--danger` | `--page` | 5.17 | Error text |
    | `--on-sky` | `--sky-top` | 2.20 | White on the top of the sky, a deliberate exception |
    | `--on-sky` | `--sky-mid` | 1.63 | White text lower on the sky drops toward this |
    | `--orange` | `--page` | 2.91 | Orange never carries text on paper |
    | `--ink` | `--page` | 5.53 | Focus ring on paper |
    | `--focus-on-sky` | `--sky-top` | 6.37 | Focus ring on the sky |
    | `--ink` | `--card` | 5.93 | Field border |
  - **Pitfalls:**
    - pixel merembes ke UI;
    - brand atau logo di papan nama;
    - huruf Jepang di konten non-Jepang, atau kanji acak;
    - info penting hanya ditulis putih di langit;
    - teks putih kecil di bawah 14px atau 700;
    - teks jingga di kertas;
    - lebih dari satu adegan;
    - bayangan atau sudut membulat;
    - gradasi kedua;
    - pemandangan yang melayang, tidak duduk di cakrawala;
    - kata raksasa yang terpecah dua baris atau meluap.
  - **Checklist:** kebalikan dari tiap pitfall, ditambah fokus 2px dan tap target 48px.

- [ ] **Step 4: Tulis `preview.html` (siang, UI)**
  Dokumen mandiri. Isinya:
  - `<link rel="stylesheet" href="tokens.css">` dan satu link Google Fonts dengan URL di Step 2.
  - Simbol `scene-konbini-day` (120×48) dan `scene-station-day` (120×40), disalin dari simbol `konbini` dan `train` di `mockups/day.html`. Warna tanah tetapnya diganti `fill: var(--page)`.
  - Hero landing produk fiktif "EKIMAE": nav di langit, `.giant` "EKIMAE" dengan `--chars: 6`, subjudul dan lede, kedua adegan berdampingan di satu `<svg viewBox="0 0 240 48">`.
  - `id="components"`: semua komponen dalam keadaan biasa, hover, fokus, dan disabled, termasuk satu `.btn.line` di atas langit dan satu `.field` dengan label serta pesan error.
  - `id="ui"`: sisa landing di kertas (trio, tiga `.numbered`, baris `.bigword` "駅前" dengan ajakan dan dua tombol, footer dengan `.pageno`).

  Teksnya bahasa Inggris, contohnya panduan jalan kaki di sekitar stasiun. Proporsinya mengikuti `mockups/day.html`, tapi ukuran kata raksasa mengikuti rumus `.giant`.

- [ ] **Step 5: Jalankan check, pastikan lulus**
  Run: `python3 scripts/check.py`
  Expected: `OK: 12 styles checked`.

- [ ] **Step 6: Cek visual**
  1. Buka preview, lalu jalankan skrip cek preview di 1280px dan 375px.
     Expected: `[]` di keduanya.
  2. Uji kata panjang. Jalankan `const g = document.querySelector('.giant'); g.textContent = 'YOGYAKARTA'; g.style.setProperty('--chars', 10);`, lalu skrip cek lagi di 375px dan 1280px.
     Expected: `[]` di keduanya.
  3. Muat ulang halaman, lalu ambil screenshot hero di 1280px. Bandingkan dengan `mockups/day.html`: langit, kata raksasa, dan adegan harus terbaca sebagai tampilan yang sama.
  4. Tekan Tab melewati nav dan tombol. Fokus harus terlihat di langit dan di kertas.

- [ ] **Step 7: Commit**
  ```bash
  git add skills/pikmi/catalog.json skills/pikmi/styles/konbini-sky
  git commit -m "feat(pikmi): add konbini-sky style for web UI"
  ```

### Task 2: Slides, social, dan app

**Files:**
- Modify: `skills/pikmi/catalog.json`, `skills/pikmi/styles/konbini-sky/STYLE.md`, `skills/pikmi/styles/konbini-sky/preview.html`

**Interfaces:**
- Consumes: semua yang diproduksi Task 1.
- Produces: simbol `scene-ruko-day`; elemen `id="slides"`, `id="social"`, `id="app"`; class kanvas `.slide` (16/9), `.post` (4/5), `.phone` (9/19.5).

- [ ] **Step 1: Ubah `media` menjadi `["ui", "slides", "social", "app"]`, pastikan check gagal**
  Run: `python3 scripts/check.py`
  Expected: exit 1, ada `konbini-sky: missing recipe 'Slides'` dan `konbini-sky: preview.html missing id="slides"`.

- [ ] **Step 2: Tambah resep `### Slides`, `### Social`, `### App` di STYLE.md**
  - **Slides:** slide judul dan slide data dari spec bagian 4. Batang grafik memakai `--ink` dengan satu batang `--orange` untuk nilai yang disorot.
  - **Social:** resep K6 (1080×1350), dengan peringatan agar tidak menyalin komposisi poster mana pun.
  - **App:** header langit dari spec bagian 4. Kertas berisi trio, daftar bernomor, satu tombol penuh, dan tab bar `--card` dengan item aktif `--ink`.
  - **Outside CSS:** tambahkan baris kanvas tetap (slide 1920×1080, post 1080×1350) untuk menggantikan `cqw`.

- [ ] **Step 3: Tambah tiga bagian di `preview.html`**
  - `id="slides"`: dua `.slide` 16:9.
    - Slide judul: "EKIMAE", "Third quarter report", adegan konbini.
    - Slide data: pita langit rata 24%, judul "Ten minutes from any exit". Angka besarnya "10" dengan caption "minutes on foot". Grafik batangnya berisi menit jalan kaki ke enam tempat fiktif, dengan tempat terjauh berwarna `--orange`. Ada kanji vertikal "徒歩" dan `.pageno`.
  - `id="social"`: satu `.post` 4:5, contoh lokal K9.
    - Langit: `.giant` "BANDUNG" (`--chars: 7`) dan subjudul "West Java".
    - Di cakrawala: adegan `scene-ruko-day`.
    - Kertas: trio "open at six", "by the station", "kopi tubruk"; `.bigword` "KOPI" di atas "PAGI" dengan `--font-sans`; satu kalimat pendek; `.pageno` "04".
  - `id="app"`: satu `.phone`, menyalin layar app di `mockups/day.html`.
    - Sapaan dan judul "SHIBUYA" dengan "渋谷" vertikal putih, baris info, adegan stasiun.
    - Trio, daftar tiga tempat, tombol "Start walking", tab bar empat item.
  - Simbol baru `scene-ruko-day` (viewBox 0 0 120 48, tanah `var(--page)` di y 43 sampai 48):
    - tiga ruko dua lantai selebar 30 unit, dengan jendela berteralis dan rolling door;
    - ruko tengah adalah minimarket dengan fasad `--ink`, garis `--orange`, huruf pixel putih abstrak, dan kaca terang;
    - dua motor parkir, satu tiang dan kabel listrik;
    - bangunan jauh berwarna biru pudar.

  Selector tombol dan tab di dalam `.slide`, `.post`, dan `.phone` tidak boleh memakai `min-height` di bawah 44px. Kalau perlu lebih kecil, hapus `min-height` di kanvas yang diperkecil itu.

- [ ] **Step 4: Jalankan check, pastikan lulus**
  Run: `python3 scripts/check.py`
  Expected: `OK: 12 styles checked`.

- [ ] **Step 5: Cek visual**
  Jalankan skrip cek preview di 1280px dan 375px.
  Expected: `[]` di keduanya.

  Ambil screenshot `#slides`, `#social`, dan `#app`, lalu bandingkan dengan `mockups/day.html` (slide dan app). Ketiganya harus duduk di garis cakrawala.

- [ ] **Step 6: Cek contoh non-Jepang**
  Run (JS): `/[぀-ヿ一-鿿]/.test(document.getElementById('social').textContent)`
  Expected: `false`.

  Screenshot post harus memperlihatkan ruko dan motor, bukan konbini atau stasiun Jepang.

- [ ] **Step 7: Commit**
  ```bash
  git add skills/pikmi/catalog.json skills/pikmi/styles/konbini-sky
  git commit -m "feat(pikmi): add slides, social and app recipes to konbini-sky"
  ```

### Task 3: Tema malam

**Files:**
- Modify: `skills/pikmi/catalog.json`, dan keempat file di `skills/pikmi/styles/konbini-sky/`

**Interfaces:**
- Consumes: role dan simbol dari Task 1 dan 2.
- Produces: blok `[data-theme="dark"]`; simbol `scene-konbini-night`, `scene-station-night`, `scene-ruko-night`; tombol `id="theme-switch"` (`role="switch"`, `aria-checked`) yang mengganti `data-theme` di `<html>`.

- [ ] **Step 1: Ubah katalog, pastikan check gagal**
  `themes` menjadi `["light", "dark"]`. `summary` ditambah ", with a lit-up night theme" sebelum titik, sehingga sama dengan K8.
  Run: `python3 scripts/check.py`
  Expected: exit 1, ada `konbini-sky: theme 'dark' missing in tokens.css` dan `konbini-sky: contrast table needs a 'Focus ring' row for theme 'dark'`.

- [ ] **Step 2: Tambah tema dark di `tokens.css` dan `tokens.json`**
  Nilai diambil dari kolom dark tabel token. Blok CSS hanya berisi role yang nilainya berbeda dari light.

- [ ] **Step 3: Perbarui STYLE.md**
  - **Identity:** "Two themes: daylight by default, a lit-up night for evening use."
  - **Visual vocabulary:** pemandangan malam (jendela terang, bintang 1px, lampu, cahaya tumpah ke tanah), halaman tinta malam, dan `--ink` yang diterangkan.
  - **Reasons:** satu baris untuk tema, yaitu konbini yang menyala di malam hari.
  - **Contrast rules:** tambahkan baris dark berikut.

  | Text | On | Ratio | Rule (awal kalimat) |
  | --- | --- | --- | --- |
  | `--text` | `--page` | 14.23 | Body text at night |
  | `--text-muted` | `--page` | 8.03 | Secondary text |
  | `--ink` | `--page` | 7.61 | Captions, numbers, the big word |
  | `--ink` | `--card` | 6.68 | Ink on night cards |
  | `--ink` | `--panel` | 7.16 | Ink on the tab bar |
  | `--on-accent` | `--accent` | 5.93 | Button text |
  | `--link` | `--page` | 7.61 | Links |
  | `--danger` | `--page` | 8.25 | Error text |
  | `--on-sky` | `--sky-top` | 17.73 | White on the night sky |
  | `--on-sky` | `--horizon` | 8.51 | White near the horizon |
  | `--orange` | `--page` | 7.01 | Orange highlight at night |
  | `--accent` | `--page` | 3.07 | Button fill against the night page (non-text) |
  | `--ink` | `--page` | 7.61 | Focus ring on the night page |
  | `--focus-on-sky` | `--sky-top` | 17.73 | Focus ring on the night sky |
  | `--ink` | `--panel` | 7.16 | Field border at night |

  Satu item Checklist: "Both themes are complete; night scenes replace day scenes."

- [ ] **Step 4: Tambah malam di `preview.html`**
  - Tombol `#theme-switch` di nav dengan label "Night", mengikuti pola tombol tema di `skills/pikmi/styles/lapis-lattice/preview.html`.
  - Simbol `scene-konbini-night` dan `scene-station-night`, disalin dari `konbini-n` dan `train-n` di `mockups/night.html`.
  - Simbol baru `scene-ruko-night`: ruko yang sama dengan jendela terang, minimarket yang menyala, bintang, dan cahaya tumpah ke tanah.
  - Setiap adegan ditulis dua kali: `.scene-day` dan `.scene-night`. CSS: `.scene-night { display: none }`, `[data-theme="dark"] .scene-day { display: none }`, `[data-theme="dark"] .scene-night { display: block }`.

- [ ] **Step 5: Jalankan check, pastikan lulus**
  Run: `python3 scripts/check.py`
  Expected: `OK: 12 styles checked`.

- [ ] **Step 6: Cek visual malam**
  Klik `#theme-switch`, lalu jalankan skrip cek preview di 1280px dan 375px.
  Expected: `[]`.

  Run (JS): `[document.documentElement.dataset.theme, document.getElementById('theme-switch').getAttribute('aria-checked'), [...document.querySelectorAll('.scene-day')].every(s => !s.getClientRects().length)]`
  Expected: `["dark", "true", true]`.

  Klik lagi. Hasil JS yang sama sekarang harus `[null, "false", false]` (atribut tema terhapus).

  Ambil screenshot hero dan `#app` di tema malam, lalu bandingkan dengan kartu "A · Malam penuh" di `mockups/night.html`.

- [ ] **Step 7: Commit**
  ```bash
  git add skills/pikmi/catalog.json skills/pikmi/styles/konbini-sky
  git commit -m "feat(pikmi): add night theme to konbini-sky"
  ```

### Task 4: README dan eval router

**Files:**
- Modify: `README.md` (tabel Styles), `evals/prompts.md`

**Interfaces:**
- Consumes: entri katalog final dari Task 3.

- [ ] **Step 1: Tambah baris README**
  Baris baru di akhir tabel Styles:
  `| [Konbini Sky](skills/pikmi/styles/konbini-sky/preview.html) | <summary katalog> | light, dark |`

- [ ] **Step 2: Tambah baris eval**
  Tambahkan baris berikut di tabel `evals/prompts.md`. Kolom Result dikosongkan sampai Step 3.

  | ID | Prompt | Project context | Expected |
  | --- | --- | --- | --- |
  | E34 | bikin landing page panduan wisata jepang yang cerah, kayak poster kota | new | offers include `konbini-sky` |
  | E35 | app jadwal kereta dengan gambar pixel jalanan | new app | offers include `konbini-sky` |
  | E36 | bikin landing page minimarket kayak lawson | new | applies `konbini-sky` directly (brand term) |
  | E37 | slide perjalanan kereta komuter jakarta, cerah dan rame | new | offers include `konbini-sky` |
  | E38 | pakai konbini sky tapi mode gelap | new | applies `konbini-sky` with its dark theme |

- [ ] **Step 3: Jalankan eval**
  Pakai cara yang tertulis di kepala `evals/prompts.md`: agent baru yang hanya membaca `skills/pikmi/SKILL.md` dan `skills/pikmi/catalog.json`, dengan Claude Sonnet sebagai router. Jalankan E34 sampai E38, ditambah E07, E16, dan E29 yang bisa berubah karena style baru.
  Expected: semua PASS. E07, E16, dan E29 tetap memuat style yang diharapkan di barisnya. Konbini Sky boleh ikut ditawarkan tapi tidak boleh menggeser style itu.

  Isi kolom Result dengan format yang sudah ada (`PASS · asked …`). Kalau ada yang FAIL, perbaiki kata kunci atau summary di `catalog.json`, lalu jalankan ulang baris itu.

- [ ] **Step 4: Catat run**
  Paragraf "Last run" yang sekarang dipindah ke atas "Earlier runs". Tulis paragraf "Last run" baru bertanggal hari itu: style apa yang ditambahkan, baris mana yang dijalankan, router yang dipakai, dan hasilnya.

- [ ] **Step 5: Cek pemilih style di situs**
  `preview_start` dengan `name: "pikmi-site"`, lalu `navigate` ke `http://localhost:8766/site/index.html`.
  Expected: Konbini Sky ada di daftar style. Memilihnya memuat preview-nya di panel preview tanpa error di `read_console_messages`.

- [ ] **Step 6: Jalankan check, lalu commit**
  Run: `python3 scripts/check.py`
  Expected: `OK: 12 styles checked`.
  ```bash
  git add README.md evals/prompts.md skills/pikmi/catalog.json
  git commit -m "docs: list konbini-sky in the README and router evals"
  ```
