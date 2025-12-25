# BAB III
# PERANCANGAN DAN IMPLEMENTASI ALGORITMA

## 3.1 Bentuk Implementasi Sistem

Sistem analisis perbandingan algoritma iteratif dan rekursif untuk perhitungan bilangan eksponen diimplementasikan dalam bentuk **aplikasi web berbasis Flask**. Aplikasi ini menggunakan arsitektur Model-View-Controller (MVC) dengan Flask sebagai backend server dan HTML/CSS/JavaScript sebagai frontend.

### 3.1.1 Arsitektur Sistem

Sistem terdiri dari beberapa komponen utama:

**1. Backend (Flask)**
   - **Framework**: Flask 3.0.0
   - **Bahasa**: Python 3.8+
   - **Fungsi**: Menangani routing, processing algoritma, dan API endpoints

**2. Frontend (HTML/CSS/JavaScript)**
   - **Template Engine**: Jinja2 3.1.2
   - **Styling**: Custom CSS dengan Glassmorphism design
   - **Interaktivitas**: Vanilla JavaScript dengan Fetch API
   - **Visualisasi**: Chart.js 4.4.0

**3. Struktur Direktori**
```
coba/
├── app.py                          # Flask backend
├── requirements.txt                # Dependencies
├── templates/                      # HTML templates
│   ├── base.html                  # Base template
│   ├── theory.html                # Halaman teori
│   ├── single_test.html           # Single input analysis
│   └── range_test.html            # Range & graph analysis
└── static/                         # Static files
    ├── css/
    │   └── style.css              # Styling
    ├── js/
    │   └── main.js                # JavaScript
    └── images/                     # Assets
```

### 3.1.2 Implementasi Algoritma Inti

Kedua algoritma diimplementasikan dalam Python dengan fungsi yang terpisah:

**Algoritma Iteratif:**
```python
def pangkatIteratif(basis, pangkat):
    """Algoritma pangkat menggunakan pendekatan iteratif"""
    result = 1
    for i in range(pangkat):
        result *= basis
    return result
```

**Karakteristik:**
- Time Complexity: O(n)
- Space Complexity: O(1)
- Menggunakan loop untuk mengalikan basis sebanyak n kali
- Tidak membutuhkan call stack tambahan

**Algoritma Rekursif:**
```python
def pangkatRekursif(basis, pangkat):
    """Algoritma pangkat menggunakan pendekatan rekursif"""
    if pangkat == 0:
        return 1    
    return basis * pangkatRekursif(basis, pangkat - 1)
```

**Karakteristik:**
- Time Complexity: O(n)
- Space Complexity: O(n)
- Menggunakan pemanggilan fungsi rekursif
- Membutuhkan stack memory untuk setiap pemanggilan

**Fungsi Pengukuran Waktu:**
```python
def measure_time(func, *args):
    """Mengukur waktu eksekusi fungsi dalam milidetik."""
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000
    return result, execution_time_ms
```

Fungsi ini menggunakan `time.perf_counter()` untuk mendapatkan pengukuran waktu dengan presisi tinggi, kemudian mengkonversi hasilnya ke milidetik untuk kemudahan analisis.

### 3.1.3 Handling Rekursi Dalam

Untuk menghindari `RecursionError` pada input besar, sistem mengimplementasikan beberapa strategi:

```python
# Menambah batas rekursi
sys.setrecursionlimit(20000)

# Validasi dan warning untuk user
if pangkat > 3000:
    warning = 'Pangkat > 3000 dapat menyebabkan RecursionError'

# Try-catch untuk menangani error
try:
    res_rec, time_rec = measure_time(pangkatRekursif, basis, pangkat)
except RecursionError:
    res_rec = None
    time_rec = None
    recursion_error = True
```

---

## 3.2 Fitur Utama Aplikasi

Aplikasi terdiri dari tiga halaman utama yang masing-masing memiliki fungsi spesifik:

### 3.2.1 Halaman Teori

**Tujuan:** Memberikan pemahaman konseptual tentang algoritma iteratif dan rekursif.

**Konten:**
1. **Pengantar**
   - Penjelasan tentang perbedaan pendekatan iteratif dan rekursif
   - Konteks studi kasus perhitungan bilangan eksponen

2. **Algoritma Iteratif**
   - Konsep perulangan (loop)
   - Time Complexity: O(n)
   - Space Complexity: O(1)
   - Implementasi kode Python
   - Pseudocode

3. **Algoritma Rekursif**
   - Konsep pemanggilan fungsi rekursif
   - Base case dan recursive case
   - Time Complexity: O(n)
   - Space Complexity: O(n)
   - Implementasi kode Python
   - Pseudocode

4. **Perbandingan Konseptual**
   - Tabel perbandingan karakteristik
   - Kelebihan dan kekurangan masing-masing
   - Kapan sebaiknya menggunakan iteratif vs rekursif

5. **Recursion Overhead**
   - Penjelasan tentang biaya tambahan pemanggilan fungsi
   - Call stack management
   - Risiko Stack Overflow

**Routing:**
```python
@app.route('/theory')
def theory():
    """Halaman Teori & Pengantar"""
    return render_template('theory.html')
```

### 3.2.2 Single Input Analysis

**Tujuan:** Membandingkan performa kedua algoritma pada satu input spesifik.

**Fitur:**
1. **Input Form**
   - Basis (integer): Bilangan dasar
   - Pangkat (integer ≥ 0): Eksponen

2. **Validasi Input**
   - Memastikan pangkat ≥ 0
   - Warning untuk input > 3000 (risiko RecursionError)

3. **Proses Komputasi**
   - Menghitung hasil dengan kedua algoritma
   - Mengukur waktu eksekusi masing-masing
   - Memvalidasi kebenaran hasil (iteratif == rekursif)

4. **Output Visualisasi**
   - **Waktu Eksekusi**: Tampilan waktu dalam milidetik dengan 6 desimal
   - **Bar Chart**: Perbandingan visual menggunakan Chart.js
   - **Hasil Komputasi**: Ringkas (jika > 100 digit)
   - **Validasi**: Indikator kecocokan hasil
   - **Kesimpulan Otomatis**: Algoritma mana yang lebih cepat

5. **Error Handling**
   - Menangani RecursionError dengan graceful fallback
   - Menampilkan pesan error yang informatif

**Routing:**
```python
@app.route('/single-test', methods=['GET', 'POST'])
def single_test():
    if request.method == 'POST':
        basis = int(request.form.get('basis', 2))
        pangkat = int(request.form.get('pangkat', 900))
        
        # Hitung iteratif
        res_iter, time_iter = measure_time(pangkatIteratif, basis, pangkat)
        
        # Hitung rekursif dengan error handling
        try:
            res_rec, time_rec = measure_time(pangkatRekursif, basis, pangkat)
            recursion_error = False
        except RecursionError:
            res_rec = None
            time_rec = None
            recursion_error = True
        
        # Return JSON response
        return jsonify({
            'success': True,
            'time_iter': time_iter,
            'time_rec': time_rec,
            'recursion_error': recursion_error,
            # ... data lainnya
        })
    
    return render_template('single_test.html')
```

### 3.2.3 Range & Graph Analysis

**Tujuan:** Menganalisis tren pertumbuhan waktu eksekusi terhadap besarnya input.

**Fitur:**
1. **Input Form**
   - Basis (integer): Bilangan dasar
   - Start Pangkat: Nilai pangkat awal
   - End Pangkat: Nilai pangkat akhir
   - Interval (Step): Jarak antar pengujian

2. **Validasi Input**
   - End > Start
   - Interval > 0

3. **Proses Komputasi Berulang**
   - Iterasi dari start hingga end dengan step interval
   - Mengukur waktu eksekusi untuk setiap titik data
   - Menangani RecursionError (skip untuk input > 5000)
   - Menyimpan semua data untuk analisis

4. **Progress Indicator**
   - Progress bar animated dengan persentase
   - Simulasi progress untuk feedback UX

5. **Output Visualisasi**
   - **Line Chart**: Tren waktu eksekusi vs input size
   - **Statistik**: Rata-rata waktu iteratif dan rekursif
   - **Tabel Data Mentah**: Semua data point dengan detail
   - **Kesimpulan**: Analisis perbandingan rata-rata

**Routing:**
```python
@app.route('/range-test', methods=['GET', 'POST'])
def range_test():
    if request.method == 'POST':
        basis = int(request.form.get('basis', 2))
        start_exp = int(request.form.get('start_exp', 10))
        end_exp = int(request.form.get('end_exp', 2000))
        step_exp = int(request.form.get('step_exp', 50))
        
        data_points = []
        input_sizes = list(range(start_exp, end_exp + 1, step_exp))
        
        for exp in input_sizes:
            # Ukur kedua algoritma
            res_iter, t_iter = measure_time(pangkatIteratif, basis, exp)
            
            if exp > 5000:
                # Skip rekursif untuk input besar
                t_rec = None
            else:
                try:
                    res_rec, t_rec = measure_time(pangkatRekursif, basis, exp)
                except RecursionError:
                    t_rec = None
            
            data_points.append({
                'input_size': exp,
                'time_iter': round(t_iter, 6),
                'time_rec': round(t_rec, 6) if t_rec else None,
                'result': str(res_iter)[:47] + "..."
            })
        
        # Hitung rata-rata dan kesimpulan
        avg_iter = sum(d['time_iter'] for d in data_points) / len(data_points)
        # ...
        
        return jsonify({
            'success': True,
            'data_points': data_points,
            'avg_iter': avg_iter,
            # ...
        })
    
    return render_template('range_test.html')
```

---

## 3.3 Visualisasi Hasil Pengujian

Visualisasi data merupakan komponen penting untuk memahami performa algoritma secara intuitif.

### 3.3.1 Bar Chart (Single Test)

**Library:** Chart.js 4.4.0

**Implementasi:**
```javascript
const ctx = document.getElementById('comparisonChart');
const chart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Iteratif', 'Rekursif'],
        datasets: [{
            label: 'Waktu Eksekusi (ms)',
            data: [timeIterative, timeRecursive],
            backgroundColor: [
                'rgba(34, 197, 94, 0.8)',   // Green for Iterative
                'rgba(139, 92, 246, 0.8)'   // Purple for Recursive
            ],
            borderColor: [
                'rgba(34, 197, 94, 1)',
                'rgba(139, 92, 246, 1)'
            ],
            borderWidth: 2
        }]
    },
    options: {
        responsive: true,
        animation: {
            duration: 1500,
            easing: 'easeInOutQuart'
        },
        scales: {
            y: {
                beginAtZero: true,
                ticks: {
                    callback: function(value) {
                        return value.toFixed(6) + ' ms';
                    }
                }
            }
        }
    }
});
```

**Fitur Visual:**
- Warna hijau untuk iteratif (melambangkan efisiensi)
- Warna ungu untuk rekursif
- Animasi smooth saat data loading
- Tooltip menampilkan nilai presisi 6 desimal
- Responsive terhadap ukuran layar

### 3.3.2 Line Chart (Range Test)

**Tujuan:** Menampilkan tren pertumbuhan waktu eksekusi seiring bertambahnya input size.

**Implementasi:**
```javascript
const trendChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: inputSizes,  // [10, 60, 110, 160, ...]
        datasets: [
            {
                label: 'Iteratif',
                data: iterativeTimes,
                borderColor: 'rgba(34, 197, 94, 1)',
                backgroundColor: 'rgba(34, 197, 94, 0.1)',
                borderWidth: 3,
                tension: 0.4,
                fill: true,
                pointRadius: 4
            },
            {
                label: 'Rekursif',
                data: recursiveTimes,
                borderColor: 'rgba(139, 92, 246, 1)',
                backgroundColor: 'rgba(139, 92, 246, 0.1)',
                borderWidth: 3,
                tension: 0.4,
                fill: true,
                pointRadius: 4
            }
        ]
    },
    options: {
        responsive: true,
        interaction: {
            mode: 'index',
            intersect: false
        },
        plugins: {
            legend: {
                display: true,
                position: 'top',
                labels: {
                    usePointStyle: true
                }
            },
            tooltip: {
                callbacks: {
                    label: function(context) {
                        return context.dataset.label + ': ' + 
                               context.parsed.y.toFixed(6) + ' ms';
                    }
                }
            }
        },
        scales: {
            y: {
                beginAtZero: true,
                title: {
                    display: true,
                    text: 'Waktu Eksekusi (ms)'
                }
            },
            x: {
                title: {
                    display: true,
                    text: 'Input Size (Pangkat)'
                }
            }
        }
    }
});
```

**Interpretasi Chart:**
- Garis hijau (iteratif) cenderung lebih rendah dan stabil
- Garis ungu (rekursif) lebih tinggi karena recursion overhead
- Kedua garis menunjukkan pertumbuhan linear O(n)
- Gap antar garis menunjukkan perbedaan performa

### 3.3.3 Data Table

Tabel data mentah menampilkan detail setiap pengujian:

| Input Size | Iteratif (ms) | Rekursif (ms) | Hasil (Ringkas) |
|-----------|---------------|---------------|-----------------|
| 10        | 0.000123      | 0.000245      | 1024            |
| 60        | 0.000678      | 0.001234      | 115292...       |
| ...       | ...           | ...           | ...             |

**Fitur:**
- Data presisi 6 desimal
- Hasil dipangkas jika > 50 karakter
- Animasi fade-in per row
- Highlight warna untuk tipe algoritma

### 3.3.4 Metrics Cards

Kartu statistik menampilkan ringkasan:

```
┌─────────────────────────┐  ┌─────────────────────────┐
│  📊 Rata-rata Iteratif  │  │  📊 Rata-rata Rekursif  │
│     0.234567 ms         │  │     0.456789 ms         │
└─────────────────────────┘  └─────────────────────────┘
```

**Kesimpulan Otomatis:**
```
💡 Secara rata-rata, Iteratif 1.95x lebih cepat 
   daripada Rekursif pada range ini.
```

### 3.3.5 UI/UX Design

**Glassmorphism Design:**
- Background gradient dengan animated floating orbs
- Kartu semi-transparan dengan `backdrop-filter: blur()`
- Shadow dan border subtle untuk depth
- Warna: Gradient dari biru tua (#0F172A) ke putih

**Animasi:**
1. **Fade-in**: Elemen muncul dengan opacity 0 → 1
2. **Slide-up**: Elemen bergeser dari bawah dengan transform
3. **Hover Effects**: Kartu ter-lift dengan scale dan shadow
4. **Loading Spinner**: Multi-ring spinner dengan blur backdrop
5. **Progress Bar**: Animated width dengan gradient background

**Responsiveness:**
- Mobile-first approach
- Breakpoints untuk tablet dan desktop
- Navigation burger menu untuk mobile
- Chart resize otomatis

---

## 3.4 Lingkungan Implementasi

### 3.4.1 Spesifikasi Perangkat Lunak

**Backend:**
- **Python**: 3.8 atau lebih baru
- **Flask**: 3.0.0 (Web framework)
- **Werkzeug**: 3.0.1 (WSGI utility library)
- **Jinja2**: 3.1.2 (Template engine)
- **Gunicorn**: 21.2.0 (Production server)

**Frontend:**
- **HTML5**: Struktur semantic
- **CSS3**: Custom styling dengan modern features
  - Flexbox & Grid
  - CSS Variables
  - Animations & Transitions
  - Backdrop-filter (Glassmorphism)
- **JavaScript ES6+**: 
  - Fetch API untuk AJAX
  - Async/await
  - Arrow functions
  - Template literals

**Library Eksternal:**
- **Chart.js**: 4.4.0 (Data visualization)
- **Font Awesome**: 6.4.0 (Icons)
- **Google Fonts**: Plus Jakarta Sans (Typography)

### 3.4.2 Dependencies (requirements.txt)

```
Flask==3.0.0
Werkzeug==3.0.1
Jinja2==3.1.2
MarkupSafe==2.1.3
itsdangerous==2.1.2
click==8.1.7
gunicorn==21.2.0
```

**Penjelasan:**
- `Flask`: Framework web utama
- `Werkzeug`: Utilities untuk Flask (routing, request handling)
- `Jinja2`: Template engine untuk rendering HTML
- `MarkupSafe`: Escaping string untuk security
- `itsdangerous`: Signing data untuk sessions
- `click`: CLI untuk Flask commands
- `gunicorn`: Production WSGI server (untuk deployment)

### 3.4.3 Konfigurasi Aplikasi

**File: app.py**
```python
from flask import Flask, render_template, request, jsonify
import time
import sys

# Konfigurasi aplikasi Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'tubesakaanalisisalgoritma2025'

# Menambah batas rekursi
sys.setrecursionlimit(20000)
```

**Konfigurasi Penting:**
- `SECRET_KEY`: Untuk session security (bisa diganti untuk production)
- `setrecursionlimit(20000)`: Mengizinkan rekursi lebih dalam (default: 1000)

### 3.4.4 Environment Setup

**1. Instalasi Python**
   - Minimal Python 3.8
   - Includes pip (package manager)

**2. Virtual Environment (Opsional tapi Recommended)**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

**4. Menjalankan Aplikasi**

**Development Mode:**
```bash
python app.py
```
Output:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: off
```

**Production Mode:**
```bash
gunicorn app:app --bind 0.0.0.0:5000 --workers 4
```

### 3.4.5 Struktur File Lengkap

```
d:\tubesAKA2\coba\
│
├── app.py                      # Flask backend (301 lines)
├── requirements.txt            # Dependencies list
├── README.md                   # Dokumentasi proyek
├── CARA_MENJALANKAN.md        # Panduan instalasi
├── Procfile                    # Untuk deployment (Heroku/Render)
├── render.yaml                 # Konfigurasi Render deployment
├── vercel.json                 # Konfigurasi Vercel deployment
│
├── templates/                  # HTML Templates
│   ├── base.html              # Base template dengan navigation
│   ├── theory.html            # Halaman teori (177 lines)
│   ├── single_test.html       # Single input analysis (263 lines)
│   └── range_test.html        # Range & graph analysis (377 lines)
│
└── static/                     # Static Assets
    ├── css/
    │   └── style.css          # Glassmorphism styling
    ├── js/
    │   └── main.js            # JavaScript utilities
    └── images/                 # Image assets (if any)
```

### 3.4.6 Browser Compatibility

**Supported Browsers:**
- Google Chrome 90+ (Recommended)
- Mozilla Firefox 88+
- Microsoft Edge 90+
- Safari 14+
- Opera 76+

**Required Features:**
- ES6+ JavaScript support
- CSS3 features (Flexbox, Grid, Backdrop-filter)
- Fetch API
- Chart.js compatibility

### 3.4.7 Deployment Options

Aplikasi dapat di-deploy ke berbagai platform:

**1. Vercel (Serverless)**
   - File: `vercel.json`
   - Serverless Python functions
   - Otomatis CDN untuk static files

**2. Render (PaaS)**
   - File: `render.yaml`
   - Auto-deploy dari Git
   - Free tier tersedia

**3. Heroku (PaaS)**
   - File: `Procfile`
   - Gunicorn sebagai production server
   - Easy scaling

**4. VPS (Manual)**
   - Install Python + dependencies
   - Nginx sebagai reverse proxy
   - Gunicorn sebagai application server
   - SSL dengan Let's Encrypt

---

## Kesimpulan Bab III

Implementasi sistem analisis perbandingan algoritma iteratif dan rekursif telah berhasil dikembangkan menggunakan Flask sebagai backend dan teknologi web modern untuk frontend. Sistem ini menyediakan tiga fitur utama: halaman teori untuk pemahaman konseptual, single input analysis untuk perbandingan detail, dan range & graph analysis untuk analisis tren.

Visualisasi data menggunakan Chart.js memberikan representasi grafis yang intuitif untuk memahami perbedaan performa kedua algoritma. Desain glassmorphism dan animasi yang halus meningkatkan user experience. Lingkungan implementasi yang terdefinisi dengan baik memastikan aplikasi dapat dijalankan dengan konsisten di berbagai platform dan dapat di-deploy ke berbagai hosting provider.

Pada BAB IV akan dibahas hasil pengujian sistem dan analisis perbandingan performa antara algoritma iteratif dan rekursif berdasarkan data yang dikumpulkan dari berbagai skenario pengujian.
