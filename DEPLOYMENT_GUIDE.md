# 🚀 Panduan Deployment Murah/Gratis

## 🆓 Opsi Deployment Gratis/Murah

### 1. **Render.com (RECOMMENDED - Gratis Selamanya)**

#### ✅ Kelebihan:
- ✅ **100% Gratis untuk tier free**
- ✅ Otomatis deploy dari GitHub
- ✅ SSL/HTTPS included
- ✅ Custom domain support
- ✅ Sangat mudah setup (5 menit)
- ✅ Tidak perlu credit card

#### 📝 Langkah Deploy ke Render:

**Step 1: Buat file konfigurasi**
Buat file `render.yaml` di root project:

```yaml
services:
  - type: web
    name: tubes-aka-algoritma
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
```

**Step 2: Update requirements.txt**
Tambahkan `gunicorn` ke requirements.txt:
```
Flask==3.0.0
Werkzeug==3.0.1
Jinja2==3.1.2
MarkupSafe==2.1.3
itsdangerous==2.1.2
click==8.1.7
gunicorn==21.2.0
```

**Step 3: Deploy**
1. Daftar di https://render.com (gratis)
2. Klik "New +" → "Web Service"
3. Connect GitHub repository: `Buzzz16/Tubes-Aka-Real`
4. Pilih branch: `main`
5. Render akan auto-detect Python
6. Klik "Create Web Service"
7. Tunggu 3-5 menit
8. **DONE!** App live di: `https://tubes-aka-algoritma.onrender.com`

**⚠️ Catatan:**
- Free tier akan "sleep" setelah 15 menit idle
- First request setelah sleep butuh ~30 detik untuk "wake up"
- Untuk app always online, upgrade ke $7/bulan

---

### 2. **PythonAnywhere (Gratis untuk 1 App)**

#### ✅ Kelebihan:
- ✅ Gratis permanen untuk 1 web app
- ✅ Khusus Python (optimized)
- ✅ Console access
- ✅ 512MB storage
- ✅ Tidak ada credit card

#### 📝 Langkah Deploy:

1. **Daftar**: https://www.pythonanywhere.com/registration/register/beginner/
2. **Clone repo**:
   ```bash
   git clone https://github.com/Buzzz16/Tubes-Aka-Real.git
   cd Tubes-Aka-Real
   ```
3. **Create virtual environment**:
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
4. **Configure Web App**:
   - Go to "Web" tab
   - Add new web app
   - Choose Flask
   - Set source code: `/home/yourusername/Tubes-Aka-Real`
   - Set WSGI file path
5. **Edit WSGI file**:
   ```python
   import sys
   path = '/home/yourusername/Tubes-Aka-Real'
   if path not in sys.path:
       sys.path.insert(0, path)
   
   from app import app as application
   ```
6. **Reload web app**
7. **Live di**: `https://yourusername.pythonanywhere.com`

**⚠️ Limitasi Free:**
- 1 web app only
- CPU time limited
- Tidak bisa custom domain di free tier

---

### 3. **Railway.app (Free $5 Credit)**

#### ✅ Kelebihan:
- ✅ $5 credit gratis per bulan (cukup untuk hobby app)
- ✅ Auto deploy dari GitHub
- ✅ Super mudah (1 klik)
- ✅ Fast deployment
- ✅ Custom domain support

#### 📝 Langkah Deploy:

1. Daftar di https://railway.app
2. Klik "New Project"
3. Pilih "Deploy from GitHub repo"
4. Pilih `Buzzz16/Tubes-Aka-Real`
5. Railway auto-detect Flask
6. Add environment variable (jika perlu)
7. **DONE!** Auto deploy

**URL Live**: `https://tubes-aka-algoritma.up.railway.app`

**💰 Biaya:**
- $5 free credit/month
- Setelah itu ~$5/month untuk hobby app
- Bisa pause service saat tidak digunakan

---

### 4. **Vercel (Gratis, tapi butuh sedikit konfigurasi)**

#### ✅ Kelebihan:
- ✅ Gratis unlimited
- ✅ Super cepat (CDN global)
- ✅ Auto deploy dari GitHub
- ✅ Custom domain gratis

#### 📝 Langkah Deploy:

**Step 1: Install Vercel CLI**
```bash
npm install -g vercel
```

**Step 2: Buat file `vercel.json`**
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

**Step 3: Deploy**
```bash
cd d:\tubesAKA2\coba
vercel
```

**⚠️ Catatan:**
- Vercel lebih cocok untuk serverless
- Flask perlu sedikit adjustment untuk serverless

---

### 5. **Heroku (Gratis dihapus, sekarang $5/month minimum)**

Heroku sudah tidak gratis lagi, tapi tetap pilihan bagus untuk $5/month.

---

## 🏆 Rekomendasi Terbaik

### **Untuk Tugas Kuliah / Demo:**
👉 **Render.com** (100% Gratis, Mudah, Reliable)

### **Untuk Production / Jangka Panjang:**
👉 **Railway.app** ($5/month dengan credit gratis)

### **Untuk Belajar Python Deployment:**
👉 **PythonAnywhere** (Gratis, Console Access)

---

## 📋 Checklist Deploy ke Render (Paling Mudah)

### **Preparation:**
- [x] Repository sudah di GitHub ✅
- [ ] Update `requirements.txt` tambahkan `gunicorn`
- [ ] Buat file `render.yaml` (opsional)
- [ ] Commit & push perubahan

### **Deploy Steps:**
1. [ ] Daftar di Render.com
2. [ ] New Web Service
3. [ ] Connect GitHub repo
4. [ ] Wait for build
5. [ ] Test URL live
6. [ ] Share link!

---

## 🔧 Persiapan File untuk Render

Saya akan buatkan file yang dibutuhkan:

### 1. Update `requirements.txt`
Tambahkan `gunicorn` untuk production server

### 2. Buat `Procfile` (opsional tapi recommended)
```
web: gunicorn app:app
```

### 3. Update `app.py` untuk production
Pastikan di akhir file:
```python
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

---

## 💰 Perbandingan Biaya

| Platform | Free Tier | Paid | Uptime | Custom Domain |
|----------|-----------|------|--------|---------------|
| **Render** | ✅ Free Forever | $7/mo | Sleep after idle | ✅ Yes |
| **Railway** | $5 credit/mo | $5+/mo | Always on | ✅ Yes |
| **PythonAnywhere** | ✅ 1 app free | $5/mo | Always on | Paid only |
| **Vercel** | ✅ Unlimited | $20/mo | Always on | ✅ Yes |
| **Heroku** | ❌ No more | $5/mo | Always on | ✅ Yes |

---

## 🎯 Solusi Terbaik untuk Anda

**Untuk DEMO TUGAS (Gratis 100%):**

```
1. Update requirements.txt (tambah gunicorn)
2. Push ke GitHub
3. Deploy ke Render.com (5 menit)
4. Share link: https://tubes-aka-real.onrender.com
```

**Total Cost: Rp 0,-** 🎉

---

## ⚠️ Tips Penting

1. **Jangan commit `.env` file** (sudah ada di `.gitignore`)
2. **Gunakan environment variables** untuk secret keys
3. **Set `debug=False`** di production
4. **Test locally** sebelum deploy
5. **Monitor usage** di free tier

---

## 🚨 Troubleshooting Deploy

### Error: "Application failed to start"
- Check `requirements.txt` lengkap
- Pastikan `gunicorn` terinstall
- Check logs di dashboard platform

### Error: "Module not found"
- Install semua dependencies di `requirements.txt`
- Check Python version compatibility

### App lambat/tidak respond
- Free tier biasanya sleep setelah idle
- First request butuh waktu untuk wake up
- Upgrade ke paid tier untuk always-on

---

## 📞 Butuh Bantuan?

Jika ada masalah saat deploy:
1. Check logs di platform dashboard
2. Baca dokumentasi platform
3. Join Discord community platform tersebut

---

**Pilihan Terbaik: Deploy ke Render.com (Gratis & Mudah)** 🚀

Butuh bantuan setup? Saya bisa bantu update file-file yang dibutuhkan!
