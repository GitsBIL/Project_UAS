class InputForm:
    @staticmethod
    def form_tambah():
        kategori = input("Masukkan Kategori Sampah (Organik/Anorganik/B3): ")
        berat = float(input("Masukkan Berat Sampah (kg): "))
        lokasi = input("Masukkan Lokasi Pengambilan: ")
        return kategori, berat, lokasi

    @staticmethod
    def form_ubah():
        kategori = input("Masukkan Kategori Sampah yang ingin diubah: ")
        berat_baru = float(input("Masukkan Berat Baru (kg): "))
        lokasi_baru = input("Masukkan Lokasi Baru: ")
        return kategori, berat_baru, lokasi_baru

    @staticmethod
    def form_hapus():
        kategori = input("Masukkan Kategori Sampah yang ingin dihapus: ")
        return kategori
