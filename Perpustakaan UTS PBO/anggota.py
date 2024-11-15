class Anggota:
    def __init__(self, nama, nomorAnggota, alamat):
        self.__nama = nama
        self.__nomorAnggota = nomorAnggota
        self.__alamat = alamat
        self.__daftarPinjaman = []

    def tampilkanInfoAnggota(self):
        print("-" * 20)
        print(f"Nama\t\t: {self.__nama}")
        print(f"Nomor Anggota\t: {self.__nomorAnggota}")
        print(f"Alamat\t\t: {self.__alamat}")
        print("Daftar Pinjaman\t: ")
        for buku in self.__daftarPinjaman:
            print(f"  - {buku.dapat_judul()} ({buku.dapat_status()})")
        print("-" * 20)

    def pinjamBuku(self, buku):
        if buku.pinjamBuku():
            self.__daftarPinjaman.append(buku)
            return True
        return False

    def kembalikanBuku(self, judulBuku):
        for buku in self.__daftarPinjaman:
            if buku.dapat_judul() == judulBuku:
                buku.kembalikanBuku()
                self.__daftarPinjaman.remove(buku)
                return True
        return False

    def dapat_nomorAnggota(self):
        return self.__nomorAnggota
