from anggota import Anggota
from buku import Buku, BukuDigital, BukuReferensi

class Perpustakaan:
    def __init__(self):
        self.__daftarBuku = []
        self.__daftarAnggota = []
        self.__daftarBuku.append(Buku("Pemrograman Python", "John Doe", "2024", "1234567890"))
        self.__daftarBuku.append(BukuDigital("Data Science dengan Python", "Jane Doe", "2023", "0987654321", "PDF", 10))
        self.__daftarBuku.append(BukuReferensi("Algoritma Pemrograman", "Alice Smith", "2021", "1122334455", "Edisi 5"))
        self.__daftarAnggota.append(Anggota("Faris", "001", "Jl. Raya No. 1"))
        self.__daftarAnggota.append(Anggota("Alex", "002", "Jl. Raya No. 2"))

    def tambahBuku(self, buku):
        self.__daftarBuku.append(buku)
        print(f"Buku '{buku.dapat_judul()}' berhasil ditambahkan.")

    def daftarBukuTersedia(self):
        print("\nDaftar Buku Tersedia:")
        for buku in self.__daftarBuku:
            if buku.dapat_status() == "tersedia":
                print(f"Jenis Buku\t: {buku.dapat_jenis_buku()}")
                buku.tampilkanInfoBuku()
                print("-" * 20)

    def tambahAnggota(self, anggota):
        self.__daftarAnggota.append(anggota)
        print(f"Anggota '{anggota.dapat_nomorAnggota()}' berhasil didaftarkan.")

    def pinjamBuku(self, nomorAnggota, judulBuku):
        anggota = next((a for a in self.__daftarAnggota if a.dapat_nomorAnggota() == nomorAnggota), None)
        buku = next((b for b in self.__daftarBuku if b.dapat_judul() == judulBuku and b.dapat_status() == "tersedia"), None)

        if anggota and buku and anggota.pinjamBuku(buku):
            print(f"Buku '{judulBuku}' berhasil dipinjam oleh '{nomorAnggota}'.")
        else:
            print("Gagal meminjam buku. Buku tidak tersedia atau anggota tidak ditemukan.")

    def kembalikanBuku(self, nomorAnggota, judulBuku):
        anggota = next((a for a in self.__daftarAnggota if a.dapat_nomorAnggota() == nomorAnggota), None)
        if anggota and anggota.kembalikanBuku(judulBuku):
            print(f"Buku '{judulBuku}' berhasil dikembalikan oleh '{nomorAnggota}'.")
        else:
            print("Pengembalian gagal. Buku tidak ditemukan dalam daftar pinjaman.")

    def tampilkanInfoAnggota(self, nomorAnggota):
        anggota = next((a for a in self.__daftarAnggota if a.dapat_nomorAnggota() == nomorAnggota), None)
        if anggota:
            anggota.tampilkanInfoAnggota()
        else:
            print("Anggota tidak ditemukan.")
