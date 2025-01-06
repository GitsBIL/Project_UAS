class ViewSampah:
    @staticmethod
    def tampilkan_sampah(data_sampah):
        if not data_sampah:
            print("Tidak ada data sampah yang tercatat.")
            return

        print("\nDaftar Sampah Rumah Tangga:")
        print("Kategori\tBerat (kg)\tLokasi")
        print("-" * 40)
        for sampah in data_sampah:
            print(f"{sampah.kategori}\t\t{sampah.berat}\t\t{sampah.lokasi}")
        print("-" * 40)

    @staticmethod
    def detail_sampah(sampah):
        if sampah:
            print("\nDetail Sampah:")
            print(f"Kategori: {sampah.kategori}")
            print(f"Berat: {sampah.berat} kg")
            print(f"Lokasi: {sampah.lokasi}")
        else:
            print("Sampah dengan kategori tersebut tidak ditemukan.")
