# Sistem Analisis Prediktif dan Pemetaan Sebaran Risiko Stunting
**Proyek Akhir Mata Kuliah IFB-451 Big Data (Health Informatics Focus)**

Dokumen ini berisi rancangan alur pengerjaan proyek akhir sistem pengolahan data skala besar untuk analisis dan pemetaan risiko stunting, disusun secara runtut mengikuti 14 modul pembelajaran dalam silabus perkuliahan.

---

## 📋 Daftar Isi
- [Tentang Proyek](#tentang-proyek)
- [Arsitektur & Alur Pengerjaan](#arsitektur--alur-pengerjaan)
  - [Fase 1: Fondasi & Perencanaan Arsitektur](#fase-1-fondasi--perencanaan-arsitektur-modul-1--2)
  - [Fase 2: Penyimpanan & Pengelolaan Data](#fase-2-penyimpanan--pengelolaan-data-modul-3-4--5)
  - [Fase 3: Pemrosesan Lanjutan & Real-Time Streaming](#fase-3-pemrosesan-lanjutan--real-time-streaming-modul-6-7--8)
  - [Fase 4: Penyimpanan NoSQL & Infrastruktur Cloud](#fase-4-penyimpanan-nosql--infrastruktur-cloud-modul-9--10)
  - [Fase 5: Penerapan Machine Learning Big Data](#fase-5-penerapan-machine-learning-big-data-modul-11--12)
  - [Fase 6: Visualisasi & Pengembangan Website Dashboard](#fase-6-visualisasi--pengembangan-website-dashboard-modul-13)
  - [Fase 7: Etika, Privasi, & Tata Kelola Data](#fase-7-etika-privasi--tata-kelola-data-modul-14)
- [Kontribusi & Lisensi](#kontribusi--lisensi)

---

## 🎯 Tentang Proyek
Proyek akhir ini bertujuan untuk membangun sebuah sistem end-to-end berbasis *Big Data* dalam domain informatika kesehatan (*Health Informatics*). Sistem ini dirancang untuk mengolah data kesehatan balita dalam skala besar, memprediksi tingkat risiko stunting secara individu, serta memetakan zona prioritas penanganan secara geospasial untuk membantu pengambilan kebijakan intervensi gizi.

---

## 🛠️ Arsitektur & Alur Pengerjaan

### Fase 1: Fondasi & Perencanaan Arsitektur (Modul 1 & 2)
* **Tujuan:** Memahami karakteristik data dan merancang arsitektur sistem pengolahan data skala besar.
* **Langkah Kerja:**
  * **Definisi 5Vs Data Stunting:** Mengidentifikasi karakteristik data (*Volume* jutaan data balita, *Velocity* pembaruan laporan bulanan Posyandu, *Variety* data terstruktur antropometri dan semi-terstruktur laporan elektronik, *Veracity* validasi data gizi, *Value* untuk intervensi kebijakan).
  * **Perancangan Arsitektur:** Menerapkan *Lambda/Kappa Architecture* untuk mengakomodasi data historis (batch) dan pembaruan data berkala dari fasilitas kesehatan.
  * **Studi Pustaka & Rujukan:** Menentukan dataset publik (misalnya data kesehatan anak/SSGI dari Kaggle atau data.gov.id) atau merancang parameter simulasi berdasarkan acuan jurnal kesehatan resmi.

### Fase 2: Penyimpanan & Pengelolaan Data (Modul 3, 4 & 5)
* **Tujuan:** Menyimpan dan melakukan pemrosesan awal (*ETL*) pada dataset besar.
* **Langkah Kerja:**
  * **Penyimpanan Terdistribusi:** Mengunggah dan mengelola dataset ke dalam lingkungan Hadoop HDFS atau penyimpanan cloud.
  * **Optimasi Format Data:** Mengonversi data mentah (CSV) ke format kolom terkompresi Apache Parquet agar kueri analitik berjalan jauh lebih efisien dan cepat.
  * **Pemrosesan Awal (ETL):** Menggunakan skrip MapReduce atau Hive untuk membersihkan data, menyaring nilai kosong, dan menggabungkan (*join*) data anak dengan data sosio-ekonomi atau sanitasi wilayah.

### Fase 3: Pemrosesan Lanjutan & Real-Time Streaming (Modul 6, 7 & 8)
* **Tujuan:** Melakukan komputasi terdistribusi yang cepat dan simulasi aliran data langsung.
* **Langkah Kerja:**
  * **Apache Spark & Spark SQL:** Memanfaatkan PySpark DataFrames dan Spark SQL untuk melakukan agregasi data (misalnya menghitung rata-rata tingkat stunting berdasarkan kecamatan dan variabel pendapatan orang tua).
  * **Spark Structured Streaming:** Mensimulasikan aliran data masuk (*stream*) dari laporan harian Posyandu untuk memantau perubahan atau lonjakan kasus secara dinamis.

### Fase 4: Penyimpanan NoSQL & Infrastruktur Cloud (Modul 9 & 10)
* **Tujuan:** Menangani data semi-terstruktur dan memanfaatkan skalabilitas komputasi awan.
* **Langkah Kerja:**
  * **NoSQL (MongoDB/Cassandra):** Menyimpan profil anak atau catatan intervensi gizi yang memiliki struktur fleksibel (dokumen JSON). Menghubungkan database NoSQL ini dengan Apache Spark menggunakan konektor khusus.
  * **Cloud Platform:** Menguji dan menjalankan alur pemrosesan data menggunakan layanan cloud (seperti Google Cloud BigQuery/Dataproc atau AWS S3/EMR).

### Fase 5: Penerapan Machine Learning Big Data (Modul 11 & 12)
* **Tujuan:** Membangun model prediktif dan analitik tingkat lanjut berbasis data berskala besar.
* **Langkah Kerja:**
  * **Spark MLlib (Klasifikasi & Clustering):**
    * Menggunakan *Logistic Regression* atau *Decision Tree* untuk memprediksi tingkat risiko stunting pada balita berdasarkan variabel berat/tinggi badan, usia, dan kondisi lingkungan.
    * Menggunakan *K-Means Clustering* untuk mengelompokkan wilayah (*clustering* kecamatan/desa) ke dalam zona prioritas penanganan (merah, kuning, hijau).
  * **Evaluasi Model:** Menguji performa model menggunakan metrik seperti *Accuracy, Precision, Recall*, dan *ROC-AUC*.

### Fase 6: Visualisasi & Pengembangan Website Dashboard (Modul 13)
* **Tujuan:** Menyajikan hasil analisis Big Data ke dalam aplikasi web interaktif yang mudah digunakan oleh tenaga kesehatan atau pengambil kebijakan.
* **Langkah Kerja:**
  * **Pengembangan Backend & Frontend Website:** Membangun antarmuka web menggunakan framework (seperti Flask, Streamlit, atau React) yang terhubung ke basis data dan model hasil pemrosesan Big Data.
  * **Fitur Utama Dashboard:**
    * *Peta Sebaran Geospasial (Heatmap):* Menampilkan peta wilayah dengan titik-titik daerah berisiko tinggi stunting.
    * *Kalkulator / Fitur Prediksi:* Halaman interaktif bagi tenaga medis untuk memasukkan parameter fisik anak dan melihat estimasi risiko stunting secara instan.
    * *Grafik Tren & Demografi:* Menampilkan visualisasi interaktif (menggunakan Plotly/Grafana) terkait tren gizi anak dari waktu ke waktu.

### Fase 7: Etika, Privasi, & Tata Kelola Data (Modul 14)
* **Tujuan:** Memastikan proyek mematuhi standar etika dan regulasi perlindungan data pribadi.
* **Langkah Kerja:**
  * **Anonimisasi Data:** Menerapkan teknik *pseudonymization* (misalnya menggunakan UUID atau menghapus identitas personal seperti NIK dan nama asli anak) pada dataset kesehatan.
  * **Kepatuhan Hukum:** Memastikan tata kelola data selaras dengan regulasi privasi seperti UU Perlindungan Data Pribadi (UU PDP) di Indonesia dan standar etika penggunaan data kesehatan (*Health Data Governance*).

---

## 👥 Kontribusi
Proyek ini dikembangkan sebagai bagian dari studi kasus mata kuliah Big Data (Health Informatics Focus). Silakan buat *pull request* atau buka *issue* jika ada saran pengembangan maupun perbaikan alur kerja.

