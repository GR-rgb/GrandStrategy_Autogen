⚔️ Grand Strategy 
Proyek ini adalah simulasi Grand Strategy berbasis teks yang digerakkan oleh AI menggunakan Microsoft AutoGen dan Ollama. Simulasi ini mengadu tiga faksi yang dikendalikan oleh agen AI dalam perebutan kekuasaan, di mana mereka harus saling menjatuhkan melalui taktik ekonomi, politik, dan kekuatan militer.
🏗️ Arsitektur Multi-Agent
Sistem ini terdiri dari 4 agen AI yang berinteraksi dalam satu lingkungan simulasi:
🎲 The Dungeon Master (Narrator)
Bertindak sebagai pengawas dunia, dewa, dan narator. Agen ini tidak ikut berperang, melainkan bertugas mengevaluasi setiap keputusan faksi, menghitung dampak peperangan atau ekonomi, memberikan kejadian acak (random events), dan mendeskripsikan hasil akhir dari setiap giliran (turn).
🔴 Faksi 1 (Masukkan Nama Faksi)
Agen AI dengan parameter dan prompt khusus. Fokus pada gaya bermain tertentu (misal: agresif militer) dengan keunggulan dan kelemahan spesifik.
🟢 Faksi 2 (Masukkan Nama Faksi)
Agen AI kompetitor. Memiliki gaya bermain yang berbeda (misal: keunggulan ekonomi dan diplomasi politik) untuk menyeimbangkan simulasi.
🔵 Faksi 3 (Masukkan Nama Faksi)
Agen AI kompetitor ketiga. Bergerak dengan strateginya sendiri berdasarkan karakteristik unik pasukannya dan kondisi politik internal.
(Setiap agen faksi tidak mengetahui prompt rahasia faksi lain, mereka hanya merespons kondisi dunia yang dinarasikan oleh Dungeon Master).
🛠️ Tech Stack
Python: Bahasa pemrograman utama.
Ollama: Menjalankan Large Language Model (LLM) secara lokal sebagai "otak" dari setiap agen. Ini memungkinkan simulasi berjalan offline tanpa biaya API.
Microsoft AutoGen: Framework untuk mengatur alur percakapan (Group Chat) dan koordinasi antar keempat agen tersebut.
🚀 Persiapan dan Cara Menjalankan
Pastikan Ollama sudah terinstal dan berjalan di sistem Anda.
Tarik (pull) model yang ingin digunakan (contoh menggunakan Llama 3 atau Mistral):
ollama run llama3


Instal dependensi Python (AutoGen):
pip install pyautogen


Jalankan simulasi:
python main.py

(Catatan: Sesuaikan nama file utama dengan skrip Python Anda)
Dibuat sebagai eksperimen arsitektur AI Multi-Agent dalam skenario game strategi.
