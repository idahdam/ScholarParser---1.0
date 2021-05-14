## Apa itu Scholar Parser?

ScholarParser adalah aplikasi yang memiliki tujuan untuk melakukan proses ekstraksi file HTML yang berisi referensi dan menyimpannya ke file XLSX. Hal yang perlu user lakukan untuk mencapai hal ini cukup mudah:
1. Buka file dengan tombol `Open File`
2. Lakukan ekstraksi dengan `Start Parse`
3. User dapat melihat hasil ekstraksi dengan `Show Content`
4. Buat file XLSX dengan GoogleScholar CustomAPI dan melakukan rekapitulasi dengan membuat file XLSX

## Apa saja isi file XLSX yang terbentuk?

File XLSX memiliki 5 kolom:
1. Nama kontributor 
2. Judul
3. Afiliasi
4. Link Publikasi
5. Link E-Print (PDF)


## Beberapa hal yang harus diperhatikan (Disclaimer)

1. Tidak ada alamat email dikarenakan tidak semua mencantumkan alamat email pada halaman scholar ataupun paper. Oleh karena itu, file publikasi diberikan pada hasil akhir.
2. Tidak semua kontributor atau pembuat dapat ditampilkan. Hal ini dapat terjadi dikarenakan antara nama kontributor belum terindeks pada GoogleScholar atau yang terindeks pada GoogleScholar tidak sinkron dengan jurnal/paper
3. Poin nomor dua juga berlaku pada afiliasi dan link. 
4. Jika tidak ditemukan, pada file XLSX akan terdapat cell yang memiliki kata `... not found`.

## Bagaimana cara menggunakannya?

1. Install Python (pembuatan menggunakan Python 3.9). Gunakan command prompt/terminal/powershell untuk melakukan pengecekan dan masukkan command berikut:
```
python --version
```
2. Install beberapa dependencies menggunakan pip:
```
pip install scholarly xlsxwriter html2text
```

3. Download file pada link [berikut](https://github.com/idahdam/ScholarParser-1.0/releases). File bernama ScholarParser-v1.0.zip. Ekstrak ke suatu folder, dengan menggunakan CMD/Terminal/Powershell, pindah ke directory yang berisi mainWindow.py dan README.txt. 
4. Jalankan program dengan command:
```
py mainWindow.py
```
5. Tedapat file bernama `exampleFile.txt` yang merupakan file untuk melakukan pengetesan. Log yang terjadi pada aplikasi akan terlihat pada terminal. Done.



## Things to be done:
1. Multithreading
2. GUI Fixing
3. Other scholar API addition

## Interested on contributing?
Just fork it and let me know how you do it!
