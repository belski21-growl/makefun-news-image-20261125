# Goldfish Review — news-image-20261125 (REVIEW PENUH)

**Reviewer:** Goldfish (penilai independen, bukan builder)
**Tanggal review:** Rab 25 Nov 2026 ~12:00 WIB
**Entry dinilai:** `entry.png` — 1024×1024 JPEG, 263.286 byte, sha256
`0639ce21ed82f2df9019d1a5b47dc49ec503a492adb0d90966c35d888e842577`
(terverifikasi cocok dengan sha di brief tugas dan build-log.md).
**Metode:** Baca langsung entry.png full + 6 crop-zoom 2× (hero 1 deck, hero 2 map,
hero 3, numbers strip, secondary panels, ALSO ON + DATE CHECK footer) + baca
`top10-analysis.md` SELURUHNYA + `build-log.md`. Verifikasi faktual INDEPENDEN
via pencarian web: **14 kueri**, tiap hero + tiap sekunder + tiap ALSO ON +
spot-check 1 item daftar eksklusi (CIA breach). Tidak ada safety refusal
(tidak ada item UNTESTED-blocked).

## VERDICT: LAYAK LANJUT BELUM LAYAK SUBMIT

Bukan TIDAK LAYAK: kerangka entry benar (koran bergambar, 3 hero kuat, DATE CHECK
jujur sebagai niat) dan 3 hero semuanya LOLOS faktual. Tapi entry ini BELUM BOLEH
submit: klaim universal DATE CHECK-nya SALAH untuk 8 dari 14 cerita, baris deck
hero 1 tidak terbaca, dan peta hero 2 menunjukkan benua yang salah. Perbaikannya
bukan mikro — ini revisi BESAR (ganti 8 item + render ulang deck hero 1 + perbaiki
peta + tambah breadth). Bila ronde fix tidak bisa menemukan pengganti 25 Nov yang
bersih dan terverifikasi, verdict berubah menjadi TIDAK LAYAK.

## BLOCKER (wajib diperbaiki sebelum submit)

### B1 — DATE CHECK SALAH untuk 8 dari 14 cerita
Footer mengklaim: *"Every story above happened or was first reported on Wed 25 Nov
2026."* Klaim universal ini SALAH. 8 item pertama kali dilaporkan 23–24 Nov, bukan
25 Nov. Builder memanen wire agregator Archynetys yang berstempel 25 Nov dini hari
UTC, padahal laporan primernya 23–24 Nov. Ini kegagalan kelas yang sama dengan
Golden Dome di ni24 r3 (yang memblokir r3) — tapi di sini bukan 1 item, melainkan
mayoritas konten non-hero. Rincian di tabel verifikasi bawah (item 4–9, 12, 13).

### B2 — Deck hero 1 baris 2 GARBLED / tidak terbaca
Crop-zoom hero 1: baris 1 *"China launches Shenzhou-24 at 00:18 UTC."* bersih;
baris 3 *"the first foreign astronaut aboard Tiangong."* bersih; tapi **baris 2
— kalimat kunci "Zeeshan Ali is the first Pakistani in orbit and …" — hancur:
huruf bertumpuk/overlap, tidak terbaca sama sekali**. Ini baris fakta terpenting
kedua di seluruh gambar (klaim "pertama" yang jadi headline). Patch PIL builder
("astronout" → "astronaut") tidak menyentuh kerusakan ini; klaim builder bahwa
teks sudah diperbaiki adalah SALAH untuk baris ini. Wajib render ulang deck hero 1.

### B3 — Peta hero 2 menunjukkan benua yang SALAH
Crop-zoom hero 2: peta di belakang dua pria berjabat tangan jelas-jelas
**Amerika Utara** (dengan Amerika Tengah/Karibia + ujung utara Amerika Selatan) +
pin-pin acak di atasnya. Ceritanya Australia + Solomon Islands (Canberra,
Pasifik). Peta yang salah benua untuk cerita Pasifik adalah kesalahan faktual
visual yang langsung terlihat judge. Wajib diganti peta Australia/Pasifik yang
benar — atau hapus peta dari hero 2 dan buat strip "WHERE IT HAPPENED" terpisah
yang benar (pola pemenang ni24).

## MAJOR (sebaiknya diperbaiki di ronde fix yang sama)

### M1 — Breadth hanya 14 cerita vs 34–40 pemenang
Hitung isi gambar: 3 hero + 6 panel sekunder + 5 ALSO ON = **14 cerita**.
Pemenang ni24 ronde 1: 34–40 cerita. Entry ni24 r1 kita yang berisi 32 cerita
(grid polos, tanggal bersih) saja rank 4805/7302. 14 cerita = kalah breadth
telak di 2v2 mana pun. Klaim builder "target ~30–34 cerita" TIDAK TERPENUHI di
gambar. Ronde fix harus memperluas ALSO ON ke ~#14–34 seperti pemenang
(dengan cerita 25 Nov yang terverifikasi, bukan filler lama).

### M2 — Build-log mengklaim cerita yang TIDAK ADA di gambar
Build-log § "Secondary panels + ALSO ON" mendaftar PAL Airlines vote mogok,
16.000 telur Kozhikode, Shirudo (OpenAI+Cisco), dsb. — **tidak satu pun muncul
di gambar**. Build-log tidak cocok dengan artefak. Perbaiki log, atau (lebih
baik) masukkan cerita-cerita itu ke gambar BILA tanggalnya terverifikasi 25 Nov
— catatan: saya TIDAK memverifikasi ketiganya karena tidak ada di gambar;
fixer wajib verifikasi independen sebelum memasukkan.

### M3 — Tidak ada strip peta dunia terpisah; region bar tanpa hitungan
Pemenang ni24 semua punya strip "WHERE IT HAPPENED" (peta + pin bernomor) dan
region bar yang jumlahnya rekonsiliasi persis dengan total cerita. Entry ini:
peta hanya di dalam hero 2 (dan salah benua, B3); region bar
("ASIA-PACIFIC • EUROPE • MIDDLE EAST • AMERICAS • AFRICA • SCIENCE • SPORT")
tanpa angka; strip timeline hanya 3 item dan "CANBERRA MORNING" tanpa jam.
Hero juga tanpa baris sumber (Reuters/AP/dll) dan tanpa badge status
(CLAIM/CONFIRMED/OFFICIAL) seperti pemenang.

### M4 — Numbers strip ikut tercemar item salah tanggal
Kotak "$1.1B TORONTO BUDGET GAP" dan "160+ SCIENTISTS VS BAAJA BILL" merujuk
ke item B1 (Toronto, BAAJA). Bila kedua item diganti, kedua kotak angka ini
wajib ikut diganti — jangan sampai numbers strip merujuk ke cerita yang sudah
tidak ada di gambar.

## Tabel verifikasi per item

| # | Item di gambar | Hasil | Bukti singkat |
|---|---|---|---|
| H1 | Shenzhou-24, 00:18 UTC, Ali Pakistan pertama di orbit + orang asing pertama di Tiangong | ✅ LOLOS (fakta) / ❌ GAGAL (visual, B2) | Wikipedia + Xinhua + Reuters 25 Nov: launch 25 Nov 00:18:52 UTC Jiuquan; Ali 40 thn, payload specialist, "first Pakistani in orbit", "first-ever foreign astronaut to visit Tiangong", 5–10 hari. Fakta 100% benar; TAPI deck baris 2 garbled (lihat B2). |
| H2 | Australia & Solomons tanda tangan pakta keamanan di Canberra; Australia mitra keamanan utama; tanpa pangkalan militer asing | ✅ LOLOS (fakta) / ❌ GAGAL (visual, B3) | pm.gov.au + AP + Reuters 25 Nov: Albanese & Wale tanda tangan di Canberra 25 Nov; "Australia as its primary security partner"; "no foreign military or security base in Solomon Islands". Fakta benar; TAPI peta = Amerika Utara (B3). |
| H3 | US Army ledakkan 68 barel lead azide di Iowa hari ini, setelah ditunda; warga diperingatkan | ✅ LOLOS | USA TODAY/Fox/AP 25 Nov: 68 barel ~9.500–9.700 lbs lead azide, Iowa Army Ammunition Plant Middletown, Rabu 25 Nov ~09:00 CT; dijadwalkan ulang dari 20 Nov, court hold dicabut 23 Nov. "To detonate" benar pada jam kompilasi 04:00 UTC (ledakan 15:00 UTC). Visual bersih. |
| S1 | CHINA RESPONDS: Beijing swipes at Canberra after the Solomons pivot | ❌ GAGAL (tanggal) | Komentar Guo Jiakun disampaikan di briefing **Selasa 24 Nov** (PINA, europesays "24 November 2026", BBC) — merespons laporan Selasa bahwa Solomons tak perpanjang pakta China. Artikel PINA berstempel 25 Nov, tapi peristiwanya 24 Nov. |
| S2 | CLIMATE: 160+ scientists urge US House to reject BAAJA bill | ❌ GAGAL (tanggal) | Surat terbuka disampaikan **Senin malam 23 Nov** ("late Monday"); liputan Guardian/dll 24 Nov; angka 160+ benar (awal 120+, lalu 160+). Wire Archynetys 25 Nov 02:05 UTC = stempel agregator, bukan laporan pertama. |
| S3 | TECH: Huawei Watch Air, 6.9 mm, thinnest smartwatch yet | ❌ GAGAL (tanggal) | Diumumkan **19 Nov** (TechNode/Gizmochina), debut di event **24 Nov** (Techtimes: "launched in China on Nov. 24"). Bukan 25 Nov. Angka 6,9 mm benar, tapi "thinnest smartwatch yet" bercatatan: angka itu kemungkinan tidak termasuk modul sensor (Notebookcheck/Gizmodo). |
| S4 | CANADA: Toronto eyes a 911 fee to close a $1.1B gap | ⚠️ ABU-ABU, condong GAGAL (tanggal) | Angka **$1.1B LOLOS** (CTV + Archynetys: shortfall $1,1 miliar 2027; fee $2/bln per line). TAPI laporan primer CTV News bertanggal **24 Nov**; versi Archynetys 25 Nov 01:49 UTC. "First reported" secara ketat = 24 Nov. Gambar konsisten menulis $1.1B di panel + numbers strip (dugaan "M vs B" di top10-analysis TIDAK TERBUKTI — tidak ada inkonsistensi di gambar). |
| S5 | BRITAIN: Ministers consult on age of consent; PIP changes agreed | ❌ GAGAL (tanggal, dua-duanya) | Konsultasi age of consent: BBC, sinyal pertama **24 Nov 22:52** (radiomason), london24news 24 Nov 22:30. PIP: Timms review dipublikasikan **24 Nov**; pemerintah terima 2 rekomendasi 24 Nov (broadcastprism, finwire: "Timms told MPs on Tuesday"). Kedua paruh panel = berita 24 Nov. |
| S6 | NIGERIA: Northern governors sack NNDC board | ❌ GAGAL (tanggal) | Rapat khusus Kaduna **Selasa 24 Nov**; dipublikasikan 24 Nov 17:53–20:42 UTC (NNU, Punch via nuus.ng). Redaksi "sack" agak menyederhanakan (dissolve + board baru, berlaku setelah resolusi) tapi tanggalnya yang gagal. |
| A1 | Fiji drought emergency may run into 2027 | ✅ LOLOS | PINA Breaking News **25 Nov 2026**: "Fiji's drought emergency could stretch into 2027". (Daruratnya sendiri dideklarasi 18 Nov, tapi angle "may run into 2027" = berita 25 Nov.) |
| A2 | Vanuatu hosts Pacific fisheries talks | ✅ LOLOS | PINA **25 Nov**: FFC145 officials meeting di Port Vila 24–26 Nov, persiapan WCPFC23 (30 Nov–5 Des). |
| A3 | Super Bowl LXI to screen live in Imax | ❌ GAGAL (tanggal) | Diumumkan **23 Nov** (Sports Business Journal 11.23.2026; Consequence 23 Nov; IMAX/Disney/Fandango posting 23 Nov). Dua hari lebih tua dari klaim. |
| A4 | Alaska M4.2 quake | ❌ GAGAL (tanggal) | Gempa **24 Nov 16:37 UTC** (07:37 AKST 24 Nov), 10 km WSW Point MacKenzie, USGS (event aka2026xhgksb). Klaim build-log "USGS, 25 Nov 02:36 UTC" SALAH — itu jam halaman dimuat ulang, bukan jam gempa. |
| A5 | Fiji A thrash Samoa 68–36 in netball | ✅ LOLOS | PINA **25 Nov**: "Fiji A … thrashing Samoa 68-36 in Brisbane" (PacificAus Sports Netball Challenge). Skor benar. |
| N1 | Numbers: 00:18 UTC liftoff / 3 crew / 1st Pakistani / $1.1B Toronto / 68 barrels / 160+ scientists | ⚠️ TERCEMAR (M4) | 4 dari 6 kotak LOLOS (00:18, 3 crew, 1st Pakistani, 68 barrels). 2 kotak merujuk item B1 (Toronto, BAAJA) — wajib diganti bersama itemnya. |
| D1 | DATE CHECK footer: 17 cerita 24 Nov dikecualikan; "Compiled 04:00 UTC" | ✅ LOLOS (spot-check) | "turkey pardon" utuh (patch builder berhasil). Spot-check: CIA/ODNI breach — NYT pertama laporkan **Selasa 24 Nov** ✓ (Nextgov 24 Nov 17:46 ET; Xinhua "Nov. 24"). 16 item eksklusi lain TIDAK diverifikasi satu-per-satu (di luar gambar utama); kejujuran daftar eksklusi tidak menyelamatkan klaim universal yang dilanggar 8 item di atas. |

**Rekap tanggal: 6 dari 14 cerita bersih 25 Nov** (H1, H2, H3, A1, A2, A5);
**8 dari 14 melanggar DATE CHECK** (S1–S6, A3, A4 — Toronto dihitung sebagai
pelanggaran ke-8 dalam hitungan longgar; secara ketat 7 gagal + 1 abu-abu).

## Penilaian visual

- **Masthead + tanggal:** bersih, serif besar, "WEDNESDAY 25 NOVEMBER 2026" benar.
  Region bar ada tapi tanpa hitungan (M3).
- **Hero 1:** ilustrasi roket + Tiangong bagus; headline bersih; **deck baris 2
  garbled total (B2)** — satu-satunya teks rusak di gambar, dan letaknya di hero.
- **Hero 2:** ilustrasi jabat tangan bagus; teks bersih; **peta = Amerika Utara (B3)**.
- **Hero 3:** bersih total (ilustrasi ledakan + teks). Satu-satunya hero tanpa cacat.
- **Numbers strip:** bersih, terbaca, konsisten dengan panel ($1.1B di dua tempat).
- **Secondary panels:** teks bersih, tidak ada typo/overlap/garbled. Ikon (bendera
  China, daun, jam, maple, parlemen, peta Afrika) sesuai.
- **ALSO ON:** satu baris, bersih, terbaca.
- **DATE CHECK footer:** bersih, terbaca penuh di crop-zoom, "turkey pardon" utuh.
- **Keterbacaan ~300px:** judul + hero terbaca; teks panel sekunder dan ALSO ON
  mengecil tapi masih terbaca; footer DATE CHECK di ~300px hampir tidak terbaca
  (wajar untuk footer — pemenang ni24 sama).
- **Format file:** JPEG 263 KB (bukan PNG vector ~50 KB seperti pemenang ni24) —
  ini gambar hasil generate raster; teksnya "ditempel" AI, yang menjelaskan B2.
  Bukan blocker per se, tapi menjelaskan kerapuhan teks.

## Estimasi jujur (chase-top-10)

- **Rank estimasi: ~2.500–6.000 dari ~9.000+** (di luar zona hadiah, jauh).
  Alasan: pembanding terdekat = ni24 r1 kita (32 cerita, tanggal bersih, grid
  polos) yang rank 4805/7302. Entry ini lebih sedikit cerita (14 vs 32), 8
  pelanggaran tanggal (kriteria #3 judge: "nothing you know to be false" —
  pelanggaran tanggal adalah yang paling dihukum), plus 2 cacat visual di hero.
  Di 2v2 vs entry koran bergambar 34+ cerita dengan tanggal bersih, entry ini
  kalah di hampir semua pasangan.
- **Peluang top-50: ~3%. Peluang top-10: <1%.**
- Estimasi ini JAUH di bawah lantai (rank 25) dan target (top 10). **Dalam bentuk
  saat ini entry ini TIDAK GUNA untuk dapat hadiah** — sesuai aturan chase-top-10,
  entry ini wajib satu ronde perbaikan besar dulu, lalu re-review Goldfish,
  sebelum boleh disebut siap-submit.

## Rencana fix yang disarankan (untuk koordinator perbaikan)

1. Ganti 8 item B1 dengan cerita 25 Nov yang terverifikasi PRIMER (bukan wire
   agregator): cari berita yang peristiwanya/laporan pertamanya 25 Nov UTC —
   perhatikan konversi zona waktu (laporan 24 Nov malam AS = 25 Nov dini hari
   UTC, itu SAH 25 Nov; laporan 24 Nov siang/sore AS = tetap 24 Nov).
   Kandidat dari build-log yang belum dipakai: PAL Airlines, telur Kozhikode,
   Shirudo — verifikasi dulu tanggal primernya sebelum dimasukkan.
2. Render ulang deck hero 1 (baris 2) sampai terbaca penuh di crop-zoom; ganti
   peta hero 2 dengan peta Australia/Pasifik, atau pindahkan peta ke strip
   "WHERE IT HAPPENED" terpisah.
3. Perluas ALSO ON ke ~#14–34 (pola pemenang) + tambah hitungan region bar yang
   rekonsiliasi + jam di timeline strip + baris sumber di hero.
4. Sinkronkan numbers strip dengan item baru; perbaiki build-log agar cocok
   dengan gambar; re-review Goldfish penuh setelah fix.

## Catatan kecil (bukan blocker, bukan major)

- "68 BARRELS, ONE BLAST" — headline hero 3 memakai koma setelah "68 BARRELS,"
  dengan gaya koran; bukan kesalahan.
- Panel NIGERIA menulis "Northern governors sack" — penyederhanaan yang masih
  dalam batas wajar (dissolve + board baru), kalah penting dibanding tanggalnya.
- "Thinnest smartwatch yet" (S3) — klaim pemasaran Huawei; bila item ini
  diganti, masalah ini ikut hilang.
- Kompilasi 04:00 UTC jujur dicantumkan di footer — bagus, tapi konsekuensinya
  breadth siang hari 25 Nov hilang (top10-analysis titik #1). Fix round yang
  dikompilasi lebih malam bisa menangkap berita siang 25 Nov.
