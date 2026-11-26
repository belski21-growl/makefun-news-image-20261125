# Top 10/20 Analysis — news-image-20261125

Ditulis: 25 Nov 2026 ~11:50 WIB (parent watch, sebelum Goldfish review).
Sumber: RULES.txt + competition.yaml kompetisi ini, kriteria judge (z-ai/glm-5.3-flash, 2v2),
pola pemenang TERVERIFIKASI dari ronde 1 news-image-20261124 (gambar pemenang r1/r2/r3/r5
dibaca langsung 25 Nov ~02:45 WIB, tercatat di entries/news-image-20261124/top10-analysis.md
§ UPDATE RONDE 1), dan entry kita sendiri.

## Status leaderboard live

- Kompetisi ini blind rounds — tidak ada rank/score/entry lawan yang terlihat sebelum ronde
  dinilai. Ronde blind #1: 25 Nov 19:00 WIB (per pola ni24: 07:00/19:00/07:00/19:00/final).
  Ronde #1 ni25 BELUM dinilai saat analisis ini ditulis.
- Konsekuensi: analisis ini TIDAK bisa mengutip entry lawan spesifik hari ini. Pola top entry
  diambil dari pemenang nyata ni24 ronde 1 (cutoff: rank 1 = 863545, rank 10 = 803073,
  rank 50 = 654221; entry kita ni24 r1: rank 4805/7302, skor 458194 — grid teks polos kalah
  telak dari koran bergambar).
- Setelah ronde #1 (19:00 WIB) analisis ini WAJIB di-update dengan board nyata sebelum
  checkpoint ⅓ (~26 Nov 23:00 WIB).

## Garis hadiah (50 tempat, total $100)

- 1st $20 · 2nd $12 · 3rd $6 · 4th–10th $2 · 11th–50th $1,20.
- Target: TOP 10. Lantai: rank 25. Di luar top 50 = $0.
- Final heat: ronde Swiss + playoff top-52; lolos ke top-52 Swiss adalah garis hidup pertama.

## Pola pemenang (terverifikasi dari gambar pemenang ni24 ronde 1)

1. **Koran bergambar, bukan grid teks polos.** Masthead serif raksasa + tanggal lengkap
   ("TUESDAY 24 NOVEMBER 2026"), strip jumlah cerita/region/field, region bar yang
   jumlahnya rekonsiliasi persis, strip timeline UTC, strip "THE DAY IN NUMBERS".
2. **3 hero besar berilustrasi vector** (headline + dek + sumber + badge status
   CLAIM / CONFIRMED / OFFICIAL / REPORTED) + ~10 panel sekunder berilustrasi kecil +
   daftar "ALSO ON" bernomor + peta dunia + pin bernomor.
3. **Footer DATE CHECK yang jujur:** klaim tanggal eksplisit + daftar cerita yang SENGAJA
   DIKECUALIKAN karena terjadi hari sebelumnya.
4. **Breadth 34–40 cerita**, lintas region (9–10 region) dan lintas beat. Rank 1 ni24
   juga 34 cerita — jumlah bukan pembeda; craft visual + struktur yang membedakan.
5. **Terbaca di ~300px, faithful, tanpa garbled/overlap.** Judge menghukum klaim tanggal
   salah dan angka yang diketahuinya salah.

## Entry kita (dinilai terhadap pola di atas)

- Judul: "THE WORLD IN ONE DAY / WEDNESDAY 25 NOVEMBER 2026". Format koran bergambar:
  masthead + region bar + timeline UTC + "THE DAY IN NUMBERS" + 3 hero + 6 panel
  sekunder + ALSO ON + footer DATE CHECK dengan daftar eksklusi jujur (17 cerita 24 Nov).
  Pola: MENGIKUTI pola pemenang ni24 (bukan grid polos seperti ni24 r1 yang kalah).
- Hero: (1) Shenzhou-24 lepas landas 00:18 UTC, Zeeshan Ali Pakistan pertama di orbit +
  orang asing pertama di Tiangong; (2) Australia & Solomon Islands tanda tangan pakta
  keamanan di Canberra 25 Nov; (3) US Army ledakkan 68 barel lead azide di Iowa 25 Nov.
- Sekunder + ALSO ON: respons China atas pivot Solomons, 160+ ilmuwan iklim vs RUU BAAJA,
  Huawei Watch Air 6,9 mm, Toronto biaya 911 gap $1,1 M, PAL Airlines vote mogok,
  Inggris (konsultasi age of consent, perubahan PIP), Nigeria (NNDC dipecat),
  16.000 telur tak aman Kozhikode, kekeringan Fiji, perikanan Vanuatu, netball Fiji A
  68–36 Samoa, Super Bowl LXI di Imax, gempa Alaska M4.2, Shirudo (OpenAI+Cisco).
- File: entry.png 1024×1024 JPEG, 263.286 byte, sha256
  0639ce21ed82f2df9019d1a5b47dc49ec503a492adb0d90966c35d888e842577. main.py stdlib-only,
  copy + verifikasi size/SHA-256/magic, 2× byte-identik (lihat build-log.md).

## Gap / titik rawan (untuk Goldfish — WAJIB diverifikasi)

| # | Titik rawan | Dampak |
|---|-------------|--------|
| 1 | **Kompilasi dini 04:00 UTC** — Amerika belum bangun; berita siang/malam 25 Nov WIB/AS tidak masuk. Footer menyebut jam kompilasi — jujur, tapi breadth siang hari hilang | Breadth vs pemenang yang mengompilasi lebih malam |
| 2 | **Peta dunia tidak ada sebagai strip terpisah** — peta + pin hanya di dalam ilustrasi hero 2 (Canberra). Pemenang ni24 semua punya strip "WHERE IT HAPPENED" sendiri | Craft/structure kalah satu elemen pola pemenang |
| 3 | **Tanggal tiap cerita** — 17 cerita 24 Nov sengaja dikecualikan (footer jujur), tapi tiap cerita yang DICANTUMKAN harus benar-benar terjadi/dilaporkan pertama kali 25 Nov. Verifikasi independen tiap hero + sekunder rawan-tanggal | Kriteria #1/#4 judge — satu klaim tanggal salah bisa menjatuhkan skor |
| 4 | **Angka spesifik**: "$1,1 M" Toronto (build-log: $1,1 M gap — cek: $1,1 MILIAR atau $1,1 juta? build-log menulis "$1.1B Toronto budget gap" di satu tempat dan "biaya 911 tutup gap $1,1 M" di tempat lain — INKONSISTEN, wajib diperiksa gambar), "68 barel", "16.000 telur", "68–36", "M4.2", "6,9 mm", "160+ ilmuwan" | Angka salah = hukuman judge |
| 5 | **Legibilitas/garbled**: file JPEG 263 KB (bukan PNG vector ~50 KB seperti pemenang ni24). Periksa teks kecil: typo, terpotong, overlap — terutama footer DATE CHECK dan ALSO ON | Keterbacaan di ~300px |
| 6 | **Hero 2**: "tanpa pangkalan militer asing" + "Australia jadi mitra keamanan utama" — verifikasi redaksi vs sumber AP/Reuters | Faithful |

## Estimasi awal (parent, sebelum Goldfish)

- Rank: top 25 plausible, top 50 likely bila fakta bersih. Peluang top 50: ~40–50%.
- Estimasi ini WAJIB dikonfirmasi/dikoreksi Goldfish — bukan angka final. Bila Goldfish
  menemukan blocker tanggal/angka, perbaiki dulu (1 ronde fix) lalu re-review.

## Update v4 — micro-fix (25 Nov ~13:05 WIB, pasca Goldfish-r3)

Goldfish-r3 masih LAYAK LANJUT: B1 terbuka (3 gagal + 1 abu-abu) + M5 baru
(#31 duplikat tema #22). v4 mengganti kelimanya dengan cerita Yonhap yang
semuanya diverifikasi primer sebagai laporan pertama Rabu 25 Nov 2026
(bukan tanggal halaman live-blog): #11 Lee vows domestic-violence law fix,
#26 Korea mortgage rates 14-year high, #27 Seoul weighs AI exam-cheating
tech, #33 FM Cho urges strategic aid at KOICA, #31 Hyundai Mobis wins
$742M parts orders. Region bar berubah jadi APAC 25 · AMERICAS 4 ·
EUROPE 4 · MIDDLE EAST 1 = 34 (Afrika + Culture hilang; APAC-heavy 25/34
adalah harga dari stok cerita bersih yang tersisa — kebersihan tanggal
(blocker) di atas keseimbangan regional). Numbers strip tidak berubah.
Estimasi bila ke-5 pengganti lolos Goldfish r4: rank ~50–150, top-50
~35–45% (proyeksi Goldfish-r3) — menunggu verifikasi Goldfish r4.

## Update v8 — grey-to-clean (25 Nov ~15:05–15:15 WIB, 08:05–08:15 UTC)

Mengganti 2 abu-abu terakhir Goldfish-r6 (#6 Houthis, #14 bigeye
tuna) — keduanya ternyata lebih rapuh dari penilaian r5 (verifikasi
koordinator 25 Nov ~15:10 WIB: pernyataan Houthi juga dilaporkan
Roya News + Jerusalem Post bertanggal 24 Nov, mungkin dikeluarkan
Selasa malam; tanggal rilis paper bigeye tidak terverifikasi, topik
sudah diumumkan FFA sejak 31 Okt, artikel PINA bigeye terkait
23–24 Nov).

ALL CLEAN — stempel primer terverifikasi sebagai laporan pertama
Rabu 25 Nov:
- #6 Houthi threat to Saudi ports → HOUTHIS SAY THEY HIT SAUDI
  REFINERY. Primer: Reuters, URL slug 2026-11-25, crawl 07:32 UTC
  ("said on Wednesday they had attacked Ras Tanura refinery and
  Riyadh's financial district"; koalisi "earlier on Wednesday"
  mencegat 4 drone di Ras Tanura). Cross-check: Maritime Executive,
  terbit 23:32 EST 24 Nov = 04:32 UTC 25 Nov — serangan Ras Tanura
  dini hari Rabu, plume satelit + data api NASA FIRMS. Headline/dek
  hanya menonjolkan REFINERY (bagian Riyadh dari klaim itu serangan
  Selasa). Region tetap MIDDLE EAST; pin Jeddah → RAS TANURA.
  URL: https://www.reuters.com/world/middle-east/yemens-houthis-say-they-attacked-saudi-oil-refinery-riyadh-financial-district-2026-11-25/
- #14 WCPFC weighs new bigeye tuna rules → AUSTRALIA APOLOGISES TO
  LGBTQ VETERANS. Primer: Reuters, terbit Wed 25 Nov 2026
  01:16:41 UTC ("issued a formal apology on Wednesday"; pidato
  Menhan Marles di parlemen). Region tetap ASIA-PACIFIC (cerita
  Australia ke-3 — kebersihan di atas keseimbangan; tidak ada
  kandidat APAC non-Australia yang lebih bersih di siklus siang).
  URL: https://www.reuters.com/world/asia-pacific/australia-apologises-lgbtq-veterans-past-discrimination-military-2026-11-25/

Region bar TIDAK berubah: APAC 23 · AMERICAS 2 · EUROPE 6 ·
MIDDLE EAST 1 · AFRICA 2 = 34. Numbers strip tidak berubah (tidak
ada angka dari #6/#14). Footer DATE CHECK kini dibuka item lama
#6/#14; kompilasi ~08:05 UTC. Entry v8: 324.007 byte, sha256
5fd850f8bcd788081b3dfc36466e25ae5ee7ddc1ef5f93ab298d2e0a41ce934a.
Tally klaim (untuk Goldfish r7): 34 bersih + 0 abu-abu + 0 gagal
(v6 terverifikasi Goldfish: 32 + 2 + 0). Estimasi bila keduanya
lolos r7: rank ~50–150, top-50 ~30–40% (sama seperti proyeksi r6;
yang menahan tetap M6 APAC/Korea-heavy + kompilasi pagi).

## Update CHECKPOINT ⅓ — 26 Nov 2026 ~06:12–06:30 WIB (koordinator, leaderboard LIVE dibaca langsung)

### Status checkpoint (dari watch run 06:12 WIB + verifikasi koordinator 06:19–06:30 WIB)

- Entry live v8 "Onward Node", submission 01a211f0-3270-73b1-9544-929d7d205032:
  **rank 3855 dari 8982, prize_rank 3850, judge 962664** (dev provisional 12 game
  8W-4D-0L ternyata noisy — BUKAN ukuran; leaderboard yang jadi ukuran).
- Zona hadiah top 50: cutoff rank 50 = 986989 (calm-pika-71-9092); rank 10 =
  989641 (mals620); rank 100 = 985537. **Gap v8 ke top-50 = 24.325 micro
  (≈2,4 poin win-rate)** — jauh. Lapangan sangat padat: rank 1–100 hanya
  selebar 991556→985537 (6.019 micro).
- Estimasi Goldfish r7 (rank ~40–120, top-50 35–45%) MELESET JAUH — pelajaran:
  estimasi yang memodelkan "lapangan klon" tanpa membandingkan ke board nyata
  tidak bisa dipakai. Board nyata sekarang ADA dan dibaca langsung (file:
  ~/workspace/makefun/leaderboard-ni25-20261126-0619.json).
- Kuota live 06:12 WIB: entries_made 1, day left 5, hard left 39,
  can_submit TRUE. Entries tutup 27 Nov 07:00 WIB (~24 jam lagi).

### Board nyata top 10/20 (judul + skor, dari leaderboard live)

| Rank | Handle | Judge | Judul (pola) |
|---|---|---|---|
| 1 | hwang-steven | 991556 | "50 stories, 10 regions, 21 fields — US tariffs and the world's reply, Asian chip rout, Pakistan's first astronaut, Cairo tanker fire" |
| 2 | wismilak | 991214 | "49 stories, 7 regions, 15 drawn, a UTC timeline — Pakistani astronaut boards Tiangong, Kospi -6.2% on AI doubts, US tariffs on 14 economies (r2)" |
| 3 | zesty-marten-97 | 990918 | "Mindful Palette" |
| 4 | gua | 990843 | "Novel Locus" |
| 5 | yossapr | 990490 | "33 dated stories, 6 regions, UTC timeline, 11 drawn scenes, how-sure labels, map" |
| 6 | tarekujjaman | 990353 | "Marine Lemma" |
| 7 | crisp-coyote-28-8869 | 989825 | "The Day Ledger — 32 stories" |
| 8 | anymore | 989784 | "36 stories from 9 regions, a drawn scene for each of the top 12" |
| 9 | thedzulkarnain | 989717 | "The World in One Day (35 stories)" |
| 10 | mals620 | 989641 | "35 dated stories from 7 regions — coalition strikes Yemen's Hodeidah port, chip rout sinks Kospi 6.2%, Ramaphosa wins Phala Phala" |
| 13 | jagdish | 989351 | "39 dated stories, 9 regions, drawn scenes, map and date check" |
| 17 | kuzan | 988891 | "40 stories (v1)" |
| 25 | putra2230 | 988123 | (cutoff rank 25) |

### Gambar top dibaca langsung (artifact .webp, /tmp/ni25-top/)

- **Rank 1 (hwang-steven):** 50 cerita, 10 region, 21 FIELDS (bar field sendiri:
  War 7 · Disaster 5 · Justice 5 · Security 5 · Diplomacy 3 · Tech 3 · Crime 2 ·
  Economy 2 · Labour 2 · Markets 2 · Rights 2 · Sport 2 · Trade 2 · Business 1 ·
  Climate 1 · Energy 1 · Environment 1 · Humanitarian 1 · Politics 1 · Science 1
  · Space 1). 3 hero BESAR berilustrasi (kapal kontainer tarif EU/China; grafik
  Kospi -6.2% SK Hynix -11.1% Samsung -9.9%; Shenzhou-24/Tiangong). 10 panel
  sekunder SEMUA berilustrasi kecil (Rusia bunuh 5/padam 5 region; 4 drone
  Houthi ditembak jatuh Ras Tanura; UK cap +26% £2.166; Solomons pact; Dhaka
  upah 17.500 taka; Bogor tambang 9 tewas; Gaza; Cape Town Ramaphosa; Jerusalem;
  Giza tanker 30 tewas). Numbers strip 5 angka besar (20% tarif · -6.2% Kospi ·
  +26% UK cap · 30+ Cairo · 9 Java). Peta "WHERE IT HAPPENED" + pin bernomor.
  ALSO ON #14–50 (37 item, 2 kolom). Footer DATE CHECK + legenda
  OFFICIAL/REPORTED/CLAIM. Tiap hero ada "WHY IT MATTERS".
- **Rank 2 (wismilak):** 49 cerita, 7 region, 15 drawn. Strip "THE DAY IN UTC"
  ber-waktu (00:30 CPI Australia 4.9% · 03:56 Shenzhou dock · 05:30 Taiex
  -4.8% · 06:30 Kospi -6.2% · 08:35 Tiangong · 13:30 US GDP · 21:00 Dow).
  3 hero berilustrasi + 12 panel sekunder SEMUA berilustrasi (Hodeidah, Hormuz
  2 tanker, Samara 2 kilang, Solomons, UK cap, Bogor, Dhaka, Gaza, Cape Town,
  Cartagena, Zaporizhzhia, Ed Damazin). Badge C/R/CL per item (CONFIRMED /
  REPORTED / CLAIM). Numbers strip 6 angka. ALSO ON #16–49 (34 item). DATE
  CHECK footer dengan daftar "left out, not 25 November" (Houthi Riyadh Tue 24
  · CAS Senegal Tue 24 · CIA-ODNI breach Tue 24 · Miss Universe Tue 24 ·
  Argentina recession Tue 24 · WHO Ebola evacuation Tue 24 · Nvidia surge Mon 23).
- **Rank 5 (yossapr):** 33 cerita SAJA tapi rank 5 — bukti jumlah bukan segalanya:
  11 drawn scenes (3 hero + 8 sekunder berilustrasi: Solomons, UN femicide
  47.000, Huawei verdict, Houthi drones, Bogor, Dhaka, Samara, WHO Ebola),
  numbers strip 6 angka, legenda "HOW SURE" (OFFICIAL/CONFIRMED/REPORTED/CLAIM),
  peta + IN BRIEF #12–33. Hero: Shenzhou, Kospi crash (grafik), Hormuz tankers.
  Footer DATE CHECK jujur (Nvidia Huang return Tue 24 · COP31 collapse Sun 22 ·
  first Riyadh PIF strike Thu 19 Nov).
- **Kriteria juri (competition.yaml, dibaca koordinator):** urutan bobot (1) satu
  hari + sebut tanggalnya; (2) SELEKSI + BREADTH — cerita paling konsekuensial
  hari itu, lintas region dan field; (3) TERBACA — tiap cerita jelas dari gambar
  + label pendek; (4) FAITHFUL — tanpa hype/spekulasi sebagai fakta; (5) CRAFT —
  komposisi jelas, terbaca ~300px, tanpa garble. Juri TIDAK punya feed berita:
  ia menilai dari gambar + pengetahuannya sendiri.

### Gap v8 vs pemenang (penyebab rank 3855 — BUKAN tanggal, tanggal sudah 34/34 bersih)

1. **KOMPILASI PAGI 08:05 UTC — gap terbesar.** v8 melewatkan SELURUH siang/malam
   25 Nov: tarif AS atas 14 ekonomi (hero #1/#3 di rank 1/2), Kospi TUTUP -6.2%
   (v8 cuma "KOSPI opens lower" #22), kebakaran tanker Kairo 30+ tewas, serangan
   koalisi ke Hodeidah, 2 tanker Hormuz kena ranjau, UK cap +26% (v8 cuma
   "decision due today" #32 — keputusannya sendiri ketinggalan), upah garmen
   Bangladesh +36%, tambang Bogor 9 tewas 17 terjebak, kilang Samara, Ramaphosa
   menang Phala Phala, WHO tarik staf Ebola dari Akwe, vonis Huawei bersalah,
   femicide PBB 47.000, mogok Tube London. Kriteria juri #2 (seleksi cerita
   paling konsekuensial) menghukum ini langsung: hero v8 #3 (68 barel Iowa)
   cuma jadi ALSO ON #42 di rank 2.
2. **BREADTH: 34 vs 49–50 cerita; 5 vs 7–10 region; 0 vs 21 fields.**
   v8: APAC 23/34, Korea ~14 cerita, Latin Amerika 0, Afrika 2, tanpa bar fields.
   Rank 1: 10 region (N. America 6 · Latin America 4 · Europe 12 · Middle East 7
   · N. Africa 2 · Sub-Saharan Africa 5 · South Asia 2 · East & SE Asia 5 ·
   Oceania 4 · Global 3) + 21 fields.
3. **SEKUNDER TANPA ILUSTRASI — gap craft terbesar.** v8: 10 panel sekunder
   teks polos. Rank 1/2/5: SEMUA sekunder berilustrasi kecil (10–12 gambar).
   Kriteria juri #3 ("each story clear from its picture") + #5 (craft).
4. **ALSO ON pendek: 21 item vs 34–37 item (2 kolom) di pemenang.**
5. **Numbers strip 5 angka vs 6 di rank 2/5; tanpa "WHY IT MATTERS" / tanpa
   legenda HOW SURE yang eksplisit (v8 punya badge tapi tanpa legenda).**
6. **Yang SUDAH benar di v8 (dipertahankan):** masthead + tanggal, region bar
   rekonsiliasi persis, timeline UTC, map + pin, footer DATE CHECK jujur,
   34/34 tanggal bersih (Goldfish r7), keterbacaan ~300px, dark fraction 11,57%.

### Rencana v9 (koordinator → builder)

Rebuild penuh sehari-penuh (kompilasi ~23:30 UTC 25 Nov = 26 Nov ~06:30 WIB):
48–50 cerita, 9–10 region, ~18–21 fields; hero BARU (1) tarif AS 14 ekonomi
(2) Kospi -6.2% chip rout + grafik (3) Shenzhou-24/Pakistan (dipertahankan);
Solomons pact turun ke sekunder berilustrasi; Iowa turun ke sekunder/ALSO ON;
9–12 panel sekunder SEMUA berilustrasi; ALSO ON ~35 item 2 kolom; numbers
strip 6 angka siang-hari (20% · -6.2% · +26% · 30+ Cairo · 47.000 · 9/17 Bogor);
bar fields; timeline UTC dengan jam-jam siang; peta + pin; DATE CHECK footer
(jujur, kompilasi ~23:30 UTC). DISIPLIN TANGGAL TETAP: tiap cerita WAJIB
first-reported 25 Nov dari primer — JANGAN salin klaim top entry mentah-mentah
(perangkap: "Houthis threaten Jeddah" di rank 2 #23 = item abu-abu v8 yang
sudah dipensiunkan karena pernyataan 24 Nov malam; "Blanche–Nvidia" 24 Nov;
Guam El Niño 18–24 Nov; Martha Ford diumumkan 24 Nov US). Estimasi awal
koordinator (BUKAN janji, Goldfish yang menetapkan): bila v9 menyamai craft
top-10 (50 cerita + sekunder berilustrasi + full-day), rank ~100–500,
top-50 ~30–40% — Goldfish re-review WAJIB mengoreksi angka ini.
