class Sampah:
    def __init__(self, kategori, berat, lokasi):
        self.kategori = kategori  
        self.berat = berat        
        self.lokasi = lokasi      


class DataSampah:
    def __init__(self):
        self.data_sampah = []

    def tambah_sampah(self, kategori, berat, lokasi):
        sampah = Sampah(kategori, berat, lokasi)
        self.data_sampah.append(sampah)

    def lihat_sampah(self):
        return self.data_sampah

    def cari_sampah(self, kategori):
        for sampah in self.data_sampah:
            if sampah.kategori.lower() == kategori.lower():
                return sampah
        return None

    def hapus_sampah(self, kategori):
      
         sampah = self.cari_sampah(kategori)
         if sampah:
             self.data_sampah.remove(sampah)
             return True
         return False

    def ubah_sampah(self, kategori, berat_baru, lokasi_baru):
      
        sampah = self.cari_sampah(kategori)
        if sampah:
            sampah.berat = berat_baru
            sampah.lokasi = lokasi_baru
            return True
        return False
