# BAB 08 - Function
# Berdasarkan materi Python Dasar.pdf

# def mendefinisikan function; parameter menerima input.
def hitung_luas(panjang, lebar):
    """Menghitung luas persegi panjang."""
    luas = panjang * lebar
    return luas  # mengembalikan hasil kepada pemanggil

hasil = hitung_luas(5, 3)
print(hasil)
print(hitung_luas(10, 2))

# Parameter default dan keyword argument.
def sapa(nama, salam="Halo"):
    return f"{salam}, {nama}!"

print(sapa("Ani"))
print(sapa(salam="Hai", nama="Budi"))

# *args menerima sejumlah argumen posisi sebagai tuple.
def total(*angka):
    return sum(angka)

print(total(1, 2, 3, 4))

# **kwargs dapat menerima banyak argumen berbentuk key=value sebagai dictionary.
def tampilkan_info(**kwargs):
    print(kwargs)

tampilkan_info(nama="Ani", umur=20)

# Lambda: function anonim satu baris.
kuadrat = lambda x: x ** 2
print(kuadrat(4))

siswa = [("Ani", 80), ("Budi", 95)]
print(max(siswa, key=lambda s: s[1]))

# Scope: variabel lokal dan global.
x = "global"
def tes():
    x = "lokal"
    print(x)

tes()
print(x)
