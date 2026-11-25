# GOLDFISH REVIEW — RE-REVIEW v2 (round 2)
## news-image-20261125 — "The World in One Day"

- **Reviewer:** Goldfish (penilai independen — bukan builder, bukan fixer)
- **Tanggal review:** 25 November 2026 (~13:00 WIB / ~05:00 UTC)
- **Entry dinilai:** `entry.png` v2 — sha256 `30b59778c802cccfe743db3e40263e668636f418f9e8d037b47537c928759ae2`, 270.327 byte, 1024×1024 JPEG
- **Entry v1 (pembanding):** sha256 `0639ce21ed82f2df9019d1a5b47dc49ec503a492adb0d90966c35d888e842577`, 263.286 byte
- **Kompetisi:** news-image-20261125 — $100, 50 tempat, juara 1 $20; deadline 27 Nov 2026 07:00 WIB; juri z-ai/glm-5.3-flash

## Metode
- Membaca langsung `entry.png` v2: full + 6 crop-zoom 2× (`/tmp/gf2/`: heroes, secondary, numbers_alsoon, map_footer, hero1_deck, hero2_map).
- Membaca penuh `build-log.md` v2 (ditulis ulang dari gambar final, 34 cerita + sumber primer + stempel tanggal + daftar pengganti + eksklusi), `goldfish-review.md` (v1), dan `top10-analysis.md`.
- Verifikasi faktual independen via web search: **37 kueri** — semua 3 hero, semua sekunder #4–13, semua ALSO ON #14–34, angka numbers strip, dan 1 spot-check eksklusi DATE CHECK (Chen Jining).
- Standar tanggal yang dipakai: tanggal **laporan pertama dari sumber primer** (outlet yang pertama kali memberitakan), bukan stempel agregator/wire re-post. Ini standar yang sama dengan review v1 — dan standar yang akan dipakai juri AI saat memeriksa tanggal.
- File entry TIDAK diubah, TIDAK disubmit, TIDAK dibuat repo.

## Status blocker & major v1
| Item v1 | Status v2 | Bukti |
|---|---|---|
| **B1 — DATE CHECK salah untuk 8 dari 14 cerita** (klaim "semua 25 Nov" palsu; builder panen stempel agregator 25 Nov untuk berita 23–24 Nov) | **MASIH TERBUKA** | Kini **9 dari 34 cerita GAGAL tanggal secara terkonfirmasi** + 2 abu-abu condong gagal = 26–32% koran. Proporsi turun dari v1 (57%), tapi jumlah absolut naik (8 → 9) dan **modus kegagalan persis sama**: stempel re-post agregator/wire dipakai sebagai tanggal laporan pertama. Daftar gagal: #6 Gaza (18 Nov), #8 Jepang (24 Nov), #11 Tidal (24 Nov), #16 op-ed ADB (24 Nov), #23 stablecoin (24 Nov), #25 Sejong (24 Nov), #26 ujian-AI (24 Nov), #27 WHO-Kuba (24 Nov), #31 Rosenberg (meninggal 28 Okt, obituari 24 Nov). Abu-abu condong gagal: #33 film lab (Variety cap 24 Nov 19:00 PT), #34 Golden Globes (Variety "Updated: Nov. 24, 2026"). |
| **B2 — Deck hero 1 baris 2 GARBLED total** | **TERTUTUP** | Crop-zoom 2×: "Shenzhou-24 lifts off at 00:18 UTC. Zeeshan Ali is the first Pakistani in orbit — and the first foreigner aboard China's Tiangong station." — bersih, terbaca penuh, tanpa overlap. |
| **B3 — Peta hero 2 = Amerika Utara** (cerita Australia + Solomon) | **TERTUTUP** | Crop-zoom 2×: peta kini Pasifik — Australia, Papua N.G., Solomon Is., pin Honiara, Selandia Baru; pin Canberra di Australia tenggara. Benua benar. |
| **M1 — Breadth hanya 14 cerita** (vs 34–40 pemenang) | **TERTUTUP** | Dihitung dari gambar: 3 hero + 10 sekunder + 21 ALSO ON = **34 cerita**. Klaim masthead "34 STORIES" benar jumlahnya. |
| **M2 — Build-log klaim cerita yang TIDAK ada di gambar** (PAL Airlines, telur Kozhikode, Shirudo) | **TERTUTUP** | Build-log v2 ditulis ulang dari gambar final; ketiga klaim itu dihapus dan masuk daftar eksklusi dengan alasan tanggal yang benar. Log kini cocok dengan artefak. |
| **M3 — Tanpa strip peta dunia; region bar tanpa hitungan; timeline cuma 3 item; hero tanpa source line/status badge** | **TERTUTUP** (untuk elemen yang terverifikasi) | Strip "WHERE IT HAPPENED" terpisah ADA dengan pin bernomor + legenda (1 Jiuquan, 2 Canberra+Honiara, 3 Iowa, 4–5 Sydney, 6 Gaza, 7 Detroit, 8 Tokyo, 9–10 Seoul, 11 New York, 12 London, 13 Los Angeles). Region bar ADA hitungan dan rekonsiliasi ke 34 (lihat bawah). Timeline ADA 5 waktu (00:18/00:30/02:02/02:59/14:00 UTC). Pin Seoul sudah di +37,5°LU (dulu −37,5, belahan selatan — diperbaiki). |
| **M4 — Numbers strip terkontaminasi** ($1,1B Toronto + 160+ BAAJA merujuk item B1) | **MASIH TERBUKA (parsial)** | $1,1B dan 160+ sudah dibuang. Tapi **27M masih terkontaminasi**: angka itu nyata (27 jt trek AI di Tidal) tapi merujuk #11 Tidal yang tanggalnya GAGAL (24 Nov). 4 dari 5 angka bersih (4,9% · 68 · 101 · 2.212); 27M wajib diganti bersama #11. |

## VERDICT: LAYAK LANJUT BELUM LAYAK SUBMIT

Frame kini benar dan bisa diperbaiki — bukan TIDAK LAYAK. Kerajinan naik kelas besar dari v1: 34 cerita, peta benar, deck bersih, strip peta dunia, timeline berwaktu, region bar berhitungan. Tapi **B1 masih terbuka**: klaim footer "EVERY STORY ABOVE WAS FIRST REPORTED WEDNESDAY 25 NOVEMBER 2026" adalah **palsu untuk minimal 9 dari 34 cerita**, dan fixer mengulangi persis kesalahan metode v1 (memakai stempel re-post agregator/wire sebagai tanggal laporan pertama). Satu cerita 24 Nov saja sudah blocker menurut brief — ini sembilan.

**Blocker tersisa:**
- **B1 (masih terbuka)** — 9 cerita GAGAL tanggal terkonfirmasi + 2 abu-abu condong gagal (daftar perbaikan di bawah). Klaim DATE CHECK "semua 25 Nov" palsu.
**Major tersisa:**
- **M4 (parsial, masih terbuka)** — angka 27M di numbers strip merujuk item tanggal-gagal #11; ganti bersama itemnya.

## Tabel verifikasi per item
Standar: LOLOS = terjadi / pertama dilaporkan 25 Nov 2026 dari sumber primer. GAGAL = laporan pertama 24 Nov atau lebih awal. ABU-ABU = tidak bisa diputus tuntas, condong ke satu arah (dicatat alasannya).

| # | Cerita (sesuai gambar) | Verdict | Bukti singkat + sumber |
|---|---|---|---|
| H1 | Shenzhou-24, Zeeshan Ali | **LOLOS** | Liftoff 25 Nov 00:18:52 UTC; Ali Pakistan pertama di orbit + orang asing pertama di Tiangong. Wikipedia / Xinhua / Reuters. |
| H2 | Treaty Australia–Solomon | **LOLOS** | Ditandatangani Canberra 25 Nov 2026; Australia mitra keamanan utama, tanpa pangkalan militer asing. pm.gov.au / AP / Reuters. |
| H3 | Iowa 68 barel | **LOLOS** | 68 barel/drum, ~9.500–9.700 lbs, diledakkan Rab 25 Nov ~09:00 CST = 14:00 UTC (timeline gambar 14:00 ✓). Guardian / US Army. |
| #4 | CPI Australia 4,9% | **LOLOS** | ABS rilis 25 Nov 11:30 AEDT = 00:30 UTC; headline 4,9%, trimmed mean 3,8%, housing +6,4% — cocok persis dengan gambar. Reuters / ABS. |
| #5 | Lamarre-Condon bersalah | **LOLOS** | Vonis Rab 25 Nov, NSW Supreme Court, juri ~2 jam. Guardian. |
| #6 | Gaza "ground push pertama sejak gencatan senjata" | **GAGAL** | Operasi itu **18 Nov 2026** (URL Al Jazeera /2026/11/18/; BBC: operasi selesai Kam 19 Nov, tank ditarik 19 Nov). Artikel 25 Nov (pan.parallax.kr) mendaur ulang verbatim cerita 18 Nov. Stempel "Al Jazeera 25 Nov 02:59 UTC" di build-log palsu — modus yang sama persis dengan v1. |
| #7 | Martha Ford meninggal 101 | **ABU-ABU condong LOLOS** | Meninggal **24 Nov** (Wikipedia: died Nov 24, aged 101; AP: "died Tuesday"). Tapi pengumuman Lions terbit **2026-11-25T02:02:01Z** dan gambar membingkainya sebagai "Detroit Lions announce death" — pengumuman itu peristiwa 25 Nov. Risiko: juri yang cek Wikipedia melihat tanggal kematian 24 Nov. |
| #8 | Jepang tolak peran nuke-ban | **GAGAL** | Motegi mengumumkan **Sel 24 Nov** (video TBS 24 Nov; Mainichi/postingan Instagram 24 Nov; "Motegi said Tuesday"). Japan Times versi Inggris 25 Nov 01:49 UTC adalah re-stamp; "25 Nov 01:34 UTC" di build-log adalah stempel agregator. |
| #9 | Mogok Seoul Metro batal | **LOLOS** | Yonhap "SEOUL, Nov. 25"; kesepakatan semalam, 2.212 pekerjaan ditunda, rekrut 500. JoongAng terbit 2026-11-24T23:48:08Z = 25 Nov 08:48 KST. |
| #10 | Ekspor Korea rekor | **LOLOS** | Yonhap "SEOUL, Nov. 25", terbit 2026-11-25T01:00:47Z; ekspor barang konsumen rekor $28,65 miliar. |
| #11 | Tidal larang musik AI | **GAGAL** | Diumumkan **Sel 24 Nov** (TechCrunch 2026/11/24; Paste 2026-11-24T15:58:16Z; postingan Tidal sendiri 24 Nov). Klaim build-log "Guardian, 25 Nov" salah sebagai laporan pertama. Angka 27M-nya nyata tapi ikut terkontaminasi (M4). |
| #12 | Review budaya Met Police | **LOLOS** | Fairfield Review terbit Rab 25 Nov; headline Guardian "Latest review of Met police culture finds little has changed". |
| #13 | Oscars VFX Top 20 | **LOLOS** | Variety eksklusif, terbit 2026-11-25 ~02:55–02:59 UTC; Disney pimpin 4 judul; 19 dari 20 terkonfirmasi — framing "Top 20 revealed" wajar. |
| #14 | PacGuard diluncurkan | **ABU-ABU condong LOLOS** | PINA "Breaking News November 25, 2026"; tapi rilis FFA sendiri berdateline 24 Nov; Post Courier: berita pecah Rab 25 Nov. Tidak bisa diputus tuntas; condong lolos atas dasar tanggal PINA. |
| #15 | Pasifik "tired of waiting" iklim | **ABU-ABU condong LOLOS** | PINA 25 Nov, bersumber AAP; keruntuhan COP31 sendiri 22–24 Nov, tapi artikel ini potongan reaksi/tindak lanjut 25 Nov (delegasi pulang, janji bertahan). |
| #16 | Op-ed ADB: Asia-Pasifik hadapi masa depan sebagai satu | **GAGAL** | Op-ed Kanda terbit **24 Nov**: Bonik Barta English header editorial "TUESDAY, November 24, 2026"; rilis ADB "Masato Kanda Begins New Term" 24 Nov. Halaman PINA /2026/11/25/ adalah **re-publikasi** op-ed bertanggal 24 Nov — untuk op-ed, tanggal terbitnya ADALAH tanggal ceritanya. |
| #17 | Kekeringan Fiji | **ABU-ABU condong LOLOS** | PINA 25 Nov; tapi alamat video NDRMO Fiji dengan isi sama diposting 24 Nov; status bencana diumumkan 18 Nov. Basis lolos sama seperti v1 (artikel PINA 25 Nov); dicatat keraguannya. |
| #18 | Vanuatu tuan rumah WCPFC | **ABU-ABU condong LOLOS** | PINA 25 Nov; pertemuan FFC145 berjalan 24–26 Nov di Port Vila (postingan FFA 23–24 Nov) — pertemuan sedang berlangsung pada 25 Nov, jadi defensibel sebagai cerita 25 Nov. |
| #19 | Fiji A 68–36 Samoa | **ABU-ABU condong LOLOS** | PINA 25 Nov, Fiji A menang 68–36 di Brisbane. Hasil pertama muncul di Facebook Netball Fiji 24 Nov — tapi artikel PINA yang dikutip memang bertanggal 25 Nov dan liputan hasil pertandingan malam sebelumnya adalah praktik koran standar. |
| #20 | Hanwha KM3 | **LOLOS** | Yonhap "SEOUL, Nov. 25", terbit 2026-11-25T01:20:10Z; diumumkan tanggal 25 (kesepakatan dasar ditandatangani "tanggal 3" — pengumumannya yang jadi berita 25 Nov). |
| #21 | Hyundai pengisian EV | **LOLOS** | Diumumkan 25 Nov ("said Wednesday", "announced on the 25th", AJP "On November 25"). |
| #22 | KOSPI anjlok | **LOLOS** | Dibuka turun 3,94% pada 25 Nov, sidecar terpicu 09:08–09:09 pagi. |
| #23 | Aturan stablecoin Korea | **GAGAL** | FSC mengungkap rancangan RUU **Sel 24 Nov** (CoinDesk "Nov 24, 2026, 5:29 a.m. EST"; The Block 2026-11-24T06:25:24-05:00; Reuters "said on Tuesday"). "25 Nov 02:08 UTC" di build-log adalah re-stamp wire Reuters. |
| #24 | Pemadam Bucheon jadi pahlawan nasional | **LOLOS** | Korea Times: kementerian veteran "said Wednesday" — pendaftaran sebagai person of national merit diumumkan 25 Nov (pemadam gugur 16–17 Okt; pendaftarannya yang jadi berita). |
| #25 | Sejong pindah 31 lembaga | **GAGAL** | Kementerian mengumumkan **Sel 24 Nov** (Yonhap "SEOUL, Nov. 24"; "the interior ministry said Tuesday"; biz.news-s.kr "finalized and announced on the 24th"). Artikel JoongAng 25 Nov bukan laporan pertama. |
| #26 | Hukuman curang ujian AI 5 tahun | **GAGAL** | Langkah dipresentasikan di rapat Kabinet **Sel 24 Nov** (JoongAng "at a Cabinet meeting on Tuesday"; sedaily "reported to the Cabinet on the 24th"; Arirang 2026-11-24 17:00 KST). |
| #27 | WHO: blokade bahan bakar Kuba | **GAGAL** | Tedros menyerukan **Sel 24 Nov** (Reuters "HAVANA, Nov 24"; "called on Tuesday"). Artikel Al Jazeera 25 Nov adalah re-publikasi. |
| #28 | Studi wildfire Indonesia | **ABU-ABU condong LOLOS** | MyNewsReader: "Mongabay · 2026-11-25"; Kind Focus: "Mongabay · Nov 24, 9:15 PM" — bila itu waktu AS Timur = 02:15 UTC 25 Nov. Zona waktu tidak bisa diputus tuntas; condong lolos atas dasar UTC. |
| #29 | Kesenjangan frailty Inggris terlebar | **LOLOS** | Guardian 25 Nov 03:40; studi KCL / BMC Medicine; 31 negara, 71.703 orang; Inggris kesenjangan terlebar. |
| #30 | Al Gore beli Carthage Courier | **ABU-ABU condong LOLOS** | Courier mengumumkan Sel 24 Nov (waktu AS); kawat AP 11/24/2026 20:26 -0500 = **01:26 UTC 25 Nov**; Guardian (UK) kemungkinan 25 Nov. Condong lolos atas dasar UTC/UK — tapi pengumuman aslinya Selasa 24 Nov waktu AS, jadi rapuh. |
| #31 | Philip Rosenberg meninggal 91 | **GAGAL** | Meninggal **28 Okt 2026**; obituari Variety **24 Nov 2026** (ref. Wikipedia; kartu LittleShelf Sel 24 Nov 20:00). Baik kematian maupun obituarinya bukan 25 Nov. Klaim build-log "Variety, 25 Nov" salah. |
| #32 | Price cap Inggris jatuh tempo hari ini | **LOLOS** | Ofgem mengumumkan cap Jan–Mar 2027 **paling lambat 25 Nov 2026**; framing gambar "due today" akurat (angka pastinya memang belum keluar saat kompilasi ~06:00 UTC — footer mengakuinya dengan jujur). BBC 25 Nov. |
| #33 | Film lab Indonesia–Prancis | **ABU-ABU condong GAGAL** | Variety eksklusif bercap **"Nov 24, 2026 7:00pm PT"** (= 03:00 UTC 25 Nov). Klaim "25 Nov" hanya bertahan lewat konversi UTC atas publikasi malam AS; juri yang membaca dateline Variety melihat 24 Nov. |
| #34 | Golden Globes: 170 film, 475 aktor | **ABU-ABU condong GAGAL** | Halaman prediksi Variety **"Updated: Nov. 24, 2026"** memuat angka 170 film / 475 aktor; cerita ballots-out juga 24 Nov; listing "Variety · 2026-11-25" adalah tanggal edisi agregator. Tidak ditemukan stempel primer 25 Nov. |
| Spot-check eksklusi | Chen Jining diselidiki | **LOLOS (sebagai eksklusi)** | Xinhua mengumumkan **Sel 24 Nov** (Wikipedia / Reuters). Footer DATE CHECK benar mengeluarkannya. |

**Rekap hitungan:** 34 cerita — LOLOS bersih 15 (H1, H2, H3, #4, #5, #9, #10, #12, #13, #20, #21, #22, #24, #29, #32) · GAGAL terkonfirmasi 9 (#6, #8, #11, #16, #23, #25, #26, #27, #31) · ABU-ABU condong LOLOS 8 (#7, #14, #15, #17, #18, #19, #28, #30) · ABU-ABU condong GAGAL 2 (#33, #34). **Yang bisa dipertahankan: 23 dari 34. Yang bermasalah: 11 dari 34 (32%).**

### Verifikasi numbers strip (4,9% · 68 · 101 · 27M · 2.212)
| Angka | Sumber di gambar | Verdict |
|---|---|---|
| 4,9% | CPI Australia #4 | ✅ benar (ABS headline 4,9%, 25 Nov) |
| 68 | Barel Iowa #3 | ✅ benar (68 barel, 25 Nov) |
| 101 | Usia Martha Ford #7 | ✅ angka benar (101 tahun); itemnya abu-abu (meninggal 24 Nov, diumumkan 25 Nov) |
| 27M | Trek AI Tidal #11 | ⚠️ **terkontaminasi** — angka nyata (27 jt trek ditandai AI) tapi itemnya GAGAL tanggal (24 Nov) |
| 2.212 | Pekerjaan Seoul Metro #9 | ✅ benar (2.212 pekerjaan ditunda, Yonhap 25 Nov) |

### Verifikasi region bar
Asia-Pacific 21 · Americas 7 · Europe 3 · Middle East 1 · Culture 2 = 34 — **rekonsiliasi benar** dengan isi gambar bila Rosenberg dihitung Americas dan film lab (#33) + Golden Globes (#34) dihitung Culture: APAC 21 (1, 2, 4, 5, 8, 9, 10, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28), Americas 7 (3, 7, 11, 13, 27, 30, 31), Europe 3 (12, 29, 32), Middle East 1 (6), Culture 2 (33, 34). Catatan: aritmetikanya benar, tapi item yang dihitung mencakup yang tanggal-gagal (#31, #33) — region bar ikut ternoda oleh B1, bukan salah hitung.

### Breadth
3 hero + 10 sekunder + 21 ALSO ON = **34 cerita** — benar sesuai klaim masthead. (Catatan: masthead menulis "34 STORIES · ALL FIRST REPORTED TODAY" — jumlahnya benar, klaim "ALL FIRST REPORTED TODAY"-nya palsu.)

## Penilaian visual
- **Keterbacaan:** bersih di semua crop 2×. Tidak ada teks garbled, terpotong, atau overlap yang ditemukan di area manapun (masthead, 3 hero, 10 panel sekunder, ALSO ON #14–34, numbers strip, region bar, timeline, peta, footer). Deck hero 1 baris 2 kini terbaca penuh (B2 tertutup).
- **Peta:** hero 2 kini Pasifik yang benar (B3 tertutup). Strip peta dunia "WHERE IT HAPPENED" terpisah hadir dengan pin bernomor + legenda; pin-pin kira-kira benar untuk peta skematik (pin 3 Iowa duduk di tengah-utara Amerika Utara — dapat diterima). Pin Seoul sudah di belahan utara yang benar.
- **DATE CHECK footer:** bersih dan terbaca penuh, daftar eksklusi akurat (spot-check Chen Jining 24 Nov ✓; daftar eksklusi lain — Huang/Schumer, Takaichi–Akane, Abrego Garcia, Shuri Castle, Dell, Venezuela, Cartagena, Thomas Markle, Pope diary, Senegal AFCON, Nepal, Keio, Microsoft, Zelensky–Magyar, Patriot — konsisten dengan temuan independen bahwa semua itu 23–24 Nov). Footer juga jujur soal waktu kompilasi: "Compiled ~06:00 UTC; later US daytime news not yet in." — pengakuan yang benar, karena berita siang AS memang belum masuk.
- **Kesan keseluruhan:** koran ini kini tampak seperti pemenang dari segi kerajinan — masthead serif raksasa + tanggal penuh, region bar, timeline berwaktu, THE DAY IN NUMBERS, 3 hero bergambar, 10 sekunder bergambar, ALSO ON bernomor, peta dunia + pin, DATE CHECK jujur. Yang merusaknya bukan tampilan, melainkan isi: sepertiga koran berisi berita kemarin.

## Estimasi jujur (chase-top-10)
- **Estimasi rank: ~800–2.500 dari ~9.000+ entri.**
- **Peluang top-50: ~10%. Peluang top-10: <1%.**
- **Alasan:** kerajinan kini setara pola pemenang ni24 (34 cerita, peta benar, deck bersih, strip peta, timeline, hitungan) — itu mengangkatnya jauh dari v1 (~2.500–6.000, top-50 ~3%). Tapi 26–32% cerita gagal aturan tanggal, dan juri AI yang memeriksa fakta akan menangkap beberapa di antaranya dan menghukum akurasi dengan berat. Pemenang ni24 punya tanggal bersih; koran dengan 9 cerita kemarin tidak bisa masuk zona hadiah (top 50; cutoff ni24 ronde 1: rank 50 = 654.221). Estimasi ini TIDAK digelembungkan: tanpa perbaikan tanggal, entry ini di luar garis hadiah.
- **Nilai perbaikan ronde 3:** bila ke-11 item bermasalah diganti dengan cerita 25 Nov yang terverifikasi primer (dan 27M diganti), estimasi naik ke **~rank 50–150, top-50 ~35–45%** — sekelas estimasi ni24 ronde 4 yang LAYAK SUBMIT. Itulah nilai satu ronde perbaikan yang dikerjakan dengan metode benar.

## Daftar perbaikan untuk ronde 3 (wajib)
Ganti 9 item GAGAL terkonfirmasi: **#6 Gaza, #8 Jepang nuke-ban, #11 Tidal, #16 op-ed ADB, #23 stablecoin, #25 Sejong, #26 ujian-AI, #27 WHO-Kuba, #31 Rosenberg** — plus 2 abu-abu condong gagal **#33 film lab, #34 Golden Globes** (ganti demi aman; bila fixer bisa membuktikan stempel primer 25 Nov untuk keduanya, boleh dipertahankan — beban bukti di fixer). Ganti angka **27M** di numbers strip bersama #11. Verifikasi ulang 8 item abu-abu condong lolos (#7, #14, #15, #17, #18, #19, #28, #30) dari outlet primernya — boleh dipertahankan, tapi konfirmasi laporan pertamanya.

**Peringatan metode (kritis — baca sebelum ronde 3):** fixer mengulangi **persis** kesalahan v1: memakai stempel re-post agregator/wire (Reuters wire, PINA re-post, artikel 25 Nov yang mendaur ulang berita 18/24 Nov) sebagai tanggal laporan pertama. Ronde 3 WAJIB memverifikasi tanggal **laporan pertama dari outlet primer** untuk tiap cerita — bukan tanggal halaman agregator, bukan tanggal wire yang me-re-stamp, bukan tanggal edisi. Dua jebakan khusus: (1) artikel PINA bertanggal 25 Nov waktu Fiji = 24 Nov UTC — bila isinya pengumuman 24 Nov, itu cerita 24 Nov; (2) publikasi malam AS (Variety 19:00 PT, AP 20:26 ET) memang jatuh 25 Nov UTC, tapi juri membaca dateline outlet — anggap 24 Nov kecuali outletnya sendiri (mis. Guardian UK) mencap 25 Nov. Setelah penggantian, verifikasi ulang klaim DATE CHECK **per item satu-satu** sebelum Goldfish re-review berikutnya.

## Catatan kecil (bukan blocker/major)
- Hero 3 menulis "~9.500 lbs" sementara laporan menyebut ~9.700 lbs — masih dalam rentang yang dilaporkan dan ada kualifikasi "about"; diterima.
- #13 "Top 20 revealed" — Variety mengonfirmasi 19 dari 20 judul + 1 belum terkonfirmasi; framing "Top 20" wajar.
- Keberadaan source line / status badge di tiap hero tidak dikonfirmasi terpisah dalam crop yang saya ambil; bila ada, baik; bila tidak, itu minor — bukan penghalang.
- Footer "Compiled ~06:00 UTC" jujur dan membantu — pertahankan pengakuan seperti ini di ronde berikutnya.
