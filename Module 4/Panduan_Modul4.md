# Panduan Pengerjaan & Presentasi Modul 4 — Hadoop Ecosystem
**Mata Kuliah:** IFB-451 Big Data — Dr. Edi Nuryatno  
**Topik Proyek Kelompok:** Sistem Analisis Prediktif dan Pemetaan Sebaran Risiko Stunting (Health Informatics Focus)  
**Dataset:** Prevalensi Stunting 38 Provinsi Indonesia (2020 - 2023)

---

## 📋 1. Struktur File yang Telah Disediakan
Seluruh berkas tugas Modul 4 telah disiapkan secara lengkap dan terstruktur rapi:
- 📁 **`data/data_stunting_clean.csv`**: Dataset 38 provinsi hasil standardisasi (memperbaiki format satu baris menjadi tabel bersih dengan pemisah koma dan desimal titik).
- 📜 **`mapper.py`**: Skrip MapReduce Mapper berbasis Python untuk memetakan kategori risiko stunting wilayah tahun 2023 (`RISIKO_TINGGI`, `RISIKO_SEDANG`, `RISIKO_RENDAH`).
- 📜 **`reducer.py`**: Skrip MapReduce Reducer berbasis Python untuk menghitung total provinsi di setiap kategori risiko secara terdistribusi.
- 📜 **`stunting_hive.hql`**: Kueri DDL dan kueri analitik HiveQL resmi untuk pembuatan database, tabel HDFS, agregasi data, klasifikasi status zona, dan konversi ke Apache Parquet.
- 📓 **`module4.ipynb`**: Jupyter Notebook interaktif yang menggabungkan seluruh pipeline: teori, data cleaning, simulasi HDFS, eksekusi MapReduce, kueri HiveQL, visualisasi grafik, dan pembahasan studi kasus.
- 📄 **`Panduan_Modul4.md`**: Dokumen panduan pengerjaan dan narasi presentasi (video/slide PPT).

---

## 🎯 2. Target yang Harus Dicapai (Learning Outcomes)
1. **Memahami Arsitektur Ekosistem Hadoop:**
   - *Storage:* HDFS (NameNode, DataNode, Block Size 128MB, Replikasi 3x).
   - *Resource Management:* YARN (ResourceManager, NodeManager, ApplicationMaster).
   - *Processing:* MapReduce (Map, Shuffle & Sort, Reduce) dan Apache Hive (SQL-on-Hadoop).
   - *Ecosystem Tools:* Apache Pig (ETL dataflow), HBase (NoSQL database low-latency), Sqoop/Flume (Ingestion), Oozie (Workflow scheduling).
2. **Menjalankan Hands-on Lab Exercise:**
   - Perintah dasar HDFS (`-mkdir`, `-put`, `-ls`, `-cat`).
   - Eksekusi MapReduce Hadoop Streaming (`mapper.py` & `reducer.py`).
   - Eksekusi kueri analitik Apache Hive (`CREATE TABLE`, `LOAD DATA`, `SELECT`, `CASE WHEN`, `ORDER BY`).
3. **Menganalisis Hasil Analisis Data Stunting Indonesia:**
   - Mengetahui tren nasional (rata-rata prevalensi turun dari 12.39% di 2020 menjadi 8.16% di 2023).
   - Mengidentifikasi wilayah zona merah prioritas penanganan (Sulawesi Barat, NTT, Kalimantan Barat, dll).
4. **Menjawab Case Study Modul:**
   - Mengintegrasikan studi kasus registri kesehatan/imunisasi anak dengan arsitektur ekosistem Hadoop.

---

## 🚀 3. Langkah Pengerjaan Praktikum (Bisa Dijalankan Langsung)

### A. Menjalankan Jupyter Notebook di VS Code / Jupyter Lab
1. Buka file **`module4.ipynb`** di VS Code.
2. Pastikan kernel Python aktif (misal Python 3.10 atau sejenisnya dengan library `pandas`, `matplotlib`).
3. Klik **Run All** (atau jalankan sel satu per satu secara berurutan).
4. Semua output tabel, teks hasil MapReduce, kueri SQL/HiveQL, dan 2 grafik visualisasi akan langsung muncul secara otomatis.

### B. Simulasi CLI MapReduce di Terminal (Opsional / Demo Video)
Jika ingin mendemonstrasikan cara kerja piping MapReduce Hadoop Streaming di terminal:
```bash
# Menjalankan pipeline Mapper -> Sort -> Reducer
type "data\data_stunting_clean.csv" | python mapper.py | sort | python reducer.py
```
*(Pada Linux/Mac/Git Bash: `cat data/data_stunting_clean.csv | python3 mapper.py | sort | python3 reducer.py`)*

### C. Menjalankan di Klaster Hadoop Resmi (Jika Disediakan Server/Docker)
```bash
# 1. Masukkan dataset ke HDFS
hdfs dfs -mkdir -p /user/hadoop/stunting/input
hdfs dfs -put data/data_stunting_clean.csv /user/hadoop/stunting/input/

# 2. Eksekusi Hadoop Streaming
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -input /user/hadoop/stunting/input/data_stunting_clean.csv \
    -output /user/hadoop/stunting/output_mapreduce \
    -mapper "python3 mapper.py" \
    -reducer "python3 reducer.py"

# 3. Jalankan Kueri HiveQL
hive -f stunting_hive.hql
```

---

## 🎙️ 4. Panduan Narasi Presentasi & Penjelasan Slide (Bahan Video / PPT)

Berikut adalah panduan teks narasi per slide yang bisa dibacakan oleh anggota kelompok saat presentasi:

### Slide 1: Judul & Pengantar Modul 4
> "Halo semuanya, kami dari kelompok Sistem Analisis Prediktif dan Pemetaan Risiko Stunting. Pada kesempatan kali ini, kami akan mempresentasikan hasil pengerjaan **Modul 4: Hadoop Ecosystem**. Fokus bahasan kami adalah bagaimana memanfaatkan komponen inti Hadoop seperti HDFS, MapReduce, dan Apache Hive untuk mengelola dan menganalisis dataset prevalensi stunting 38 provinsi di Indonesia dari tahun 2020 hingga 2023."

### Slide 2: Arsitektur Ekosistem Hadoop
> "Ekosistem Hadoop terdiri dari tiga lapisan utama. Pertama, **HDFS** sebagai media penyimpanan terdistribusi yang membagi data menjadi blok 128 MB dengan replikasi tiga kali agar tahan kerusakan. Kedua, **YARN** yang bertindak sebagai manajer sumber daya komputasi klaster. Dan ketiga, lapisan pemrosesan seperti **MapReduce** untuk pemrosesan batch paralel, serta **Apache Hive** yang memudahkan kita melakukan kueri SQL di atas data HDFS tanpa perlu menulis kode Java yang rumit."

### Slide 3: Penyiapan & Ingestion Dataset Stunting
> "Dataset yang kami gunakan mencakup data historis prevalensi stunting anak balita di 38 provinsi Indonesia. Pada tahap ingestion, kami melakukan pembersihan data dari format mentah menjadi format CSV standar dengan pemisah koma dan desimal titik. Data ini kemudian diunggah ke HDFS menggunakan perintah `hdfs dfs -put` ke direktori terdistribusi `/user/hadoop/stunting/input/`."

### Slide 4: Pemrosesan Terdistribusi MapReduce (Hadoop Streaming)
> "Untuk pemrosesan terdistribusi, kami menerapkan konsep Hadoop Streaming dengan Python. Skrip `mapper.py` bertugas memfilter data dan memetakan nilai prevalensi tahun 2023 ke dalam kategori risiko: Tinggi, Sedang, atau Rendah, lalu mengeluarkan pasangan Key-Value. Setelah melalui tahap Shuffle and Sort oleh Hadoop, skrip `reducer.py` melakukan agregasi frekuensi untuk menghitung berapa banyak provinsi yang berada di tiap zona risiko secara akurat."

### Slide 5: Data Warehousing dengan Apache Hive (HiveQL)
> "Pada lapisan Data Warehouse, kami merancang tabel `prevalensi_stunting` menggunakan HiveQL. Kami mengeksekusi beberapa kueri analitik penting, di antaranya:
> 1. Menemukan 5 provinsi dengan stunting tertinggi (seperti Sulawesi Barat di angka 23.2% dan NTT di angka 17.4%).
> 2. Menemukan 5 provinsi dengan stunting terendah (seperti DKI Jakarta di angka 1.0% dan Papua Pegunungan di angka 1.4%).
> 3. Menghitung progres penurunan stunting dari 2020 ke 2023, serta mengklasifikasikan zona intervensi kesehatan menggunakan klausa `CASE WHEN`."

### Slide 6: Visualisasi Tren & Temuan Utama
> "Dari visualisasi yang kami buat, terlihat tren positif di mana rata-rata prevalensi stunting nasional turun signifikan dari 12.39% pada tahun 2020 menjadi 8.16% pada tahun 2023. Namun, disparitas antar-wilayah masih cukup nyata, sehingga zonasi prioritas hasil olahan Hive ini sangat krusial untuk membantu pemerintah menentukan alokasi intervensi gizi secara tepat sasaran."

### Slide 7: Pembahasan Case Study & Penutup
> "Sesuai studi kasus Modul 4 mengenai registri kesehatan nasional, ekosistem Hadoop membuktikan kekuatannya: Hive untuk analitik agregat jutaan rekam medis, Pig untuk ETL pembersihan data puskesmas, HBase untuk pencarian cepat profil anak perorangan, dan Oozie untuk otomatisasi alur kerja bulanan. Dengan fondasi Modul 4 ini, sistem Big Data stunting kelompok kami siap melangkah ke modul pemrosesan lanjutan berikutnya. Terima kasih!"

---

## 💡 5. Hubungan Modul 4 dengan Roadmap Proyek Akhir
Sesuai silabus di `README.md` repositori:
- **Modul 1 & 2 (Fase 1):** Fondasi 5Vs Big Data & Setup Spark/PySpark Environment.
- **Modul 3, 4 & 5 (Fase 2):** Penyimpanan & Pengelolaan Data (HDFS, MapReduce, Hive, dan Optimasi Parquet). *-> Target Modul 4 tercapai penuh di sini!*
- **Modul 6, 7 & 8 (Fase 3):** Pemrosesan Lanjutan PySpark DataFrames & Spark Structured Streaming.
- **Modul 11 & 12 (Fase 5):** Machine Learning (Prediksi Risiko & K-Means Clustering Wilayah).
- **Modul 13 (Fase 6):** Website Dashboard Interaktif Stunting.
