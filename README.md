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
- `get_judul()`: Mengembalikan judul buku.
- `get_status()`: Mengembalikan status buku.

### Kelas `BukuDigital` (Subkelas dari `Buku`)
Kelas ini digunakan untuk buku dengan format digital seperti PDF atau EPUB. Menambahkan informasi tentang format file dan ukuran file.

#### Metode:
- `tampilkanInfoBuku()`: Menampilkan informasi buku digital termasuk format dan ukuran file.
- `get_jenis_buku()`: Mengembalikan jenis buku sebagai "Digital".

### Kelas `BukuReferensi` (Subkelas dari `Buku`)
Kelas ini digunakan untuk buku referensi. Menambahkan informasi tentang edisi buku.

#### Metode:
- `tampilkanInfoBuku()`: Menampilkan informasi buku referensi termasuk edisi.
- `get_jenis_buku()`: Mengembalikan jenis buku sebagai "Referensi".

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

### Menambah Buku Baru:
