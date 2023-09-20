Nama : Catherine Hana Natalie

NPM : 2206083123

Kelas : PBP B

Link Adaptable: https://hanagrosir.adaptable.app/main/

===================================== Tugas PBP 3 =======================================================

1. Apa perbedaan antara form POST dan form GET dalam Django?
   Django adalah framework web yang biasanya digunakan untuk mengembangkan aplikasi web dengan bahasa pemrograman Python. Di sini, kita dapat menggunakan metode HTTP POST dan GET untuk mengirimkan data antara server web dengan browser klien. Ini adalah perbedaan dari form POST dan form Get:

   - Tujuan,

     - Form POST: Biasa digunakan untuk mengirimkan data yang akan disimpan dan diproses oleh server.
     - Form GET: Biasa digunakan untuk mengambil data dari server tanpa memengaruhi atau mengubah data di server

   - Kemananan,

     - Form POST: Data yang dikirim akan dikirim secara tersembunyi ke server. Ini membuat proses lebih aman digunakan untuk mengirim data sensitif, seperti informasi pribadi atau kata sandi. Data-data yang dikirim juga tidak terlihat di URL
     - Form GET: Data yang dikirim akan dikirim sebagai parameter URL. Ini dilakukan agar terlihat di URL. Berbeda dengan POST, GET tidak aman untuk mengirim data sensitif

   - Batasan panjang data,

     - Form POST: Tidak memiliki batasan panjang data yang bisa dikirim sehingga cocok untuk mengirimkan data dengan ukuran yang sangat besar
     - Form GET: Ada batasan pada panjang URL sehingga tidak disarankan untuk mengirimkan data dengan ukuran yang sangat besar

   - Tampilan URL,

     - Form POST: Di sini, parameter data tidak terlihat di URL
     - Form GET: Di sini parameter data terlihat di URL

   - Bookmarking dan caching,
     - Form POST: Di sini, data yang dikirm tidak dapat di-bookmark dan tidak disimpan di dalam cache browser
     - FORM GET: DI sini data ang dikirim dapat di-bookmark dan disimpan di dalam cache browser

2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
   JSON, XML, dan HTML adalah format yang digunakan dalam pengiriman data di web dan aplikasi. JSON adalah singkatan dari JavaScript Object Notation. XML adalah singkatan dari eXtensible Markup Language. HTML adalah singkatan dari HyperText Markup Language. Berikut perbedaan dari ketiga format tadi:

   - Tujuan,

     - JSON: Merupakan format data yang digunakan untuk melakukan proses pertukaran data antar aplikasi. JSON mudah dibaca oleh manusia dan diproses oleh komputer
     - XML: Merupakan format data yang digunakan untuk mengatur dan menyimpan data dalam struktur hirarkis. XML biasa digunakan untuk pertukaran data yang sangat terstruktur dan dapat digunakan di platform-platform
     - HTML: Merupakan bahasa markup yang digunakan untuk membuat tampilan konten dan struktur di web. HTML bisa untuk pertukaran data tapi tidak begitu lengkap

   - Syntax,

     - JSON: Syntax yang digunakan adalah pasangan nama-nilai(key-value pairs) dalam format teks
     - XML: Syntax yang digunakan adalah tag yang mendefinisikan elemen dan atribut untuk menyusun data
     - HTML: Syntax yang digunakan adalah tag, tetapi berbeda dengan XML, fungsi di HTML adalah untuk mengatur tampilan di konten halaman web

   - Ekosistem,

     - JSON: JSON sudah menjadi format standar untuk RESTful API dan banyak bahasa pemrograman sudah memiliki dukungan bawaan untuk memproses JSON
     - XML: XML sudah memiliki dukungan luas dan banyak alat untuk memproses dan mengurai datanya
     - HTML: HTML sudah didukung oleh semua web

   - Kemudahan untuk dibaca,
     - JSON: Dengan syntax yang sederhana, JSON mudah dibaca oleh manusia
     - XML: Struktur dari XML kuat tetapi sulit dibaca oleh manusia karena syntaxnya cenderung lebih kompleks
     - HTML: HTML sudah dirancang untuk mudah dibaca oleh manusia dan untuk membuat tampilan web.

3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
   JSON sering digunakan dalam pertukaran data antara aplikasi web modern karena JSON memiliki banyak keunggulan yang membuatnya cocok untuk mengembangkan web saat ini. Berikut adalah keuntungan-keuntungan dari JSON:

   - JSON memiliki syntax yang sangat sederhana dan mudah dimengerti oleh manusia. Syntax dari JSON adalah key-value pairs dalam format teks, ini mirip dengan objek dalam bahasa pemrograman. Dengan kemudahannya untuk dimengerti dan dibaca, JSON membuat tim pengembangan web dapat dengan cepat memeriksa dan memahami data-data yang ditransmisi.

   - JSON mudah diproses oleh komputer. JSON sangat efisien dalam pengembangan aplikasi karena sebagian besar bahasa pemrograman sudah punya pusataka atau modul bawaan untuk mengurai JSON.

   - JSON dapat ditransmisikan dengan cepat melalui jaringan dan tidak memberikan beban yang besar atau lebi dari yang diperlukan kepada sumber daya

   - JSON dapat digunakan di berbagai platform dan bahasa pemrograman. JSON menjadi ideal untuk pertukaran data antara berbagai sistem.

   - JSON memungkinkan kita untuk menyususn data dalam hierarki yang dalam dan kompleks dengan adanya struktur data bersarang. Ini juga membuat JSON mempunya representasi data yang fleksibel

   - JSON sudah menjad standar untuk pertukaran di banyak layanan web RESTful(Representational State Transfer). API yang menggunakan JSON biasanya lebih mudah dipahami dan digunakan

   - JSON mendukung berbagai tipe dasar, seperti string, int, boolean, dll. Hal ini membuat kita untuk menggambarkan berbagai jenis data dengan mudah di JSON

   - JSON adalah bagian integral dari JavaScript sehingga JSON dapat dengan mudah diintegrasikan dengan JAvaScript. Hal ini membuat aplikasi web yang dibuat dengan bahasa JAvaScript dapat dengan mudah mengurai dan memproses data JSON

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- Membuat form sederhana untuk menginput data barang pada aplikasi dengan menambahkan kode di forms.py. Kode ini untuk membuat struktur form yang dapat menerima data produk baru. Model yang dipakai sesuai dengan tugas PBP 2, yaitu Item
- Mengisi field pada kode pembuatan forms sesuai kebutuhan. Di kasus saya ada name, price, description, picture, ammount, weight
- Membuat fungsi baru dengan nama create_product di berkas views.py dan import semua yang diperlukan. Fungsi create_product akan menerima parameter request
- Membuat ProductForm baru dengan memasukkan QueryDict berdasarkan input dari user pada requeat.POST dengan kode form = ProductForm(request.POST or None)
- Memvalidasi dan menyimpan data dan input dari form
- Memasukan kode products = Item.objects.all() pada berkas views.py di fungsi show_main untuk mengambil seluruh objek Item yang tersimpan di database
- Import fungsi create_product di berkas urls.py di main
- Menambahkan path UTL ke dalam urlpatterns di urls.py di main untuk mengakses fungsi yang sudah di-import
- Membuat berkas create_product.html, yaitu berkas html baru di folders templates pada main untuk mengatur tampilan dari web saat pengguna ingin menambahkan product baru
- Menambahkan kode {% block content %} di main.html untuk menampilkan data produk dalam bentuk tabel beserta tombol "Add New Product" yang akan di redirect ke halaman form
- Membuat fungsi baru di views.py pada main. Fungsi baru tersebut bernama show_xml dan menerima parameter request. Di dalam fungsi ini juga ada variabel data untuk menyimpan hasil query dari seluruh data yang ada pada Item.
- Melakukan import HTTpResponse dan Serializer pada views.py di main
- Menambahkan retrun function berupa HTTpResponse yang berisi paramater data hasil query yang sudah diserialisasi menjadi parameter dan XML ke dalam fungsi show_xml
- Import fungsi show_xml ke urls.py di main.
- Menambahkan path url show_xml ke dalam urlpattern untuk megakses fungsi show_xml
- Membuat dungsi baru bernama show_json yang menerima parameter request dan sebuah cariabel data untuk menimpan hasil query seluruh data di Item di views.py pada main
- Menambahkan return function berupa HTTpResponse yang berisi parameter data hasi query yang sdah diserialisasi menjadi parameter dan JSON ke dalan fungsi show_json
- import fungsi show_json ke urls.py di main dan menambahkan path url show_json ke dalam urlpatterns untuk mengakses fungsi show_json
- Membuat fungsi baru yang menerima parameter request dan id dengan nama show_xml_by_id dan show_json_by_id di views.py pada main
- Membuat variabel data di dalam kedua fungsi tadi untuk meyimpan hasil query dari data dengan id tertentu yang ada pada Item
- Menambakan return function berupa HTTpResponse yang berisi parameter data dan hasil query yang sudah diserialisasi menjadi JSON atau XML dan parameter conten_type dengan value application/xml untuk format XML atau application/json untuk JSON
- Import fungsi show_xml_by_id dan show_json_by_id ke dalam urls.py di main
- Menambahkan path url show_xml_by_id dan show_json_by_id ke dalam urlpatterns untuk mengakses kedua fungsi tersebut
- Memastikan bahwa perintah python manage.py runserver sudah berjalan
- Mendownload dan membuka postman
- Membuat request baru dengan method GET dan url untuk XML atau JSON untuk mengetes apakah data terkirimkan dengan baik
- Untuk mengetes fungsi pengambilan data produk berdasarkan ID, kita bisa mengubah url dengan menambahkan "/[id]"

5. Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md
   ![SS HTML](PBP3_HTML.jpg)
   ![SS JSON](PBP3_JSON.jpg)
   ![SS XML](PBP3_XML.jpg)
   ![SS JSON dengan ID](PBP3_JSON_ID.jpg)
   ![SS XML dengan ID](PBP3_XML_ID.jpg)

========================================= Selesai Tugas PBP 3 ===========================================

========================================== Tugas PBP 2 ==================================================

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

========================================= Selesai Tugas PBP 2 ===========================================
