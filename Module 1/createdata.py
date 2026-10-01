import pandas as pd
import numpy as np
import os

# Membuat folder 'data' secara otomatis jika belum ada
output_dir = "data"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Menentukan total target baris untuk mencapai ~1 GB (sekitar 13 juta baris)
total_rows = 13000000 
chunk_size = 500000  # Dibagi per chunk agar aman untuk memori RAM
file_name = os.path.join(output_dir, "stunting_nasional_1gb.csv")

# Kamus wilayah yang diperluas mencakup Pulau Jawa dan Pulau Sumatra
provinsi_kabupaten = {
    "Jawa Barat": ["Bandung", "Garut", "Bogor", "Cirebon", "Bekasi", "Tasikmalaya"],
    "Jawa Tengah": ["Semarang", "Solo", "Banyumas", "Tegal", "Magelang", "Brebes"],
    "Jawa Timur": ["Surabaya", "Malang", "Sidoarjo", "Jember", "Kediri", "Banyuwangi"],
    "Banten": ["Serang", "Tangerang", "Cilegon", "Pandeglang", "Lebak"],
    "Sumatera Utara": ["Medan", "Deli Serdang", "Binjai", "Padang Sidempuan", "Tapanuli Utara", "Asahan"],
    "Sumatera Barat": ["Padang", "Bukittinggi", "Payakumbuh", "Pesisir Selatan", "Agam", "Solok"],
    "Sumatera Selatan": ["Palembang", "Prabumulih", "Lubuklinggau", "Banyuasin", "Ogan Komering Ilir"],
    "Lampung": ["Bandar Lampung", "Metro", "Lampung Selatan", "Lampung Tengah", "Lampung Timur"],
    "Nusa Tenggara Timur": ["Kupang", "Timor Tengah Selatan", "Manggarai", "Sumba Timur", "Flores Timur"],
    "Sulawesi Selatan": ["Makassar", "Gowa", "Maros", "Bone", "Palopo", "Toraja Utara"]
}

provs = list(provinsi_kabupaten.keys())

print(f"Memulai pembuatan dataset Big Data (~1 GB) dengan wilayah Jawa & Sumatra, total target: {total_rows:,} baris...")

# Loop per chunk untuk menulis ke CSV secara bertahap
for i in range(0, total_rows, chunk_size):
    actual_chunk = min(chunk_size, total_rows - i)
    
    id_anak = [f"ID_CHILD_{j:08d}" for j in range(i + 1, i + actual_chunk + 1)]
    provinsi_val = np.random.choice(provs, size=actual_chunk)
    kabupaten_val = [np.random.choice(provinsi_kabupaten[p]) for p in provinsi_val]
    kecamatan_val = [f"Kecamatan_{np.random.randint(1, 150)}" for _ in range(actual_chunk)]
    
    jenis_kelamin = np.random.choice(["Laki-laki", "Perempuan"], size=actual_chunk)
    usia_bulan = np.random.randint(0, 61, size=actual_chunk)
    
    berat_lahir = np.random.normal(3.0, 0.5, size=actual_chunk).clip(1.2, 5.0)
    panjang_lahir = np.random.normal(49.0, 2.0, size=actual_chunk).clip(40.0, 55.0)
    
    berat_aktual = berat_lahir + (usia_bulan * 0.4) + np.random.normal(0, 1.0, size=actual_chunk)
    tinggi_aktual = panjang_lahir + (usia_bulan * 1.1) + np.random.normal(0, 3.0, size=actual_chunk)
    
    # Simulasi Z-Score TB/U
    z_score = np.random.normal(-0.6, 1.3, size=actual_chunk)
    
    def tentukan_status(z):
        if z < -3.0:
            return "Sangat Pendek (Severely Stunted)"
        elif -3.0 <= z < -2.0:
            return "Pendek (Stunted)"
        elif -2.0 <= z <= 3.0:
            return "Normal"
        else:
            return "Tinggi"

    status_stunting = [tentukan_status(z) for z in z_score]
    sanitasi = np.random.choice(["Layak", "Tidak Layak"], size=actual_chunk, p=[0.7, 0.3])
    asi_eksklusif = np.random.choice(["Ya", "Tidak"], size=actual_chunk, p=[0.6, 0.4])
    sumber_air = np.random.choice(["Air Bersih Terlindungi", "Air Tidak Terlindungi"], size=actual_chunk, p=[0.75, 0.25])
    pendapatan = np.random.choice(["Di Bawah UMR", "Di Atas UMR"], size=actual_chunk, p=[0.55, 0.45])

    df_chunk = pd.DataFrame({
        "ID_Anak": id_anak,
        "Provinsi": provinsi_val,
        "Kabupaten_Kota": kabupaten_val,
        "Kecamatan": kecamatan_val,
        "Jenis_Kelamin": jenis_kelamin,
        "Usia_Bulan": usia_bulan,
        "Berat_Lahir_kg": np.round(berat_lahir, 2),
        "Panjang_Lahir_cm": np.round(panjang_lahir, 2),
        "Berat_Aktual_kg": np.round(berat_aktual, 2),
        "Tinggi_Aktual_cm": np.round(tinggi_aktual, 2),
        "Z_Score_TB_U": np.round(z_score, 2),
        "Status_Stunting": status_stunting,
        "Riwayat_ASI_Eksklusif": asi_eksklusif,
        "Akses_Sanitasi": sanitasi,
        "Sumber_Air_Minum": sumber_air,
        "Pendapatan_Keluarga": pendapatan
    })
    
    # Mode 'w' untuk iterasi awal, 'a' (append) untuk iterasi berikutnya
    mode = 'w' if i == 0 else 'a'
    header = True if i == 0 else False
    
    df_chunk.to_csv(file_name, mode=mode, header=header, index=False)
    print(f"Progress: Berhasil menulis {i + actual_chunk:,} dari {total_rows:,} baris...")

print("Selesai! Dataset Big Data 1 GB dengan cakupan wilayah Sumatra & Jawa berhasil dibuat.")