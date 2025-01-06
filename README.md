# Project_UAS

# Pengelolaan Sampah Rumah Tangga
Nama    :   Nabil Putra Alamsyah
NIM     :   312410376

## Deskripsi Program
Program Pengelolaan Sampah Rumah Tangga adalah aplikasi sederhana berbasis Python yang dirancang untuk membantu mencatat, mengelola, dan menganalisis data sampah rumah tangga. Dengan program ini, pengguna dapat mencatat jenis sampah, berat, dan lokasi pengumpulan. Program ini juga memberikan statistik sederhana seperti total berat sampah organik dan anorganik, serta lokasi pengumpulan dengan sampah terbanyak.

##  Fitur
   -Tambah Data Sampah: Mencatat jenis sampah, berat, dan lokasi pengumpulan.
   -Tampilkan Data: Menampilkan daftar semua data sampah dalam bentuk tabel.
   -Hapus & Ubah Data: Memungkinkan penghapusan atau pengubahan data tertentu.
   -Statistik: Menyediakan statistik sampah organik, anorganik, dan lokasi dengan pengumpulan sampah terbanyak.
   -Struktur Modular: Program menggunakan struktur folder yang rapi untuk memisahkan logika data, tampilan, dan alur utama.

## Struktur Folder
├── data
│   ├── __init__.py
│   ├── sampah.py       -Model data dan logika pengelolaan data
├── view
│   ├── __init__.py
│   ├── input_form.py   -Input form untuk interaksi pengguna
│   ├── sampah.py       -Tampilan tabel dan hasil data
├── main.py             -Program utama yang mengatur menu dan alur program

## Menu Utama
Program Pengelolaan Sampah Rumah Tangga
    1. Tambah Data Sampah
    2. Lihat Data Sampah
    3. Ubah Data Sampah
    4. Hapus Data Sampah
    5. Keluar

## Tabel Data Sampah
+----+--------------+------------+-------------------+
| No | Jenis Sampah | Berat (kg) | Lokasi            |
+----+--------------+------------+-------------------+
| 1  | Organik      | 5.0        | Kebun             |
| 2  | Anorganik    | 3.5        | Jalan Utama       |
+----+--------------+------------+-------------------+

## Penjelasan Code Program
    1. File Data/sampah.py
    File ini berisi model data yang digunakan untuk mengelola informasi sampah.

     -Class DataSampah:
         1.Digunakan untuk menyimpan data terkait sampah, seperti kategori, berat, dan lokasi.
         2.Memiliki metode untuk menambah, menghapus, mengubah, dan menampilkan data sampah.

![Gambar](./Gambar/Gambar%201.png)

Metode seperti tambah_sampah, hapus_sampah, ubah_sampah, dan lihat_sampah diimplementasikan untuk memanipulasi data dalam bentuk list.

    2. File View/input_form.py
    File ini bertanggung jawab untuk mengelola input dari pengguna saat menambahkan data sampah.

       -Class InputForm:
          1.Mengambil input berupa kategori, berat, dan lokasi.
          2.Fungsi ini dipanggil saat pengguna memilih untuk menambah data sampah.

![Gambar](./Gambar/Gambar%202.png)

    3. File View/sampah.py
    File ini bertanggung jawab untuk menampilkan data sampah ke layar.

       -Class ViewSampah:
          1.Berisi metode seperti lihat_sampah dan lihat_detail untuk menampilkan semua data sampah atau detail tertentu.

![Gambar](./Gambar/Gambar%203.png)

    4. File main.py
    File ini adalah program utama yang berisi menu navigasi untuk mengelola program.

       -Fungsi menu_utama:
          1.Menampilkan menu utama dan meminta pengguna memilih aksi (1-5).
          2.Opsi: Tambah Sampah, Lihat Daftar Sampah, Ubah Data Sampah, Hapus Sampah, Keluar.

       -Fungsi main:
          1.Mengontrol alur program berdasarkan pilihan pengguna.
          2.Contoh:
               -Jika pengguna memilih 1, akan memanggil fungsi tambah sampah.
               -Jika memilih 5, program akan berhenti

![Gambar](./Gambar/Gambar%204.png)
