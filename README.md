# 📊 Analisis Perbandingan Efisiensi Algoritma Iteratif dan Rekursif

Aplikasi web berbasis Flask untuk menganalisis dan membandingkan performa algoritma iteratif dan rekursif dalam menghitung bilangan eksponen.

## 🎯 Fitur Utama

### 1. **Halaman Teori & Pengantar**
- Penjelasan konsep algoritma iteratif dan rekursif
- Analisis Time Complexity dan Space Complexity
- Visualisasi pseudocode dan implementasi kode
- Penjelasan Recursion Overhead

### 2. **Single Input Analysis**
- Input basis dan pangkat
- Perhitungan dengan kedua algoritma
- Pengukuran waktu eksekusi (milidetik)
- Validasi hasil
- Grafik perbandingan (Bar Chart)
- Kesimpulan otomatis

### 3. **Range & Graph Analysis**
- Input range dengan interval custom
- Pengujian berulang pada rentang input
- Grafik tren waktu eksekusi (Line Chart)
- Statistik rata-rata
- Tabel data mentah hasil pengujian
- Progress bar real-time

## 🎨 Desain UI/UX

- **Tema**: Biru tua gradasi putih dengan efek glassmorphism
- **Animasi**: Smooth transitions, hover effects, scroll animations
- **Responsif**: Mobile-friendly design
- **Interaktif**: Real-time feedback dan visualisasi

## 📁 Struktur Proyek

```
coba/
│
├── app.py                      # Flask backend & algoritma core
│
├── templates/                  # Template HTML (Jinja2)
│   ├── base.html              # Template dasar dengan navigation
│   ├── theory.html            # Halaman teori
│   ├── single_test.html       # Halaman single test
│   └── range_test.html        # Halaman range analysis
│
├── static/                     # Static files
│   ├── css/
│   │   └── style.css          # Styling dengan glassmorphism
│   ├── js/
│   │   └── main.js            # JavaScript untuk animasi & Chart.js
│   └── images/                # Folder untuk gambar (opsional)
│
└── requirements.txt            # Dependencies Python
```

## 🚀 Cara Menjalankan

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Jalankan Aplikasi

```bash
python app.py
```

### 3. Buka Browser

Akses aplikasi di: `http://localhost:5000`

## 🔧 Teknologi yang Digunakan

### Backend
- **Flask 3.0.0** - Python web framework
- **Jinja2** - Template engine
- **Python 3.x** - Core logic

### Frontend
- **HTML5** - Struktur halaman
- **CSS3** - Styling dengan Glassmorphism
- **JavaScript (ES6+)** - Interaksi & animasi
- **Chart.js 4.4.0** - Visualisasi grafik

### Libraries & Frameworks
- **Font Awesome 6.4.0** - Icons
- **Google Fonts (Plus Jakarta Sans)** - Typography

## 💡 Logika Algoritma

### Algoritma Iteratif
```python
def pangkatIteratif(basis, pangkat):
    result = 1
    for i in range(pangkat):
        result *= basis
    return result
```

**Kompleksitas:**
- Time: O(n)
- Space: O(1)

### Algoritma Rekursif
```python
def pangkatRekursif(basis, pangkat):
    if pangkat == 0:
        return 1    
    return basis * pangkatRekursif(basis, pangkat - 1)
```

**Kompleksitas:**
- Time: O(n)
- Space: O(n) - Call stack

### Pengukuran Waktu
```python
def measure_time(func, *args):
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000
    return result, execution_time_ms
```

## 🎓 Alur Kerja Aplikasi

### 1. **Request Flow**
```
Browser → Flask Route → Algoritma Core → Response (JSON/HTML)
```

### 2. **Single Test Flow**
1. User input basis & pangkat via form
2. JavaScript submit form via AJAX (POST request)
3. Flask route `/single-test` menerima data
4. Eksekusi kedua algoritma dengan `measure_time()`
5. Return hasil dalam format JSON
6. JavaScript render hasil & buat chart
7. Tampilkan dengan animasi

### 3. **Range Test Flow**
1. User input range parameters
2. Submit form via AJAX dengan progress tracking
3. Flask iterasi melalui range input
4. Collect data points untuk setiap pangkat
5. Return array data dalam JSON
6. JavaScript render line chart & tabel
7. Tampilkan statistik & kesimpulan

### 4. **Rendering Flow**
```
Flask → Jinja2 Template → HTML → Browser
        ↓
    url_for() untuk static files
        ↓
    CSS (Glassmorphism) + JS (Animations)
```

## 📊 Endpoint API

### `GET /` atau `GET /theory`
Halaman teori dan pengantar

### `GET /single-test`
Halaman form single test

### `POST /single-test`
Proses single test analysis
- Input: `basis`, `pangkat`
- Output: JSON dengan hasil analisis

### `GET /range-test`
Halaman form range test

### `POST /range-test`
Proses range analysis
- Input: `basis`, `start_exp`, `end_exp`, `step_exp`
- Output: JSON dengan array data points

## 🎨 Fitur Animasi

1. **Floating Gradient Orbs** - Background animasi
2. **Glassmorphism Cards** - Efek kaca blur
3. **Hover Tilt Effect** - 3D card tilt
4. **Progress Bar** - Animated gradient progress
5. **Chart Animations** - Smooth data visualization
6. **Scroll Animations** - Fade in & slide up
7. **Button Ripple** - Material design ripple
8. **Loading Spinner** - Multi-ring spinner
9. **Navbar Scroll** - Dynamic navbar background

## 📝 Catatan Akademik

### Kelebihan Implementasi
- ✅ Kode modular dan mudah dipahami
- ✅ Pemisahan concerns (Backend/Frontend)
- ✅ Error handling untuk recursion limit
- ✅ Visualisasi data yang informatif
- ✅ UI/UX yang engaging

### Limitasi
- ⚠️ Recursion limit untuk input sangat besar (>5000)
- ⚠️ Performa browser untuk dataset sangat besar
- ⚠️ Tidak ada persistent storage (no database)

### Pengembangan Lebih Lanjut
- 💾 Tambah database untuk menyimpan history
- 👤 Implementasi user authentication
- 📤 Export hasil ke PDF/Excel
- 🔄 Real-time collaboration
- 📱 Progressive Web App (PWA)

## 👥 Tim Pengembang

**Tugas Besar Analisis Kompleksitas Algoritma**
- Babass
- Gathfann

© 2025

## 📄 Lisensi

Proyek ini dibuat untuk keperluan akademik.

---

**Happy Coding! 🚀**
