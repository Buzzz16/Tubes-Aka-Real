# ☁️ Panduan Deployment
## Membawa Aplikasi ke Internet

<div align="center">

![Cloud](https://img.shields.io/badge/☁️-Deployment-22C55E?style=for-the-badge)
![Vercel](https://img.shields.io/badge/▲-Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)

**Panduan untuk Dosen/Mahasiswa yang ingin mengonlinekan aplikasi ini.**

</div>

---

## 1. Vercel (Rekomendasi)
Paling mudah dan gratis untuk proyek mahasiswa.

1. **Install Vercel CLI**:
   ```bash
   npm i -g vercel
   ```
2. **Login**:
   ```bash
   vercel login
   ```
3. **Deploy**:
   ```bash
   vercel
   ```
   - Jawab `Y` untuk setup.
   - Pilih scope (akun anda).
   - Link ke existing project? `N`.
   - Project name? `aka-bakteri`.
   - Directory? `./`.
   - Settings? Default (No).

4. **Selesai!** Anda akan dapat link `https://aka-bakteri.vercel.app`.

*Catatan: File `vercel.json` sudah disiapkan di proyek ini.*

---

## 2. Render.com
Alternatif bagus jika butuh server yang selalu aktif (walaupun versi free akan sleep).

1. Buat akun di [Render.com](https://render.com).
2. Klik **New +** -> **Web Service**.
3. Connect repository GitHub anda.
4. Settings:
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
5. Klik **Create Web Service**.

*Catatan: File `render.yaml` sudah disiapkan.*

---

## 3. PythonAnywhere
Sering digunakan di lingkungan akademik.

1. Daftar akun Beginner (Gratis).
2. Buka tab **Bash** console.
3. Clone repo:
   ```bash
   git clone https://github.com/username/aka-bakteri.git
   ```
4. Buat Virtualenv di tab **Web**.
5. Point WSGI configuration file ke `app.py`.

---

<div align="center">

**Siap dipresentasikan di kelas! 🎓**

</div>
