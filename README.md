# Pertemuan 10 - String dan Pengolahan Teks

Nama: Fikri Yustiawan
NIM: 2225250075
Kelas: 3-E

Mata Kuliah: Algoritma dan Pemrograman
Program Studi: S1 Pendidikan Matematika FKIP Universitas Sultan Ageng Tirtayasa
Dosen Pengampu: Dr. Aan Hendrayana, S.Si., M.Pd.
Tahun Ajaran: 2026/2027 Ganjil

## Tujuan

Mengolah dan menormalisasi data teks dengan string Python: akses karakter, slicing, pencarian, pembersihan, pemisahan, penggabungan, dan transformasi teks, lalu menerapkannya pada data nama mahasiswa dan kode kelas.

## Struktur Repositori

```
pertemuan-10-string-2225250075/
|-- README.md
|-- .gitignore
|-- latihan/
|   |-- 01_dasar_string.py
|   |-- 02_indeks_slicing.py
|   |-- 03_method_string.py
|   |-- 04_bersihkan_teks.py
|   |-- 05_split_join.py
|   `-- 06_pencarian_kata.py
`-- tugas/
    `-- normalisasi_data_mahasiswa.py
```

## Cara Menjalankan

Latihan (jalankan satu per satu dari folder utama repositori):

```bash
python3 latihan/01_dasar_string.py
python3 latihan/02_indeks_slicing.py
python3 latihan/03_method_string.py
python3 latihan/04_bersihkan_teks.py
python3 latihan/05_split_join.py
python3 latihan/06_pencarian_kata.py
```

Tugas 4:

```bash
python3 tugas/normalisasi_data_mahasiswa.py
```

Program akan meminta dua input: `Nama` dan `Kode kelas`. Di VS Code, program juga bisa dijalankan lewat Run Python File.

## Algoritma

Tugas 4 memakai empat fungsi. Prosesnya:

1. Baca nama dan kode kelas sebagai string dengan `input()`.
2. `normalisasi_nama`: `strip()` menghapus spasi di awal dan akhir, `split()` memecah nama menjadi list kata (spasi berlebih di tengah hilang), `join()` menggabungkannya lagi dengan satu spasi, lalu `title()` membuat huruf awal tiap kata kapital.
3. `hitung_kata`: pecah nama yang sudah bersih dengan `split()` lalu hitung panjang list dengan `len()`.
4. `buat_inisial`: ambil karakter indeks 0 dari setiap kata pada nama bersih, lalu gabungkan.
5. `normalisasi_kode`: `strip()` dan `upper()` untuk huruf besar, `split()` memecah berdasarkan spasi, lalu `"-".join()` mengganti spasi dengan tanda hubung.
6. Tampilkan keempat hasil dengan f-string agar rapi.

## Test Case

Semua test case dijalankan langsung pada `tugas/normalisasi_data_mahasiswa.py`.

| No | Input Nama | Input Kode | Hasil yang Diharapkan | Hasil Aktual | Status |
|----|-----------|-----------|----------------------|--------------|--------|
| 1 | ` aan hendrayana` | `pmat a 2026` | Aan Hendrayana, PMAT-A-2026, 2 kata, AH | Aan Hendrayana, PMAT-A-2026, 2 kata, AH | Lulus |
| 2 | `fATHIYYAH mUTHMAINNAH` | `kelas b` | Fathiyyah Muthmainnah, KELAS-B, 2 kata, FM | Fathiyyah Muthmainnah, KELAS-B, 2 kata, FM | Lulus |
| 3 | `BUDI` | `pmtk 01` | Budi, PMTK-01, 1 kata, B | Budi, PMTK-01, 1 kata, B | Lulus |
| 4 | ` siti nur aisyah` | `kelas c` | Siti Nur Aisyah, KELAS-C, 3 kata, SNA | Siti Nur Aisyah, KELAS-C, 3 kata, SNA | Lulus |

Contoh keluaran (test case 1):

```
Nama: aan hendrayana
Kode kelas: pmat a 2026
Nama bersih : Aan Hendrayana
Kode kelas  : PMAT-A-2026
Jumlah kata : 2
Inisial     : AH
```

Hasil enam latihan:

| Latihan | Hasil |
|---------|-------|
| 01 Dasar String | `Algoritma`, `9`, `ALGORITMA`, `algoritma` |
| 02 Indeks dan Slicing | `P`, `n`, `Pemr`, `ograman`, `namargormeP` |
| 03 Method String | `fATHIYYAH mUTHMAINNAH`, `Fathiyyah Muthmainnah`, `FATHIYYAH MUTHMAINNAH` |
| 04 Bersihkan Teks | `Belajar python untuk pendidikan` |
| 05 split dan join | `['data', 'teks', 'perlu', 'dibersihkan']`, `data-teks-perlu-dibersihkan` |
| 06 Pencarian Kata | `True`, `2`, `0` |

## Refleksi

Masalah teks yang saya temukan adalah nama dengan spasi berlebih dan kapitalisasi acak, misalnya `" siti   nur aisyah"`. Kalau hanya memakai `strip()` dan `title()`, spasi ganda di tengah nama tetap ada, karena `strip()` hanya menghapus spasi di awal dan akhir. Perbaikannya adalah `split()` lalu `join()` dengan satu spasi, jadi spasi berlebih di mana pun ikut hilang. Cara yang sama saya pakai untuk kode kelas, dengan tanda hubung sebagai penggabungnya.

## Exit Ticket

- Operasi string yang paling berguna hari ini adalah `split()` dan `join()` karena keduanya bisa memecah teks menjadi kata lalu menyusunnya kembali dengan format yang saya mau, termasuk membuang spasi berlebih di tengah teks.
- Kesalahan pengolahan teks yang paling mungkin saya lakukan adalah mengira `strip()` menghapus semua spasi, padahal hanya di awal dan akhir, serta lupa menyimpan hasil method ke variabel karena string bersifat immutable. Selain itu, memakai `find()` tanpa mengecek hasil `-1`, atau mengakses `nama[0]` pada string kosong sehingga terjadi `IndexError`.
- Hubungan list dan string yang saya pahami adalah keduanya urutan yang punya indeks, bisa di-slicing, bisa ditelusuri dengan `for`, dan punya `len()`. Bedanya, elemen string berupa karakter dan string tidak bisa diubah per indeks, sedangkan list bisa.
- Konsep Pertemuan 10 yang akan membantu Pertemuan 11 adalah memecah teks menjadi kata dengan `split()` dan menormalisasinya dengan `lower()`. Kata-kata itu nanti bisa dihitung dan disimpan sebagai pasangan key-value pada dictionary, misalnya untuk frekuensi kata.

## Sumber dan Bantuan

- Bahan Ajar Pertemuan 10 (Dr. Aan Hendrayana, S.Si., M.Pd.) sebagai acuan latihan, spesifikasi, dan test case.
- Python 3 Documentation: Text Sequence Type (`str`).
- Bantuan AI dipakai untuk menyusun kerangka kode dan draf README. Kode dan test case sudah saya jalankan serta pelajari, dan saya dapat menjelaskan alasan pemilihan operasi string pada setiap fungsi.
