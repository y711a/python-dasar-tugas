# BAB 04 - Operator
# Berdasarkan materi Python Dasar.pdf

# Operator aritmatika.
print(7 + 3)    # penjumlahan: 10
print(7 - 3)    # pengurangan: 4
print(7 * 3)    # perkalian: 21
print(7 / 3)    # pembagian biasa
print(7 // 3)   # pembagian bulat: 2
print(7 % 3)    # sisa pembagian: 1
print(7 ** 3)   # pangkat: 343
print(2 + 3 * 4 ** 2)  # urutan operasi menghasilkan 50

# Operator perbandingan dan logika.
umur = 20
punya_ktp = True
print(umur >= 17 and punya_ktp)
print(umur < 13 or umur > 60)
print(not punya_ktp)

# Operator penugasan.
skor = 10
skor += 5      # sama dengan skor = skor + 5
skor *= 2      # sama dengan skor = skor * 2
print(skor)

# Operator keanggotaan: in dan not in.
buah = ["apel", "jeruk", "mangga"]
print("apel" in buah)
print("anggur" not in buah)
print("th" in "Python")

# Operator perbandingan: ==, !=, >, <, >=, <=.
