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
