# Hyperbolic
Hyperbolic auto bot chat

---

## 🤖 HISTORIAI — Gabungan AI Text, Image, dan Audio (dengan Logging Otomatis)

Program ini akan menjalankan **AI Text Q&A**, **Image Generation**, dan **Voice Generation** secara bergantian setiap hari, dengan hasil log otomatis disimpan ke dalam file `HISTORIAI.txt`.

---

### 💡 Fitur
- 🔁 Menjalankan 3 task AI: Text, Gambar, dan Suara secara bergantian
- 📝 Log status otomatis ke file `HISTORIAI.txt`
- 🔑 Menggunakan API dari **Groq** dan **Hyperbolic**
- 🔧 Jumlah task & hari bisa diatur bebas oleh user

---

## 📥 Cara Download (Clone Repo)

```bash
git clone https://github.com/ademulyanaDEV/Hyperbolic.git
cd Hyperbolic
```

---

## 🔐 Cara Mendapatkan API Key

### 1. **Groq API Key (untuk TEXT, IMAGE, AUDIO prompt)**
- Buka: [https://console.groq.com/keys](https://console.groq.com/keys)
- Klik `+ New Key`, lalu salin API Key-nya
- Kamu bisa pakai satu key yang sama untuk semua request (text, image, audio)

### 2. **Hyperbolic API Key (untuk generate gambar dan suara)**
- Daftar di: [https://hyperbolic.xyz](https://hyperbolic.xyz)
- Login, lalu salin API Key dari dashboard

---

## ▶️ Cara Menjalankan Program

```bash
python main.py
python3 main.py
py main.py
```

Lalu isi:
- 🎯 **Berapa task per hari**? (misal: `3`)
- 📆 **Berapa hari ingin dijalankan**? (misal: `2`)

Program akan otomatis menjalankan:
- `3` text Q&A
- `3` image generation
- `3` voice generation

... per hari, selama `2` hari berturut-turut.

---

## 🗃️ Log Output

Semua status disimpan ke file:

```
HISTORIAI.txt
```

Contoh isi log:
```
=== [Hari 1 - TEXT 1] ===
Status: ✅ Sukses
========================================

=== [Hari 1 - IMAGE 2] ===
Status: ❌ Gagal (403)
========================================
```

---

## 📁 Struktur Folder

```
📁 Hyperbolic/
├── main.py          # Script utama gabungan
├── HISTORIAI.txt           # File log hasil task
└── README.md               # Dokumentasi
```

---

## 💡 Tips Tambahan

- Script ini pakai `requests` bawaan Python (tidak perlu install tambahan)
- Ingin otomatis harian? Jalankan dengan scheduler seperti `cron` (Linux) atau `Task Scheduler` (Windows)
- Lebih mudah gunakan screen saja
- Ubah `time.sleep()` jika ingin mempercepat jeda antar task

---

