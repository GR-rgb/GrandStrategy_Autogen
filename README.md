# ⚔️️ Grand Strategy Simulasi AI

Proyek ini adalah simulasi Grand Strategy berbasis teks yang digerakkan oleh AI menggunakan **Microsoft AutoGen** dan **Ollama**. Simulasi ini mengadu tiga faksi yang dikendalikan oleh agen AI dalam perebutan kekuasaan, di mana mereka harus saling menjatuhkan melalui taktik ekonomi, politik, dan kekuatan militer.

## 🏯 Arsitektur Multi-Agent

Sistem ini terdiri dari 4 agen AI yang berinteraksi dalam satu lingkungan simulasi:

*   **🎲 The Dungeon Master (Narrator):** Bertindak sebagai pengawas dunia, dewa, dan narator. Agen ini tidak ikut berperang, melainkan bertugas mengevaluasi setiap keputusan faksi, menghitung dampak peperangan atau ekonomi, memberikan kejadian acak (*random events*), dan mendeskripsikan hasil akhir dari setiap giliran (*turn*)[cite: 5].
*   **🔴 Faksi 1 :** Agen AI dengan parameter dan prompt khusus[cite: 5]. Fokus pada gaya bermain tertentu (misal: agresif militer) dengan keunggulan dan kelemahan spesifik[cite: 5].
*   **🟢 Faksi 2 :** Agen AI kompetitor[cite: 5]. Memiliki gaya bermain yang berbeda (misal: keunggulan ekonomi dan diplomasi politik) untuk menyeimbangkan simulasi[cite: 5].
*   **🔵 Faksi 3 :** Agen AI kompetitor ketiga[cite: 5]. Bergerak dengan strateginya sendiri berdasarkan karakteristik unik pasukannya dan kondisi politik internal[cite: 5].

*(Catatan: Setiap agen faksi tidak mengetahui prompt rahasia faksi lain, mereka hanya merespons kondisi dunia yang dinarasikan oleh Dungeon Master)[cite: 5].*

## 🛠️ Tech Stack

*   **Python:** Bahasa pemrograman utama[cite: 5].
*   **Ollama:** Menjalankan Large Language Model (LLM) secara lokal sebagai "otak" dari setiap agen[cite: 5]. Ini memungkinkan simulasi berjalan offline tanpa biaya API[cite: 5].
*   **Microsoft AutoGen:** Framework untuk mengatur alur percakapan (*Group Chat*) dan koordinasi antar keempat agen tersebut[cite: 5].

## 🚀 Persiapan dan Cara Menjalankan

1. Pastikan **Ollama** sudah terinstal dan berjalan di sistem Anda[cite: 5].
2. Tarik (*pull*) model yang ingin digunakan (contoh menggunakan Llama 3 atau Mistral)[cite: 5]:
   ```bash
   ollama run llama3
