# 🎯 QUICK START GUIDE

## Instalasi Cepat (3 Langkah)

### Step 1: Install Flask
```bash
pip install Flask
```

### Step 2: Jalankan Aplikasi
```bash
cd d:\tubesAKA2\coba
python app.py
```

### Step 3: Buka Browser
```
http://localhost:5000
```

---

## 🎨 Preview Fitur

### 1. Halaman Theory
- URL: `http://localhost:5000/theory`
- Konten: Penjelasan algoritma, kompleksitas, kode

### 2. Single Test
- URL: `http://localhost:5000/single-test`
- Input: Basis = 2, Pangkat = 900
- Output: Grafik bar chart + waktu eksekusi

### 3. Range & Graph
- URL: `http://localhost:5000/range-test`
- Input: Basis=2, Start=10, End=2000, Step=50
- Output: Line chart + tabel data

---

## 🔥 Test Case Recommended

### Test 1: Small Input
- Basis: 2
- Pangkat: 100
- Expected: Kedua algoritma sangat cepat

### Test 2: Medium Input
- Basis: 2
- Pangkat: 1000
- Expected: Perbedaan waktu mulai terlihat

### Test 3: Large Input
- Basis: 2
- Pangkat: 2500
- Expected: Rekursif jauh lebih lambat

### Test 4: Range Analysis
- Basis: 2
- Start: 10
- End: 3000
- Step: 100
- Expected: Grafik tren naik linear

---

## ⚡ Keyboard Shortcuts

- `Ctrl/Cmd + K` - Focus ke input pertama
- `ESC` - Close mobile menu
- `Ctrl + F5` - Hard refresh (jika CSS tidak muncul)

---

## 🐛 Common Issues & Solutions

### Issue 1: "Module 'flask' not found"
**Solution:**
```bash
pip install Flask
```

### Issue 2: "Port 5000 already in use"
**Solution:** Edit `app.py` line terakhir:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Issue 3: "RecursionError"
**Solution:** Gunakan pangkat < 3000 atau tingkatkan limit di `app.py`:
```python
sys.setrecursionlimit(30000)  # Hati-hati, bisa crash
```

### Issue 4: CSS/JS tidak muncul
**Solution:**
1. Hard refresh: `Ctrl + Shift + R`
2. Clear cache: `Ctrl + Shift + Delete`
3. Check terminal untuk error

---

## 📊 Expected Results

### Single Test (Basis=2, Pangkat=1000)
- Iteratif: ~0.05-0.15 ms
- Rekursif: ~0.20-0.50 ms
- **Iteratif 2-3x lebih cepat**

### Range Test (Basis=2, Range=10-2000)
- Grafik: Linear growth untuk kedua
- Rekursif selalu di atas iteratif
- Rata-rata iteratif < rata-rata rekursif

---

## 💡 Tips untuk Demo/Presentasi

1. **Siapkan browser dalam fullscreen mode**
2. **Test semua fitur sebelum presentasi**
3. **Gunakan input yang sudah teruji**
4. **Jelaskan grafik dengan jelas**
5. **Highlight perbedaan waktu eksekusi**

---

## 🎓 Penjelasan untuk Laporan

### Perbandingan dengan Streamlit:
1. **Flask** memberikan kontrol penuh atas UI/UX
2. **Custom CSS** memungkinkan desain glassmorphism
3. **Chart.js** lebih fleksibel daripada Altair
4. **JavaScript** memungkinkan animasi kompleks
5. **Routing** lebih eksplisit dan mudah dipahami

### Keunggulan Implementasi:
1. Modular dan maintainable
2. Responsive design (mobile-friendly)
3. Animasi yang engaging
4. Error handling yang robust
5. Dokumentasi lengkap

---

## 📞 Troubleshooting Checklist

- [ ] Python 3.8+ terinstall?
- [ ] Flask sudah di-install via pip?
- [ ] Sudah di folder yang benar? (`cd d:\tubesAKA2\coba`)
- [ ] Port 5000 available?
- [ ] Browser sudah updated?
- [ ] JavaScript enabled di browser?

---

## ✅ Verification Steps

Setelah aplikasi berjalan, test:

1. ✅ Navigation links berfungsi
2. ✅ Form bisa di-submit
3. ✅ Loading overlay muncul
4. ✅ Chart ter-render dengan benar
5. ✅ Animasi smooth
6. ✅ Responsive di mobile
7. ✅ Data table muncul
8. ✅ Footer tampil di bawah

---

**Jika semua berjalan lancar, aplikasi siap digunakan! 🎉**

---

**Need Help?** 
- Baca `README.md` untuk dokumentasi lengkap
- Baca `CARA_MENJALANKAN.md` untuk panduan detail
- Baca `RINGKASAN_PROYEK.md` untuk overview teknis
