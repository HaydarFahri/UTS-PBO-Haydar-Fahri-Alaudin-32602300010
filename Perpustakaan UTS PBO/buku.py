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

    def dapat_judul(self):
        return self.__judul

    def dapat_status(self):
        return self.__status

    def siap_status(self, status):
        self.__status = status

    def dapat_jenis_buku(self):
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

    def dapat_formatFile(self):
        return self.__formatFile

    def dapat_ukuranFile(self):
        return self.__ukuranFile

    def dapat_jenis_buku(self):
        return "Digital"


class BukuReferensi(Buku):
    def __init__(self, judul, pengarang, tahunTerbit, ISBN, edisi, status="tersedia"):
        super().__init__(judul, pengarang, tahunTerbit, ISBN, status)
        self.__edisi = edisi

    def tampilkanInfoBuku(self):
        super().tampilkanInfoBuku()
        print(f"Edisi\t\t: {self.__edisi}")

    def dapat_edisi(self):
        return self.__edisi

    def dapat_jenis_buku(self):
        return "Referensi"
