# BAB 06 - Perulangan
# Berdasarkan materi Python Dasar.pdf

# for dan range(): batas akhir range tidak ikut.
for i in range(1, 4):
    print(f"Putaran ke-{i}")

buah = ["apel", "jeruk", "mangga"]
for b in buah:
    print(b.upper())

# range(0, 10, 2) menghasilkan 0, 2, 4, 6, 8.
for angka in range(0, 10, 2):
    print(angka)

# while mengulang selama kondisi bernilai True.
hitung = 3
while hitung > 0:
    print(f"Hitung mundur: {hitung}")
    hitung -= 1
print("Meluncur!")

# break menghentikan loop; continue melewati sisa putaran.
for n in range(1, 10):
    if n == 3:
        continue  # lewati angka 3
    if n == 6:
        break     # berhenti saat n bernilai 6
    print(n)

# pass adalah placeholder dan tidak melakukan apa-apa.
for i in range(3):
    pass  # TODO: isi nanti
