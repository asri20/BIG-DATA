#!/usr/bin/env python3
"""
MapReduce Reducer: Agregasi Jumlah Wilayah per Kategori Risiko Stunting
Mata Kuliah: IFB-451 Big Data (Modul 4 - Hadoop Ecosystem)

Alur Kerja Reducer:
1. Membaca stream pasangan (Key, Value) dari sys.stdin yang telah di-shuffle dan di-sort oleh Hadoop.
2. Mengagregasi (menjumlahkan) frekuensi nilai untuk setiap Key unik.
3. Menampilkan hasil rekapitulasi akhir (Key, Total_Count).
"""

import sys
from collections import defaultdict

def main():
    counts = defaultdict(int)
    
    # Membaca input dari STDIN (keluaran dari Mapper / Hadoop Shuffle)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        try:
            word, count = line.split("\t")
            counts[word] += int(count)
        except ValueError:
            # Mengabaikan baris yang tidak sesuai format Key\tValue
            continue
    
    # Menampilkan hasil agregasi terdistribusi
    print("==================================================")
    print("HASIL AGREGASI MAPREDUCE: DISTRIBUSI RISIKO STUNTING 2023")
    print("==================================================")
    for word, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}\t: {count} Provinsi")
    print("==================================================")

if __name__ == "__main__":
    main()
