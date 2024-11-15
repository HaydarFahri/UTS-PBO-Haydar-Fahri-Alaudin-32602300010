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
            jenisbuku = input("Jenis Buku (Digital/Referensi/Normal): ").lower()
            judul = input("Judul Buku: ")
            pengarang = input("Pengarang: ")
            tahunTerbit = input("Tahun Terbit: ")
            ISBN = input("ISBN: ")

            if jenisbuku == "digital":
                formatFile = input("Format File (PDF/EPUB): ")
                ukuranFile = float(input("Ukuran File (MB): "))
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
            nomorAnggota = input("Nomor Anggota: ")
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
