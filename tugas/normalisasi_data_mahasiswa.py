"""
Tugas 4 - Normalisasi Data Mahasiswa
Algoritma dan Pemrograman | Pertemuan 10

Nama  : Fikri Yustiawan
NIM   : 2225250075
Kelas : 3-E
"""


def normalisasi_nama(nama):
    """Hapus spasi berlebih (awal, akhir, dan antar kata) lalu ubah ke title case."""
    return " ".join(nama.strip().split()).title()


def buat_inisial(nama):
    """Ambil huruf awal setiap kata pada nama yang sudah dinormalisasi."""
    kata = normalisasi_nama(nama).split()
    return "".join(k[0] for k in kata)


def normalisasi_kode(kode):
    """Ubah ke huruf besar, lalu ganti spasi (satu atau lebih) dengan tanda hubung."""
    kata = kode.strip().upper().split()
    return "-".join(kata)


def hitung_kata(nama):
    """Hitung jumlah kata pada nama lengkap."""
    return len(normalisasi_nama(nama).split())


def main():
    nama = input("Nama: ")
    kode = input("Kode kelas: ")

    nama_bersih = normalisasi_nama(nama)
    kode_bersih = normalisasi_kode(kode)
    jumlah_kata = hitung_kata(nama)
    inisial = buat_inisial(nama)

    print(f"Nama bersih : {nama_bersih}")
    print(f"Kode kelas  : {kode_bersih}")
    print(f"Jumlah kata : {jumlah_kata}")
    print(f"Inisial     : {inisial}")


if __name__ == "__main__":
    main()
