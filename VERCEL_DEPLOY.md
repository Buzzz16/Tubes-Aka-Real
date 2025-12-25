# 🚀 Cara Deploy ke Vercel (MUDAH & GRATIS)

## ✅ File Sudah Siap!

File `vercel.json` sudah dibuat dan di-push ke GitHub ✅

---

## 📝 Langkah Deploy ke Vercel

### **Metode 1: Via Website Vercel (TERMUDAH - 3 MENIT)**

#### **Step 1: Login ke Vercel**
1. Buka: **https://vercel.com**
2. Klik **"Sign Up"** atau **"Login"**
3. Pilih **"Continue with GitHub"**
4. Authorize Vercel untuk akses GitHub

#### **Step 2: Import Project**
1. Di dashboard Vercel, klik **"Add New..."** → **"Project"**
2. Pilih **"Import Git Repository"**
3. Cari repository: **`Buzzz16/Tubes-Aka-Real`**
4. Klik **"Import"**

#### **Step 3: Configure Project**
Vercel akan auto-detect Python/Flask. Setting default sudah OK:

```
Framework Preset: Other
Build Command: (kosongkan atau: pip install -r requirements.txt)
Output Directory: (kosongkan)
Install Command: pip install -r requirements.txt
```

**Root Directory**: `.` (root)

#### **Step 4: Deploy!**
1. Klik **"Deploy"**
2. Tunggu 2-3 menit (building...)
3. ✅ **DONE!**

**URL Live**: `https://tubes-aka-real.vercel.app`
(atau nama custom yang Vercel generate)

---

### **Metode 2: Via Vercel CLI (Untuk Developer)**

#### **Step 1: Install Vercel CLI**
```bash
npm install -g vercel
```

#### **Step 2: Login**
```bash
vercel login
```

#### **Step 3: Deploy**
```bash
cd d:\tubesAKA2\coba
vercel
```

Ikuti prompt:
- Set up and deploy? **Y**
- Which scope? **Your account**
- Link to existing project? **N**
- Project name? **tubes-aka-real**
- Directory? **./*** (enter untuk default)
- Auto-detected: **Y**

#### **Step 4: Production Deploy**
```bash
vercel --prod
```

**URL Live**: Link akan muncul di terminal

---

## 🎯 Setelah Deploy Berhasil

### **Custom Domain (Opsional)**
1. Di dashboard Vercel → Project settings
2. Klik **"Domains"**
3. Add domain (gratis .vercel.app atau custom domain sendiri)

### **Environment Variables (Jika Perlu)**
1. Dashboard → Project → Settings
2. **"Environment Variables"**
3. Add variables (misalnya SECRET_KEY)

---

## 🔄 Auto Deploy dari GitHub

Setiap kali Anda push ke GitHub:
```bash
git add .
git commit -m "Update fitur baru"
git push
```

Vercel akan **otomatis re-deploy** dalam 2-3 menit! 🚀

---

## ✅ Kelebihan Vercel

- ✅ **100% Gratis** (unlimited bandwidth untuk hobby)
- ✅ **Auto Deploy** dari GitHub
- ✅ **SSL/HTTPS** included
- ✅ **CDN Global** (super cepat)
- ✅ **Custom domain** gratis
- ✅ **No sleep** (always on, tidak seperti Render free)
- ✅ **Instant rollback** jika ada masalah

---

## 📊 Vercel vs Platform Lain

| Fitur | Vercel | Render | Railway |
|-------|--------|--------|---------|
| Gratis | ✅ Unlimited | ✅ Tapi sleep | $5 credit |
| Auto Deploy | ✅ Yes | ✅ Yes | ✅ Yes |
| Custom Domain | ✅ Free | ✅ Free | ✅ Free |
| CDN Global | ✅ Yes | ❌ No | ❌ No |
| Always On | ✅ Yes | ❌ Sleep idle | ✅ Yes |

---

## ⚠️ Troubleshooting

### **Error: "Build Failed"**
**Solusi:**
- Check `requirements.txt` lengkap
- Pastikan Python version compatible (3.9-3.11)

### **Error: "Module not found"**
**Solusi:**
- Vercel menginstall dari `requirements.txt`
- Pastikan semua dependencies tercantum

### **Static files tidak muncul**
**Solusi:**
- Check `vercel.json` routes sudah benar
- Path harus `/static/...` bukan `static/...`

### **App tidak berjalan**
**Solusi:**
- Check logs di Vercel dashboard
- Tab "Deployments" → Pilih deployment → "View Function Logs"

---

## 🎓 Untuk Tugas Kuliah

**Share Link ke Dosen:**
```
Live Demo: https://tubes-aka-real.vercel.app
GitHub: https://github.com/Buzzz16/Tubes-Aka-Real
```

**Screenshot untuk Laporan:**
1. Tampilan website deployed
2. Dashboard Vercel (showing deployment success)
3. GitHub commits history

---

## 💡 Tips Pro

1. **Preview Deployment**: Setiap branch otomatis dapat preview URL
2. **Analytics**: Dashboard Vercel punya analytics gratis
3. **Performance**: Vercel optimized untuk performance
4. **Monitoring**: Built-in error tracking

---

## 🚀 Ready to Deploy!

**Sekarang tinggal:**
1. Buka: **https://vercel.com**
2. Login dengan GitHub
3. Import `Buzzz16/Tubes-Aka-Real`
4. Klik Deploy
5. **DONE!** 🎉

**Deployment selesai dalam 3 menit!**

---

## 📞 Butuh Bantuan?

Dokumentasi Vercel: https://vercel.com/docs
Support: https://vercel.com/support

---

**Good luck dengan deployment! 🚀**

File sudah siap, tinggal deploy via dashboard Vercel!
