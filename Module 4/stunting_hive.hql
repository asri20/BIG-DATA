-- =====================================================================
-- SKRIP APACHE HIVE / HIVEQL: ANALISIS DATA STUNTING INDONESIA
-- Mata Kuliah: IFB-451 Big Data (Modul 4 - Hadoop Ecosystem)
-- =====================================================================

-- 1. Membuat Database Khusus Sistem Stunting
CREATE DATABASE IF NOT EXISTS stunting_db;
USE stunting_db;

-- 2. Membuat Skema Tabel Hive Berbasis CSV yang Tersimpan di HDFS
-- Format Delimited dengan pemisah koma ',', melewati baris header
CREATE TABLE IF NOT EXISTS prevalensi_stunting (
    provinsi STRING,
    th_2020 FLOAT,
    th_2021 FLOAT,
    th_2022 FLOAT,
    th_2023 FLOAT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
tblproperties ("skip.header.line.count"="1");

-- 3. Memuat Data dari HDFS ke Dalam Tabel Hive
-- Catatan: Pastikan file telah di-upload ke HDFS sebelumnya:
-- hdfs dfs -put data_stunting_clean.csv /user/hadoop/stunting/
LOAD DATA INPATH '/user/hadoop/stunting/data_stunting_clean.csv' 
OVERWRITE INTO TABLE prevalensi_stunting;

-- =====================================================================
-- KUERI ANALITIK HIVEQL (DATA WAREHOUSING HEALTH INFORMATICS)
-- =====================================================================

-- Query 1: Top 5 Provinsi dengan Tingkat Stunting Tertinggi Tahun 2023 (Zona Merah)
SELECT 
    provinsi, 
    th_2023 AS prevalensi_2023
FROM prevalensi_stunting 
ORDER BY th_2023 DESC 
LIMIT 5;

-- Query 2: Top 5 Provinsi dengan Tingkat Stunting Terendah Tahun 2023 (Zona Hijau)
SELECT 
    provinsi, 
    th_2023 AS prevalensi_2023
FROM prevalensi_stunting 
ORDER BY th_2023 ASC 
LIMIT 5;

-- Query 3: Analisis Progres Penurunan Stunting Tertinggi (2020 vs 2023)
-- Mengukur keberhasilan intervensi kesehatan di tiap daerah
SELECT 
    provinsi,
    th_2020,
    th_2023,
    ROUND(th_2020 - th_2023, 2) AS penurunan_poin
FROM prevalensi_stunting
ORDER BY penurunan_poin DESC;

-- Query 4: Klasifikasi Status Zona Intervensi Kesehatan (Case When Statement)
SELECT 
    provinsi, 
    th_2023,
    CASE 
        WHEN th_2023 >= 15.0 THEN 'Zona Merah (Prioritas Intervensi Khusus)'
        WHEN th_2023 >= 5.0 THEN 'Zona Kuning (Waspada/Pemantauan Rutin)'
        ELSE 'Zona Hijau (Terkendali/Pemberdayaan)'
    END AS status_zona
FROM prevalensi_stunting
ORDER BY th_2023 DESC;

-- Query 5: Agregasi Makro Tren Rata-rata Nasional dari Tahun ke Tahun
SELECT 
    ROUND(AVG(th_2020), 2) AS rata_nasional_2020,
    ROUND(AVG(th_2021), 2) AS rata_nasional_2021,
    ROUND(AVG(th_2022), 2) AS rata_nasional_2022,
    ROUND(AVG(th_2023), 2) AS rata_nasional_2023
FROM prevalensi_stunting;

-- Query 6: Optimasi Format Kolom Big Data (Apache Parquet)
-- Mengonversi tabel Text CSV ke Apache Parquet terkompresi Snappy
CREATE TABLE IF NOT EXISTS prevalensi_stunting_parquet (
    provinsi STRING,
    th_2020 FLOAT,
    th_2021 FLOAT,
    th_2022 FLOAT,
    th_2023 FLOAT
)
STORED AS PARQUET;

INSERT OVERWRITE TABLE prevalensi_stunting_parquet
SELECT * FROM prevalensi_stunting;
