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
cd Kelompok-11_Komputasi-Paralel-dan-Terdistribusi
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
- 500.000 simulasi
- 1.000.000 simulasi

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

# Video Demo

https://drive.google.com/file/d/12Zn-8-6wC4_yimGfDYY6mTnuaLw2y7VR/view?usp=drive_link

# Dashboard

<img width="1394" height="726" alt="Screenshot 2026-06-03 135316" src="https://github.com/user-attachments/assets/8f29787d-4fef-4664-a4c9-4388c6d0d114" />
<img width="1262" height="714" alt="Screenshot 2026-06-03 135348" src="https://github.com/user-attachments/assets/2478748a-29ce-4da5-bdf2-c1a6eea5ff3c" />
<img width="1298" height="703" alt="Screenshot 2026-06-02 211242" src="https://github.com/user-attachments/assets/ece33531-f6da-471a-b0fe-775f09a89929" />
<img width="1257" height="553" alt="Screenshot 2026-06-03 153817" src="https://github.com/user-attachments/assets/4b3115e2-c19d-4b2a-8618-955ec937575b" />
