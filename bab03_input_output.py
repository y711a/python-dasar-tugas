# BAB 03 - Input & Output
# Berdasarkan materi Python Dasar.pdf

# print() dapat menerima beberapa nilai sekaligus.
print("Halo", "Dunia")
print("A", "B", "C", sep="-")

# end mengubah akhiran print (default-nya baris baru).
print("Loading", end="...")
print("selesai")

harga = 15000 / 7
print(f"Harga: Rp{harga:.2f}")   # 2 angka di belakang desimal
print(f"Total: {1500000:,}")     # pemisah ribuan

# input() selalu menghasilkan string, jadi konversi input angka.
nama = input("Siapa namamu? ")
umur = int(input("Berapa umurmu? "))

tahun_depan = umur + 1
print(f"Halo {nama}!")
print(f"Tahun depan kamu {tahun_depan} tahun")
