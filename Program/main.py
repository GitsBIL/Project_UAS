from Data.sampah import DataSampah
from View.input_form import InputForm
from View.sampah import ViewSampah

def menu_utama():
    print("\n=== Sistem Pengelolaan Sampah Rumah Tangga ===")
    print("1. Tambah Sampah")
    print("2. Lihat Daftar Sampah")
    print("3. Ubah Data Sampah")
    print("4. Hapus Sampah")
    print("5. Keluar")
    pilihan = input("Pilih menu: ")
    return pilihan

def main():
    data_sampah = DataSampah()

    while True:
        pilihan = menu_utama()

        if pilihan == "1":
            print("\n=== Tambah Sampah ===")
            kategori, berat, lokasi = InputForm.form_tambah()
            data_sampah.tambah_sampah(kategori, berat, lokasi)
            print("Data sampah berhasil ditambahkan!")

        elif pilihan == "2":
            print("\n=== Daftar Sampah ===")
            sampah_list = data_sampah.lihat_sampah()
            ViewSampah.tampilkan_sampah(sampah_list)

        elif pilihan == "3":
            print("\n=== Ubah Data Sampah ===")
            kategori, berat_baru, lokasi_baru = InputForm.form_ubah()
            if data_sampah.ubah_sampah(kategori, berat_baru, lokasi_baru):
                print("Data sampah berhasil diubah!")
            else:
                print("Kategori sampah tidak ditemukan.")

        elif pilihan == "4":
            print("\n=== Hapus Sampah ===")
            kategori = InputForm.form_hapus()
            if data_sampah.hapus_sampah(kategori):
                print("Data sampah berhasil dihapus!")
            else:
                print("Kategori sampah tidak ditemukan.")

        elif pilihan == "5":
            print("Keluar dari program. Terima kasih!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
