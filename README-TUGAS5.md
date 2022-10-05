Muhammad Fauzan Rizky Ramadhan
2106654315
Kode Asdos : ZEF
Kelas : PBP E




1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
--> Internal: Kode CSS pada inline diletakkan dalam bagian <head> pada halaman. hanya akan aktif pada halaman tersebut. Kode CSS Internal diletakkan di dalam tag <style></style>

    Kelebihan : Perubahan hanya terjadi pada 1 halaman
                Class dan ID bisa digunakan oleh internal stylesheet
                Tidak perlu upload beberapa file karena HTML dan CSS bisa digunakan di file yang sama

    Kekurangan : Meningkatkan waktu untuk akses website
                Perubahan hanya terjadi pada 1 halaman, tidak efisien jika ingin menggunakan CSS yang sama pada beberapa file
    
--> External: Menambahkan kode CSS ke website dengan cara menghubungkannya ke file .CSS eksternal. File CSS diletakkan setelah bagian <head> pada halaman, sebagai contoh:
            <head>
                <link rel="stylesheet" type="text/css" href="style.css" />
            </head>
            Lalu kira tinggal menulis kode css di file style.css
    
    Kelebihan: Ukuran file HTML menjadi lebih kecil dan strukturnya lebih rapi
               Kecepatan loading menjadi lebih cepat
               File CSS yang sama bisa digunakan di banyak halaman.
    
    Kekurangan: Halaman belum tampil secara sempurna hingga file CSS selesai dipanggil.

--> Inline: Inline CSS digunakan jika kita ingin mengaplikasikan kode CSS untuk tag HTML tertentu. Contoh, jika kita ingin menggunakan inline style:
            <!DOCTYPE html>
            <html>
            <body style="background-color:black;">
            
            <h1 style="color:white;padding:30px;">Ini Inline Style hehe</h1>
            <p style="color:white;">Custom CSS ditulis di tag HTML :).</p>
            
            </body>
            </html>

    Kelebihan: Berguna jika ingin menguji dan melihat perubahan pengaplikasian css
               Berguna untuk perbaikan cepat
               Modifikasi tag tertentu

2. Jelaskan tag HTML5 yang kamu ketahui.
<a> : Hyperlink
<body> : Document body
<br> : Line break (Jarak)
<button> : Membuat tombol yang bisa di click
<div> : specify bagian dalam suatu dokumen/halaman
<form> : Mendefinisikan HTML form untuk input dari user
<head> : Head page
<img> : Merepresentasikan gambar (memasukkan gambar di html)
<input> : Input control
<li> : Untuk list item
<meta> : Menyediakan struktur metadata untuk konten dokumen
<style> : Untuk CSS


3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.
    1. Element selector: Memilih tags HTML berdasarkan nama, misal : p, h1, div, dll
    misal: h1 {
                color: red;
                font-size: 3rem;
            }

    2. ID Selector: Menggunakan atribut ID dari tags html untuk edit css tersebut
    misal: #div-container{
                            color: blue;
                            background-color: gray;
                        }

    3. Universal Selector: CSS yang diaplikasikan di universal selector berlaku ke seluruh tags/elements html dalam page tersebut
    misal: * {
                color: white;
                background-color: black;
            }
    4. Group selector: Menggunakan koma untuk memilih seluruh elemen/tags html yang ingin diaplikasikan cssnya
    misal: 
                #div-container, .paragraph-class, h1{
                color: white;
                background-color: purple;
                font-family: monospace;    
            }

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
    --> Saya melakukan kustomisasi web menggunakan bootstrap, saya mengikuti dokumentasi dan memodifikasi beberapa elemen, juga melihat beberapa tutorial youtube untuk membuat web yang sudah saya buat. Untuk cara membuat web menjadi responsive, penggunaan bootstrap sepertinya otomatis membuat tampilan web menjadi responsive.