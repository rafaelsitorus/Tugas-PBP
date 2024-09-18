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