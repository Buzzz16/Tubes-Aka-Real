# 🦠 Analisis Perbandingan Efisiensi Algoritma
## Studi Kasus: Pertumbuhan Bakteri *Vibrio natriegens*

<div align="center">

![Banner](https://capsule-render.vercel.app/api?type=waving&color=22C55E&height=200&section=header&text=Bakteri%20V.%20natriegens&fontSize=50&animation=fadeIn&fontAlignY=38&desc=Analisis%20Algoritma%20Iteratif%20vs%20Rekursif&descAlignY=55&descAlign=50)

![Student Project](https://img.shields.io/badge/🎓-Student_Project-22C55E?style=for-the-badge)
![Assessment](https://img.shields.io/badge/📝-Dosen_Assessment-10B981?style=for-the-badge)
![Bacteria](https://img.shields.io/badge/🦠-Vibrio_natriegens-059669?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-14B8A6?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0.0-0D9488?style=for-the-badge&logo=flask&logoColor=white)

<br/>

**[ 🚀 Quick Start ](QUICK_START.md) • [ 📂 Struktur ](STRUKTUR_PROYEK.md) • [ 📝 Changelog ](CHANGELOG.md) • [ ☁️ Deploy ](DEPLOYMENT.md)**

<br/>

> *"Aplikasi ini dikembangkan sebagai tugas kuliah Analisis Kompleksitas Algoritma. Kami membuat aplikasi simulasi ilmiah pertumbuhan bakteri tercepat di dunia untuk memvisualisasikan perbedaan Big-O Notation pada algoritma Iteratif dan Rekursif secara nyata."*

</div>

---

## 📑 Daftar Isi
- [🎓 Konteks Pengembangan](#-konteks-pengembangan)
- [🧬 Mengapa Vibrio natriegens?](#-mengapa-vibrio-natriegens)
- [⚔️ Perbandingan Algoritma](#️-perbandingan-algoritma)
- [✨ Fitur Unggulan](#-fitur-unggulan)
- [🛠️ Teknologi](#️-teknologi)
- [🚀 Cara Menjalankan](#-cara-menjalankan)

---

## 🎓 Konteks Pengembangan

Proyek ini bertujuan untuk menjawab pertanyaan akademis:
> *"Bagaimana perbedaan performa algoritma Iteratif ($O(1)$ Space) dan Rekursif ($O(n)$ Space) saat menangani pertumbuhan eksponensial yang masif?"*

Kami tidak hanya membuat program CLI, tetapi membungkusnya dalam **Web App Modern** agar:
1.  **Visual**: Grafik memudahkan pemahaman data.
2.  **Interaktif**: Pengguna bisa mencoba berbagai skenario input.
3.  **Relevan**: Menggunakan studi kasus biologi nyata.

---

## 🧬 Mengapa *Vibrio natriegens*?

<div align="center">
<table>
<tr>
<td align="center" width="30%">
<h1>🦠</h1>
<b>Vibrio natriegens</b>
</td>
<td width="70%">

Bakteri ini adalah **organisme dengan pertumbuhan tercepat di dunia**.
- **Waktu Generasi**: ~10 Menit (E. coli butuh 20-30 menit).
- **Dampak Algoritma**: Dalam 24 jam, jumlah pembelahan sangat masif, membuat perbedaan efisiensi algoritma menjadi sangat krusial dan mudah diamati.

**Rumus Pertumbuhan:**
$$N(t) = N_0 \times 2^{(t / t_{gen})}$$

</td>
</tr>
</table>
</div>

---

## ⚔️ Perbandingan Algoritma

Aplikasi ini membandingkan dua pendekatan untuk menghitung $2^n$:

| Fitur | 🔄 Iteratif (Loop) | 🌿 Rekursif (Stack) |
| :--- | :--- | :--- |
| **Konsep** | Mengalikan angka dalam loop `for/while` | Fungsi memanggil dirinya sendiri |
| **Time Complexity** | $O(n)$ | $O(n)$ |
| **Space Complexity** | $O(1)$ (Efisien) | $O(n)$ (Boros Memori Stack) |
| **Kelebihan** | Cepat, Hemat Memori, Stabil | Kode Elegan, Definisi Matematis Alami |
| **Kelemahan** | Kode lebih panjang | Rawan `RecursionError` (Stack Overflow) |

---

## ✨ Fitur Unggulan

| 🔬 Single Test | 📊 Range Test | 📚 Edukasi |
| :--- | :--- | :--- |
| Simulasi satu kasus pertumbuhan dengan parameter kustom. | Analisis tren performa dengan ratusan data sekaligus. | Penjelasan teori lengkap dengan pseudocode. |
| ✅ **Export Chart PNG** | ✅ **Export Data CSV** | ✅ **Dark Mode UI** |

<div align="center">

### 🎨 Tampilan UI Modern
*Glassmorphism Design • Green Bacterial Theme • Responsive Mobile*

</div>

---

## 🛠️ Teknologi

Kami menggunakan stack teknologi modern untuk memastikan performa dan estetika:

| Komponen | Teknologi | Deskripsi |
|----------|-----------|-----------|
| **Backend** | Python + Flask | Logic algoritma & Server |
| **Frontend** | HTML5 + CSS3 | Glassmorphism UI |
| **Visualisasi** | Chart.js | Rendering grafik interaktif |
| **Styling** | CSS Variables | Dark mode & Theming |

---

## 🚀 Cara Menjalankan

Hanya butuh 3 langkah untuk menjalankan di lokal:

1.  **Clone & Masuk Direktori**
    ```bash
    git clone https://github.com/username/aka-bakteri.git
    cd aka-bakteri
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Jalankan!**
    ```bash
    python app.py
    ```
    Buka browser di `http://localhost:5000`

---

<div align="center">

<br/>


*Untuk Dosen AKA Ibu Lidya  - oleh Babass & Ghatfan*

<br/>

![Footer](https://capsule-render.vercel.app/api?type=waving&color=22C55E&height=100&section=footer)

</div>
