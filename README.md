Nama : Catherine Hana Natalie

NPM : 2206083123

Kelas : PBP B

Link Adaptable: https://hanagrosir.adaptable.app

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Membuat direktori baru dengan nama Hana_Grosir di direktori lokal
- Membuat repository baru dengna sifat public dan dengan nama Tugas02PBP
- Membuat dan mengaktifkan virtual environment di command prompt tempat direktori lokal tadi
- Membuat file baru dengan nama requirements.txt yang berisikan dependencies yang diperlukan
- Memasang dependencies dengan perintah di command prompt
- Membuat proyek Django bernama Hana_Grosir di command prompt
- Menambahkan ("_") pada bagian ALLOWED_HOSTS di dalam file settings.py di direktori lokal untuk deployment web. ALLOWED_HOSTS adalah daftar host yang dapat mengakses aplikasi web, dengan menambahkan ("_"), semua host dapat mengakses aplikasi.
- Menjalankan perintah untuk menjalankan server Django di command prompt
- Membuat aplikasi baru bernama main dalam proyek Hana_Grosir
- Menjalankan perintah untuk membuat aplikasi baru. Setelah ini akan ada direktori baru di dalam direktri lokal dengan nama main yang berisi struktur awal aplikasi
- Mendaftarkan aplikasi main ke dalam proyek dengan menambahkan kode "main," ke dalam variabel INSTALLED_APPS di berkan settings.py dalam drektori proyek Hana_Grosir
- Membuat routing pada proyek agar aplikasi main bisa berjalan dengan membuat berkas urls.py di dalam direktori aplikasi main. Kodenya meliput mengimport path dari django.urls untuk mendefinisikan pola url, mengimport show_main dari main.views, nama aplikasi, yaitu main pada pola url di aplikasi, dan path ke fungsi show_main
- Membuat model dalam aplikasi main dengan nama item dan memiliki atribut name, amount, description, price, dan weight di dalam file models.py di direktori aplikasi main untuk mendefinisikan model baru. Dimulai dengan meng-import models dari django.db dan membuat kelas item sebagai nama model berisi attribut tadi.
- Melakukan migrasi model dan migrasi ke dalam basis data lokal setiap melakukan perubahan di model
- Membuat fungsi show_main di file views.py dalam direktori aplikasi main untuk dikembalikan di folder templates di file main.html. Ini akan menunjukkan nama aplikasi, nama, kelas, dan isi dari aplikasinya. Ada kode return render juga untuk memunculkan file views.py di file main.html
- Membuat routing pada file urls.py di direktori aplikasi main untuk memetakan fungsi yang telah dibuat di views.py. Routing ini ada di urlpatterns dengan perintah path. Dan ada import show_main dari main.views
- Melakukan deployment ke Adaptable terhadap aplikasi main dengan cara membuat app baru, menghubungkan repository Tugas02PBP, memilih python app template sebagai template deployment, memilih PostgreSQL sebagai tipe basis data yang akan digunakan, menyesuaikan versi python saya, yaitu versi 3.10, dan pada bagian start command memasukkan perintah python manage.py migrate && gunicorn Hana_Grosir.wsgi
- Memberikan nama untuk aplikasi
- Mencentang bagian HTTP Listener on Prt dan klik Deploy App
- Menunggu sampai App berhasil di deploy

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
   ![Bagan PBP](BaganPBP.jpg)

3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment adalah sebuah alat yang digunakan dalam pengembangan proyek untuk mengisolasi dependensi dan paket-paket dalam proyek tertentu. Kita menggunakan virtual environment karena virtual environment memiliki peran-peran penting dalam mengembangkan perangkat lunak. Peran-peran penting tersebut adalah

- Keamanan,
  Dengan virtual environment, kita dapat mengontrol sumber dependensi di proyek dan mengisolasi proyek kita dari sistem operasi secara keseluruhan. Dengan mengontrol sumber dependensi kita bisa menghindari penggunaan dependesi yang tidak aman. Dengan mengisolasi proyek, kita bisa menghindari terjadinya konflik antara proyek kita dan sistem operasi yang ada.

- Isolasi dependensi,
  Virtual environtment memungkinkan kita untuk mengisolasi dependensi yang berbeda untuk proyek-proyek yang berbeda saat kita mengembangkan perangkat lunak. Bisa ada proyek-proyek tertentu yang memerlukan versi yang berbeda dari paket atau dependensi lainnya sehingga isolasi dependensi ini dapat membuat satu proyek terisolasi dengan semua yang diperlukan. Ini dapat membuat pengembangan perangkat lunak berjalan dengan lancar. Tanpa isolasi, bisa saja ada proyek yang tidak bisa berjalan di suatu versi dependensi yang digunakan.

- Pengelolaan,
  Dengan virtual environment, kita bisa menjaga proyek kita tetap teratur. Kita bisa mengelola dependensi secara terpisah dengan dependesi sistem operasi kita. Hal ini mempermudah kita dalam memperbarui, merawat, dan menghapus dependensi proyek lain tanpa memengaruhi sistem operasi kita dan dependesi lainnya.

- Kemudahan dalam mengakses,
  Dengan virtual environment, kita dapat dengan mudah membagikan proyek dengan orang lain atau memindahkannya ke sistem lain tanpa perlu khawatir tentang konflik atau persyaratan lainnya. Kita bisa membuat dan membagikan file konfigurasi yang menjelaskan dependensi proyek kita.

4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
   MVC, MVT, dan MVVM adalah pola arsitektur perangkat lunak yang digunakan untuk mengatur kode dalam aplikasi.

- MVC (Model-View-Controller),
  MVC adalah salah satu pola arsitektur dalam industri perangkat lunak yang paling dikenal. Pola ini memfasilitasi pemisahan perhatian dengan membagi aplikasi menjadi:

  - Model,
    Bagian ini mewakili data dan logika bisnis dalam aplikasi. Ini bertanggung jawab untuk mengelola, memproses, dan menyimpan data. Ini jga menerapkan aturan bisnis yang diperlukan
  - View,
    Bagian ini mewakili antarmuka pengguna(UI) dalam aplikasi dan lapisan presentasi, artinya bagian ini bertanggung jawab untuk menampilkan data kepada pengguna dan menanggapi input dari pengguna.
  - Controller,
    Bagian ini bertindak sebagai perantara antara tampilan dan model. Bagian ini menangani interaksi pengguna dan meneruskan permintaan di bagian view ke bagian model.

- MVT (Model-View-Template),
  Ada tiga komponen utama dalam bagian ini, yaitu:

  - Model,
    Bagian ini mewakili data dan logika bisnis dalam aplikasi. Bagian ini mirip dengan komponen model dalam MVC
  - View,
    Bagian ini bertanggung jawab dalam menangani presentasi data kepada pengguna
  - Template,
    Bagian ini bertanggung jawab dalam mengatur penampilan data dalam HTML dari sistem hingga tata caranya. Bagian ini terpisah dari view.

- MVVM(Model-View-ViewModel),
  Model ini memiliki tiga komponen utama, yaitu:
  - Model,
    Bagian ini mewakili data dan logika bisnis. Bagian ini masih sama dengan MVC dan MVT. Bagian ini bertanggung jawab dalam menyimpan dan mengambil data dan memprosesnya.
  - View,
    Bagian ini mewakili antarmuka pengguna, menampilkan data dari ViewModel dan menanggapi tindakan dari pengguna.
  - ViewModel,
    Bagian ini berfungsi sebagai jembatan antara model dan view. Bagian ini bertanggung jawab dalam mengelola logika tampilan dan menjalankan operasi untuk mengubah data sebelum ditampilkan di view.

Perbedaan:

- MVC,
  Pada pola ini, ketiga komponen utama, yaitu model, view, dan controller memiliki tanggung jawab yang jelas dan terpisah. MVC biasa digunakan untuk pengembangan aplikasi dekstop dan web. Bagian model dan view juga tidak tahu satu sama lain secara langsung, mereka hanya berkomunikasi lewat controller. Controller juga mengontrol logika aplikasi

- MVT,
  Pola ini biasanya digunakan dalam kerangka web, seperti Django di Python. Perbedaan utama terdapat dalam bagian template. Pola ini menggabungkan prinsip WVC dengan bagian template yang memisahkan tampilan dari logika sehingga tampilan dapat didefinisikan terpisah dalam file template. Ini khususnya digunakan dalam pengembangan web

- MVVN,
  Pola ini sering digunakan untuk mengembangkan aplikasi berbasis data. Pola ini mengenalkan ViewModel sebagai lapisan tambahan yang akan memisahkan tampilan dan logika dari bagian model. ViewModel mengelola tampilan secara terpusat sehingga bisa ada transformasi data sebelum ditampilkan di bagian view. Hasilnya, pengelolaan tampilan dalam menjadi lebih fleksibel. Hal inilah yang membuat pola ini sering digunakan di dalam aplikasi web modern dan berbasis mobile
