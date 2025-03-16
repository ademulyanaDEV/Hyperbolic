# Hyperbolic
Hyperbolic auto bot chat


---

## 🤖 HISTORIAI — Gabungan AI Text, Image, dan Audio (dengan Logging Otomatis)

Program ini akan menjalankan **AI Text Q&A**, **Image Generation**, dan **Voice Generation** secara bergantian setiap hari, dengan hasil log otomatis disimpan ke dalam file `HISTORIAI.txt`.

### 💡 Fitur
- 🔁 Menjalankan 3 jenis task (Text, Image, Audio) secara bergantian
- 📝 Log status (sukses/gagal) untuk setiap task
- 🔑 Menggunakan API dari Groq & Hyperbolic AI
- 🔧 Fleksibel: bisa diatur jumlah task per hari & jumlah hari eksekusi

---

## 📦 Cara Install

1. **Pastikan Python 3.9+ sudah terinstal**

Cek dengan:
```bash
python --version
```

2. **Install library yang dibutuhkan**
```bash
pip install requests
```

---

## 🔐 Cara Mendapatkan API Key

### 1. **Groq API Key (untuk TEXT, IMAGE, AUDIO prompt)**
- Kunjungi: [https://console.groq.com/keys](https://console.groq.com/keys)
- Klik `+ New Key`, lalu simpan API Key-nya.
- Kamu butuh **3 key berbeda** (atau pakai yang sama, tapi idealnya 3):

  | Fungsi     | Simpan Sebagai        |
  |------------|------------------------|
  | Text       | `TEXT_GROQ_API`        |
  | Image Prompt | `IMAGE_GROQ_API`      |
  | Audio Prompt | `AUDIO_GROQ_API`      |

### 2. **Hyperbolic API Key (untuk generate Image & Audio)**
- Daftar di: [https://hyperbolic.xyz](https://hyperbolic.xyz)
- Setelah login, buka dashboard dan salin **API Key** milikmu.
- Simpan di variabel: `HYPERBOLIC_API_KEY`

---

## ▶️ Cara Menjalankan Program

```bash
python main.py
python3 main.py
py main.py
```

Lalu masukkan:
- Berapa task per hari (misal: `2` → 2 text, 2 image, 2 audio)
- Berapa hari mau dijalankan (misal: `3`)

Log akan tersimpan otomatis di file:
```
HISTORIAI.txt
```

Contoh isi log:
```
=== [Hari 1 - TEXT 1] ===
Status: ✅ Sukses
========================================

=== [Hari 1 - IMAGE 1] ===
Status: ❌ Gagal (403)
========================================
```

---

## 🛠 Struktur File

```
📁 proyek/
├── main.py         # Main script
└── HISTORIAI.txt          # File log output
```

---

## 🧠 Tips & Catatan

- Jangan lupa jaga limit rate API dari Groq dan Hyperbolic
- Kalau ingin jeda antar task lebih lama, ubah bagian `time.sleep(x)`
- Bisa dijalankan di server/VPS untuk otomatisasi berkala

---

