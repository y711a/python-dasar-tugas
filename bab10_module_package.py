# BAB 10 - Module & Package
# Berdasarkan materi Python Dasar.pdf

import math
from random import randint
import datetime as dt

print(math.sqrt(16))
print(math.pi)
print(randint(1, 6))
print(dt.date.today().year)

# Contoh module sendiri:
# Misalnya file utils/hitung.py berisi:
# def rata_rata(data):
#     return sum(data) / len(data)
#
# Dari file main.py, dapat digunakan dengan:
# from utils.hitung import rata_rata
# nilai = [80, 90, 70]
# print(rata_rata(nilai))
#
# Package adalah folder berisi module; materi memperlihatkan __init__.py.
#
# Perintah terminal untuk membuat virtual environment:
# python -m venv .venv
#
# Aktivasi di Windows PowerShell:
# .venv\\Scripts\\Activate.ps1
#
# Instal paket:
# python -m pip install pandas requests
#
# Simpan dependensi:
# python -m pip freeze > requirements.txt
#
# Instal dependensi dari file:
# python -m pip install -r requirements.txt
