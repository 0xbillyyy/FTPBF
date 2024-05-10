# FTP Brute Force Tool

![FTP Brute Force Tool](https://raw.githubusercontent.com/username/repo/master/ftp_brute_force_tool.png)

**FTP Brute Force Tool** adalah skrip Python sederhana untuk melakukan serangan brute force pada layanan FTP. Ini memungkinkan Anda untuk menguji banyak password dari sebuah wordlist terhadap sebuah server FTP untuk mencoba masuk ke dalamnya.

## Penggunaan

Pastikan Anda telah menginstal Python di sistem Anda. Kemudian, ikuti langkah-langkah di bawah ini:

1. **Persiapan Lingkungan:**
   - Pastikan Anda telah menginstal modul `ftplib` yang diperlukan. Jika belum, instal dengan menjalankan perintah berikut di terminal:
     ```
     pip install ftplib
     ```

2. **Menjalankan Skrip:**
   - Unduh Repository Ini.
   - Buka terminal atau command prompt di direktori di mana skrip tersebut disimpan.
   - Jalankan skrip dengan perintah berikut:
     ```
     python main.py -H [target_host] -u [target_username] -wl [wordlist_path]
     ```
     - `[target_host]`: Alamat host target FTP.
     - `[target_username]`: Nama pengguna target FTP.
     - `[wordlist_path]` (opsional): Path ke file wordlist yang berisi daftar kata sandi yang akan dicoba. Jika tidak disediakan, skrip akan menggunakan file `wordlist.txt` di direktori yang sama.

## Contoh Penggunaan

python main.py -H ftp.example.com -u user -wl my_wordlist.txt


## Catatan

- Skrip ini dibuat untuk tujuan pendidikan dan pengujian keamanan. Gunakan dengan bijak dan hanya untuk tes pada sistem yang Anda miliki izin untuk melakukan uji coba.

- Skrip ini menggunakan modul bawaan Python `argparse` untuk menangani argumen baris perintah. Pastikan Anda menjalankan skrip dengan argumen yang sesuai seperti yang dijelaskan di bagian "Menjalankan Skrip".

## Kontribusi

Jika Anda menemukan bug atau memiliki saran perbaikan, jangan ragu untuk membuat "Issue" atau "Pull Request" di repositori ini.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.

