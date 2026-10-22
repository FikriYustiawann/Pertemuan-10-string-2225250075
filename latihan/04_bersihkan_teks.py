# Latihan 4 - Membersihkan Teks
teks = "  belajar   python  untuk   pendidikan  "
teks = teks.strip()
while "  " in teks:
    teks = teks.replace("  ", " ")
print(teks.capitalize())
