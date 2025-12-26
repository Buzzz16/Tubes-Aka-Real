# 📂 Struktur Proyek Aplikasi
## Analisis Algoritma Pertumbuhan Bakteri

<div align="center">

![Structure](https://img.shields.io/badge/📂-Project_Structure-22C55E?style=for-the-badge)
![MVC](https://img.shields.io/badge/Pattern-MVC-10B981?style=for-the-badge)

**Dokumentasi susunan file dan folder untuk memudahkan Dosen/Reviewer memahami arsitektur aplikasi.**

</div>

---

## 🌳 Pohon Direktori

```bash
d:\aka - bakteri\
│
├── 📄 app.py                 # [CORE] File utama aplikasi Flask (Controller & Model)
├── 📄 requirements.txt       # Daftar library Python yang dibutuhkan
├── 📄 Procfile               # Konfigurasi untuk deployment (Gunicorn)
├── 📄 vercel.json            # Konfigurasi deployment Vercel
├── 📄 render.yaml            # Konfigurasi deployment Render
│
├── 📂 static/                # [ASSETS] File statis (CSS, JS, Images)
│   ├── 📂 css/
│   │   └── 📄 style.css      # Styling utama (Green Theme, Dark Mode, Glassmorphism)
│   └── 📂 js/
│       └── 📄 main.js        # Interaksi frontend (Chart.js, Toggle, Export)
│
├── 📂 templates/             # [VIEWS] Template HTML (Jinja2)
│   ├── 📄 base.html          # Layout utama (Navbar, Footer, Meta tags)
│   ├── 📄 index.html         # Halaman Beranda (Landing Page)
│   ├── 📄 theory.html        # Halaman Teori & Penjelasan Algoritma
│   ├── 📄 single_test.html   # Halaman Uji Coba Tunggal
│   └── 📄 range_test.html    # Halaman Uji Coba Rentang (Grafik Garis)
│
└── 📂 Dokumentasi/           # [DOCS] Panduan & Laporan
    ├── 📄 README.md          # Halaman muka dokumentasi
    ├── 📄 CHANGELOG.md       # Riwayat perubahan
    ├── 📄 CARA_MENJALANKAN.md # Panduan instalasi
    ├── 📄 DEPLOYMENT.md      # Panduan upload ke server
    └── 📄 QUICK_START.md     # Panduan cepat
```

---

## 📝 Penjelasan File Penting

### 1. `app.py` (Backend)
Berisi logika utama aplikasi:
- **Routing**: Mengatur URL (`/`, `/theory`, `/single-test`, dll).
- **Algoritma**: Fungsi `bakteri_iteratif()` dan `bakteri_rekursif()`.
- **API**: Endpoint untuk menerima data dari frontend dan mengembalikan hasil perhitungan JSON.

### 2. `static/css/style.css` (Styling)
Mengatur tampilan visual:
- Menggunakan **CSS Variables** untuk kemudahan pergantian tema (Light/Dark).
- Implementasi **Flexbox** untuk layout yang responsif.
- Desain **Glassmorphism** (efek kaca) pada kartu hasil.

### 3. `templates/base.html` (Layout)
Template induk yang diwariskan ke halaman lain:
- Memuat library eksternal (Chart.js, FontAwesome, Google Fonts).
- Menyediakan struktur navigasi yang konsisten.

---

<div align="center">

**Disusun untuk memenuhi standar dokumentasi tugas kuliah.**

</div>
