import sys
import pyautogui as pt
import time
import random

def type_paragraph(paragraph, min_delay=0.02, max_delay=0.15, error_chance=0.01):
    """
    Mengetik paragraf karakter demi karakter dengan variasi kecepatan
    dan kemungkinan kesalahan kecil untuk meniru pengetikan manusia.
    
    Args:
        paragraph (str): Teks yang akan diketik
        min_delay (float): Delay minimum antar karakter (detik)
        max_delay (float): Delay maksimum antar karakter (detik)
        error_chance (float): Peluang membuat kesalahan ketik (0-1)
    """
    # Tambahkan jeda sebelum mulai mengetik
    time.sleep(random.uniform(0.5, 1.0))
    
    lines = paragraph.split('\n')
    
    for line_idx, line in enumerate(lines):
        i = 0
        while i < len(line):
            char = line[i]
            
            # Cek apakah akan membuat kesalahan (typo)
            if random.random() < error_chance and i > 0:
                # Buat kesalahan kecil
                wrong_char = random.choice('asdfghjkl;')
                pt.typewrite(wrong_char)
                time.sleep(random.uniform(0.1, 0.3))
                
                # Hapus karakter yang salah
                pt.press('backspace')
                time.sleep(random.uniform(0.05, 0.15))
            
            # Ketik karakter dengan delay acak
            pt.typewrite(char)
            
            # Delay antar karakter dengan variasi
            if char in '.,!?;:':
                # Delay lebih lama setelah tanda baca
                delay = random.uniform(0.2, 0.4)
            elif char == ' ':
                # Delay setelah spasi
                delay = random.uniform(0.05, 0.15)
            else:
                # Delay normal
                delay = random.uniform(min_delay, max_delay)
            
            time.sleep(delay)
            i += 1
        
        # Jika bukan baris terakhir, tekan Enter
        if line_idx < len(lines) - 1:
            # Delay sebelum pindah baris
            time.sleep(random.uniform(0.3, 0.7))
            pt.press('enter')
            # Delay setelah pindah baris
            time.sleep(random.uniform(0.5, 1.0))

def get_paragraph_from_file(filename):
    """Membaca paragraf dari file teks"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: File '{filename}' tidak ditemukan.")
        return None

def main():
    try:
        print("=" * 50)
        print("PARAGRAPH TYPING SIMULATOR")
        print("=" * 50)
        print("\nPilih sumber teks:")
        print("1. Input dari keyboard")
        print("2. Baca dari file teks")
        
        choice = input("\nPilihan Anda (1/2): ").strip()
        
        if choice == '1':
            print("\nMasukkan paragraf Anda (tekan Enter 2 kali untuk selesai):")
            lines = []
            while True:
                line = input()
                if line == "" and len(lines) > 0:
                    # Cek jika dua baris kosong berturut-turut
                    if lines[-1] == "":
                        lines.pop()  # Hapus baris kosong terakhir
                        break
                lines.append(line)
            paragraph = '\n'.join(lines)
            
        elif choice == '2':
            filename = input("Masukkan nama file teks (contoh: text.txt): ").strip()
            paragraph = get_paragraph_from_file(filename)
            if paragraph is None:
                return
        else:
            print("Pilihan tidak valid!")
            return
        
        if not paragraph:
            print("Error: Paragraf tidak boleh kosong!")
            return
        
        print("\n" + "=" * 50)
        print("PREVIEW TEKS:")
        print("=" * 50)
        print(paragraph)
        print("=" * 50)
        
        # Konfigurasi kecepatan
        print("\nKonfigurasi kecepatan mengetik:")
        print("1. Lambat (mirip pengetikan manual)")
        print("2. Sedang (seperti mengetik biasa)")
        print("3. Cepat (masih terlihat natural)")
        
        speed_choice = input("Pilihan kecepatan (1/2/3): ").strip()
        
        if speed_choice == '1':
            min_delay, max_delay = 0.05, 0.25
            error_chance = 0.02
        elif speed_choice == '2':
            min_delay, max_delay = 0.03, 0.15
            error_chance = 0.01
        elif speed_choice == '3':
            min_delay, max_delay = 0.01, 0.08
            error_chance = 0.005
        else:
            print("Menggunakan kecepatan default (sedang)...")
            min_delay, max_delay = 0.03, 0.15
            error_chance = 0.01
        
        repeat = input("Ulangi berapa kali? (default: 1): ").strip()
        repeat_count = int(repeat) if repeat.isdigit() and int(repeat) > 0 else 1
        
        print(f"\nSiap mengetik! Beralih ke aplikasi target dalam...")
        for i in range(5, 0, -1):
            print(f"{i}...")
            time.sleep(1)
        
        print("\nMemulai pengetikan otomatis... (Tekan Ctrl+C untuk berhenti)")
        
        for iteration in range(repeat_count):
            if repeat_count > 1:
                print(f"\nIterasi ke-{iteration + 1} dari {repeat_count}")
            
            type_paragraph(paragraph, min_delay, max_delay, error_chance)
            
            if iteration < repeat_count - 1:
                # Delay antar pengulangan
                delay_between = random.uniform(2, 5)
                print(f"\nMenunggu {delay_between:.1f} detik sebelum pengulangan berikutnya...")
                time.sleep(delay_between)
        
        print(f"\n✓ Selesai! Telah mengetik {repeat_count} paragraf.")
        
    except KeyboardInterrupt:
        print("\n\n❌ Pengetikan dihentikan oleh pengguna.")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Pastikan Anda telah menginstal modul yang diperlukan:")
        print("pip install pyautogui")

if __name__ == "__main__":
    # Cek apakah modul terinstal
    try:
        import pyautogui
    except ImportError:
        print("Modul pyautogui belum terinstal!")
        print("Instal dengan: pip install pyautogui")
        sys.exit(1)
    
    main()
