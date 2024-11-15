from perpustakaan import Perpustakaan
from buku import Buku, BukuDigital, BukuReferensi
from anggota import Anggota

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
            jenisbuku = ""
            while jenisbuku not in ["digital", "referensi", "normal"]:
                jenisbuku = input("Jenis Buku (Digital/Referensi/Normal): ").lower()
                if jenisbuku not in ["digital", "referensi", "normal"]:
                    print("Pilihan tidak valid. Silakan pilih 'Digital', 'Referensi', atau 'Normal'.")

            judul = input("Judul Buku: ")
            pengarang = input("Pengarang: ")

            tahunTerbit = ""
            while not tahunTerbit.isdigit():
                tahunTerbit = input("Tahun Terbit: ")
                if not tahunTerbit.isdigit():
                    print("Tahun Terbit harus berupa angka. Coba lagi.")
            tahunTerbit = int(tahunTerbit)

            ISBN = ""
            while not ISBN.isdigit():
                ISBN = input("ISBN: ")
                if not ISBN.isdigit():
                    print("ISBN harus berupa angka. Coba lagi.")

            if jenisbuku == "digital":
                formatFile = ""
                while formatFile not in ["pdf", "epub"]:
                    formatFile = input("Format File (PDF/EPUB): ").lower()
                    if formatFile not in ["pdf", "epub"]:
                        print("Format file tidak valid. Pilih antara 'PDF' atau 'EPUB'.")

                ukuranFile = ""
                while not ukuranFile.replace('.', '', 1).isdigit() or float(ukuranFile) <= 0:
                    ukuranFile = input("Ukuran File (MB): ")
                    if not ukuranFile.replace('.', '', 1).isdigit() or float(ukuranFile) <= 0:
                        print("Ukuran File harus berupa angka positif. Coba lagi.")
                ukuranFile = float(ukuranFile)

                buku = BukuDigital(judul, pengarang, tahunTerbit, ISBN, formatFile, ukuranFile)
                perpustakaan.tambahBuku(buku)

            elif jenisbuku == "referensi":
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

            nomorAnggota = ""
            while not nomorAnggota.isdigit():
                nomorAnggota = input("Nomor Anggota: ")
                if not nomorAnggota.isdigit():
                    print("Nomor Anggota harus berupa angka. Coba lagi.")

            alamat = input("Alamat Anggota: ")
            anggota = Anggota(nama, nomorAnggota, alamat)
            perpustakaan.tambahAnggota(anggota)

        elif perintah == "4" or perintah == "pinjam buku":
            nomorAnggota = input("Nomor Anggota: ")
            judulBuku = input("Judul Buku yang Dipinjam: ")
            perpustakaan.pinjamBuku(nomorAnggota, judulBuku)

        elif perintah == "5" or perintah == "kembalikan buku":
            nomorAnggota = input("Nomor Anggota: ")
            judulBuku = input("Judul Buku yang Dikembalikan: ")
            perpustakaan.kembalikanBuku(nomorAnggota, judulBuku)

        elif perintah == "6" or perintah == "info anggota":
            nomorAnggota = input("Nomor Anggota: ")
            perpustakaan.tampilkanInfoAnggota(nomorAnggota)

        elif perintah == "7" or perintah == "exit":
            print("Terima kasih telah menggunakan aplikasi!")
            break
        else:
            print("Perintah tidak dikenal. Coba lagi.")

if __name__ == "__main__":
    main()
