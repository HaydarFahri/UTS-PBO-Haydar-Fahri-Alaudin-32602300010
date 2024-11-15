# UTS-PBO-Haydar-Fahri-Alaudin-32602300010
# Aplikasi Manajemen Perpustakaan

Aplikasi ini dibuat untuk mengelola buku, anggota, dan peminjaman di perpustakaan. Pengguna dapat menambah buku baru, melihat buku yang tersedia, meminjam dan mengembalikan buku, serta menambah anggota perpustakaan. Aplikasi ini mendukung tiga jenis buku: buku normal, buku digital, dan buku referensi.

## Fitur
1. **Menambah Buku**: Menambah buku baru dengan tipe buku (Normal, Digital, Referensi).
2. **Lihat Buku**: Menampilkan daftar buku yang tersedia beserta detailnya (judul, pengarang, tahun terbit, ISBN, dan jenis buku).
3. **Menambah Anggota**: Menambah anggota baru dengan nama, nomor anggota, dan alamat.
4. **Pinjam Buku**: Anggota dapat meminjam buku yang tersedia di perpustakaan.
5. **Kembalikan Buku**: Anggota dapat mengembalikan buku yang telah dipinjam.
6. **Info Anggota**: Menampilkan informasi anggota, termasuk daftar buku yang sedang dipinjam.

## Struktur Kode
Program ini adalah sistem manajemen perpustakaan yang memungkinkan pengguna untuk mengelola buku dan anggota perpustakaan, meminjam dan mengembalikan buku. Sistem ini terdiri dari beberapa kelas seperti `Anggota`, `Buku`, dan berbagai jenis buku seperti `BukuDigital` dan `BukuReferensi`, serta kelas utama `Perpustakaan` untuk mengelola semua proses tersebut.

### Kelas dan Penjelasannya

#### 1. **Kelas Anggota**
   - **Fungsi Utama**: Menyimpan informasi tentang anggota perpustakaan, termasuk nama, nomor anggota, dan alamat.
   - **Atribut**:
     - `__nama`: Nama anggota.
     - `__nomorAnggota`: Nomor anggota.
     - `__alamat`: Alamat anggota.
     - `__daftarPinjaman`: Daftar buku yang dipinjam oleh anggota.
   - **Metode**:
     - `tampilkanInfoAnggota()`: Menampilkan informasi lengkap tentang anggota dan daftar buku yang dipinjam.
     - `pinjamBuku(buku)`: Memungkinkan anggota untuk meminjam buku, jika buku tersedia.
     - `kembalikanBuku(judulBuku)`: Mengembalikan buku yang dipinjam oleh anggota.
     - `dapat_nomorAnggota()`: Mengambil nomor anggota.

#### 2. **Kelas Buku**
   - **Fungsi Utama**: Menyimpan informasi umum tentang buku, seperti judul, pengarang, tahun terbit, ISBN, dan status (tersedia atau dipinjam).
   - **Atribut**:
     - `__judul`: Judul buku.
     - `__pengarang`: Pengarang buku.
     - `__tahunTerbit`: Tahun terbit buku.
     - `__ISBN`: ISBN buku.
     - `__status`: Status buku, apakah tersedia atau dipinjam.
   - **Metode**:
     - `tampilkanInfoBuku()`: Menampilkan informasi lengkap tentang buku.
     - `pinjamBuku()`: Mengubah status buku menjadi "dipinjam" jika buku tersedia.
     - `kembalikanBuku()`: Mengubah status buku menjadi "tersedia" saat dikembalikan.
     - `dapat_judul()`: Mengambil judul buku.
     - `dapat_status()`: Mengambil status buku.
     - `dapat_jenis_buku()`: Mengembalikan jenis buku (Normal).

#### 3. **Kelas BukuDigital (Turunan dari Buku)**
   - **Fungsi Utama**: Menyimpan informasi tentang buku digital, termasuk format file dan ukuran file.
   - **Atribut**:
     - `__formatFile`: Format file (misalnya PDF atau EPUB).
     - `__ukuranFile`: Ukuran file dalam MB.
   - **Metode**:
     - `tampilkanInfoBuku()`: Menampilkan informasi lengkap buku digital, termasuk format dan ukuran file.
     - `dapat_formatFile()`: Mengambil format file buku digital.
     - `dapat_ukuranFile()`: Mengambil ukuran file buku digital.
     - `dapat_jenis_buku()`: Mengembalikan jenis buku sebagai "Digital".

#### 4. **Kelas BukuReferensi (Turunan dari Buku)**
   - **Fungsi Utama**: Menyimpan informasi tentang buku referensi, termasuk edisi.
   - **Atribut**:
     - `__edisi`: Edisi buku referensi.
   - **Metode**:
     - `tampilkanInfoBuku()`: Menampilkan informasi lengkap tentang buku referensi, termasuk edisi.
     - `dapat_edisi()`: Mengambil edisi buku referensi.
     - `dapat_jenis_buku()`: Mengembalikan jenis buku sebagai "Referensi".

#### 5. **Kelas Perpustakaan**
   - **Fungsi Utama**: Mengelola buku dan anggota perpustakaan. Termasuk fungsionalitas untuk menambah buku dan anggota, serta meminjam dan mengembalikan buku.
   - **Atribut**:
     - `__daftarBuku`: Daftar buku yang tersedia di perpustakaan.
     - `__daftarAnggota`: Daftar anggota yang terdaftar di perpustakaan.
   - **Metode**:
     - `tambahBuku(buku)`: Menambahkan buku baru ke daftar buku.
     - `daftarBukuTersedia()`: Menampilkan semua buku yang tersedia.
     - `tambahAnggota(anggota)`: Menambahkan anggota baru.
     - `pinjamBuku(nomorAnggota, judulBuku)`: Meminjam buku dengan judul yang diberikan untuk anggota yang terdaftar.
     - `kembalikanBuku(nomorAnggota, judulBuku)`: Mengembalikan buku yang dipinjam oleh anggota.
     - `tampilkanInfoAnggota(nomorAnggota)`: Menampilkan informasi tentang anggota berdasarkan nomor anggota.

#### 6. **Fungsi Main**
   - **Fungsi Utama**: Menyediakan antarmuka pengguna untuk berinteraksi dengan sistem perpustakaan melalui input perintah.
   - **Perintah yang Tersedia**:
     - Menambah buku.
     - Menampilkan buku yang tersedia.
     - Menambah anggota.
     - Meminjam buku.
     - Mengembalikan buku.
     - Menampilkan informasi anggota.
     - Keluar dari aplikasi.

### Struktur Direktori
```
Perpustakaan UTS PBO/
│
├── anggota.py          # Definisi kelas Anggota
├── buku.py             # Definisi kelas Buku, BukuDigital, BukuReferensi
├── perpustakaan.py     # Definisi kelas Perpustakaan
└── main.py             # Program utama yang menjalankan aplikasi
```

## Instruksi Penggunaan

1. Jalankan aplikasi di terminal atau IDE yang mendukung Python.
2. Pilih perintah yang ingin dijalankan dengan memasukkan nomor perintah yang sesuai:
    - **1**: Menambah buku baru.
    - **2**: Lihat buku yang tersedia.
    - **3**: Menambah anggota baru.
    - **4**: Meminjam buku.
    - **5**: Mengembalikan buku.
    - **6**: Menampilkan informasi anggota.
    - **7**: Keluar dari aplikasi.

## Contoh Input
Inputan dapat berupa nomor menu ataupun nama menu yang dipilih contohnya saat ingin menambahkan sebuah buku maka bisa langsung memilih nomor sesuai menu yaitu angka 1 atau bisa langsung mengetik "menambah buku".

### Menambah Buku Baru:
dalam menu penambahan buku dapat memilih antara buku digital, refrensi, dan normal

![image](https://github.com/user-attachments/assets/de6de281-b03b-4818-b083-b3d860cc9ecd)

### Info buku 
dalam menu info buku dapat melihat informasi dari buku tersebut seperti jenis buku, status buku tersedia atau dipinjam dan informasi umum dari buku yang ada.

![image](https://github.com/user-attachments/assets/67fef6aa-1bce-492b-89a5-0a07d4c0762d)
![image](https://github.com/user-attachments/assets/3a6f5213-b28b-4eee-a4bf-1429aaa11975)

### Tambah anggota
dalam menu tambah anggota dapat menambahkan anggota dan memasukan informasi untuk data dari anggota.

![image](https://github.com/user-attachments/assets/9a5e9dea-ae9e-448e-a217-6d8bc23f85ae)

### Pinjam buku
dalam menu ini dapat memasukan data anggota yang meminjam buku.

![image](https://github.com/user-attachments/assets/3dafdb5d-c3b0-4eff-8458-6dc9b04fab14)

### Kembalikan buku
dalam menu ini dapat memasukan data untuk anggota yang sudah mengembalikan buku untuk memperbarui status dari buku yang dipinjam menjadi tersedia kembali.

![image](https://github.com/user-attachments/assets/1e3f9e33-d49f-4845-b31a-53fce62a8a9d)

### Info anggota 
dalam menu ini dapat melihat anggota yang sudah terdaftar.

![image](https://github.com/user-attachments/assets/e43ac8f6-2b34-4c3f-9669-65ba56c40816)

### Exit
dengan mengetik atau memilih menu exit supaya user dapat meninggalkan atau mematikan program / aplikasi.
![image](https://github.com/user-attachments/assets/04c14add-b5b9-410a-8398-164277ef04fd)

## Kesimpulan
Aplikasi ini adalah sistem perpustakaan sederhana namun komprehensif yang dapat menangani peminjaman dan pengembalian buku, serta memberikan informasi lengkap tentang anggota dan buku









