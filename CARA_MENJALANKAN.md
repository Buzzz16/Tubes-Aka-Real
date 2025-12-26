# 📋 Panduan Instalasi & Menjalankan Aplikasi
## Proyek Analisis Algoritma Pertumbuhan Bakteri

<div align="center">

![Install](https://img.shields.io/badge/📥-Installation_Guide-22C55E?style=for-the-badge)
![Student](https://img.shields.io/badge/🎓-Student_Project-10B981?style=for-the-badge)

**Panduan langkah demi langkah untuk menjalankan aplikasi di komputer lokal (Localhost).**

</div>

---

## 📋 Prasyarat Sistem

Sebelum memulai, pastikan komputer Anda memiliki:

| Requirement | Versi Minimal | Keterangan |
|-------------|---------------|------------|
| 🐍 **Python** | 3.8+ | Bahasa pemrograman utama |
| 📦 **pip** | Latest | Package manager Python |
| 🌐 **Browser** | Chrome/Edge | Untuk tampilan terbaik |

---

## 🛠️ Langkah Instalasi

### 1️⃣ Buka Terminal / Command Prompt

**Windows:**
Tekan `Win + R`, ketik `cmd`, lalu Enter.

**Mac/Linux:**
Buka aplikasi Terminal.

---

### 2️⃣ Masuk ke Folder Proyek

Arahkan terminal ke folder dimana Anda menyimpan file proyek ini.
```bash
cd path/to/aka-bakteri
```

---

### 3️⃣ (Opsional) Buat Lingkungan Virtual
Disarankan agar library tidak tercampur dengan sistem utama.

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

✅ Jika berhasil, akan muncul tulisan `(venv)` di awal baris terminal.

---

### 4️⃣ Install Library Pendukung

Install semua kebutuhan aplikasi (Flask, dll) dengan satu perintah:

```bash
pip install -r requirements.txt
```

⏳ Tunggu hingga proses selesai.

---

### 5️⃣ Jalankan Aplikasi

```bash
python app.py
```

Jika berhasil, akan muncul pesan seperti ini:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

---

### 6️⃣ Buka Aplikasi

Buka browser dan kunjungi alamat:
👉 **http://localhost:5000**

---

## 🐛 Troubleshooting (Masalah Umum)

### ❌ "Python is not recognized..."
**Solusi:** Pastikan Python sudah diinstall dan ditambahkan ke PATH environment variable Windows.

### ❌ "ModuleNotFoundError: No module named 'flask'"
**Solusi:** Ulangi langkah nomor 4 (`pip install -r requirements.txt`).

### ❌ Port 5000 Error / Already in Use
**Solusi:**
Buka `app.py`, cari baris paling bawah, ubah menjadi:
```python
app.run(debug=True, port=5001)
```
Lalu jalankan ulang dan buka `http://localhost:5001`.

---

<div align="center">

**Terima kasih telah mencoba aplikasi ini!**
*Semoga mendapatkan nilai terbaik! Aamiin.* 🤲

</div>
