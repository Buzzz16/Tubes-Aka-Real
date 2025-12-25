# 🚀 Panduan Instalasi dan Menjalankan Aplikasi

## Prasyarat

1. **Python 3.8 atau lebih baru** harus sudah terinstall
2. **pip** (Python package manager)
3. **Web browser** modern (Chrome, Firefox, Edge, Safari)

## Langkah-Langkah Instalasi

### 1. Buka Terminal/Command Prompt

**Windows:**
- Tekan `Win + R`, ketik `cmd`, Enter
- Atau gunakan PowerShell

**Mac/Linux:**
- Buka Terminal

### 2. Navigasi ke Folder Proyek

```bash
cd d:\tubesAKA2\coba
```

### 3. (Opsional) Buat Virtual Environment

Virtual environment direkomendasikan untuk mengisolasi dependencies:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

Tunggu hingga semua package terinstall.

### 5. Jalankan Aplikasi Flask

```bash
python app.py
```

Anda akan melihat output seperti:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://0.0.0.0:5000
 * Running on http://127.0.0.1:5000
```

### 6. Buka Browser

Buka browser dan akses salah satu URL berikut:
- `http://localhost:5000`
- `http://127.0.0.1:5000`

## 🎯 Cara Menggunakan Aplikasi

### Halaman Teori
1. Halaman ini akan terbuka secara otomatis saat pertama kali akses
2. Baca penjelasan tentang algoritma iteratif dan rekursif
3. Pahami konsep time complexity dan space complexity

### Single Input Analysis
1. Klik menu "Single Test" di navigation bar
2. Masukkan nilai **Basis** (contoh: 2)
3. Masukkan nilai **Pangkat** (contoh: 900)
4. Klik tombol "Mulai Analisis"
5. Lihat hasil perbandingan waktu eksekusi
6. Perhatikan grafik bar chart yang muncul

### Range & Graph Analysis
1. Klik menu "Range & Graph" di navigation bar
2. Masukkan parameter:
   - **Basis**: 2
   - **Start Pangkat**: 10
   - **End Pangkat**: 2000
   - **Interval**: 50
3. Klik tombol "Generate Grafik & Analisis"
4. Tunggu progress bar selesai
5. Lihat hasil:
   - Line chart tren waktu eksekusi
   - Statistik rata-rata
   - Tabel data mentah

## ⚠️ Troubleshooting

### Error: Port sudah digunakan
Jika port 5000 sudah digunakan, ubah di `app.py` baris terakhir:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Ganti ke port lain
```

### Error: Module not found
Pastikan semua dependencies sudah terinstall:
```bash
pip install Flask
```

### RecursionError pada input besar
Ini normal untuk algoritma rekursif. Gunakan input pangkat < 3000 untuk hasil terbaik.

### Browser tidak memuat CSS/JS
1. Clear browser cache (Ctrl + Shift + Delete)
2. Hard refresh (Ctrl + F5)
3. Pastikan Flask running tanpa error

## 🛑 Menghentikan Aplikasi

Di terminal/command prompt, tekan:
- **Windows**: `Ctrl + C`
- **Mac/Linux**: `Ctrl + C`

## 📱 Tips Penggunaan

1. **Input Optimal**:
   - Single Test: Pangkat 100-2000
   - Range Test: Range 10-3000 dengan step 50-100

2. **Browser Terbaik**:
   - Chrome (recommended)
   - Firefox
   - Edge

3. **Performance**:
   - Untuk range test besar, gunakan interval yang lebih besar
   - Jangan menutup browser saat processing

## 🎓 Untuk Presentasi/Demo

1. Siapkan beberapa test case:
   - Small input: Basis=2, Pangkat=100
   - Medium input: Basis=2, Pangkat=1000
   - Large input: Basis=2, Pangkat=2500

2. Tampilkan perbedaan waktu eksekusi yang jelas

3. Jelaskan grafik dengan baik

## 📞 Support

Jika ada masalah, pastikan:
- ✅ Python terinstall dengan benar
- ✅ Semua file ada di folder yang benar
- ✅ Dependencies sudah terinstall
- ✅ Port tidak bentrok dengan aplikasi lain

---

**Selamat mencoba! 🚀**
