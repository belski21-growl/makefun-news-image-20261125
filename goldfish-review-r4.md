# GOLDFISH REVIEW — MICRO RE-REVIEW v4 (round 4)
## news-image-20261125 — "The World in One Day"

- **Reviewer:** Goldfish (penilai independen — bukan builder, bukan fixer)
- **Tanggal review:** 25 November 2026 (~13:20 WIB / ~06:20 UTC)
- **Entry dinilai:** `entry.png` v4 — sha256 `4edbd9944d3a228978d479f762b8c0c4c55667575fd5311fa9d51e703c5c64ed`, 272.076 byte, 1024×1024 JPEG
- **Entry v3 (pembanding):** sha256 `df4a30ca10053c6005b37b0c2a82dbddd0d1699f2f7f50f8f857df5fab136f6c`, 276.540 byte
- **Kompetisi:** news-image-20261125 — $100, 50 tempat, juara 1 $20; deadline 27 Nov 2026 07:00 WIB; juri z-ai/glm-5.3-flash

## Metode
- Membaca langsung `entry.png` v4: full + 4 crop-zoom 2× (`/tmp/gf4/`: secondary panels, ALSO ON + numbers strip, map + footer DATE CHECK, masthead + region bar) — semua area yang diubah + spot-check tetangga yang lolos.
- Membaca penuh `build-log.md` (bagian v4: 5 pengganti + outlet primer + stempel UTC + URL + daftar ditolak + validasi 2×), `goldfish-review-r3.md`, dan `top10-analysis.md` (catatan v4).
- Verifikasi faktual independen: **5 buka langsung artikel primer** (kelima URL Yonhap pengganti — dibaca penuh, bukan cuplikan) + **1 kueri web spot-check** (#6 Houthis, abu-abu condong lolos dari r3). Total 6 aksi verifikasi.
- Standar tanggal yang dipakai: tanggal **insiden/peristiwa dan laporan pertama dari sumber primer** (artikel langsung outlet yang pertama kali memberitakan), bukan tanggal halaman live-blog, bukan stempel agregator/wire re-post. Standar yang sama dengan review v1/r2/r3.
- File entry TIDAK diubah, TIDAK disubmit, TIDAK dibuat repo.

## Status blocker & major v3
| Item v3 | Status v4 | Bukti |
|---|---|---|
| **B1 — DATE CHECK salah (3 gagal + 1 abu-abu condong gagal dari 34)** | **TERTUTUP** | Kelima item bermasalah diganti dan **semuanya LOLOS** dari artikel primer yang dibuka langsung (lihat tabel bawah). Tidak ada lagi cerita GAGAL tanggal terkonfirmasi di antara 34 cerita. Klaim footer "EVERY STORY ABOVE WAS FIRST REPORTED WEDNESDAY 25 NOVEMBER 2026" kini benar sejauh yang terverifikasi (25 LOLOS bersih + 9 abu-abu condong lolos, 0 gagal). |
| **B2 — Deck hero 1 baris 2 GARBLED total** | **TERTUTUP** (tetap) | Tidak diubah di v4; tetap bersih seperti r3. |
| **B3 — Peta hero 2 = Amerika Utara** | **TERTUTUP** (tetap) | Tidak diubah di v4; tetap peta Pasifik yang benar. |
| **M1 — Breadth hanya 14 cerita** | **TERTUTUP** (tetap) | 34 cerita, dihitung dari gambar. |
| **M2 — Build-log klaim cerita yang TIDAK ada di gambar** | **TERTUTUP** (tetap) | Build-log v4 ditulis dari gambar final; 5 pengganti ada di gambar dengan nomor yang sama. |
| **M3 — Tanpa strip peta dunia; region bar tanpa hitungan; timeline tanpa jam; hero tanpa source line/badge** | **TERTUTUP** (tetap) | Strip "WHERE IT HAPPENED" + pin bernomor + legenda tetap ada; pin 11 kini SEOUL (terpisah jelas dari pin 9-10 di crop 2×); timeline 5 waktu tetap; region bar ADA hitungan dan rekonsiliasi 25+4+4+1=34 (lihat bawah). |
| **M4 — Numbers strip terkontaminasi** | **TERTUTUP** (tetap) | Strip tidak disentuh v4: 4,9% · 68 · 101 · 25,113 · 2,212 — semua sudah terverifikasi bersih di r3. |
| **M5 — #31 duplikat tema #22 (dua jepretan KOSPI)** | **TERTUTUP** | #31 kini "Hyundai Mobis wins $742M in parts orders" — pesanan suku cadang otomotif, tema berbeda dari #22 "KOSPI opens sharply lower". Satu slot tidak lagi terbuang. |

## VERDICT: LAYAK SUBMIT

**Tidak ada lagi blocker.** B1 — satu-satunya blocker yang tersisa sejak v1 — tertutup: kelima pengganti terverifikasi bersih tanggal dari artikel primer yang saya buka langsung, bukan dari stempel agregator. Kerajinan setara pola pemenang ni24 (masthead serif raksasa + tanggal penuh, region bar berhitungan, timeline berwaktu, THE DAY IN NUMBERS, 3 hero bergambar + badge, 10 sekunder bergambar, ALSO ON bernomor, peta dunia + pin, DATE CHECK jujur dengan daftar eksklusi + pengakuan jam kompilasi). Satu major tersisa (M6, konsentrasi Korea — lihat bawah) dicatat jujur, tapi itu trade-off yang disengaja demi kebersihan tanggal dan BUKAN blocker: tanggal bersih adalah syarat yang juri periksa duluan, dan stok cerita 25 Nov bersih non-Korea sudah terbukti tipis (v3: hanya 4 bersih dari ~20 kandidat yang diverifikasi).

## Tabel verifikasi kelima pengganti
Standar: LOLOS = terjadi / pertama dilaporkan 25 Nov 2026 dari sumber primer (artikel langsung). GAGAL = laporan pertama 24 Nov atau lebih awal. ABU-ABU = tidak bisa diputus tuntas.

| # | Pengganti (sesuai gambar) | Verdict | Bukti singkat + sumber |
|---|---|---|---|
| #11 | Lee vows domestic-violence law fix | **LOLOS** | Artikel Yonhap dibuka langsung: "SEOUL, Nov. 25 (Yonhap) — President Lee Jae Myung said Wednesday that his government will seek to revise the law to enable punishment for perpetrators of domestic violence even when their victims fail or refuse to file a complaint." Post X Lee untuk International Day for the Elimination of Violence against Women — 25 Nov. Foto ilustrasi rapat kabinet 24 Nov hanya foto, bukan isi berita. Deck gambar ("Victims need not file a complaint for abusers to face charges.") cocok dengan isi. |
| #26 | Korea mortgage rates hit 14-year high | **LOLOS** | Artikel Yonhap dibuka langsung: "SEOUL, Nov. 25 (Yonhap) — Banks' household mortgage loan rates rose ... to the highest point in 14 years and seven months in October on rising market interest, central bank data showed Wednesday." Stempel terbit: **2026-11-25T13:54:15+09:00** (= 04:54 UTC). Angka gambar cocok: mortgage 4,98%, new bank loans 4,64%, household loans 5,02% (pertama di atas 5% sejak Nov 2023). Data Oktober DIRILIS 25 Nov — pola yang sama dengan #16 yang dipertahankan (data September dirilis 25 Nov). BUKAN analisis susulan atas data lama (beda dengan #26 v3 yang datanya dirilis 12 Nov). |
| #27 | Seoul weighs tech to stop AI exam cheating | **LOLOS** | Artikel Yonhap dibuka langsung: "SEOUL, Nov. 25 (Yonhap) — The government is reviewing various technologies to prevent cheating using artificial intelligence (AI) ... the science minister said Wednesday." Foto event: "Science Minister Bae Kyung-hoon speaks at an AI strategy meeting in Seoul on Nov. 25, 2026." Jamming, watermark, CCTV behaviour recognition — semua ada di artikel. |
| #33 | FM Cho urges strategic aid at KOICA | **LOLOS** | Artikel Yonhap dibuka langsung: "SEOUL, Nov. 25 (Yonhap) — Foreign Minister Cho Hyun on Wednesday called on the new head of the Korea International Cooperation Agency (KOICA) to pursue strategic, demand-driven grant aid programs." Upacara penyerahan surat pengangkatan Rabu; foto: "in Seoul on Nov. 25, 2026." |
| #31 | Hyundai Mobis wins $742M in parts orders | **LOLOS tanggal + duplikat TERTUTUP** | Artikel Yonhap dibuka langsung: "SEOUL, Nov. 25 (Yonhap) — Hyundai Mobis Co. said Wednesday it has secured auto parts orders worth about 1 trillion won (US$742.3 million) from major automakers in Europe and North America so far in the fourth quarter." iMEB brakes + EPS steering, pabrik Slovakia + Amerika Utara — semua cocok. Tema suku cadang otomotif, BUKAN pergerakan pasar — duplikasi dengan #22 tertutup. |

**Rekap hitungan v4 (34 cerita):** LOLOS bersih 25 (3 hero + #4, #5, #9, #10, #12, #13, #20, #21, #22, #24, #29, #32 + pengganti #8, #16, #23, #25, #34 + 5 pengganti v4) · ABU-ABU condong LOLOS 9 (#6, #7, #14, #15, #17, #18, #19, #28, #30 — tidak berubah dari r3) · ABU-ABU condong GAGAL 0 · **GAGAL terkonfirmasi 0**. Yang bisa dipertahankan: **34 dari 34**.

### Spot-check #6 (abu-abu condong lolos dari r3 — diverifikasi ulang)
- Kueri web independen: Reuters wire "Nov 25 (Reuters) — Yemen's Houthis said on Wednesday the Saudi Arabian port of Jeddah and all other Saudi ports on the Red Sea coast would be targeted..." + analisis House of Saud: "On November 25, Houthi armed forces spokesman Yahya Saree extended the target list to every Saudi Red Sea port, posted maps on Telegram marking Yanbu, Jazan, King Fahd Industrial Port, Jeddah port, and Riyadh's King Abdullah Financial District." Perkembangan 25 Nov (perluasan daftar + peta Telegram) nyata — status **tetap ABU-ABU condong LOLOS** (ancaman yang sama pertama dibuat 20 Nov, diperluas 22 Nov; tapi item gambar menyajikan perkembangan Rabu, dan deck-nya "Jeddah and all Saudi Red Sea ports targeted if Hodeidah is hit" cocok dengan kawat Reuters 25 Nov). Bukan blocker.

### Verifikasi region bar
ASIA-PACIFIC 25 · AMERICAS 4 · EUROPE 4 · MIDDLE EAST 1 = **34 — rekonsiliasi benar** dengan isi gambar: APAC 25 (H1, H2, #4, #5, #8, #9, #10, #11, #14, #15, #16, #17, #18, #19, #20, #21, #22, #23, #24, #25, #26, #27, #28, #31, #33), Americas 4 (H3, #7, #13, #30), Europe 4 (#12, #29, #32, #34), Middle East 1 (#6). Afrika + Culture hilang dari bar (benar: #11 Khartoum → Seoul, #33 film lab → KOICA) — kategorinya ikut hilang, bukan salah hitung.

## Penilaian visual
- **Kartu SEC #11:** crop 2× bersih — "LEE VOWS DOMESTIC VIOLENCE LAW FIX" + deck "Victims need not file a complaint for abusers to face charges." + "YONHAP" — tanpa garble, terpotong, atau overlap. Tetangga #10/#12 utuh.
- **ALSO ON #26/#27/#31/#33:** crop 2× bersih — keempat baris terbaca penuh ("Korea mortgage rates hit 14-year high", "Seoul weighs tech to stop AI exam cheating", "Hyundai Mobis wins $742M in parts orders", "FM Cho urges strategic aid at KOICA"), tanpa terpotong atau overlap; tetangga (#24, #25, #28, #29, #30, #32, #34) utuh.
- **Numbers strip:** tidak berubah — 4,9% · 68 · 101 · 25,113 · 2,212, semua terbaca penuh.
- **Peta + legenda:** pin 11 kini di Asia Timur (Seoul), terpisah jelas dari pin 9-10 di crop 2×; legenda "11 SEOUL" cocok. Pin 6 Jeddah tetap di jazirah Arab. Tidak ada pin yang tumpang tindih.
- **Region bar + masthead:** "ASIA-PACIFIC 25 · AMERICAS 4 · EUROPE 4 · MIDDLE EAST 1" + "COMPILED ~05:50 UTC" terbaca penuh; masthead "THE WORLD IN ONE DAY / WEDNESDAY 25 NOVEMBER 2026 · 34 STORIES · ALL FIRST REPORTED TODAY" bersih.
- **DATE CHECK footer:** terbaca penuh sampai tepi bawah — klaim "EVERY STORY ABOVE WAS FIRST REPORTED WEDNESDAY 25 NOVEMBER 2026." + daftar eksklusi yang diperbarui (10 eksklusi baru v4: Guinea clashes 11 Nov, DR Congo Cessna 24 Nov, NATO space vow 23 Nov, Kim Yo-jong Swiss office 24 Nov, BJP–SAD alliance 24 Nov, Zelenskiy Sparta II 24 Nov, SK minister quits 22 Nov, Dutch climate ruling 24 Nov, Lim/Lee split 24 Nov, Eisenkot pact 24 Nov) + "Compiled ~05:50 UTC; later US daytime news not yet in." — jujur dan membantu.

## Major tersisa
- **M6 (baru, bukan blocker) — Konsentrasi Korea / APAC 25 dari 34.** 14 dari 34 cerita bertema Korea (termasuk kelima pengganti v4 yang semuanya Yonhap), dan region bar kini hanya 4 kategori (APAC 25 · AMERICAS 4 · EUROPE 4 · MIDDLE EAST 1) versus 9–10 region pada pemenang ni24. Ini kelemahan breadth yang nyata: juri 2v2 bisa menilai entry ini "koran Korea + dunia" dibanding pemenang yang merata 9–10 region. Tapi ini harga yang dibayar untuk menutup B1 — stok cerita 25 Nov bersih non-Korea terbukti tipis (v3: 4 bersih dari ~20 kandidat; v4: 10 cerita ditolak karena pertama dilaporkan 24 Nov atau lebih awal). Menukar cerita Korea yang bersih tanggal dengan cerita non-Korea yang abu-abu tanggal akan membuka lagi B1 yang baru saja tertutup — pertukaran yang buruk. Diterima sebagai major yang tercatat, bukan blocker.

## Estimasi jujur (chase-top-10)
- **Estimasi rank: ~50–150 dari ~9.000+ entri.**
- **Peluang top-50: ~35–45%. Peluang top-10: ~5%.**
- **Alasan:** sesuai proyeksi Goldfish-r2/r3 untuk entry bertanggal bersih (bila 11/11 pengganti bersih → rank 50–150, top-50 ~35–45%) — kini tercapai: 0 gagal tanggal, kerajinan setara pola pemenang (34 cerita, 3 hero bergambar + badge, 10 sekunder bergambar, ALSO ON bernomor, peta + pin, DATE CHECK jujur). Yang menahan estimasi di bawah top-10 adalah M6 (konsentrasi Korea/APAC) + 9 item abu-abu condong lolos (bukan gagal, tapi rapuh bila juri memeriksa ketat — terutama #6 dan #7 yang bergantung pada tanggal pengumuman, bukan tanggal peristiwa) + kompilasi dini ~05:50 UTC (berita siang/malam 25 Nov waktu AS belum masuk). Estimasi ini TIDAK digelembungkan: cutoff ni24 ronde 1 (rank 50 = 654.221) menunjukkan garis hadiah menuntut skor tinggi, dan entry ini masih membawa 9 item yang hanya condong lolos. Tapi lantai chase-top-10 terpenuhi (top-50 ≥30%) dan target rank 50–150 berada dalam zona hadiah.

## Catatan kecil (bukan blocker/major)
- Hero 3 menulis "~9.500 lbs" sementara laporan menyebut ~9.700 lbs — masih dalam rentang yang dilaporkan dan ada kualifikasi "about"; diterima (sama seperti r2/r3).
- #13 "Top 20 revealed" — Variety mengonfirmasi 19 dari 20 judul + 1 belum terkonfirmasi; framing "Top 20" wajar (sama seperti r3).
- #34 adalah feature BBC, bukan breaking news — dapat diterima sebagai cerita 25 Nov karena tanggal publikasinya bersih (00:34:05Z), tapi jangan jadikan preseden untuk memakai feature lama (sama seperti r3).
- Footer "Compiled ~05:50 UTC" jujur dan membantu — pertahankan pengakuan seperti ini di ronde berikutnya.
- 3 hero + 8 item abu-abu condong lolos (#7, #14, #15, #17, #18, #19, #28, #30) tidak diverifikasi ulang penuh di ronde ini karena tidak diubah — statusnya dibawa dari r2/r3, kecuali #6 yang di-spot-check ulang dan bertahan.
- Micro-fixer melaporkan main.py direvisi dalam 5 pesan asisten (bukan 4 seperti tertulis di satu bagian build-log — selisih pencatatan, bukan cacat entry; parent yang memverifikasi hitungan pesan untuk bundling).
