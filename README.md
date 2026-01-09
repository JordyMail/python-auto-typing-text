# python-auto-typing-text

Program Python untuk mengetik paragraf secara otomatis karakter demi karakter, meniru pengetikan manual manusia dengan kecepatan dan pola alami.

1. Install Python
Pastikan Python 3.6 atau lebih baru telah terinstall:

bash
python --version
2. Install Modul yang Diperlukan
bash
pip install pyautogui
🚀 Instalasi
Download program:

bash
git clone [repository-url]
cd [repository-name]
Atau buat file manual:

Salin kode type_paragraph.py ke folder yang diinginkan

Buat file teks untuk contoh (opsional)

### Cara Penggunaan
Mode Interaktif (Rekomendasi)
bash
python type_paragraph.py
Langkah-langkah:

Pilih sumber teks:

text
1. Input dari keyboard
2. Baca dari file teks
Jika pilih 1 (keyboard):

text
Masukkan paragraf Anda (tekan Enter 2 kali untuk selesai):
Ini adalah contoh paragraf.
Baris kedua akan ditulis setelah Enter.

[tekan Enter lagi untuk selesai]
Jika pilih 2 (file):

text
Masukkan nama file teks (contoh: text.txt): contoh.txt
Pastikan file berada di folder yang sama

Pilih kecepatan:

text
1. Lambat (mirip pengetikan manual)
2. Sedang (seperti mengetik biasa)
3. Cepat (masih terlihat natural)
Atur pengulangan:

text
Ulangi berapa kali? (default: 1): 3
Siapkan aplikasi target:

text
Beralih ke aplikasi target dalam...
5...
4...
3...
2...
1...
Contoh File Teks
Buat file contoh.txt:

txt
Dear Tim,

Saya ingin menginformasikan bahwa rapat rutin bulanan akan diadakan pada:
Tanggal: 15 November 2024
Waktu: 10:00 - 12:00 WIB
Tempat: Ruang Rapat Utama

Agenda:
1. Laporan performa kuartalan
2. Diskusi proyek baru
3. Alokasi anggapan 2025

Harap persiapkan materi yang diperlukan sebelum rapat.
Terima kasih.

Hormat saya,
Manajer
Mode Command Line (Opsional)
Untuk penggunaan lebih lanjut, Anda bisa modifikasi program untuk menerima argumen command line.

 
 Konfigurasi Kecepatan
Mode	Min Delay	Max Delay	Error Chance	Keterangan
Lambat	0.05s	0.25s	2%	Mirip pengetikan manual pemula
Sedang	0.03s	0.15s	1%	Seperti mengetik biasa
Cepat	0.01s	0.08s	0.5%	Cepat namun masih natural

### Panduan Keamanan
SEBELUM MENJALANKAN:
Pastikan kursor aktif di aplikasi target

Backup data penting di aplikasi target

Tutup aplikasi yang tidak perlu

Simpan pekerjaan yang sedang berlangsung

SELAMA PROSES:
Monitor pengetikan untuk memastikan tidak ada kesalahan

Siapkan Ctrl+C untuk emergency stop

Jangan sentuh mouse/keyboard selama proses berjalan

EMERGENCY STOP:
Tekan Ctrl+C di terminal untuk menghentikan program segera.

### Troubleshooting
Masalah Umum dan Solusi:
Masalah	Penyebab	Solusi
"ModuleNotFoundError: No module named 'pyautogui'"	Modul belum terinstall	pip install pyautogui
Program tidak mengetik	Kursor tidak aktif	Klik dulu di aplikasi target
Karakter aneh muncul	Layout keyboard salah	Pastikan keyboard dalam mode EN/US
Program berjalan terlalu cepat/ lambat	Setting delay tidak sesuai	Pilih kecepatan yang berbeda
Tidak bisa input file	File tidak ditemukan	Pastikan file berada di folder yang sama
Tips Optimal:
Testing kecil dulu dengan teks pendek

Gunakan mode lambat untuk aplikasi penting

Siapkan template di file teks untuk penggunaan berulang

Nonaktifkan autocorrect di aplikasi target untuk hasil terbaik

### Contoh Penggunaan Praktis
1. Mengirim pesan panjang di WhatsApp:
bash
python type_paragraph.py
- Pilih: 2 (file)
- File: pesan_whatsapp.txt
- Kecepatan: 2 (sedang)
- Ulang: 1
2. Mengisi form berulang:
bash
python type_paragraph.py
- Pilih: 1 (keyboard)
- Masukkan data form
- Kecepatan: 3 (cepat)
- Ulang: 10 (untuk 10 form)
3. Menulis draft dokumen:
bash
python type_paragraph.py
- Pilih: 2 (file)
- File: draft_laporan.txt
- Kecepatan: 1 (lambat, untuk efek natural)
- Ulang: 1
- 

Gunakan program ini dengan bijak dan bertanggung jawab!!!


Commit perubahan (git commit -m 'Menambahkan fitur')

Push ke branch (git push origin fitur-baru)

Buat Pull Request

📄 Lisensi
Program ini dibuat untuk tujuan edukasi dan produktivitas pribadi. Gunakan dengan bijak.
