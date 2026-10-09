# BAB 09 - Error Handling
# Berdasarkan materi Python Dasar.pdf

# Contoh jenis error (disimpan sebagai komentar agar program tetap berjalan):
# SyntaxError: penulisan kode tidak sesuai aturan.
# IndentationError: indentasi blok tidak konsisten.
# NameError: variabel belum pernah dibuat.
# TypeError: operasi pada tipe data yang salah, misalnya "5" + 3.
# ValueError: nilai tidak valid, misalnya int("abc").
# ZeroDivisionError: pembagian dengan nol, misalnya 10 / 0.
# IndexError: indeks di luar list, misalnya [1, 2][5].
# KeyError: key tidak ada, misalnya {"a": 1}["b"].

# try-except-else-finally.
try:
    angka = int(input("Masukkan angka: "))
    hasil = 100 / angka
except ValueError:
    print("Harus berupa angka!")
except ZeroDivisionError:
    print("Tidak bisa dibagi nol!")
else:
    print(f"Hasil: {hasil}")
finally:
    print("Selesai.")

# raise digunakan untuk memunculkan error secara sengaja.
def set_umur(umur):
    if umur < 0:
        raise ValueError("Umur tidak valid")
    return umur

try:
    set_umur(-5)
except ValueError as e:
    print(f"Error: {e}")
