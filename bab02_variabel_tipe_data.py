# BAB 02 - Variabel & Tipe Data
# Berdasarkan materi Python Dasar.pdf

# Variabel dibuat saat pertama kali diberi nilai.
nama = "Budi"       # str: teks
umur = 20           # int: bilangan bulat
tinggi = 170.5      # float: bilangan desimal
aktif = True        # bool: True atau False

# Nilai variabel dapat diperbarui.
umur = umur + 1

# Multiple assignment: memberi nilai ke beberapa variabel sekaligus.
x, y, z = 1, 2, 3
print(nama, umur, x + y + z)

# Memeriksa tipe data.
print(type(10))
print(type(3.14))
print(type("A"))
print(type(True))

# Casting / konversi tipe data.
angka = int("25")
print(angka + 5)

harga = float("12500.75")
print(type(harga))
print("Umur: " + str(umur))
print(bool(0), bool("hai"))

# Bekerja dengan string.
nama_program = "Python Dasar"
print(len(nama_program))
print(nama_program.upper())
print(nama_program[0:6])
print(nama_program.split(" "))

bab = 2
print(f"Belajar {nama_program} bab {bab}")

# Contoh nama variabel yang valid: nama_siswa, _total
# Nama tidak boleh diawali angka, mengandung spasi, atau memakai keyword.
