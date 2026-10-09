# BAB 11 - Pengolahan Data Sederhana
# Berdasarkan materi Python Dasar.pdf
# File nilai.csv akan dibuat jika belum tersedia.

import csv
from pathlib import Path

csv_path = Path(__file__).with_name("nilai.csv")

# Contoh data pada slide.
if not csv_path.exists():
    rows = [
        {"nama": "Ani", "kelas": "A", "nilai": 85},
        {"nama": "Budi", "kelas": "B", "nilai": 72},
        {"nama": "Citra", "kelas": "A", "nilai": 93},
        {"nama": "Dodi", "kelas": "B", "nilai": 64},
        {"nama": "Eka", "kelas": "A", "nilai": 78},
    ]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["nama", "kelas", "nilai"])
        writer.writeheader()
        writer.writerows(rows)

# Membaca CSV dengan csv.DictReader.
data = []
with open(csv_path, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for baris in reader:
        baris["nilai"] = int(baris["nilai"])  # isi CSV awalnya berupa teks
        data.append(baris)

print(len(data), "baris")
print(data[0])

# List comprehension, rata-rata, filter, dan nilai tertinggi.
nilai = [d["nilai"] for d in data]
rata = sum(nilai) / len(nilai)
print(f"Rata-rata: {rata:.1f}")

lulus = [d["nama"] for d in data if d["nilai"] >= 75]
print("Lulus:", lulus)

top = max(data, key=lambda d: d["nilai"])
print("Tertinggi:", top["nama"])

# Rekap rata-rata berdasarkan kelas.
rekap = {}
for d in data:
    k = d["kelas"]
    rekap.setdefault(k, []).append(d["nilai"])

print(f"{'Kelas':<6}{'Jumlah':>8}{'Rata':>8}")
for k, v in sorted(rekap.items()):
    rata_kelas = sum(v) / len(v)
    print(f"{k:<6}{len(v):>8}{rata_kelas:>8.1f}")

# Contoh pandas pada slide. Pasang dahulu dengan: python -m pip install pandas
# Jalankan bagian ini setelah pandas tersedia.
try:
    import pandas as pd
except ImportError:
    print("pandas belum terpasang; bagian pandas dilewati.")
else:
    df = pd.read_csv(csv_path)
    print(df.groupby("kelas")["nilai"].mean())
    print(df[df["nilai"] >= 75]["nama"].tolist())
    print(df.sort_values("nilai").tail(1))
