#!/usr/bin/env python3
"""
MapReduce Mapper: Analisis Kategori Risiko Stunting Indonesia (Tahun 2023)
Mata Kuliah: IFB-451 Big Data (Modul 4 - Hadoop Ecosystem)

Alur Kerja Mapper:
1. Membaca baris data dari sys.stdin (format: Provinsi,2020,2021,2022,2023).
2. Melewati baris header.
3. Mengklasifikasikan prevalensi stunting tahun 2023 ke dalam kategori risiko:
   - RISIKO_TINGGI  (>= 15.0%)
   - RISIKO_SEDANG  (5.0% - 14.9%)
   - RISIKO_RENDAH  (< 5.0%)
4. Mengeluarkan pasangan (Key, Value) berupa: <Kategori_Risiko>\t1
"""

import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        
        # Melewati header file CSV
        if line.startswith("Provinsi") or line.startswith("provinsi"):
            continue
        
        parts = line.split(",")
        if len(parts) >= 5:
            provinsi = parts[0].strip()
            try:
                # Mengambil nilai prevalensi tahun 2023 (kolom ke-5 / indeks 4)
                val_2023 = float(parts[4].strip())
                
                # Klasifikasi tingkat risiko prevalensi stunting
                if val_2023 >= 15.0:
                    kategori = "RISIKO_TINGGI (>= 15%)"
                elif val_2023 >= 5.0:
                    kategori = "RISIKO_SEDANG (5.0% - 14.9%)"
                else:
                    kategori = "RISIKO_RENDAH (< 5.0%)"
                
                # Emit pasangan Key-Value untuk Hadoop Reducer
                print(f"{kategori}\t1")
            except ValueError:
                # Jika ada data yang tidak bisa dikonversi ke float
                continue
        else:
            # Fallback untuk pengujian text WordCount umum (sesuai modul asli)
            for word in line.split():
                print(f"{word}\t1")

if __name__ == "__main__":
    main()
