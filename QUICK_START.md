# 🚀 Quick Start Guide
## Mulai Analisis dalam 5 Menit

<div align="center">

![Banner](https://capsule-render.vercel.app/api?type=waving&color=22C55E&height=150&section=header&text=Quick%20Start&fontSize=40&animation=fadeIn&fontAlignY=40)

![Fast](https://img.shields.io/badge/⚡-Ready_in_5_Min-22C55E?style=for-the-badge)
![Easy](https://img.shields.io/badge/👌-Easy_Setup-10B981?style=for-the-badge)

**Panduan cepat untuk Dosen/Pengguna mencoba fitur utama aplikasi.**

</div>

---

## 1️⃣ Persiapan Singkat

Pastikan Python sudah terinstall, lalu jalankan di terminal:

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Jalankan aplikasi
python app.py
```

👉 Buka browser di: `http://localhost:5000`

---

## 2️⃣ Skenario Pengujian (Test Cases)

Gunakan tabel ini saat mendemokan aplikasi untuk menunjukkan perbedaan performa algoritma secara jelas.

| Skenario | Parameter Input | Ekspektasi Hasil |
| :--- | :--- | :--- |
| **A. Dasar**<br>*(Cek Fungsi)* | **Menu**: Single Test<br>• $N_0$: `10`<br>• Waktu: `Menit`<br>• Durasi: `60`<br>• Laju: `20` | ✅ Kedua algoritma sangat cepat (< 0.1ms).<br>✅ Hasil populasi sama persis. |
| **B. Menengah**<br>*(Mulai Beda)* | **Menu**: Single Test<br>• $N_0$: `100`<br>• Waktu: `Jam`<br>• Durasi: `5`<br>• Laju: `10` | ✅ Iteratif sedikit lebih cepat.<br>✅ Rekursif mulai memakan memori stack. |
| **C. Stress Test**<br>*(Rekursif Limit)* | **Menu**: Range Test<br>• $N_0$: `1`<br>• Tipe: `Kejadian`<br>• Mulai: `10` • Akhir: `2000`<br>• Interval: `100` | ✅ Grafik Iteratif datar (stabil).<br>⚠️ Grafik Rekursif naik tajam / error (Stack Overflow). |

---

## 3️⃣ Fitur Wajib Coba (Demo Checklist)

Pastikan Anda menunjukkan fitur-fitur ini saat presentasi:

- [ ] **Toggle Dark Mode** 🌙 (Pojok kanan atas)
- [ ] **Export Chart PNG** 📷 (Ikon kamera di atas grafik)
- [ ] **Export Data CSV** 📄 (Tombol di halaman Range Test)
- [ ] **Halaman Teori** 📚 (Tunjukkan penjelasan Big-O)

---

<div align="center">

**Selamat Mencoba! 🦠**

</div>
