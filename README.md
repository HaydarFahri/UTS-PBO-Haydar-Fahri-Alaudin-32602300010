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

### Kelas `Buku`
Kelas ini berfungsi untuk mendefinisikan buku yang dapat dipinjam. Buku memiliki atribut seperti judul, pengarang, tahun terbit, ISBN, dan status (tersedia/dipinjam).

#### Metode:
- `tampilkanInfoBuku()`: Menampilkan informasi buku.
- `pinjamBuku()`: Mengubah status buku menjadi dipinjam jika buku tersedia.
- `kembalikanBuku()`: Mengubah status buku menjadi tersedia.
- `getjudul()`: Mengembalikan judul buku.
- `getstatus()`: Mengembalikan status buku.

### Kelas `BukuDigital` (Subkelas dari `Buku`)
Kelas ini digunakan untuk buku dengan format digital seperti PDF atau EPUB. Menambahkan informasi tentang format file dan ukuran file.

#### Metode:
- `tampilkanInfoBuku()`: Menampilkan informasi buku digital termasuk format dan ukuran file.
- `getjenisbuku()`: Mengembalikan jenis buku sebagai "Digital".

### Kelas `BukuReferensi` (Subkelas dari `Buku`)
Kelas ini digunakan untuk buku referensi. Menambahkan informasi tentang edisi buku.

#### Metode:
- `tampilkanInfoBuku()`: Menampilkan informasi buku referensi termasuk edisi.
- `getjenisbuku()`: Mengembalikan jenis buku sebagai "Referensi".

### Kelas `Anggota`
Kelas ini digunakan untuk mendefinisikan anggota perpustakaan yang dapat meminjam buku. Anggota memiliki atribut seperti nama, nomor anggota, alamat, dan daftar buku yang dipinjam.

#### Metode:
- `tampilkanInfoAnggota()`: Menampilkan informasi anggota beserta daftar buku yang sedang dipinjam.
- `pinjamBuku()`: Memungkinkan anggota untuk meminjam buku.
- `kembalikanBuku()`: Memungkinkan anggota untuk mengembalikan buku.

### Kelas `Perpustakaan`
Kelas ini adalah inti dari aplikasi yang mengelola daftar buku dan anggota. Kelas ini juga menangani peminjaman dan pengembalian buku.

#### Metode:
- `tambahBuku()`: Menambahkan buku baru ke perpustakaan.
- `daftarBukuTersedia()`: Menampilkan daftar buku yang tersedia untuk dipinjam.
- `tambahAnggota()`: Menambahkan anggota baru ke perpustakaan.
- `pinjamBuku()`: Meminjam buku untuk anggota tertentu.
- `kembalikanBuku()`: Mengembalikan buku yang telah dipinjam.
- `tampilkanInfoAnggota()`: Menampilkan informasi anggota berdasarkan nomor anggota.

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
Inputan dapat berupa nomor menu ataupun nama menu yang dipilih.

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









