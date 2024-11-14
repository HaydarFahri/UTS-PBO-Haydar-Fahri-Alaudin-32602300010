class Buku:
    def __init__(self, judul, pengarang, tahunTerbit, ISBN, status="tersedia"):
        self.__judul = judul
        self.__pengarang = pengarang
        self.__tahunTerbit = tahunTerbit
        self.__ISBN = ISBN
        self.__status = status

    def tampilkanInfoBuku(self):
        print(f"Judul\t\t: {self.__judul}")
        print(f"Pengarang\t: {self.__pengarang}")
        print(f"Tahun Terbit\t: {self.__tahunTerbit}")
        print(f"ISBN\t\t: {self.__ISBN}")
        print(f"Status\t\t: {self.__status}")

    def pinjamBuku(self):
        if self.__status == "tersedia":
            self.__status = "dipinjam"
            return True
        return False

    def kembalikanBuku(self):
        self.__status = "tersedia"

    def get_judul(self):
        return self.__judul

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def get_jenis_buku(self):
        return "Normal"


class BukuDigital(Buku):
    def __init__(self, judul, pengarang, tahunTerbit, ISBN, formatFile, ukuranFile, status="tersedia"):
        super().__init__(judul, pengarang, tahunTerbit, ISBN, status)
        self.__formatFile = formatFile
        self.__ukuranFile = ukuranFile

    def tampilkanInfoBuku(self):
        super().tampilkanInfoBuku()
        print(f"Format File\t: {self.__formatFile}")
        print(f"Ukuran File\t: {self.__ukuranFile} MB")

    def get_formatFile(self):
        return self.__formatFile

    def get_ukuranFile(self):
        return self.__ukuranFile

    def get_jenis_buku(self):
        return "Digital"


class BukuReferensi(Buku):
    def __init__(self, judul, pengarang, tahunTerbit, ISBN, edisi, status="tersedia"):
        super().__init__(judul, pengarang, tahunTerbit, ISBN, status)
        self.__edisi = edisi

    def tampilkanInfoBuku(self):
        super().tampilkanInfoBuku()
        print(f"Edisi\t\t: {self.__edisi}")

    def get_edisi(self):
        return self.__edisi

    def get_jenis_buku(self):
        return "Referensi"


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
            print(f"  - {buku.get_judul()} ({buku.get_status()})")
        print("-" * 20)

    def pinjamBuku(self, buku):
        if buku.pinjamBuku():
            self.__daftarPinjaman.append(buku)
            return True
        return False

    def kembalikanBuku(self, judulBuku):
        for buku in self.__daftarPinjaman:
            if buku.get_judul() == judulBuku:
                buku.kembalikanBuku()
                self.__daftarPinjaman.remove(buku)
                return True
        return False

    def get_nomorAnggota(self):
        return self.__nomorAnggota


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
        print(f"Buku '{buku.get_judul()}' berhasil ditambahkan.")

    def daftarBukuTersedia(self):
        print("\nDaftar Buku Tersedia:")
        for buku in self.__daftarBuku:
            if buku.get_status() == "tersedia":
                print(f"Jenis Buku\t: {buku.get_jenis_buku()}")
                buku.tampilkanInfoBuku()
                print("-" * 20)

    def tambahAnggota(self, anggota):
        self.__daftarAnggota.append(anggota)
        print(f"Anggota '{anggota.get_nomorAnggota()}' berhasil didaftarkan.")

    def pinjamBuku(self, nomorAnggota, judulBuku):
        anggota = next((a for a in self.__daftarAnggota if a.get_nomorAnggota() == nomorAnggota), None)
        buku = next((b for b in self.__daftarBuku if b.get_judul() == judulBuku and b.get_status() == "tersedia"), None)

        if anggota and buku and anggota.pinjamBuku(buku):
            print(f"Buku '{judulBuku}' berhasil dipinjam oleh '{nomorAnggota}'.")
        else:
            print("Gagal meminjam buku. Buku tidak tersedia atau anggota tidak ditemukan.")

    def kembalikanBuku(self, nomorAnggota, judulBuku):
        anggota = next((a for a in self.__daftarAnggota if a.get_nomorAnggota() == nomorAnggota), None)
        if anggota and anggota.kembalikanBuku(judulBuku):
            print(f"Buku '{judulBuku}' berhasil dikembalikan oleh '{nomorAnggota}'.")
        else:
            print("Pengembalian gagal. Buku tidak ditemukan dalam daftar pinjaman.")

    def tampilkanInfoAnggota(self, nomorAnggota):
        anggota = next((a for a in self.__daftarAnggota if a.get_nomorAnggota() == nomorAnggota), None)
        if anggota:
            anggota.tampilkanInfoAnggota()
        else:
            print("Anggota tidak ditemukan.")


def main():
    perpustakaan = Perpustakaan()
    print("-" * 40)
    print("Selamat datang di Aplikasi Manajemen Perpustakaan!")
    while True:
        print("\nMasukkan perintah:")
        print("1. tambah buku\t\t: Menambah buku baru")
        print("2. lihat buku\t\t: Menampilkan daftar buku yang tersedia")
        print("3. tambah anggota\t: Menambah anggota baru")
        print("4. pinjam buku\t\t: Meminjam buku")
        print("5. kembalikan buku\t: Mengembalikan buku")
        print("6. info anggota\t\t: Menampilkan informasi anggota")
        print("7. exit\t\t\t: Keluar dari aplikasi")

        perintah = input(">> ").strip().lower()

        if perintah == "1" or perintah == "tambah buku":
            jenis_buku = input("Jenis Buku (Digital/Referensi/Normal): ").lower()
            judul = input("Judul Buku: ")
            pengarang = input("Pengarang: ")
            tahunTerbit = input("Tahun Terbit: ")
            ISBN = input("ISBN: ")

            if jenis_buku == "digital":
                formatFile = input("Format File (PDF/EPUB): ")
                ukuranFile = float(input("Ukuran File (MB): "))
                buku = BukuDigital(judul, pengarang, tahunTerbit, ISBN, formatFile, ukuranFile)
                perpustakaan.tambahBuku(buku)
            elif jenis_buku == "referensi":
                edisi = input("Edisi Buku: ")
                buku = BukuReferensi(judul, pengarang, tahunTerbit, ISBN, edisi)
                perpustakaan.tambahBuku(buku)
            else:
                buku = Buku(judul, pengarang, tahunTerbit, ISBN)
                perpustakaan.tambahBuku(buku)

        elif perintah == "2" or perintah == "lihat buku":
            perpustakaan.daftarBukuTersedia()

        elif perintah == "3" or perintah == "tambah anggota":
            nama = input("Nama Anggota: ")
            nomorAnggota = input("Nomor Anggota: ")
            alamat = input("Alamat Anggota: ")
            anggota = Anggota(nama, nomorAnggota, alamat)
            perpustakaan.tambahAnggota(anggota)

        elif perintah == "4" or perintah == "pinjam buku":
            nomorAnggota = input("Nomor Anggota: ")
            judulBuku = input("Judul Buku yang dipinjam: ")
            perpustakaan.pinjamBuku(nomorAnggota, judulBuku)

        elif perintah == "5" or perintah == "kembalikan buku":
            nomorAnggota = input("Nomor Anggota: ")
            judulBuku = input("Judul Buku yang dikembalikan: ")
            perpustakaan.kembalikanBuku(nomorAnggota, judulBuku)

        elif perintah == "6" or perintah == "info anggota":
            nomorAnggota = input("Nomor Anggota: ")
            perpustakaan.tampilkanInfoAnggota(nomorAnggota)

        elif perintah == "7" or perintah == "exit":
            print("Terima kasih telah menggunakan Aplikasi Perpustakaan!")
            break

        else:
            print("Perintah tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
