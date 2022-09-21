 1.  Jelaskan perbedaan antara JSON, XML, dan HTML!
 -> JSON : JSON adalah JavaScript Object Notation. JSON adalah self-describing, sehingga lebih mudah dimengerti dibanding XML.
        Data pada JSON disimpan dalam bentuk dictionary (key dan value). Kelebihan JSON adalah, mudah memodelkan data atau pemetaan langsung, karena
        sintaks nya relatif mudah. Untuk performa, JSON cukup cepat karena menggunakan ruang memori yang sedikit (ukuran file kecil), sangat cocok untuk sistem
        atau grafik objek besar.

 -> XML : XML adalah eXtensible Markup Language. XML adalah self-descriptive. XML hanya informasi yang dibungkus didalam tag.
       Programmer perlu menulis program untuk mengirim, menerima, menyimpan, atau menampilkan informasi tersebut.
       Dokumen XML berbentuk struktur seperti tree yang terdiri dari root, lalu branch, hingga leave. File XML harus mengandung root element
       yang merupakan parent dari elemen lainnya.

       Meskipun XML tidak mudah dibaca jika dibandingkan dengan JSON, XML membuat pertukaran data menjadi lebih mudah, karena struktur data yang jelas
       dan membantu dalam konfigurasi dinamis dan pemuatan variabel

       XML dirancang untuk membawa data, bukan menampilkan data. XML besar dan lambat dalam penguraian, hal ini menyebabkan transmisi data lebih lambat.

 -> HTML : HTML adalah HyperText Markup Language, HTML dirancang untuk menampilkan data di internet (XML dirancang untuk membawa data).
            dan HTML lebih mudah di edit/modifikasi

2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    -> Kita memerlukan data delivery dalam pengimplementasian sebuah platform karena untuk mengirimkan data dari suatu database agar
    dapat ditampilkan di laman web, programmer tidak bisa menaruh data di views dan template, programmer harus menaruh data di database, dan mengirim ke template melalui view.


3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
    1. Membuat aplikasi baru bernama mywatchlist di proyek django pekan 2
        -> run python manage.py startupp mywatchlist
    2. menambahkan path mywatchlist
        -> Menambahkan 'mywatchlist' di variabel INSTALLED_APPS dalam file settings.py dalam folder project_django
    3. Membuat model mywatchlist dengan beberapa atribut
        -> modifikasi models.py yang ada di folder mywatchlist, buat class, dan masukan atribut yang dibutuhkan beserta tipe data yg diperlukan
    4. Menambahkan minimal 10 data untuk objek MyWatchList yang sudah dibuat
        -> Membuat folder fixtures di mywatchlist, dan membuat file json untuk data awal yang diperlukan, masukkan data disitu.
    5. Membuat routing sehingga data dapat diakses melalui URL html, xml, dan json
        -> Membuat sebuah fungsi yang menerima parameter request xml dan json di mywatchlist/views. Lalu
           Membuat file urls.py di folder aplikasi mywatchlist. Lalu import request json dan xml, lalu masukkan path /html /json /xml di urlpatterns
    6. Melakukan deployment ke HEROKU
        -> Push local repository yang sudah diupdate ke github, repository github untuk tugas pbp sudah otomatis terhubung dengan heroku.


4. Screenshot Postman
![]('../../Screenshots/postman_html.png?')
![]('../../Screenshots/postman_json.png?')
![]('../../Screenshots/postman_xml.png?')

LINK MENUJU HEROKU:
1. https://pbp-task2-rev.herokuapp.com/mywatchlist/html
2. https://pbp-task2-rev.herokuapp.com/mywatchlist/xml
3. https://pbp-task2-rev.herokuapp.com/mywatchlist/json