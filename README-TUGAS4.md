1.  Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
--> CSRF adalah singkatan dari Cross-Site Request Forgery. CSRF adalah serangan yang memungkinkan penyerang untuk menyebabkan user melakukan hal yang tak diinginkan. Sehingga, programmer menggunakan {% csrf_token %} untuk menghindari serangan tersebut. {% csrf_token %} bersifat rahasia, unik, dan tak dapat diprediksi, token tersebut dihasilkan oleh server-side suatu aplikasi, lalu di transmisi ke client sehingga dapat menghindari serangan.
Jika programmer tidak menggunakan {% csrf_token %}, website/aplikasi akan berjalan seperti biasa, namun akan terdapat celah di bagian user dan site yang dapat dimanfaatkan oleh attacker karena tidak terproteksi. User dan site termasuk hal yang paling penting dalam suatu web/aplikasi, dan Django tidak membiarkan deployment tanpa menggunakan {% csrf_token %}


2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
--> Programmer dapat membuat form secara manual dengan tag <input> </input> didalam tag <form></form>. Lalu, untuk mendapatkan data form tersebut dapat menggunakan request.POST.get("____") 


3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
--> Alur: 
    1. User menekan submit setelah mengisi form
    2. Data dari user dapat diakses dengan POST.get yang diaplikasikan di views.py
    3. Programmer dapat menyimpan data ke database menggunakan method save(), atau langsung buat objek dari class form yang dibuat dengan syntax: ClassName.object.create(param1,param2,param3,...)
    4. views.py dapat meminta data ke models.py menggunakan variableData = ToDoList.objects.filter(user=request.user), lalu variableData di pass ke file .html untuk ditampilkan



4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
    1. Membuat suatu aplikasi baru bernama todolist di proyek tugas Django yang sudah digunakan sebelumnya
    --> python manage.py startapp todolist

    2. Menambahkan path todolist sehingga pengguna dapat mengakses http://localhost:8000/todolist.
    --> menambahkan path('todolist/', include('todolist.urls')), pada urls.py pada folder django_project

    3. Membuat sebuah model Task yang memiliki atribut user, date, title, dan description
    --> Membuat class baru pada models.py, dan menambahkan data fields yang dibutuhkan (user,date,title,description,is_finished)

    4.  Mengimplementasikan form registrasi, login, dan logout agar pengguna dapat menggunakan todolist dengan baik.
    --> buat fungsi-fungsi pada views.py yang dapat memproses request tersebut. Lalu membuat templates register.html dan login.html untuk form register dan login

    5. Membuat halaman utama todolist yang memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.
    --> Membuat template todolist.html, yang nantinya dipanggil melalui views.py. dan implementasikan fungsi-fungsi HTML lainnya.

    6. Membuat halaman form untuk pembuatan task.
    --> membuat file forms.py yang digunakan untuk validation, Class nya adalah input yang nanti akan dimasukan oleh client (title, description). buat template create-task juga untuk tampilan halaman webnya, modifikasi juga viewsnya agar dapat menerima dan memproses data-data untuk ditampilkan pada halaman web.
    
    7. Membuat routing sehingga dapat mengakses beberapa fungsi
    -- > Menambahkan path fungsi-fungsi tersebut pada urls.py pada folder todolist
