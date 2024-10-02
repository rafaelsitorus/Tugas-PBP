1. Cara saya mengimplementasi checklist yang terdapat pada tugas 2 PBP ini adalah dengan menggunakan Django, Visual Studio Code, serta terminal/cmd yang membantu saya menjalankan ketentuan-ketentuan yang diperlukan.

2. https://drive.google.com/file/d/1KUvkupTEtB38aMu46401hJ0UPhYSpfh9/view?usp=sharing 
Penjelasan tambahan mengenai kaitan urls.py, views.py, models.py, dan berkas html:
    - User atau pengguna melakukan request kepada url
    - Url melakukan request kepada view mengenai pesan yang dikirimkan user kepada url
    - View kemudian mengirimkan permintaan pada model dan template mengenai pesan yang dikirimkan oleh user/pengguna
    - Model dan template me-reply kembali kepada view mengenai pesan yang dikirimkan oleh user/pengguna
    - View kemudian melakukan tugas terakhirnya untuk menampilkan seluruh pesan yang telah dibalas oleh model dan template untuk dapat dilihat pengguna dengan mengirimkannya kepada HTTP Response (HTML)

3. Fungsi git dalam pengembangan perangkat lunak adalah sebagai media interaksi antar pengembang agar setiap update atau implementasi baru yang dilakukan salah satu pengembang dapat di track oleh sesama pengembang lainnya, dengan adanya git, pengembangan perangkat lunak juga semakin mudah dikarenakan kita dapat membagi tugas antar pengembang dan mengintegrasikannya kembali di git ketika projek sudah dianggap seleseai.

4. Menurut saya Django dijadikan framework pilihan bagi mahasiswa fasilkom karena Django merupakan framework yang bekerja dibawah bahasa Python, yang mana mahasiswa fasilkom sangatlah erat dengan bahasa tersebut, serta kita akan menggunakan Flutter yang nantinya dapat digunakan oleh mahasiswa untuk mengembangkan aplikasi mobile yang mana Flutter sendiri adalah aplikasi yang komunikasi dengan backendnya menggunakan Django Web Service.

5. Model pada Django disebut ORM adalah karena ORM adalah fitur yang memungkinkan pengguna berinteraksi dengan database dengan cara yang sama seperti saat pengguna berinteraksi dengan SQL.

6. URL : http://pbp.cs.ui.ac.id/raja.rafael/tugaspbpraja

TUGAS - 3

1. Dalam mengembangkan suatu platform, ada kalanya kita perlu mengirimkan data dari satu stack ke stack lainnya, sehingga kita memerlukan data delivery.

2. Menurut saya keduanya memiliki fungsi yang sama dan tidak ada yang lebih baik diantaranya hanya saja json lebih mudah digunakan bagi kita yang menggunakan Javascript.

3. is_valid() merupakan suatu fungsi yang digunakan untuk memvalidasi isi dari input yang diberikan didalam form.

4. csrf_token berfungsi sebagai token atau id yang diciptakan untuk mencegah adanya serangan siber.

5. Dalam membuat tugas kali ini saya pertama kali membuat file form yang saya taruh pada direktori products, dimana form tersebut mengambil fungsi Product sebagai label-label yang akan diisi pada saat melakukan input kepada web, kemudian saya membuat beberapa function tambahan pada views.py dan beberapa perubahan pada urls.py agar isi dari input pengguna dapat disimpan dalam bentuk file json atau xml.

(Screenshot 2024-09-18 at 22.03.35)
(Screenshot 2024-09-18 at 22.03.42)

TUGAS - 4

1. HttpResponseRedirect() argumen pertama hanya dapat diisi URL. redirect yang pada akhirnya akan mengembalikan HttpResponseRedirect dapat menerima model, tampilan, atau url sebagai argumen.

2. Untuk menghubungkan Product dengan User saya menggunakan ForeignKey, dimana ForeignKey berguna untuk menciptakan hubungan antara dua tabel.

3. Authentication adalah proses untuk memverifikasi identitas pengguna, sedangkan authorization adalah proses untuk menentukan akses user setelah mereka terautentikasi. Di Django, authentication bekerja melalui model User dan form authentication dan authorization dikelola menggunakan permission, groups, dan decorators untuk mengontrol akses ke berbagai views.

4. Django mengingat pengguna yang telah login dengan menggunakan session, yang secara otomatis menyimpan informasi tentang pengguna di server dan mengaitkannya dengan session ID yang disimpan dalam cookie di browser pengguna. Cookies juga memiliki kegunaan lain yaitu untuk menyimpan preferensi pengguna, dsb. Tidak semua cookies aman digunakan, karena beberapa cookies rentan terhadap serangan siber.

5. Pertama-tama, karena struktur direktori saya berbeda dengan tutorial, saya harus melihat isi dari tiap file saya untuk memastikan program yang akan saya ikuti dari tutorial dapat terpasang dengan baik pada program saya, pertama saya membuka views.py yang terdapat pada direktori products untuk menambahkan fungsi-fungsi yang diperlukan seperti register, login_user, logout_user. Kemudian setelah semua hal tersebut telah rampung, saya mulai membangun koneksi antara User dan Product agar terintegrasi yang berfungsi agar tiap form yang diisi oleh user berdiri atas id-nya masing-masing. Setelah itu, saya menambahkan sedikit fitur seperti cookie last_login yang berfungsi sebagai bukti jejak adanya login dari suatu user.

TUGAS - 5
1. Prioritas pengambilan CSS didapat dari seberapa spesifik sebuah aturan. Gaya yang ditulis langsung pada elemen HTML, juga dikenal sebagai gaya inline, selalu memiliki prioritas tertinggi. Aturan dengan ID (#id) lebih kuat daripada aturan yang menggunakan class (.class), atribut, atau pseudo-class. Aturan yang hanya bergantung pada tag HTML, seperti div atau p, tidak penting. Aturan yang paling spesifik akan digunakan jika ada beberapa aturan yang berlaku untuk elemen yang sama. Aturan yang ditulis sebelumnya akan diterapkan jika sama tepatnya.

2. Karena pengguna dapat mengakses web dari berbagai perangkat dengan ukuran layar yang berbeda, seperti ponsel, tablet, dan komputer, responsive design sangat penting untuk pengembangan aplikasi web karena tampilan dan fitur aplikasi web dapat dengan otomatis menyesuaikan dengan ukuran layar perangkat sehingga pengalaman pengguna tetap nyaman dan efisien. Sebagai contoh, aplikasi seperti Instagram dan Twitter sudah memakai desain responsif yang membuat tampilan yang sama baiknya di desktop maupun ponsel. Sebaliknya, situs web lama yang hanya dirancang untuk desktop dan tidak dapat disesuaikan dengan perangkat kecil belum mengadopsi konsep ini, sehingga tampilan ponsel sering berantakan.

3. Dalam CSS, margin, border, dan padding mengatur jarak dan tata letak elemen. Margin adalah ruang di luar elemen, yang mengatur jarak dari elemen lain, border adalah garis di sekitar elemen, yang dapat memiliki warna, ketebalan, dan gaya yang berbeda, dan padding adalah ruang di dalam elemen, antara isi elemen dan batas (border). Untuk melakukannya, kita dapat menggunakan sintaks CSS seperti margin: 10px untuk membuat jarak di luar elemen, border: 1px solid black untuk membuat batas, dan padding: 20px untuk membuat jarak di dalam elemen sebelum isi.

4. Flexbox adalah metode CSS untuk mengatur elemen satu dimensi (baris atau kolom). Ini bagus untuk tata letak sederhana seperti menyusun item secara fleksibel dalam satu arah, seperti display: flex, dan digunakan untuk item yang dapat menyesuaikan ruang. Grid layout adalah teknik dua dimensi yang memungkinkan pengaturan elemen dalam baris dan kolom. Ini cocok untuk tata letak yang kompleks seperti galeri atau dashboard. Contohnya adalah display: grid, yang memungkinkan pengaturan elemen dalam grid dengan baris dan kolom yang disesuaikan.

5. Pertama-tama, karena struktur direktori saya berbeda dengan tutorial, saya harus melihat isi dari tiap file saya untuk memastikan program yang akan saya ikuti dari tutorial dapat terpasang dengan baik pada program saya, pertama saya membuka views.py yang terdapat pada direktori products untuk menambahkan fungsi-fungsi yang diperlukan seperti delete_mood dan edit_product. Kemudian setelah semua hal tersebut telah rampung, saya mulai membuat home.html, namun terdapat sedikit kendala saat saya ingin mencoba mengaplikasikan url product_entry dikarenakan saya lupa untuk melakukan iterasi terhadap product_entries. Setelah masalah tersebut selesai, saya mengintegrasikan CSS dengan program HTML saya agar tampilan web lebih nyaman digunakan pengguna, saya juga menambahkan Tailwind CSS Navbar agar mempermudah pemakaian web oleh tiap pengguna. Disini saya menggunakan framework CSS Tailwind untuk mempermudah kegiatan web development saya.