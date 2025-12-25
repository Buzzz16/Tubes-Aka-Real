# 📂 STRUKTUR LENGKAP PROYEK

## Directory Tree

```
d:\tubesAKA2\coba\
│
├── 📄 app.py                           # Flask Application (Backend)
│   ├── Core Algorithms:
│   │   ├── pangkatIteratif()          # O(n) time, O(1) space
│   │   ├── pangkatRekursif()          # O(n) time, O(n) space
│   │   └── measure_time()             # Pengukuran waktu (ms)
│   │
│   └── Routes:
│       ├── GET  /                     → theory.html
│       ├── GET  /theory               → theory.html
│       ├── GET  /single-test          → single_test.html
│       ├── POST /single-test          → JSON response
│       ├── GET  /range-test           → range_test.html
│       └── POST /range-test           → JSON response
│
├── 📁 templates/                       # Jinja2 Templates
│   │
│   ├── 📄 base.html                   # Base Template
│   │   ├── Navigation bar (glassmorphism)
│   │   ├── Animated background (3 gradient orbs)
│   │   ├── Footer dengan credits
│   │   └── Loading overlay (multi-ring spinner)
│   │
│   ├── 📄 theory.html                 # Halaman Teori
│   │   ├── Hero section
│   │   ├── Penjelasan algoritma iteratif
│   │   ├── Penjelasan algoritma rekursif
│   │   ├── Code showcase + pseudocode
│   │   ├── Recursion overhead warning
│   │   └── CTA buttons ke testing pages
│   │
│   ├── 📄 single_test.html            # Single Input Analysis
│   │   ├── Form input (basis, pangkat)
│   │   ├── Warning alert (conditional)
│   │   ├── Validation status
│   │   ├── Metrics cards (rekursif, iteratif)
│   │   ├── Conclusion section
│   │   ├── Bar chart (Chart.js)
│   │   └── JavaScript untuk AJAX + chart
│   │
│   └── 📄 range_test.html             # Range & Graph Analysis
│       ├── Form range input (basis, start, end, step)
│       ├── Progress bar section
│       ├── Line chart (Chart.js)
│       ├── Statistics (avg iteratif, avg rekursif)
│       ├── Conclusion box
│       ├── Data table (sortable)
│       └── JavaScript untuk AJAX + chart + table
│
├── 📁 static/                          # Static Files
│   │
│   ├── 📁 css/
│   │   └── 📄 style.css               # Main Stylesheet (1700+ lines)
│   │       ├── CSS Variables (color palette)
│   │       ├── Animated background (floating orbs)
│   │       ├── Glassmorphism effects
│   │       ├── Navigation (responsive)
│   │       ├── Hero sections
│   │       ├── Form styling
│   │       ├── Card components
│   │       ├── Metrics & charts
│   │       ├── Table styling
│   │       ├── Animations (keyframes)
│   │       └── Media queries (responsive)
│   │
│   ├── 📁 js/
│   │   └── 📄 main.js                 # Main JavaScript
│   │       ├── Navigation interactions
│   │       ├── Mobile menu toggle
│   │       ├── Scroll effects
│   │       ├── Form animations
│   │       ├── Button hover effects
│   │       ├── Card tilt effect
│   │       ├── Intersection observer
│   │       ├── Chart.js config
│   │       └── Utility functions
│   │
│   └── 📁 images/                     # Images Folder
│       └── (Kosong - siap untuk gambar pseudocode/screenshots)
│
├── 📄 requirements.txt                 # Python Dependencies
│   ├── Flask==3.0.0
│   ├── Werkzeug==3.0.1
│   ├── Jinja2==3.1.2
│   ├── MarkupSafe==2.1.3
│   ├── itsdangerous==2.1.2
│   └── click==8.1.7
│
├── 📄 README.md                        # Dokumentasi Utama
│   ├── Fitur aplikasi
│   ├── Teknologi yang digunakan
│   ├── Cara instalasi
│   ├── Logika algoritma
│   ├── Alur kerja aplikasi
│   └── Endpoint API
│
├── 📄 CARA_MENJALANKAN.md             # Panduan Instalasi Detail
│   ├── Prasyarat
│   ├── Langkah instalasi step-by-step
│   ├── Cara menggunakan aplikasi
│   ├── Troubleshooting
│   └── Tips penggunaan
│
├── 📄 RINGKASAN_PROYEK.md             # Summary Lengkap
│   ├── Checklist fitur
│   ├── Perbandingan Streamlit vs Flask
│   ├── File-file penting
│   ├── Keunggulan implementasi
│   └── Poin untuk presentasi
│
├── 📄 QUICK_START.md                   # Panduan Cepat
│   ├── Instalasi 3 langkah
│   ├── Test case recommended
│   ├── Common issues & solutions
│   └── Tips untuk demo
│
├── 📄 STRUKTUR_PROYEK.md              # File ini
│   └── Penjelasan struktur detail
│
└── 📄 .gitignore                       # Git Ignore
    ├── Python cache (__pycache__)
    ├── Virtual environment (venv/)
    ├── IDE files (.vscode/, .idea/)
    └── OS files (.DS_Store)
```

## 📊 Statistik Proyek

### Lines of Code (Approx.)
- **Python (app.py)**: ~200 lines
- **HTML (4 files)**: ~600 lines
- **CSS (style.css)**: ~1,700 lines
- **JavaScript (main.js)**: ~400 lines
- **Total**: ~2,900 lines

### File Count
- Python: 1 file
- HTML Templates: 4 files
- CSS: 1 file
- JavaScript: 1 file
- Markdown Docs: 6 files
- Config: 2 files (.gitignore, requirements.txt)
- **Total**: 15 files

### Dependencies
- Python packages: 6
- CDN libraries: 3 (Chart.js, Font Awesome, Google Fonts)

## 🎯 Flow Diagram

### Request-Response Flow

```
┌──────────┐
│ Browser  │
└────┬─────┘
     │ HTTP GET /theory
     ▼
┌──────────────┐
│ Flask App    │ → render_template('theory.html')
└────┬─────────┘
     │
     ▼
┌──────────────┐
│ Jinja2       │ → Proses template
└────┬─────────┘
     │
     ▼
┌──────────────┐
│ HTML + CSS   │ → Load static files
│ + JavaScript │
└────┬─────────┘
     │
     ▼
┌──────────────┐
│ Browser      │ → Tampilkan halaman
│ (Rendered)   │
└──────────────┘


┌──────────┐
│ User     │
│ Submit   │
│ Form     │
└────┬─────┘
     │ POST /single-test (AJAX)
     ▼
┌──────────────┐
│ Flask Route  │
└────┬─────────┘
     │
     ▼
┌──────────────────┐
│ pangkatIteratif  │ → measure_time()
└────┬─────────────┘
     │
     ▼
┌──────────────────┐
│ pangkatRekursif  │ → measure_time()
└────┬─────────────┘
     │
     ▼
┌──────────────┐
│ JSON Response│ → {success, time_iter, time_rec, ...}
└────┬─────────┘
     │
     ▼
┌──────────────┐
│ JavaScript   │ → Parse JSON
└────┬─────────┘
     │
     ▼
┌──────────────┐
│ Chart.js     │ → Render chart
└────┬─────────┘
     │
     ▼
┌──────────────┐
│ Update DOM   │ → Display results
└──────────────┘
```

## 🎨 Design System

### Color Palette
```css
Primary Dark:   #0F172A (Slate 900)
Primary Navy:   #1E293B (Slate 800)
Primary Slate:  #334155 (Slate 700)
Accent Blue:    #3B82F6 (Blue 500)
Accent Purple:  #8B5CF6 (Violet 500)
Accent Green:   #22C55E (Green 500)
Accent Cyan:    #06B6D4 (Cyan 500)
Text White:     #F8FAFC (Slate 50)
Text Light:     #E2E8F0 (Slate 200)
Text Gray:      #CBD5E1 (Slate 300)
Text Muted:     #94A3B8 (Slate 400)
```

### Typography
- **Font Family**: Plus Jakarta Sans
- **Weights**: 400 (Regular), 500 (Medium), 600 (Semibold), 700 (Bold), 800 (Extrabold)

### Spacing Scale
- XS: 0.5rem (8px)
- SM: 1rem (16px)
- MD: 1.5rem (24px)
- LG: 2rem (32px)
- XL: 3rem (48px)

### Border Radius
- SM: 8px
- MD: 12px
- LG: 16px
- XL: 24px

## 🔧 Technology Stack

### Backend
- **Framework**: Flask 3.0.0
- **Template Engine**: Jinja2
- **Language**: Python 3.8+

### Frontend
- **Markup**: HTML5
- **Styling**: CSS3 (Custom, no frameworks)
- **Scripting**: Vanilla JavaScript (ES6+)
- **Charts**: Chart.js 4.4.0

### External Libraries (CDN)
1. **Chart.js** - Data visualization
2. **Font Awesome 6.4.0** - Icons
3. **Google Fonts** - Typography

### Development Tools
- Git (version control)
- VS Code (recommended IDE)
- Browser DevTools

## 📝 Naming Conventions

### Python (app.py)
- Functions: `camelCase` (sesuai original: `pangkatIteratif`)
- Variables: `snake_case` (Flask standard)
- Routes: `kebab-case` (/single-test)

### HTML Templates
- Files: `snake_case.html`
- IDs: `camelCase` (#loadingOverlay)
- Classes: `kebab-case` (.glass-card)

### CSS
- Classes: `kebab-case`
- IDs: `camelCase`
- Variables: `--kebab-case`

### JavaScript
- Functions: `camelCase`
- Variables: `camelCase`
- Constants: `UPPER_SNAKE_CASE`

## 🚀 Deployment Ready

### Checklist
- ✅ Production-ready code
- ✅ No hardcoded secrets
- ✅ Error handling
- ✅ Responsive design
- ✅ Cross-browser compatible
- ✅ Documentation complete
- ✅ .gitignore configured

### Recommended Hosting
- **Heroku** - Easy deployment
- **PythonAnywhere** - Python-specific
- **Render** - Modern platform
- **Railway** - Simple setup

## 📚 Documentation Files

1. **README.md** - Main documentation
2. **CARA_MENJALANKAN.md** - Installation guide
3. **RINGKASAN_PROYEK.md** - Project summary
4. **QUICK_START.md** - Quick reference
5. **STRUKTUR_PROYEK.md** - This file
6. **Code Comments** - Inline documentation

---

**Dibuat dengan ❤️ menggunakan Flask & modern web technologies**

**© 2025 - Tugas Besar Analisis Kompleksitas Algoritma**
