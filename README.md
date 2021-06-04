# Tugas-Akhir-MetodeNumerik-2021
Reporsitori ini dibuat untuk memenuhi Tugas Akhir Metode Numerik Oseanografi 2021. Reporsitor ini memuat executable (.exe) file yang dapat memproses beberapa persamaan metode numerik untuk penyelesaian perhitungan numerik. seluruh script yang dibuat adalah hasil kelompok 1 Oseanografi 2019. semoga dapat bermanfaat!


# Modul 2
# Metode Setengah Interval
Metode Setengah Interval merupakan metode analisis numerik paling sederhana diantara metode-metode analisis lainnya. Metode ini termasuk metode yang tangguh, meskipun metode ini sangat sederhana namun selalu dapat menemukan akar persamaan yang dicari. Kelebihan dari metode ini adalah selalu berhasil dalam menentukan akar-akar yang dicari atau dengan kata lain selalu konvergen. Selain kelebihan, dalam metode ini juga terdapat kekurangan, yaitu hanya dapat dilakukan apabila ada akar persamaan pada interval yang diberikan. Jika terdapat beberapa akar pada interval yang diberikan maka hanya satu akar saja yang dapat ditemukan.
# Metode Interpolasi Linier
Metode Interpolasi Linier hampir mirip dengan metode setengah interval. Prinsip pencarian akar persamaan dari metode ini didasarkan pada penggunaan interpolasi linier. Interpolasi linier dilakukan melalui dua titik pertama dengan garis interpolasi memotong sumbu x dan dititik perpotongan tersebut didapatkan pendekatan akar yang pertama. Kemudian pendekatan tersebut dievaluasi pada fungsi nonlinier sehingga diperoleh titik pada fungsi nonlinier tersebut. Kemudian dilakukan lagi interpolasi melalui ujung sebelumnya dan diperoleh pendekatan akar berikutnya.
# Metode Newton Rhapson
Metode Newton-Raphson merupakan metode yang sederhana,namun cukup handal dalam mendapatkan akar persamaan nonlinier, dengan catatan terkaan awal yang diberikan cukup dekat. Metode Newton-Raphson tidak memerlukan dua buah terkaan awal, melainkan cukup satu saja tetapi diusahakan terkaan tersebut cukup dekat dengan akar persamaan yang dicari. Metode Newton-Raphson memiliki laju konvergensi lebih cepat, akan tetapi, syarat yang harus dipenuhi adalah bahwa taksiran awal yang diberikan harus sedekat mungkin dengan harga eksaknya. Metode Newton-Raphson memiliki kelebihan dan kekurangan. Kelebihan dari metode Newthon-Raphson adalah nilai yang konvergensi yang dihasilkan lebih cepat. Sedangkan kelemahan dari metode ini adalah tidak selalu menemukan akar (divergen) , kemungkinan sulit dalam mencari f’(xn) dan penetapan harga awal (xn) yang sulit.
# Metode Secant
Pada dasarnya metode Secant sama dengan metode Newton-Raphson, perbedaannya hanya terletak pada pendekatan untuk turunan pertama dari f saja. Pendekatan f' pada metode Secant didekati dengan ungkapan beda hingga yang didasarkan pada taksiran akar sebelumnya (beda mundur), yaitu disebut juga Metode Interpolasi Linear, dalam prosesnya tidak dilakukan penjepitan akar [x0, x1] dan tidak harus mengandung akar yang akan dicari, sehingga f(x0) dan f(x1) bisa bertanda sama serta iterasi berlangsung sampai batas maksimum atau sampai dipenuhinya batas Toleransi (T).
# Metode Iterasi
Metode iterasi (tidak langsung) merupakan metode yang berbasiskan terhadap aplikasi dari langkah algoritma sederhana yang diulang-ulang pada sistem persamaan tersebut hingga sistem persamaan mencapai keadaan konvergen yang merepresentasikan solusi dari suatu sistem persamaan. Pada metode iterasi, banyaknya langkah-langkah perhitungan yang dilakukan tidak dapat diprediksi, dimana tipikalnya adalah sebanyak N perhitungan per satu kali iterasi. Kekurangan lainnya adalah, jika sistem persamaan tidak berada pada kondisi yang kondusif, maka konvergensi dari suatu sistem persamaan tidak dapat terjamin. Kelebihan dari penggunaan metode iterasi adalah sedikitnya memori komputer yang digunakan sebagai akibat dari algoritma yang mendesain agar komputer hanya menyimpan koefisien-koefisien yang tidak nol. 
# Modul 3
# Metode Gauss
Metode Gauss adalah suatu cara mengoperasikan nilai-nilai di dalam matriks menjadi matriks yang lebih sederhana dan banyak digunakan dalam penyelesaian sistem persamaan linier. Prosedur penyelesaian dari metode ini adalah dengan melakukan operasi baris menjadi matriks eselon-baris. Metode ini mengubah persamaan linear tersebut ke dalam matriks augmentasi dan mengoperasikannya. Metode eliminasi gauss termasuk dalam metode penyelesaian persamaan linear dengan cara langsung. Metode Gauss ini adalah membawa persamaan kedalam bentuk matriks dan menyederhanakan matriks menjadi bentuk segitiga atas. Setelah mendapat bentuk matriks tersebut dilakukan subtitusi balik untuk mendapat nilai dari akar persamaan.
# Metode Gauss Jordan
Metode Gauss-Jordan adalah pengembangan dari eliminasi Gauss yang hasilnya lebih sederhana lagi. Metode ini meneruskan operasi baris dari eliminasi Gauss sehingga menghasilkan matriks yang Eselon-baris dan juga dapat digunakan sebagai salah satu metode penyelesaian persamaan linear dengan menggunakan matriks. Metode Gauss-Jordan juga dapat digunakan untuk mencari invers dari sebuah matriks.
# Metode Gauss Seidel
Metode iterasi Gauss-Seidel adalah metode yang menggunakan proses iterasi hingga diperoleh nilai-nilai yang berubah-ubah dan akhirnya relatif konstan. Metode iterasi Gauss- Seidel dikembangkan dari gagasan metode iterasi pada solusi persamaan tak linier. Metode eliminasi gauss-seidel digunakan untuk menyelesaikan SPL yang berukuran kecil karena metode ini lebih efisien. Dengan metode iterasi Gauss-Seidel toleransi pembulatan dapat diperkecil karena iterasi dapat diteruskan sampai seteliti mungkin sesuai dengan batas toleransi yang diinginkan. Kelemahan dari metode ini adalah masalah pivot (titik tengah) yang harus benar–benar diperhatikan, karena penyusunan yang salah akan menyebabkan iterasi menjadi divergen dan tidak diperoleh hasil yang benar.
# Metode Jacobi
Metode iterasi Jacobi digunakan untuk menyelesaikan persamaan linier yang proporsi koefisien nol nya besar. Iterasi dapat diartikan sebagai suatu proses atau metode yang digunakan secara berulang-ulang (pengulangan) dalam menyelesaikan suatu permasalahan matematika. Kelebihan dari metode ini adalah langkah penyelesaiannya yang sederhana, sedangkan kelemahannya adalah proses iterasinya lambat. Terutama untuk persamaan linear serentak dengan ordo tinggi dan hanya dapat digunakan menyelesaikan persamaan linear serentak.
# MODUL 4
Integrasi numerik merupakan cara alternatif untuk mengintegrasikan suatu persamaan, disamping integrasi analitis. Integrasi analitis terkadang merupakan cara integrasi yang sulit, khususnya pada persamaan-persamaan yang kompleks dan rumit. 
# 1. Metode Trapesium Banyak PIAS
Metode trapesium merupakan metode pendekatan integral numerik dengan persamaan polinomial order satu. Dalam metode ini kurve lengkung dari fungsi f (x) digantikan oleh garis lurus.  Pada metode trapesium satu pias memberikan kesalahan sangat besar. Untuk mengurangi kesalahan yang terjadi maka kurve lengkung didekati oleh sejumlah garis lurus, sehingga terbentuk banyak pias. Luas bidang adalah jumlah dari luas beberapa pias tersebut.  Semakin kecil pias yang digunakan, hasil yang didapat menjadi semakin teliti. Metode trapesium dapat digunakan untuk integral suatu fungsi yang diberikan dalam bentuk numerik pada interval diskret.
#2. Metode Simspon 1/3
Kaidah simpson 1/3 adalah kaidah yang mencocokkan polinomial derajat pada tiga titik data diskrit yang mempunyai jarak yang sama.  Hampiran nilai integrasi yang lebih baik dapat ditingkatkan dengan menggunakan polinom interpolasi berderajat yang lebih tinggi. Rumus Simpson dapat diturunkan berdasarkan deret Taylor. Metode simpson 1/3 dapat menghasilkan ketelitian orde 3 dan hanya memerlukan 3 titik.  Pada simpson 1/3 hanya berlaku untuk jumlah pias genap.
# MODUL 5
Persamaan diferensial adalah persamaan yang memuat turunan satu atau beberapa fungsi yang tak diketahui.  Persamaan diferensial biasa hanya mengandung satu variable bebas. Metode satu langkah persamaan diferensial biasa ilaha metode euler maupun metode heun.
# 1. Metode Euler
Metode Euler dapat diturunkan dari Deret Taylor. etode Euler menggunakan garis tangen ke fungsi di awal interval sebagai perkiraan kemiringan fungsi selama interval, dengan asumsi bahwa jika ukuran langkah kecil, kesalahan akan menjadi kecil.  Metode Euler digunakan sebagai dasar untuk metode Heun. Metode ini pada dasarnya adalah merepresentasikan solusinya dengan beberapa suku deret Taylor. Metode Euler adalah salah satu dari metode satu langkah yang paling sederhana. Di banding dengan beberapa metode lainnya, metode ini paling kurang teliti. Namun demikian metode ini perlu dipelajari mengingat kesederhanaannya dan mudah pemahamannya.
# 2. Metode Heun
Metode Heun adalah salah satu metode numerik yang dapat digunakan untuk menyelesaikan berbagai persoalan matematika yang mempunyai masalah nilai awal. Metode ini melibatkan 2 buah persamaan. Persamaan pertama disebut sebagai persamaan prediktor yang digunakan untuk memprediksi nilai integrasi awal.  Persamaan kedua disebut sebagai persamaan korektor yang mengoreksi hasil integrasi awal.

# Nama anggota Kelompok 1 :
1. Sylvia Tursina 26050119140157
2. Almira Calosa Adiska 26050119140152
3. Ayesha Waneta 26050119140151
4. Rena Sagita 26050119140149
5. Riska Widyah Ningrum 26050119120002
6. Marihot Axell Adellio 26050119140147
7. Luis Figo 26050119140154
8. M.Firouz Dimas Sadewo 26050119140153
9. Arij Kemala Yasmin Ridarto 26050119140144


# saran :
1. untuk praktikum selanjutnya dimohon diberikan tutorial yang lebih jelas
2. untuk tutorial selanjutnya diberikan screenschot proses yang gagal dan proses yang sukses

Kami dari kelompok 1 mengucapkan banyak banyak terimaksih kepada dosen pengampu dan asisten praktikum yang telah membimbing dari modul 1 hingga modul 5 praktikum metode numerik 2021.
