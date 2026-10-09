# BAB 07 - List, Tuple, Set & Dictionary
# Berdasarkan materi Python Dasar.pdf

# LIST: berurutan, dapat diubah, dan boleh memiliki duplikat.
nilai = [80, 65, 90]
nilai.append(75)
nilai.remove(65)
nilai[0] = 85
print(nilai)
print(nilai[-1], len(nilai))
print(sorted(nilai))

# TUPLE: berurutan, tetapi tidak dapat diubah (immutable).
titik = (3, 7)
warna = (255, 128, 0)
x, y = titik  # unpacking
print(f"x={x}, y={y}")
print(warna[0], len(warna))
print(titik.count(3), titik.index(7))
# Baris berikut sengaja tidak dijalankan karena akan menimbulkan TypeError:
# titik[0] = 10

# SET: menyimpan nilai unik; urutan tidak dijamin.
angka = {1, 2, 2, 3, 3, 3}
print(angka)
ipa = {"Ani", "Budi", "Citra"}
ips = {"Budi", "Dodi"}
print(ipa | ips)  # union / gabungan
print(ipa & ips)  # intersection / irisan
print(ipa - ips)  # difference / selisih

# DICTIONARY: pasangan key-value.
siswa = {"nama": "Sari", "umur": 19}
siswa["kota"] = "Bandung"
siswa["umur"] = 20
print(siswa["nama"])
print(siswa.get("hobi", "-"))
for k, v in siswa.items():
    print(f"{k}: {v}")
