# Desain Arsitektur Big Data: Sistem Analisis Risiko Stunting

## 1. Komponen Ekosistem yang Digunakan
* **Storage Layer:** Menggunakan sistem penyimpanan file terdistribusi (HDFS / Cloud Storage) untuk menampung data mentah antropometri balita (~1.8 GB)[cite: 22, 29].
* **Processing Engine:** Menggunakan **Apache Spark** untuk pemrosesan data skala besar secara in-memory[cite: 22, 41].
* **Ingestion:** Menggunakan skrip batch untuk menyerap data laporan bulanan dari fasilitas kesehatan.

## 2. Pemilihan Pola Arsitektur (*Architectural Pattern*)
* **Batch Architecture:** Dipilih untuk pemrosesan data historis bulanan secara periodik (rekapitulasi data stunting kabupaten/provinsi)[cite: 22].
* **Hybrid/Lambda Consideration:** Memadukan *Batch Layer* untuk analisis tren jangka panjang dan persiapan *Speed Layer* untuk pemantauan data secara real-time di masa mendatang[cite: 22, 26].