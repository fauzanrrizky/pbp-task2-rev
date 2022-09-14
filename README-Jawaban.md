1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;

Bagan :
![]('../../Bagan-Alur-DJango.png?')

Client mengirim request melalui URL, lalu konfigurasi URL memilih Views yang digunakan. Jika diminta, Views mengirim QuerySet ke models untuk
pertukaran data dengan Database. Lalu Models mengirim respond data tersebut kembali ke Views. Views memilih template html, lalu kembali ke Client dalam bentuk Webpage.

2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
--> Kita menggunakan virtual environment karena suatu project mempunyai kebutuhan yang berbeda-beda antara satu dengan yang lainnya. Virtual environment digunakan
supaya tidak merubah configuration pada sistem operasi yang digunakan.
Membuat aplikasi web berbasis Django tanpa menggunakan virtual environment hanya dapat menggunakan modul-modul global saja, dan berpotensi merubah configuration
pada sistem operasi yang digunakan.

3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
--> 
    1. Saya membuat sebuah fungsi yang menerima parameter request dan mengembalikan render(request, "katalog.html")
    2. Untuk melakukan routing, saya membuat variabel app_name = 'katalog' dan memberi method path dengan beberapa parameter. Saya juga mendaftarkan aplikasi katalog
       ke urls.py yang ada di folder project_django
    3. Untuk pemetaan data ke HTLM, saya menggunakan {{nama}} dan {{npm}}, penggunaan {{}} sesuai dengan dokumentasi template tags pada django.
    4. Untuk deployment ke Heroku, saya menginguti panduan lab0, push local repository yang sudah saya buat, buat aplikasi di web Heroku, masukan variabel di repository
       secrets di github, dan lakukan deployment

4. Link aplikasi Heroku
https://pbp-tugas2-fauzan.herokuapp.com/katalog/
