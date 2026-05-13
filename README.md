# Monte Carlo Battle RPG Simulator

Simulasi Battle RPG sederhana berbasis Monte Carlo Simulation untuk menganalisis peluang kemenangan karakter dan membandingkan performa Sequential vs Parallel Computing menggunakan Python Multiprocessing.

---

# Anggota Kelompok 11

| Nama | NIM | Peran |
|---|---|---|
| Nevan Jovanie Ismail | 2430305030008 | Core Developer / QA |
| Satriya Justisia | 2430205030021 | Project Manager |
| Vallentino Gaudy Bo’as | 2430305030013 | Core Developer |
| Yesaya Mei Dinata Tarigan | 2430305030024 | System Architect |

---

# Deskripsi Proyek

Proyek ini mengimplementasikan Monte Carlo Simulation pada sistem Battle RPG sederhana. Dua karakter dengan atribut berbeda akan bertarung secara otomatis hingga salah satu karakter kalah.

Simulasi dijalankan berulang kali untuk menghitung:
- peluang kemenangan,
- execution time,
- speedup,
- efficiency.

Sistem mendukung:
- Sequential Computing
- Parallel Computing menggunakan multiprocessing.

---

# Fitur Sistem

- Simulasi Battle RPG 1 vs 1
- Monte Carlo Simulation
- Sequential & Parallel Execution
- Multiprocessing Support
- Analisis Performa
- Visualisasi Grafik
- Dashboard Interaktif Streamlit

---

# Teknologi yang Digunakan

- Python
- Streamlit
- Pandas
- Matplotlib
- Multiprocessing

---

# Struktur Project

```text
MonteCarlo-Battle-RPG/
│
├── app.py
├── simulation.py
├── requirements.txt
│
├── assets/
│   ├── reaper.png
│   └── cyber_mage.png
│
├── docs/
│   ├── Proposal.pdf
│   ├── SDD.pdf
│   └── diagrams/
│
├── screenshots/
│
└── README.md
```

---

# Cara Menjalankan Program

## 1. Clone Repository

```bash
git clone https://github.com/satriyaj/Kelompok-11_Komputasi-Paralel-dan-Terdistribusi.git
```

---

## 2. Masuk ke Folder Project

```bash
cd MonteCarlo-Battle-RPG
```

---

## 3. Install Dependency

```bash
pip install -r requirements.txt
```

---

## 4. Jalankan Streamlit

```bash
streamlit run app.py
```

---

# Skenario Pengujian

Pengujian dilakukan menggunakan:
- 10.000 simulasi
- 50.000 simulasi
- 100.000 simulasi

Dengan jumlah proses:
- 1 proses
- 2 proses
- 4 proses
- 8 proses

---

# Output Sistem

Sistem menghasilkan:
- Win Rate Karakter
- Execution Time
- Speedup
- Efficiency
- Grafik Performa
- Riwayat Pengujian

---

# Contoh Hasil Pengujian

| Parameter | Hasil |
|---|---|
| Total Simulasi | 100.000 |
| Mode | Sequential |
| Execution Time | 2.1152 s |
| Reaper Win Rate | 71.36% |
| Cyber Mage Win Rate | 28.64% |
| Speedup | 1.0x |
| Efficiency | 100% |

---

# Pengembangan Selanjutnya

- AI Enemy
- Distributed Computing
- GPU Acceleration
- Real-Time Battle System

---

# Lisensi

Project ini dibuat untuk keperluan tugas UAS Mata Kuliah Parallel & Distributed Computing.
