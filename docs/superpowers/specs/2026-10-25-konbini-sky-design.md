# Konbini Sky: style baru untuk pikmi

Tanggal: 2026-10-25. Status: disetujui user (2026-10-25). Rencana implementasi:
`docs/superpowers/plans/2026-10-25-konbini-sky.md`.

## 1. Maksud dan alasan

User ingin pikmi punya style dengan tampilan keseluruhan seperti empat poster kota Jepang yang ia
tunjukkan di chat (gambar tidak ada di repo):

- **Hokkaido:** langit biru muda, kata "HOKKAIDO" putih raksasa, konbini pixel art bersalju di garis
  cakrawala, bagian bawah putih dengan tiga caption biru sejajar, katakana コンビニ besar biru, satu
  paragraf kecil di kanan bawah, dan nomor halaman.
- **Tokyo:** susunan yang sama, tapi pemandangannya foto konbini asli, dengan kanji 東京 vertikal di samping
  judul.
- **Brand Name:** versi template dari poster Hokkaido.
- **Kamakura:** judul condensed, trem pixel di stasiun tepi laut, caption memakai huruf mono, dan kanji
  鎌倉 besar biru.

User tidak mau meniru konsep posternya. Yang diinginkan adalah "overall looks"-nya: warna, tata letak,
dan lain-lain, yang bisa dipakai untuk UI, slide, post sosial, dan app.

Di pikmi belum ada style seperti ini. Japanese Minimal tipis, pastel, dan sunyi. Indigo Woodblock adalah
cetak kayu Edo. Konbini Sky mengisi celah di antaranya: huruf tebal ala poster Swiss, langit siang yang
cerah, dan satu pemandangan jalanan sehari-hari.

## 2. Tujuan, bukan tujuan, anti-tujuan

**Tujuan**
- Style `konbini-sky` yang lengkap di pikmi: `STYLE.md`, `tokens.css`, `tokens.json`, `preview.html`, entri
  `catalog.json`, satu baris di tabel README, dan baris eval baru. `scripts/check.py` lolos.
- Bisa dipakai di empat medium: ui, slides, social, app.
- Dua tema: terang (siang) sebagai tema utama, gelap (malam) sebagai tema kedua.

**Bukan tujuan**
- Bukan template poster, dan tidak menyalin komposisi keempat referensi satu per satu.
- Tidak memakai AI pembuat gambar atau foto. Pemandangan digambar agen sebagai SVG.
- Tidak ada UI pixel: huruf pixel, sudut tombol bertangga, atau langit bergradasi bertingkat. Arah ini
  ditolak user (lihat bagian 3).

**Anti-tujuan** (gagal walaupun secara teknis jalan)
- Hasilnya terasa seperti game retro karena pixel merembes ke huruf atau komponen.
- Nama, logo, atau produk konbini sungguhan muncul di hasil (aturan pikmi).
- Tanpa pemandangan, hasilnya jatuh menjadi "SaaS biru" generik. Pembagian langit dan kertas, kata raksasa
  putih, tiga caption, dan satu kata besar di kertas (bagian 4, Tipografi) harus tetap ada walaupun
  pemandangannya dihilangkan.
- Pemandangan pixel terlihat seperti clip art atau berisik. Harus berupa satu jalan yang tenang dengan
  satu bangunan utama.

## 3. Yang diputuskan user

Semua poin ini keputusan user di brainstorming, disimpulkan dari mockup yang ia lihat.

1. **Arah A dari tiga arah:** pixel art hanya untuk ilustrasi pemandangan. Huruf, komponen, dan tata letak
   tetap bersih seperti poster Swiss. Arah B (tanpa pixel sama sekali) dan C (pixel ikut masuk ke UI)
   ditolak.
2. **Mockup landing page, slide, dan app arah A disetujui** apa adanya ("semuanya sangat bagus"), termasuk:
   paragraf panjang memakai navy, jingga sangat dihemat, sudut siku tanpa bayangan, satu kanji besar per
   halaman, dan nomor kecil ala nomor halaman. Rinciannya di bagian 4.
3. **Langit siang:** bagian atas `#5CB9E8`, tepat 2.20 : 1 terhadap putih. User minta "sedikit saja lebih
   dalam" dari `#62BDEA` (2.10), lalu menyebut angka 2.20 : 1. Usulan `#3A9BDC` (3.04) ditolak karena
   terlalu dalam.
4. **Teks di atas langit tetap putih**, termasuk teks kecil. Usulan teks kecil navy di langit ditolak. Ini
   pengecualian yang disengaja dari aturan pikmi "kontras WCAG AA untuk semua teks" (spec pikmi bagian 11,
   antislop R-25). Aturan pengamannya ada di bagian 5.
5. **Pemandangan pixel digambar agen sendiri** sebagai SVG kotak-kotak, bukan dengan AI pembuat gambar.
   User menerima bahwa pemandangannya lebih sederhana daripada referensi Hokkaido.
6. **Versi malam = "malam penuh"** sebagai tema gelap: halaman ikut gelap, bukan hanya langitnya. Varian
   "langit malam, kertas putih" ditolak.
7. **Nama:** Konbini Sky, id `konbini-sky`.
8. **Gradasi langit tetap seperti di mockup:** `#5CB9E8` hanya ditahan sampai sekitar 28% tinggi langit,
   lalu memudar. Teks putih boleh duduk di bagian yang sudah mulai memudar. Usulan menahan biru rata sampai
   di bawah teks terakhir ditolak. Akibatnya, kontras teks putih yang lebih bawah memang di bawah 2.20 : 1
   (di mockup sekitar 1.75 sampai 1.97 : 1); lihat bagian 5.
9. **Bukan hanya untuk konten Jepang.** Style ini boleh dipakai untuk konten apa pun. Untuk konten yang
   tidak berhubungan dengan Jepang, kata Jepang besar diganti satu kata besar dalam bahasa kontennya, dan
   pemandangannya menjadi jalanan lokal (misalnya minimarket di Bandung). Pembagian langit dan kertas, kata
   raksasa putih, dan tiga caption tetap ada.

## 4. Tampilan yang disetujui

Mockup yang disetujui disalin ke `docs/superpowers/specs/2026-10-25-konbini-sky-mockups/`:
- `day.html`: landing page, dua slide (judul dan data), dan satu layar app, semuanya di tema siang.
- `night.html`: layar app dan slide judul di tema malam. Kartu "A · Malam penuh" yang dipilih; kartu B
  ditolak.

Kedua file adalah acuan nilai, proporsi, dan gambar pixel, bukan isi. Teksnya fiktif ("Ekimae", panduan
jalan kaki di sekitar stasiun). Kedua file juga memakai Inter dan Inter Tight; lihat catatan font di
bawah.

### Warna, tema siang

| Peran | Nilai | Dipakai untuk |
| --- | --- | --- |
| langit atas | `#5CB9E8` | warna langit di belakang semua teks putih |
| langit tengah | `#96D3F0` | gradasi di belakang pemandangan |
| cakrawala | `#E3F2FA` | ujung bawah gradasi langit |
| kertas (halaman) | `#F7F7F4` | zona bawah, latar konten |
| kartu / tab bar | `#FFFFFF` | permukaan di atas kertas |
| kobalt | `#1D5BD8` | caption, angka, kanji, garis, tombol, judul kecil di kertas |
| navy | `#1E2B4A` | paragraf panjang dan teks isi di kertas |
| jingga | `#EE6A2B` | di pemandangan, ditambah paling banyak satu sorotan per halaman |
| garis tipis | kobalt 28% (`rgba(29,91,216,.28)`) | pemisah baris |
| teks di langit | `#FFFFFF` | semua teks di atas langit |

Gradasi langit: `#5CB9E8` ditahan dari 0 sampai sekitar 28% tinggi langit, lalu `#96D3F0` di 68% dan
`#E3F2FA` di 100%. Ini berlaku juga untuk pita langit di slide data. Teks putih boleh melewati batas 28%
(keputusan user, bagian 3 poin 8). Selain langit, tidak ada gradasi di bagian lain.

### Warna, tema malam

| Peran | Nilai | Dipakai untuk |
| --- | --- | --- |
| langit atas | `#0B1733` | 0 sampai 28% |
| langit tengah | `#1B3263` | 68% |
| cakrawala | `#2F4C80` | 100% |
| halaman | `#0E1526` | zona bawah |
| panel / tab bar | `#121B31` | permukaan di atas halaman |
| kobalt terang | `#7EA6FF` | menggantikan kobalt untuk caption, angka, kanji, garis |
| teks isi | `#DCE4F2` | menggantikan navy |
| jingga | `#FF7A35` | pemandangan dan satu sorotan |
| garis tipis | `rgba(126,166,255,.25)` | pemisah baris |
| tombol | isian `#1D5BD8`, teks putih | sama dengan siang |

Pemandangan malam menyala: jendela terang, garis jingga lebih cerah, lampu peron, bintang 1px, dan cahaya
tipis yang tumpah ke tanah di depan bangunan. Benda di kejauhan berwarna navy gelap dengan beberapa jendela
kuning `#F2C96B`.

### Tipografi

- **Kata raksasa:** neo-grotesk 900, tracking sekitar -0.05em, line-height sekitar 0.8, putih di langit.
  Satu kata per halaman, ukurannya hampir memenuhi lebar (di mockup 18 sampai 22% dari lebar wadah).
- **UI dan caption:** keluarga yang sama, berat 700. Teks isi 500.
- **Kata besar di kertas:** satu kata besar per halaman, kobalt di atas kertas, atau putih dan vertikal di
  samping judul di atas langit. Untuk konten Jepang, kata ini berupa kanji atau kana dengan Noto Sans JP 900.
  Untuk konten lain, kata ini ditulis dalam bahasa kontennya dengan font display 900 (lihat K2).
- **Catatan font:** mockup memakai Inter Tight dan Inter. Spec pikmi (bagian 11, R-06) menggolongkan Inter
  sebagai font bawaan AI yang butuh alasan tertulis. Lihat bagian 7, keputusan K1.

### Tata letak

- Dua zona, langit di atas dan kertas di bawah, dipisah garis cakrawala.
- Pemandangan duduk tepat di garis cakrawala. Bagian tanah di bawah gambar memakai warna halaman, supaya
  bangunannya terlihat berdiri di atas kertas.
- Tepat di bawah cakrawala selalu ada tiga caption pendek berwarna kobalt, disebar kiri, tengah, kanan.
- Setiap halaman atau layar punya satu kata besar di kertas (kanji atau kana untuk konten Jepang).
- Blok bernomor: angka besar 900 dengan garis kobalt 2px di atasnya. Baris daftar dipisah garis tipis.
- Ada nomor kecil ala nomor halaman di pojok kanan bawah.
- Grid tegas, banyak ruang kosong.

Proporsi per medium, diambil dari mockup:
- **Landing:** nav putih di langit (wordmark di kiri; tautan dan tombol garis putih di kanan), kata raksasa,
  baris subjudul dan lede, lalu pemandangan lebar (dua adegan berdampingan). Di kertas: tiga caption, tiga
  fitur bernomor, baris kanji besar dengan ajakan dan dua tombol, lalu footer dengan nomor.
- **Slide judul:** langit 66% dan kertas 34%. Judul di kiri atas, pemandangan sekitar 62% lebar di kanan,
  tepat di cakrawala. Tiga caption di kertas, kanji di kiri bawah, nomor di kanan bawah.
- **Slide data:** pita langit 24% di atas berisi judul putih. Satu angka besar kobalt, grafik batang kobalt
  dengan satu batang jingga untuk nilai yang disorot, kanji vertikal di kanan, dan nomor halaman.
- **App:** header langit berisi status bar, sapaan, judul tempat dengan kanji vertikal, satu baris info,
  dan pemandangan. Sisanya kertas: tiga caption, judul seksi, daftar bernomor, tombol penuh, dan tab bar
  putih.

### Bentuk dan kedalaman

- Sudut siku di mana-mana (radius 0), tanpa bayangan.
- Tombol berupa blok kobalt solid dengan teks putih, atau garis kobalt 1.5px. Di atas langit, tombolnya
  garis putih 1.5px.

### Aturan pemandangan pixel

- SVG dengan `shape-rendering: crispEdges` di atas grid bilangan bulat. viewBox kecil (mockup memakai
  120×48 untuk konbini dan 120×40 untuk stasiun), lalu diskalakan ke lebar wadah.
- Satu bangunan utama (konbini, peron dengan kereta, dan sejenisnya) duduk di cakrawala. Benda di kejauhan
  memudar ke biru langit. Kabel listrik berupa garis tipis.
- Pemandangan mengikuti tempat kontennya: jalanan Jepang untuk konten Jepang, jalanan lokal untuk konten
  lain (misalnya minimarket, warung, atau stasiun kereta komuter). Bentuk dan aturannya sama.
- Generik: tanpa nama atau logo brand sungguhan. Papan nama memakai huruf pixel abstrak, atau nama produk
  yang sedang dibuat.
- Satu adegan per halaman atau layar. Landing boleh menjajarkan dua adegan menjadi satu jalan.
- Mockup berisi empat adegan yang bisa dipakai ulang: konbini dan stasiun, masing-masing versi siang dan
  malam.

## 5. Kontras

Angka dihitung dengan rumus WCAG yang dipakai `check.py`.

| Teks | Di atas | Tema | Rasio | Catatan |
| --- | --- | --- | --- | --- |
| putih | `#5CB9E8` | siang | 2.20 | zona langit paling atas; keputusan user (bagian 3, poin 3 dan 4) |
| putih | `#96D3F0` | siang | 1.63 | titik 68% gradasi; teks putih yang lebih bawah berada di antara 2.20 dan angka ini (bagian 3, poin 8) |
| kobalt | kertas `#F7F7F4` | siang | 5.53 | |
| kobalt | putih | siang | 5.93 | |
| navy | kertas | siang | 13.05 | |
| putih | kobalt | siang dan malam | 5.93 | teks tombol |
| jingga `#EE6A2B` | kertas | siang | 2.91 | jingga tidak pernah dipakai untuk teks kecil |
| navy | `#5CB9E8` | siang | 6.37 | untuk cincin fokus di atas langit, bukan untuk teks |
| putih | `#0B1733` | malam | 17.73 | |
| `#7EA6FF` | `#0E1526` | malam | 7.61 | |
| `#DCE4F2` | `#0E1526` | malam | 14.23 | |
| `#FF7A35` | `#0E1526` | malam | 7.01 | |
| `#1D5BD8` (isian tombol) | `#0E1526` | malam | 3.07 | kontras non-teks tombol |

Tabel kontras di STYLE.md harus jujur: tulis kedua baris putih di atas, beserta catatan bahwa teks putih yang
melewati batas 28% kontrasnya lebih rendah dari 2.20 : 1 atas keputusan user.

Aturan pengaman untuk teks putih di langit siang. Ini keputusan saya, lihat K3:
- Teks putih yang paling kecil (nav, caption, info baris) sebisa mungkin ditaruh di bagian atas langit.
  Kata raksasa dan subjudul tebal boleh lebih ke bawah.
- Teks putih kecil di langit minimal 14px dan berat 700.
- Info penting tidak boleh hanya ada sebagai teks putih di langit: harga, jam, pesan error, label form, dan
  instruksi. Taruh di kertas.
- Cincin fokus di atas langit memakai navy, karena warnanya bukan teks dan `check.py` mewajibkan baris
  "Focus ring" minimal 3.0 : 1.

## 6. Yang perlu diubah di repo

- `skills/pikmi/styles/konbini-sky/STYLE.md`, `tokens.css`, `tokens.json`, `preview.html`, mengikuti format
  di spec pikmi bagian 7 dan aturan antislop di bagian 11, kecuali pengecualian kontras di bagian 3.
- `skills/pikmi/catalog.json`: entri baru, `media` keempatnya, `themes` `["light", "dark"]`.
- `README.md`: satu baris di tabel Styles.
- `evals/prompts.md`: baris baru untuk Konbini Sky, ditambah pengecekan ulang baris yang mungkin berubah
  karena style ini (lihat K7).
- `site/` membaca `catalog.json` sendiri, jadi tidak perlu diubah. Cukup dicek bahwa preview baru tampil di
  pemilih style.

## 7. Keputusan yang saya ambil (perlu dicek user)

- **K1. Font.** Ganti Inter dan Inter Tight dengan neo-grotesk yang bukan bawaan AI dan punya berat 900,
  lalu cocokkan hasilnya dengan mockup (kandidat untuk dicoba builder: Schibsted Grotesk, Hanken Grotesk,
  Archivo). Kalau tidak ada yang bisa mencapai rasa tebal dan rapat Inter Tight 900, pertahankan Inter Tight
  dan tulis alasannya di Reasons.
- **K2. Kata besar sebagai label.** Setiap halaman punya satu kata besar yang berhubungan dengan isinya,
  dan artinya harus benar, bukan huruf acak sebagai hiasan. Untuk konten Jepang, kata ini berupa kanji atau
  kana (駅前 "depan stasiun", 報告 "laporan", 来客 "pengunjung"). Untuk konten lain, kata ini ditulis
  dalam bahasa kontennya, satu atau dua kata pendek, dengan font display 900 berwarna kobalt dan
  ditumpuk per kata seperti kanji di mockup (misalnya "KOPI" di atas "PAGI"). Konten non-Jepang tidak
  memakai huruf Jepang sebagai hiasan.
- **K3. Aturan pengaman kontras** di bagian 5. Usulan saya agar biru ditahan rata di belakang semua teks
  ditolak user, jadi aturan yang tersisa hanya soal ukuran, berat, posisi teks kecil, dan info penting.
- **K4. Dial:** `ENERGY 2 / RHYTHM 2 / MOTION 1`. Gerak pelan: fade dan pergeseran kecil, atau tanpa
  gerak, dengan jalur `prefers-reduced-motion`.
- **K5. Cocok dan tidak cocok.** Cocok untuk panduan kota dan wisata, kuliner dan toko lokal, transportasi
  dan peta, majalah, dan halaman acara. Kurang cocok untuk dashboard padat, produk mewah, enterprise atau
  keuangan, dan konten yang butuh nada serius atau duka.
- **K6. Resep social.** Belum ada mockup-nya. 1080×1350: langit sekitar 60% dengan kata raksasa, adegan di
  cakrawala, lalu di kertas tiga caption, kanji besar, satu paragraf pendek di kanan bawah, dan nomor. Ini
  medium yang paling dekat dengan referensi, jadi builder harus menjaga agar komposisinya tidak menyalin
  salah satu poster.
- **K9. Contoh di preview.html.** Selain contoh Jepang, preview memuat minimal satu contoh konten lokal
  non-Jepang (kata besar dalam bahasa Indonesia dan jalanan lokal), supaya agen melihat bahwa style ini tidak
  terbatas pada Jepang.
- **K7. Kata kunci katalog.**
  - `en`: konbini, convenience store, japan, japan travel, city poster, travel poster, tokyo, sky blue,
    swiss poster, pixel art, train station, street scene, city guide, everyday life.
  - `id`: jepang modern, poster kota, wisata jepang, minimarket, warung, langit biru, cerah, stasiun,
    pemandangan jalan, panduan kota, kayak poster jepang, pixel.
  - `brand_terms`: 7-eleven, seven-eleven, lawson, familymart. Artinya "kayak Lawson" atau "ala 7-Eleven"
    langsung memakai Konbini Sky tanpa tawaran (SKILL.md langkah 2), sama seperti "ala teenage
    engineering" dan Instrument Panel. Nama-nama ini juga dijaga `check.py` agar tidak muncul di file
    style. Tambah satu baris eval yang mengharapkan penerapan langsung ini.
  - Baris eval E07 ("bikin kayak game sci-fi jadul"), E16 ("menu restoran jepang tradisional"), dan baris
    landing page kedai kopi dicek ulang. Konbini Sky boleh muncul sebagai tawaran, tapi tidak boleh
    menggeser style yang memang diharapkan di baris itu.
- **K8. Summary katalog** harus membedakannya dari Japanese Minimal dan Indigo Woodblock. Draf: "Bright
  daytime sky over white paper, giant white grotesk type, cobalt captions and one pixel-art street scene on
  the horizon; bolder and sunnier than Japanese Minimal, with a lit-up night theme."

## 8. Diserahkan ke builder

- Kata-kata di STYLE.md, nama token tambahan di luar peran standar, dan detail resep per medium.
- Pilihan font akhir, dalam batas K1.
- Tata letak `preview.html`, dengan isi minimal sesuai spec pikmi bagian 7: komponen utama, satu potongan
  UI, satu slide 16:9, satu post 4:5, dan satu layar app, untuk kedua tema.
- Adegan pixel tambahan di luar empat adegan di mockup.
- Detail gerak dalam batas K4.
- Kalimat baris eval baru.
