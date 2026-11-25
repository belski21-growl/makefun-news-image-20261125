# GOLDFISH REVIEW — RE-REVIEW v3 (round 3)
## news-image-20261125 — "The World in One Day"

- **Reviewer:** Goldfish (penilai independen — bukan builder, bukan fixer)
- **Tanggal review:** 25 November 2026 (~13:30 WIB / ~06:30 UTC)
- **Entry dinilai:** `entry.png` v3 — sha256 `df4a30ca10053c6005b37b0c2a82dbddd0d1699f2f7f50f8f857df5fab136f6c`, 276.540 byte, 1024×1024 JPEG
- **Entry v2 (pembanding):** sha256 `30b59778c802cccfe743db3e40263e668636f418f9e8d037b47537c928759ae2`, 270.327 byte
- **Kompetisi:** news-image-20261125 — $100, 50 tempat, juara 1 $20; deadline 27 Nov 2026 07:00 WIB; juri z-ai/glm-5.3-flash

## Metode
- Membaca langsung `entry.png` v3: full + 6 crop-zoom 2× (`/tmp/gf3/`: heroes, secondary, numbers_alson_top, alson_bottom, map_footer) — semua area yang diubah + spot-check tetangga yang lolos.
- Membaca penuh `build-log.md` (bagian v3: 11 pengganti + outlet primer + stempel UTC + URL + catatan kejujuran riset), `goldfish-review-r2.md`, dan `top10-analysis.md`.
- Verifikasi faktual independen via web search: **12 kueri + 1 buka langsung artikel primer** (Yonhap #25) — ke-11 pengganti satu per satu, angka numbers strip baru, dan 2 spot-check (Leiter, Sudan).
- Standar tanggal yang dipakai: tanggal **laporan pertama dari sumber primer** (outlet yang pertama kali memberitakan), bukan stempel agregator/wire re-post, bukan tanggal halaman live-blog. Ini standar yang sama dengan review v1/r2 — dan standar yang akan dipakai juri AI saat memeriksa tanggal.
- File entry TIDAK diubah, TIDAK disubmit, TIDAK dibuat repo.

## Status blocker & major v2
| Item v2 | Status v3 | Bukti |
|---|---|---|
| **B1 — DATE CHECK salah (9 gagal + 2 abu-abu condong gagal dari 34)** | **MASIH TERBUKA** | Kini **3 GAGAL terkonfirmasi** (#11 Sudan–Ethiopia, #26 India CPI, #27 Leiter) + **1 abu-abu condong gagal** (#33 Stokes) dari 34. Turun besar dari v2 (9+2), tapi klaim footer "EVERY STORY ABOVE WAS FIRST REPORTED WEDNESDAY 25 NOVEMBER 2026" **masih palsu untuk 3 cerita** — dan dua di antaranya parah: #27 berumur ~2 bulan, #11 berumur ~3 minggu. |
| **B2 — Deck hero 1 baris 2 GARBLED total** | **TERTUTUP** | Crop-zoom 2×: "Shenzhou-24 lifts off at 00:18 UTC. Zeeshan Ali is the first Pakistani in orbit — and the first foreigner aboard China's Tiangong station." — bersih, terbaca penuh. |
| **B3 — Peta hero 2 = Amerika Utara** | **TERTUTUP** | Crop-zoom 2×: peta kini Pasifik — Australia, Papua N.G., Solomon Is., pin Honiara + Canberra. Benua benar. |
| **M1 — Breadth hanya 14 cerita** | **TERTUTUP** | Dihitung dari gambar: 3 hero + 10 sekunder + 21 ALSO ON = **34 cerita**. |
| **M2 — Build-log klaim cerita yang TIDAK ada di gambar** | **TERTUTUP** | Build-log v3 ditulis dari gambar final; semua item di log ada di gambar dan sebaliknya (diverifikasi silang saat review). |
| **M3 — Tanpa strip peta dunia; region bar tanpa hitungan; timeline tanpa jam; hero tanpa source line/badge** | **TERTUTUP** | Strip "WHERE IT HAPPENED" terpisah ADA + pin bernomor + legenda; region bar ADA hitungan dan rekonsiliasi ke 34 (lihat bawah); timeline ADA 5 waktu (00:18/00:30/02:02/02:28/14:00 UTC); hero ADA source line + badge (OFFICIAL / SIGNED TODAY / CONFIRMED). Pin 6 Jeddah dan 11 Khartoum terpisah jelas di peta. |
| **M4 — Numbers strip terkontaminasi (27M merujuk #11 Tidal yang gagal tanggal)** | **TERTUTUP** | 27M dibuang; strip kini 4,9% · 68 · 101 · **25,113** · 2,212 — kelima angka terverifikasi bersih (lihat bawah). |

## VERDICT: LAYAK LANJUT BELUM LAYAK SUBMIT

Kemajuan nyata: gagal tanggal turun dari 9+2 (v2) menjadi 3+1 (v3); kerajinan tetap setara pola pemenang; numbers strip bersih. Tapi **B1 masih terbuka**: 3 cerita GAGAL tanggal terkonfirmasi, dan dua di antaranya bukan selisih satu hari melainkan **berita lama yang dihidupkan kembali oleh halaman live-blog** — #27 insiden 23 September 2026, #11 penutupan konsulat 4–5 November 2026. Satu cerita seperti itu saja sudah blocker menurut brief; ini tiga. Fixer jujur mengakui hanya 4/11 pengganti yang bersih — verifikasi independen saya mengonfirmasi angka itu (6 bersih tanggal, 1 condong lolos, 1 condong gagal, 3 gagal; selisihnya karena saya menilai #31 bersih tanggal meski duplikat tema, dan #6 condong lolos).

**Blocker tersisa:**
- **B1 (masih terbuka)** — 3 cerita GAGAL tanggal terkonfirmasi: **#11 Sudan–Ethiopia** (4–5 Nov), **#26 India food inflation** (data 12 Nov), **#27 Leiter car-ramming** (23 Sep) — plus 1 abu-abu condong gagal: **#33 Ben Stokes** (laporan pertama 24 Nov malam).
**Major tersisa:**
- **M5 (baru) — #31 duplikat tema #22.** "KOSPI sinks 5%+ by midday" dan "KOSPI opens sharply lower" adalah dua jepretan dari pergerakan pasar yang sama di hari yang sama. Tanggalnya bersih, tapi satu slot dari 34 terbuang untuk cerita yang sama. Sebaiknya diganti sekalian di ronde mikro (lihat bawah).

## Tabel verifikasi ke-11 pengganti
Standar: LOLOS = terjadi / pertama dilaporkan 25 Nov 2026 dari sumber primer. GAGAL = laporan pertama 24 Nov atau lebih awal. ABU-ABU = tidak bisa diputus tuntas, condong ke satu arah.

| # | Pengganti (sesuai gambar) | Verdict | Bukti singkat + sumber |
|---|---|---|---|
| #8 | Japan–Singapore defence meeting, Tokyo | **LOLOS** | MINDEF Singapura merilis 25 Nov (URL /25nov26-nr/); kunjungan 24–25 Nov, tapi **meeting + joint statement-nya 25 Nov** (Koizumi presser 24 Nov: meeting "scheduled for tomorrow, the 25th"). "60 years of ties" benar (SJ60). |
| #16 | Korea births +12,2%, 25.113, fertility 0,90 | **LOLOS** | AJP "SEOUL, November 25" — data Kementerian dirilis tanggal 25; Sept births 25.113 (+12,2%), Jan–Sep 218.896 (+14,3%), TFR Q3 0,90. Yonhap Infomax mengonfirmasi rilis "on the 25th". |
| #23 | Remains Cpl. Ahn Gyu-tae return home | **LOLOS** | Yonhap "SEOUL, Nov. 25" + AJP "November 25" — upacara pemulangan Rabu 25 Nov 16:00 KST di Seoul Air Base; resepsi Hawaii 23 Nov hanya latar, peristiwa pulang-nya 25 Nov. Timeline gambar 02:28 = jam kawat Yonhap (11:28 KST) ✓. |
| #25 | Korea–UN peacekeeping working group | **LOLOS** | Artikel Yonhap dibuka langsung: "SEOUL, Nov. 25 (Yonhap) — ... the foreign ministry said Wednesday." Pertemuan di New York memang Senin 23 Nov, tapi **pengumumannya Rabu 25 Nov** — pola yang sama dengan #9/#20/#24 yang dipertahankan. |
| #33 | Ben Stokes enters IPL auction ₹2 crore | **ABU-ABU condong GAGAL** | Register dibagikan ke franchise **"Tuesday evening"** (Cricbuzz) = 24 Nov; cricketwinner terbit **24 Nov 23:53 IST** (= 18:23 UTC 24 Nov). Liputan besar memang 25 Nov pagi (Cricbuzz update 25 Nov 04:52 UTC), tapi laporan pertama sudah 24 Nov malam. Sama seperti preseden #33 v2 (Variety cap 19:00 PT). |
| #34 | "Why tiny cars are taking off across Europe" | **LOLOS** | BBC Technology, terbit **25 Nov 00:34:05Z** (terverifikasi di 2 mirror independen). Memang feature, bukan breaking — tapi tanggal publikasinya bersih 25 Nov. |
| #26 | India food inflation 8,94% in October | **GAGAL** | Data CPI Oktober dirilis **12 Nov 2026** (MoSPI, embargo s.d. 12 Nov 16:00; Reuters "NEW DELHI, Nov 12"; food inflation 8,94%, retail 6,09%). Artikel BBC 25 Nov (bila ada) hanyalah analisis susulan atas data 13 hari — berita yang sama bentuknya dengan #16 ADB op-ed yang gagal di v2. Fixer sendiri menandainya RISKY. |
| #6 | Houthis threaten Jeddah + Saudi Red Sea ports | **ABU-ABU condong LOLOS** | Reuters wire berdateline **"Nov 25"** + "said on Wednesday"; pada 25 Nov Saree memperluas daftar target + memposting peta Telegram (dikonfirmasi analisis House of Saud). Kelemahan: ancaman yang sama pertama dibuat 20 Nov dan diperluas 22 Nov; slug URL re-post /2026/11/24/ mencerminkan tanggal CMS AS, bukan tanggal peristiwa. Perkembangan 25 Nov-nya (peta + perluasan daftar) nyata — condong lolos, tapi rapuh. |
| #27 | Israeli soldier hurt in West Bank car-ramming | **GAGAL** | Insiden Neria Leiter terjadi **23 September 2026** (AP 23 Sep; CNN 24 Sep; "critically wounded on September 23"; update 11 Nov: sudah >6 minggu, dipindah ke rehab). Halaman live Al Jazeera 25 Nov hanya memunculkan ulang cerita 2 bulan lalu. Gambar menyajikannya sebagai berita hari ini — salah besar. |
| #31 | KOSPI sinks 5%+ by midday on tech rout | **LOLOS tanggal / MAJOR duplikat** | Tanggal bersih: AJP "Posted: November 25, 2026, 11:32" — KOSPI −5,68% ke 4.721,60 pukul 11:20. Tapi **tema duplikat #22** ("KOSPI opens sharply lower", −3,94% saat buka) — dua jepretan pergerakan yang sama di hari yang sama. Bukan gagal tanggal; ini major kerajinan (M5). |
| #11 | Sudan, Ethiopia shut consulates | **GAGAL** | Penutupan terjadi **4–5 November 2026**: Ethiopia tutup konsulat Asosa 4 Nov, Sudan tutup konsulat Gedaref 5 Nov (SRN News "Wed, Nov 4, 2026"; URL Al Jazeera /2026/11/4/; Al Jazeera 5 Nov 04:33). Halaman live Al Jazeera "Sudan war | Today's latest" 25 Nov memunculkan ulang cerita 3 minggu lalu. Gambar menyajikannya sebagai berita hari ini — salah besar. |

**Rekap hitungan v3 (34 cerita):** LOLOS bersih 21 (3 hero + #4, #5, #9, #10, #12, #13, #20, #21, #22, #24, #29, #32 + pengganti #8, #16, #23, #25, #34, #31-tanggal) · ABU-ABU condong LOLOS 9 (#7, #14, #15, #17, #18, #19, #28, #30 + #6) · ABU-ABU condong GAGAL 1 (#33) · **GAGAL terkonfirmasi 3 (#11, #26, #27)**. Yang bisa dipertahankan: 30 dari 34. Yang bermasalah: 4 dari 34 (12%) — turun dari 11 dari 34 (32%) di v2.

### Verifikasi numbers strip (4,9% · 68 · 101 · 25,113 · 2,212)
| Angka | Sumber di gambar | Verdict |
|---|---|---|
| 4,9% | CPI Australia #4 | ✅ benar (ABS headline 4,9%, 25 Nov) |
| 68 | Barel Iowa H3 | ✅ benar (68 barel, 25 Nov) |
| 101 | Usia Martha Ford #7 | ✅ angka benar (101 tahun); itemnya abu-abu (meninggal 24 Nov, diumumkan 25 Nov) |
| 25,113 | Kelahiran Korea Sept #16 | ✅ benar (AJP/Yonhap: 25.113, +12,2%, 25 Nov) |
| 2,212 | Pekerjaan Seoul Metro #9 | ✅ benar (2.212 pekerjaan ditunda, Yonhap 25 Nov) |

### Verifikasi region bar
Asia-Pacific 22 · Americas 4 · Europe 4 · Middle East 2 · Africa 1 · Culture 1 = 34 — **rekonsiliasi benar** dengan isi gambar: APAC 22 (H1, H2, #4, #5, #8, #9, #10, #14, #15, #16, #17, #18, #19, #20, #21, #22, #23, #24, #25, #26, #28, #31), Americas 4 (H3, #7, #13, #30), Europe 4 (#12, #29, #32, #34), Middle East 2 (#6, #27), Africa 1 (#11), Culture 1 (#33). Catatan: aritmetikanya benar, tapi item yang dihitung mencakup yang tanggal-gagal (#11, #26, #27) — region bar ikut ternoda oleh B1, bukan salah hitung.

### Breadth
3 hero + 10 sekunder + 21 ALSO ON = **34 cerita** — benar sesuai klaim masthead. (Catatan: masthead menulis "34 STORIES · ALL FIRST REPORTED TODAY" — jumlahnya benar, klaim "ALL FIRST REPORTED TODAY"-nya masih palsu untuk 3 cerita.)

## Penilaian visual
- **Keterbacaan:** bersih di semua crop 2×. Tidak ada teks garbled, terpotong, atau overlap di area yang diubah (kartu SEC #6/#8/#11, numbers strip 25,113, 8 item ALSO ON pengganti, pin peta Jeddah + Khartoum, footer DATE CHECK) maupun di tetangga yang lolos. Deck hero 1 baris 2 tetap bersih (B2 tertutup). Hero 2 tetap peta Pasifik yang benar (B3 tertutup).
- **Peta:** strip "WHERE IT HAPPENED" terpisah hadir; pin 6 (Jeddah) dan 11 (Khartoum) terpisah jelas — 6 di jazirah Arab, 11 di Afrika tengah; legenda cocok (1 Jiuquan, 2 Canberra+Honiara, 3 Iowa, 4–5 Sydney, 6 Jeddah, 7 Detroit, 8 Tokyo, 9–10 Seoul, 11 Khartoum, 12 London, 13 Los Angeles). Pin-pin kira-kira benar untuk peta skematik.
- **DATE CHECK footer:** bersih dan terbaca penuh, termasuk daftar eksklusi baru (16 tambahan v3) dan pengakuan jujur "Compiled ~05:30 UTC; later US daytime news not yet in." Satu catatan: footer menyebut "Hodeidah strikes (24 Nov)" sebagai eksklusi sementara #6 membahas ancaman terhadap Jeddah — tidak kontradiktif (ancaman ≠ serangan), tapi juri yang teliti bisa menganggapnya berdekatan; bukan blocker.
- **Kesan keseluruhan:** kerajinan kini setara pola pemenang ni24 (masthead serif raksasa + tanggal penuh, region bar berhitungan, timeline berwaktu, THE DAY IN NUMBERS, 3 hero bergambar + badge, 10 sekunder bergambar, ALSO ON bernomor, peta dunia + pin, DATE CHECK jujur). Yang merusaknya tinggal isi: 3 cerita kemarin (satu berumur 2 bulan) + 1 abu-abu.

## Estimasi jujur (chase-top-10)
- **Estimasi rank: ~150–600 dari ~9.000+ entri.**
- **Peluang top-50: ~20–25%. Peluang top-10: ~2–3%.**
- **Alasan:** kerajinan setara pemenang dan 30/34 cerita bisa dipertahankan — itu mengangkatnya jauh dari v2 (~800–2.500, top-50 ~10%). Tapi 3 cerita gagal tanggal, dua di antaranya berita lama berminggu-minggu/bulan, akan memotong skor akurasi secara berat setiap kali juri memeriksanya dalam 2v2; pemenang ni24 punya tanggal bersih. Estimasi ini TIDAK digelembungkan: tanpa perbaikan tanggal, entry ini masih di luar garis hadiah yang aman (cutoff ni24 ronde 1: rank 50 = 654.221). Proyeksi r2 (bila 11/11 bersih → rank 50–150, top-50 ~35–45%) belum tercapai karena hanya 6/11 pengganti yang bersih tanggal.

## Daftar perbaikan untuk ronde mikro (wajib sebelum LAYAK SUBMIT)
Satu ronde mikro — ganti **4 item** (3 di antaranya one-liner ALSO ON, murah):
1. **#11 Sudan–Ethiopia** (panel sekunder; konsulat tutup 4–5 Nov) → cerita 25 Nov terverifikasi primer. Bila penggantinya bukan Afrika, hitung ulang region bar (Afrika jadi 0 — hapus kategorinya atau isi dengan cerita Afrika 25 Nov lain).
2. **#26 India food inflation** (ALSO ON; data 12 Nov) → cerita 25 Nov terverifikasi primer. JANGAN pakai analisis susulan atas data lama — tanggal RILIS DATA yang dihitung, bukan tanggal artikel analisis.
3. **#27 Leiter car-ramming** (ALSO ON; insiden 23 Sep) → cerita 25 Nov terverifikasi primer. JANGAN pakai item halaman live-blog tanpa memverifikasi tanggal insidennya — live blog mendaur ulang konteks lama.
4. **#33 Ben Stokes** (ALSO ON; laporan pertama 24 Nov malam) → cerita 25 Nov terverifikasi primer. Opsional tapi sangat dianjurkan: satu ronde mikro yang menyisakan abu-abu tidak menutup B1 sepenuhnya.
- Opsional dalam ronde yang sama: **#31 KOSPI midday** → cerita berbeda yang bukan pasar Korea (menutup M5 duplikat tema).
- Setelah penggantian: verifikasi ulang klaim DATE CHECK **per item satu-satu**; perbarui numbers strip bila angka yang dirujuk ikut diganti (saat ini strip sudah bersih — jangan sentuh kecuali itemnya berubah); hitung ulang region bar; Goldfish **micro re-review** (hanya item pengganti + visual area yang diubah) sebelum LAYAK SUBMIT.
- **Apakah ronde mikro masih masuk akal? YA.** Hanya 4 item (3 one-liner), generator PIL sudah ada, dan stok cerita 25 Nov belum habis — kompilasi v3 ~05:30 UTC, sementara berita siang/malam 25 Nov (waktu AS) masih terus keluar; kandidat bisa juga diambil dari kawat siang 25 Nov, bukan hanya pagi hari. Yang TIDAK masuk akal adalah ronde penuh keempat — kerangka sudah benar, yang kurang hanya 4 slot.
- **Peringatan metode (tetap berlaku):** dua dari tiga gagal v3 berasal dari **halaman live-blog yang mendaur ulang berita lama** (Al Jazeera "Today's latest"). Ronde mikro WAJIB memverifikasi tanggal **insiden/peristiwa dan laporan pertamanya**, bukan tanggal halaman yang menampilkannya. Satu artikel live-blog bertanggal 25 Nov TIDAK membuktikan ceritanya 25 Nov.

## Catatan kecil (bukan blocker/major)
- Hero 3 menulis "~9.500 lbs" sementara laporan menyebut ~9.700 lbs — masih dalam rentang yang dilaporkan dan ada kualifikasi "about"; diterima (sama seperti r2).
- #13 "Top 20 revealed" — Variety mengonfirmasi 19 dari 20 judul + 1 belum terkonfirmasi; framing "Top 20" wajar.
- #34 adalah feature BBC, bukan breaking news — dapat diterima sebagai cerita 25 Nov karena tanggal publikasinya bersih, tapi jangan jadikan preseden untuk memakai feature lama di ronde berikut.
- Footer "Compiled ~05:30 UTC" jujur dan membantu — pertahankan pengakuan seperti ini di ronde berikutnya.
- 3 hero + 8 item abu-abu condong lolos (#7, #14, #15, #17, #18, #19, #28, #30) tidak diverifikasi ulang di ronde ini karena tidak diubah — statusnya dibawa dari r2.
