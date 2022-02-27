# Tucil2_STIMA
Tucil 2 Strategi Algoritma

## Penulis
Nathanael Santoso/13520129

## Pendahuluan
Pada Repository ini terdapat implentasi dari "myConvexHull.py" yaitu suatu library yang mampu menghitung convex hull dari sebuah dataset. Convex hull bidang yang dibentuk titik terluar sebuah kumpulan titik sehingga untuk titik sembarang dalam kumpulan titik, terdapat di dalam Convex hull. Library ini diimplementasikan menggunakan OOP yaitu membuat class bernama ConvexHull yang memiliki atribut array points sebagai kumpulan titik, dan array hull sebagai kumpulan titik pada convex hull. Class juga memiliki metode getHull untuk menyelesaikan metode lainnya. Data kemudian dapat divisualisasikan menggunakan pustaka matplotlib, numpy, pandas, dan sklearn. Library ini memanfaatkan library math untuk mempermudah perhitungan akar kuadrat.

## Cara menjalankan
1. Ubah Working Directory menjadi "%PATH%\src" atau jika sudah berada pada folder repository, lakukan "cd src".
2. Masukkan command "python myConvexHull.py" untuk menjalankan program.
3. Jangan lupa close window hasil visualisasi jika selesai.
4. Jika ingin menggunakan dataset lain lakukan hal berikut:
 - pada bagian bawah program setelah baris "if \_\_name\_\_ == "\_\_main\_\_":" ubah baris "data = datasets.load_wine()" pada bagian load wine dengan toy dataset yang tersedia pada scipy. (cth. load_iris(), load_breast_cancer(), dsb.)
 - ubah title pada baris "plt.title('Wine Alcohol vs Malic Acid')" menjadi title yang sesuai
 - ubah index pada baris yang mengandung "xlabel" dan "ylabel" menjadi kolom yang sesuai
 - ubah index pada baris yang mengandung "iloc" menjadi kolom sesuai kolom di atas
 - ubah path pada baris yang mengandung "plt.savefig('c:/Github/Tucil2_STIMA/test/Alcohol.png')" menjadi path yang diinginkan atau jika perlu. Jangan lupa mengubah nama gambar. (cth: "plt.savefig('%PATH%/test/nama_gambar.png))
 - untuk dataset yang mengandung lebih dari 3 kelas, tambahkan jenis warna pada array colors
 - Jika tetap tidak bisa, maka dataset tersebut tidak bisa dipakai dalam visualisasi ini atau diperlukan implementasi visualisasi per kasus (tidak ada implementasi visualisasi data one size fits all)

## Requirement
- Python 3 (dianjurkan versi terbaru)
- library numpy, pandas, matplotlib, sklearn (install pada command prompt dengan command "pip install lib_name" cth: "pip install numpy")