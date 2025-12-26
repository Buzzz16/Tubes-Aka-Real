# 📝 Catatan Perubahan (Changelog)
## Perjalanan Pengembangan Aplikasi Analisis Algoritma

<div align="center">

![Status](https://img.shields.io/badge/Status-Active_Development-22C55E?style=for-the-badge)
![Version](https://img.shields.io/badge/Version-2.0.0-10B981?style=for-the-badge)

**Dokumentasi lengkap perubahan dari aplikasi sederhana menjadi simulasi ilmiah.**

</div>

---

## 📅 [Terbaru] - Transformasi Total & Penyempurnaan UI
*Fokus: Meningkatkan kualitas aplikasi untuk penilaian dosen dan pengalaman pengguna.*

### 🎨 UI/UX & Tema
- **Transformasi Tema**: Mengubah total tema aplikasi dari "Kalkulator Pangkat" menjadi **"Analisis Pertumbuhan Bakteri *V. natriegens*"**.
- **Color Palette**: Menerapkan skema warna hijau (#22C55E, #10B981, #059669) untuk nuansa biologis.
- **Dark Mode**: Menambahkan fitur Dark Mode dengan tombol toggle matahari/bulan (🌙/☀️) yang statusnya disimpan di `localStorage`.
- **Responsive Design**: Mengubah layout dari CSS Grid ke **Flexbox** agar tampilan rapi di HP dan Tablet.
- **Navigasi**: Memperbaiki animasi hamburger menu dan dropdown navbar.

### 🔬 Fitur Ilmiah & Algoritma
- **Algoritma Baru**: Mengganti fungsi `pangkatIteratif/Rekursif` menjadi `bakteri_iteratif` dan `bakteri_rekursif` yang lebih relevan dengan konteks biologi.
- **Konversi Waktu**: Menambahkan fungsi `peubah_waktu()` untuk menangani input dalam Detik, Menit, dan Jam.
- **Validasi Input**: Mencegah input negatif dan menangani `RecursionError` dengan pesan yang user-friendly.

### 📊 Visualisasi & Data
- **Export PNG**: Menambahkan tombol kamera (📷) untuk mengunduh grafik hasil analisis.
- **Export CSV**: Menambahkan fitur unduh data mentah (📄) pada halaman Range Test untuk keperluan laporan.
- **Interval Kontrol**: Menambahkan fitur interval pada Range Test agar grafik tidak terlalu padat.

---

## 📅 [Fase 2] - Peningkatan Fungsionalitas
*Fokus: Menambahkan fitur yang diminta untuk tugas kuliah.*

- **Halaman Teori**: Menambahkan halaman penjelasan tentang *Vibrio natriegens* dan analisis kompleksitas algoritma.
- **Single Test Page**: Membuat halaman untuk pengujian satu kasus pertumbuhan.
- **Range Test Page**: Membuat halaman untuk membandingkan performa dalam rentang data besar (Big-O visualization).
- **Loading State**: Menambahkan animasi loading saat proses perhitungan berlangsung.

---

## 📅 [Fase 1] - Inisialisasi Proyek
*Fokus: Membangun fondasi aplikasi Python Flask.*

- **Setup Flask**: Inisialisasi struktur proyek Flask (MVC pattern).
- **Basic Algorithm**: Implementasi awal algoritma pemangkatan sederhana.
- **Template Dasar**: Membuat `base.html` sebagai kerangka utama aplikasi.

---

<div align="center">

**Catatan Pengembang (Mahasiswa):**
*"Perubahan terbesar dilakukan pada fase terakhir untuk memastikan aplikasi tidak hanya berfungsi secara teknis, tetapi juga memiliki konteks studi kasus yang kuat (Bakteri) agar lebih menarik saat dipresentasikan kepada Dosen."*

</div>
