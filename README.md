# PBP Tugas
**BattleChar-App**<br>
**Link:** https://battlechar.adaptable.app/main/ <br>
Dimas Herjunodarpito Notoprayitno<br>
2206081282<br>
PBP C<br>

# PBP Tugas 2
## Checklist Tugas
Checklist untuk tugas ini adalah sebagai berikut (Asumsi penilai memakai Debian linux, karena saya memakainya).<br>
- [x] Membuat sebuah proyek Django baru. <br>
    - Membuat direktori untuk menyimpan proyek menggunakan perintah ```mkdir battlechar``` <br>
    - Masuk ke dalam direktori tersebut menggunakan perintah ```cd battlechar``` <br>
    - Membuat virtual environment Python dengan menggunakan perintah ```python -m venv env``` <br>
    - Mengaktifkan virtual environment python dengan perintah ```source env/bin/activate``` <br>
    - Install semua requirements (requirements bisa disimpan di dalam .txt file agar lebih memudahkan) dengan perintah ```python -m pip install -r requirements.txt --break-system-packages``` <br>
    - Membuat proyek dengan nama ```battlechar``` menggunakan perintah ```django-admin startproject battlechar .``` <br>
    - Menambahkan ```*``` pada list ```ALLOWED_HOSTS``` di dalam ```settings.py``` yang ada di dalam folder ```battlechar``` <br>
        ```python
        ...
        ALLOWED_HOSTS = [*]
        ...
        ```
    - Menguji apakah proyek telah berhasil dibuat dengan ```./manage.py runserver``` (Pengujian ini dapat dilakukan berkali-kali untuk menguji hasil pengerjaan) <br>
    - Membuat ```.gitignore``` yang berisi file yang tidak diperlukan agar tidak memenuhi space <br>
- [x] Membuat aplikasi dengan nama ```main``` pada proyek tersebut. <br>
    - Membuat aplikasi ```main``` dengan perintah ```python manage.py startapp main``` <br>
    - Mendaftarkan aplikasi ```main``` ke ```battlechar``` dengan menambahkan ```main``` pada list ```INSTALLED_APPS``` di dalam file ```settings.py``` <br>
        ```python
        INSTALLED_APPS = [
            ...,
            "main",
            ...
        ]
        ```
    - Membuat direktori ```template``` di dalam direktori ```main``` dan membuat file ```main.html``` serta modifikasi dengan memasukan rancangan <br>
        ```html
        <!-- Table from https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_th -->
        <style>
        table, th, td {
            border: 1px solid black;
        }
        </style>

        <h1>BattleChar</h1>

        <h5>Name: </h5>
        <p>Dimas Herjunodarpito N</p> <!-- Ubahlah sesuai dengan nama kamu -->
        <h5>Class: </h5>
        <p>PBP C</p> <!-- Ubahlah sesuai dengan kelas kamu -->

        <table>
            <tr>
                <th>Name</th>
                <th>Unit</th>
                <th>Primary weapon</th>
                <th>Secondary weapon</th>
                <th>Ammo</th>
                <th>Armor</th>
                <th>Speed</th>
                <th>Description</th>
                <th>Price</th>
            </tr>
            <tr>
                <td><center>{{ name }}</center></td>
                <td><center>{{ unit }}</center></td>
                <td><center>{{ primary_weapon }}</center></td>
                <td><center>{{ secondary_weapon }}</center></td>
                <td><center>{{ amount }}</center></td>
                <td><center>{{ armor }}</center></td>
                <td><center>{{ speed }}</center></td>
                <td>{{ description }}</td>
                <td><center>{{ price }}</center></td>
            </tr>
        </table>
        ```
- [x] Melakukan routing pada proyek agar dapat menjalankan aplikasi ```main```. <br>
    - Membuat file ```urls.py``` di dalam direktori ```battlechar``` untuk melakukan konfigurasi routing tampilan ```main``` <br>
        ```python
        """
        URL configuration for battlechar project.

        The `urlpatterns` list routes URLs to views. For more information please see:
            https://docs.djangoproject.com/en/4.2/topics/http/urls/
        Examples:
        Function views
            1. Add an import:  from my_app import views
            2. Add a URL to urlpatterns:  path('', views.home, name='home')
        Class-based views
            1. Add an import:  from other_app.views import Home
            2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
        Including another URLconf
            1. Import the include() function: from django.urls import include, path
            2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
        """
        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('main/', include('main.urls')),
        ]
        ```
- [x] Membuat model pada aplikasi ```main``` dengan nama ```Item``` dan memiliki atribut wajib sebagai berikut. <br>
    - ```name``` sebagai nama item dengan tipe ```CharField```. <br>
    - ```amount``` sebagai jumlah item dengan tipe ```IntegerField```. <br>
    - ```description``` sebagai deskripsi item dengan tipe ```TextField```. <br>
        - Membuat desain ```model``` dengan memodifikasi file ```models.py``` di direktori ```main``` <br>
            ```python
            from django.db import models
            from django.core.validators import MinValueValidator, MaxValueValidator

            class Operator(models.Model):
                name = models.CharField(max_length=255)
                unit = models.CharField(max_length=255)
                primary_weapon = models.CharField(max_length=255)
                secondary_weapon = models.CharField(max_length=255)
                amount = models.IntegerField()
                # Validator agar nilai minimal 1 dan nilai maksimal 3
                armor = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
                speed = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)]) 
                description = models.TextField()
                price = models.IntegerField()
            ```
        - Melakukan migrasi ```model``` dengan perintah ```python manage.py makemigrations``` lalu ```python manage.py migrate```<br>
- [x] Membuat sebuah fungsi pada ```views.py``` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu. <br>
    - Melakukan integrasi komponen MVT dengan memodifikasi file ```views.py``` di direktori ```main``` <br>
        ```python
        from django.shortcuts import render

        # Create your views here.
        def show_main(request):
            context = {
                'name': 'Fuze',
                'unit': 'Spetsnaz',
                'primary_weapon': '6P41',
                'secondary_weapon': 'Makarov PMM',
                'amount': 200,
                'armor': 3,
                'speed': 1,
                'description': "Fuze is best played as an aggressive flanker and area denial Operator. His strengths allow him to dispatch defensive capabilities and harass enemies anchored in defensive positions. Fuze's APM-6 cluster charge propels a group of explosive cluster grenades through any soft breach surface.",
                'price': 12500,
            }

            return render(request, "main.html", context)
        ```
- [x] Membuat sebuah routing pada ```urls.py``` aplikasi main untuk memetakan fungsi yang telah dibuat pada ```views.py```. <br>
    - Melakukan konfigurasi routing URL aplikasi ```main``` dengan memodifikasi file ```urls.py``` di direktori ```main``` <br>
        ```python
        from django.urls import path
        from main.views import show_main

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
        ]
        ```
- [x] Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet. <br>
    - Melakukan ```push``` ke repo GitHub pribadi dengan ```git add *```, ```git commit -m "Sudah menyelesaikan Tugas 2"```, dan ```git push origin master``` secara berurutan. <br>
    - Membuka website Adaptable lalu sign-in <br>
    - Memilih ```create a new app``` lalu memilih ```Connect an Existing Repository``` dan dilanjutkan dengan memilih repository dimana proyek ```battlechar``` berada <br>
    - Memilih ```Python App Template``` sebagai template deployment <br>
    - Memilih ```PostgreSQL``` sebagai tipe basis data yang akan digunakan <br>
    - Menyesuaikan versi Python di virtual environment dengan versi Python untuk template settings <br>
    - Menyisipkan perintah ```python manage.py migrate && gunicorn battlechar.wsgi``` pada bagian ```start command``` di template settings <br>
    - Masukkan nama aplikasi <br>
    - Mencentang opsi ```HTTP Listener on PORT``` dan klik ```Deploy``` <br>

- [x] Membuat sebuah ```README.md``` yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut. <br>
    - Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). <br>
    **Jawab:** <br>
    Sudah dijelaskan secara rinci di atas. <br><br>
    **BONUS** <br>
    Saya menambahkan unit test <br>
        ```python
        from django.test import TestCase, Client

        class mainTest(TestCase):
            # Uji apakah main/ eksis
            def test_main_url_is_exist(self):
                response = Client().get('/main/')
                self.assertEqual(response.status_code, 200)

            # Uji apakah main/ menggunakan template main.html
            def test_main_using_main_template(self):
                response = Client().get('/main/')
                self.assertTemplateUsed(response, 'main.html')

            # Uji apakah header yang digunakan sesuai
            def test_table_has_correct_headers(self):
                response = Client().get('/main/')
                self.assertContains(response, '<th>Name</th>', html=True)
                self.assertContains(response, '<th>Unit</th>', html=True)
                self.assertContains(response, '<th>Primary weapon</th>', html=True)
                self.assertContains(response, '<th>Secondary weapon</th>', html=True)
                self.assertContains(response, '<th>Ammo</th>', html=True)
                self.assertContains(response, '<th>Armor</th>', html=True)
                self.assertContains(response, '<th>Speed</th>', html=True)
                self.assertContains(response, '<th>Description</th>', html=True)
                self.assertContains(response, '<th>Price</th>', html=True)

            # Uji apakah data yang ditampilkan sesuai
            def test_table_row_contains_data(self):
                data = {
                    'name': 'Fuze',
                    'unit': 'Spetsnaz',
                    'primary_weapon': '6P41',
                    'secondary_weapon': 'Makarov PMM',
                    'amount': 200,
                    'armor': 3,
                    'speed': 1,
                    'description': "Fuze is best played as an aggressive flanker and area denial Operator. His strengths allow him to dispatch defensive capabilities and harass enemies anchored in defensive positions. Fuze's APM-6 cluster charge propels a group of explosive cluster grenades through any soft breach surface.",
                    'price': 12500,
                }
                response = Client().get('/main/')
                for key, value in data.items():
                    if key != 'description':
                        self.assertContains(response, f'<td><center>{value}</center></td>', html=True)
                    else:
                        self.assertContains(response, f'<td>{value}</td>', html=True)
        ```
        <br>
    - Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara ```urls.py```, ```views.py```, ```models.py```, dan berkas ```html```. <br>
    **Jawab:** <br>
    ![bagan dimas](/doks_md/bagan_dimas.png) <br><br>
        1. Klien mengakses situs web dengan membuka browser <br>
        2. Klien mengunjungi situs web, kemudian web server melayani permintaan dari klien <br>
        3. WSGI mengolah server HTTP untuk situs web berbasis Python <br>
        4. Middleware menghubungkan integrasi teknologi yang digunakan dalam proyek untuk mengolah permintaan <br>
        5. URL Router mengalihkan URL proyek berdasarkan permintaan klien (```urls.py```), kemudian dialihkan ke fungsi yang berada di ```views.py``` <br>
        6. Views (```views.py```) mengompilasi semua yang nantinya akan ditampilkan ke template ```html```, olahan data diambil dari database yang sudah terkompilasi dengan ORM yang ada di ```models.py``` <br>
        7. Context processor mengirimkan data dari ```views.py``` ke template ```html``` <br>
        8. Template ```html``` menampilkan antarmuka depan proyek berdasarkan data konteks yang diambil dari ```views.py``` dan logika dari tag-tag template <br>
        9. Middleware menghubungkan integrasi teknologi yang digunakan dalam proyek untuk mengolah respons <br>
        10. WSGI mengolah server HTTP untuk situs web berbasis Python <br>
        11. Web server menampilkan respons dari server untuk disampaikan ke klien <br>
        12. Klien mendapatkan respons dari server web <br><br>
    - Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? <br>
    **Jawab:** <br>
    **Pentingnya virtual environment:** <br>
    Virtual environment dibutuhkan sedemikian rupa sehingga memungkinkan sistem dapat berjalan di lingkungan yang terisolasi dikarenakan setiap proyek memiliki spesifikasi yang berbeda. Dengan menggunakan virtual environment, proyek dapat berjalan menyesuaikan dengan ketergantungannya tanpa mengkonfigurasi sistem operasi yang digunakan. "requirements.txt" berfungsi sebagai catatan daftar ketergantungan dari sebuah proyek yang dijalankan di virtual environment tertentu. Sehingga dengan mengetahui daftar ketergantungan yang dimiliki melalui "requirements.txt" sebuah mesin host, misalnya "Adaptable" dapat mengetahui ketergantungan apa saja yang harus dimanfaatkan agar dapat menjalankan server tersebut. Hal ini juga mempermudah proses penyimpanan dikarenakan pengguna tidak perlu melakukan push pada virtual environment karena sudah tercatat dengan baik di dalam "requirements.txt" (virtual environment adalah sebuah direktori yang cukup menghabiskan penyimpanan repository/host sehingga meniadakannya dengan .gitignore dapat menyederhanakan proyek). <br><br>
    **Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?** <br>
    Apabila hanya dilakukan di lingkungan server lokal maka hal ini dapat dilakukan. Pengguna cukup memanfaatkan lingkungan Python standar komputer (root) untuk mengkonfigurasi ketergantungan yang diperlukan untuk proyek Django sehingga proyek Django dapat dijalankan di server "lokal". Bagaimanapun, apabila ingin menjalankannya di sebuah penyedia layanan online, hal ini menjadi cukup kompleks dikarenakan server host akan mencocokkan daftar ketergantungan yang ada di "requirements.txt" dengan paket ketergantungan yang tersedia di mesin penyedia layanan tersebut. Apabila "requirements.txt" tidak ada dikarenakan lingkungan virtual tidak terinisialisasi, maka mesin host tersebut tidak akan pernah menyadari apa saja ketergantungan yang dibutuhkan untuk menjalankan server sehingga proyek juga akan tidak dapat berjalan. <br><br>
    - Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya. <br>
    **Jawab:** <br>
        1. MVC (Model-View-Controller)<br>
            - Model: Mewakili data atau logika bisnis dalam aplikasi. Model ini bertanggung jawab untuk mengelola data dan status aplikasi. <br>
            - View: Bertanggung jawab untuk menampilkan data dari Model ke pengguna dan menerima input pengguna. Ini adalah antarmuka pengguna (UI). <br>
            - Controller: Bertindak sebagai penghubung antara Model dan View. Ini mengatur alur kontrol dan merespons input pengguna. Controller juga memperbarui Model dan View sesuai dengan perubahan yang terjadi. <br>
            - Perbedaan utama dengan MVT dan MVVM: MVC adalah pola desain yang lebih tua dan lebih sederhana dibandingkan dengan MVT dan MVVM. MVT dan MVVM adalah variasi yang lebih modern dan khusus. <br><br>
        2. MVT (Model-View-Template) <br>
            - Model: Sama seperti dalam MVC, ini mengelola data dan logika bisnis. <br>
            - View: Mirip dengan View dalam MVC, menangani tampilan dan presentasi data. <br>
            - Template: Komponen baru dalam MVT. Template ini adalah bagian dari tampilan yang mengatur cara data dari Model ditampilkan dalam View. <br>
            - Perbedaan utama dengan MVC dan MVVM: MVT adalah variasi dari MVC yang biasanya digunakan dalam kerangka kerja berbasis Python seperti Django. Perbedaannya terletak pada penggunaan Template yang memisahkan logika tampilan lebih jauh. <br><br>
        3. MVVM (Model-View-ViewModel) <br>
            - Model: Sama seperti dalam MVC dan MVT, mengelola data dan logika bisnis <br>
            - View: Mirip dengan View dalam pola lainnya, menangani tampilan dan presentasi data <br>
            - ViewModel: Komponen baru dalam MVVM. ViewModel berperan sebagai perantara antara Model dan View. Ini mengonversi data dari Model ke format yang sesuai untuk tampilan dan menerima perubahan dari View untuk diteruskan ke Model. <br>
            - Perbedaan utama dengan MVC dan MVT: MVVM menambahkan lapisan ViewModel untuk memisahkan lebih jauh logika tampilan dari Model, membuatnya lebih cocok untuk pengembangan aplikasi berbasis tampilan yang dinamis. <br>

# PBP Tugas 3
## Checklist Tugas
Checklist untuk tugas ini adalah sebagai berikut: <br>
- [x] Membuat input ```form``` untuk menambahkan objek model pada app sebelumnya. <br>
    - Melakukan routing ```main/``` ke ```/``` agar langsung masuk ke halaman utama tanpa peringatan ```404 error``` jika tidak ditambahkan ```main/``` pada URL secara manual. <br>
        - Memodifikasi ```urls.py``` pada folder ```battlechar``` dengan mengubah path ```main/``` menjadi ```""``` pada list ```urlpatterns``` seperti berikut. <br>
            ```python
            urlpatterns = [
                path('admin/', admin.site.urls),
                path('', include('main.urls')),
            ]
            ```
    - Membuat kerangka ```views``` dengan menggunakan ```skeleton```. Hal ini bermanfaat agar desain situs web memiliki konsistensi dan memperkecil peluang terjadinya redundansi kode. <br>
        - Membuat folder ```templates``` pada folder root dan membuat sebuah file HTML dengan nama ```base.html```. File HTML tersebut berfungsi sebagai template dasar yang dapat digunakan sebagai kerangka secara general untuk halaman web lain yang ada di dalam proyek. Berikut isi ```base.html```: <br>
            ```html
            {% load static %}
            <!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="UTF-8" />
                    <meta
                        name="viewport"
                        content="width=device-width, initial-scale=1.0"
                    />
                    {% block meta %}
                    {% endblock meta %}
                </head>

                <body>
                    {% block content %}
                    {% endblock content %}
                </body>
            </html>
            ```
        - Memodifikasi file ```settings.py``` yang ada pada subfolder ```battlechar``` dengan menambahkan kode di bagian dictionary dengan key ```DIRS``` pada variabel list ```TEMPLATES```  seperti berikut: <br>
            ```python
            TEMPLATES = [
                {
                    'BACKEND': 'django.template.backends.django.DjangoTemplates',
                    'DIRS': [BASE_DIR / 'templates'], # Tambahkan kode ini
                    'APP_DIRS': True,
                    'OPTIONS': {
                        'context_processors': [
                            'django.template.context_processors.debug',
                            'django.template.context_processors.request',
                            'django.contrib.auth.context_processors.auth',
                            'django.contrib.messages.context_processors.messages',
                        ],
                    },
                },
            ]
            ```
        - Memodifikasi ```main.html``` pada folder ```main``` seperti berikut: <br>
            ```html
            <!-- Table from https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_th -->
            {% extends 'base.html' %}

            {% block content %}
            <style>
                table, th, td {
                    border: 1px solid black;
                }
            </style>

            <h1>BattleChar</h1>

            <h5>Name: </h5>
            <p>{{ creator }}</p> <!-- Ubahlah sesuai dengan nama kamu -->
            <h5>Student ID: </h5>
            <p>{{ student_id }}</p>
            <h5>Class: </h5>
            <p>{{ class }}</p> <!-- Ubahlah sesuai dengan kelas kamu -->

            {% endblock content %}
            ```
    - Membuat form input data operator dan menampilkan data operator-operator pada HTML <br>
        - Membuat file ```forms.py``` di dalam folder main yang dapat menerima data produk baru. Berikut kode di dalam ```forms.py```: <br>
            ```python
            from django.forms import ModelForm
            from main.models import Operator

            class OperatorForm(ModelForm):
                class Meta:
                    model = Operator
                    fields = ["name", "unit", "primary_weapon", 
                            "secondary_weapon", "primary_weapon_ammo_amount", "secondary_weapon_ammo_amount", 
                            "armor", "speed", "description", "price"]
            ```
        - Memodifikasi file ```views.py``` yang terdapat di folder ```main``` sebagai berikut: <br>
            ```python
            from django.shortcuts import render
            from django.http import HttpResponseRedirect
            from main.forms import OperatorForm
            from django.urls import reverse
            from main.models import Operator
            from django.http import HttpResponse
            from django.core import serializers

            def create_operator(request):
                form = OperatorForm(request.POST or None)

                if form.is_valid() and request.method == "POST":
                    form.save()
                    return HttpResponseRedirect(reverse("main:show_main"))
                
                context = {"form": form}
                return render(request, "create_operator.html", context)
            ```
        - Memodifikasi ```urls.py``` yang terdapat pada folder ```main``` dengan import fungsi ```create_operator```. <br>
            ```python
            from main.views import show_main, create_operator
            ```
        - Menambahkan path URL data form ke dalam ```urlpatterns``` pada ```urls.py``` yang terdapat di folder ```main```. <br>
            ```python
            path('create-operator', create_operator, name='create_operator'),
            ```
        - Membuat file dengan nama ```create_operator.html``` di dalam folder ```main/templates``` dengan isi: <br>
            ```html
            {% extends 'base.html' %}

            {% block content %}
            <h1>Add Operator</h1>

            <form method="POST">
            {% csrf_token %}
            <table>
                {{ form.as_table }}
                <tr>
                <td></td>
                <td>
                    <input type="submit" value="Add Operator">
                </td>
                </tr>
            </table>
            </form>

            {% endblock %}
            ```
        - Memodifikasi ```main.html``` yang terdapat di ```main/templates``` dengan menambahkan kode di bawah ini di dalam ```{% block content %}``` untuk menampilkan data operator yang telah dimasukkan dan sebuah tombol untuk redirect ke halaman form. <br>
            ```html
            <br />
            <h3>{{ roster_size }}</h3> <!-- BONUS -->
            <table>
                <tr>
                    <th>Name</th>
                    <th>Unit</th>
                    <th>Primary weapon</th>
                    <th>Secondary weapon</th>
                    <th>Primary weapon ammo</th>
                    <th>Secondary weapon ammo</th>
                    <th>Armor</th>
                    <th>Speed</th>
                    <th>Description</th>
                    <th>Price</th>
                </tr>

                {% for operator in operators %}
                    <tr>
                        <td><center>{{ operator.name }}</center></td>
                        <td><center>{{ operator.unit }}</center></td>
                        <td><center>{{ operator.primary_weapon }}</center></td>
                        <td><center>{{ operator.secondary_weapon }}</center></td>
                        <td><center>{{ operator.primary_weapon_ammo_amount }}</center></td>
                        <td><center>{{ operator.secondary_weapon_ammo_amount }}</center></td>
                        <td><center>{{ operator.armor }}</center></td>
                        <td><center>{{ operator.speed }}</center></td>
                        <td>{{ operator.description }}</td>
                        <td><center>{{ operator.price }}</center></td>
                    </tr>
                {% endfor %}
            </table>

            <br />

            <a href="{% url 'main:create_operator' %}">
                <button>
                    Add New Operator
                </button>
            </a>

            {% endblock content %}
            ```
- [x] Tambahkan 5 fungsi ```views``` untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID. <br>
    - Memodifikasi fungsi ```show_main``` di dalam ```views.py``` pada folder ```main``` agar dapat mengembalikan render HTML berupa data pembuat web, data operator yang telah dimasukkan, serta berapa jumlah operator yang sudah dimasukkan (BONUS). <br>
        ```python
        def show_main(request):
            operators = Operator.objects.all()
            # BONUS
            roster_size = len(operators)
            roster_size_message = f"You have {roster_size} operator(s) in your roster"

            context = {
                'creator': 'Dimas Herjunodarpito Notoprayitno',
                'student_id': '2206081282',
                'class': 'PBP C',
                'operators': operators,
                'roster_size': roster_size_message,
            }

            return render(request, "main.html", context)
        ```
    - Membuat fungsi untuk mengembalikan data-data dalam bentuk HTML dengan menambahkan kode pada ```views.py``` seperti berikut:
        ```python
        def show_html(request):
            operators = Operator.objects.all()
            roster_size = len(operators)
            roster_size_message = f"You have {roster_size} operator(s) in your roster"
            
            context = {
                'operators': operators,
                'roster_size': roster_size_message,
            }

            return render(request, "show_only_operators.html", context)
        ```
        Serta menambahkan juga file HTML di dalam ```main/templates``` dengan nama ```show_only_operators.html``` seperti berikut: <br>
        ```html
        <!-- Table from https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_th -->
        {% extends 'base.html' %}

        {% block content %}
        <style>
            table, th, td {
                border: 1px solid black;
            }
        </style>

        <br />
        <h3>{{ roster_size }}</h3>
        <table>
            <tr>
                <th>Name</th>
                <th>Unit</th>
                <th>Primary weapon</th>
                <th>Secondary weapon</th>
                <th>Primary weapon ammo</th>
                <th>Secondary weapon ammo</th>
                <th>Armor</th>
                <th>Speed</th>
                <th>Description</th>
                <th>Price</th>
            </tr>

            {% for operator in operators %}
                <tr>
                    <td><center>{{ operator.name }}</center></td>
                    <td><center>{{ operator.unit }}</center></td>
                    <td><center>{{ operator.primary_weapon }}</center></td>
                    <td><center>{{ operator.secondary_weapon }}</center></td>
                    <td><center>{{ operator.primary_weapon_ammo_amount }}</center></td>
                    <td><center>{{ operator.secondary_weapon_ammo_amount }}</center></td>
                    <td><center>{{ operator.armor }}</center></td>
                    <td><center>{{ operator.speed }}</center></td>
                    <td>{{ operator.description }}</td>
                    <td><center>{{ operator.price }}</center></td>
                </tr>
            {% endfor %}
        </table>

        {% endblock content %}
        ```
    - Membuat fungsi untuk mengembalikan data-data dalam bentuk XML dengan menambahkan kode pada ```views.py``` seperti berikut: <br>
        ```python
        def show_xml(request):
            data = Operator.objects.all()
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
        ```
    - Membuat fungsi untuk mengembalikan data-data dalam bentuk JSON dengan menambahkan kode pada ```views.py``` seperti berikut: <br>
        ```python
        def show_json(request):
            data = Operator.objects.all()
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")
        ```
    - Membuat fungsi untuk mengembalikan data dari suatu ID tertentu dalam bentuk XML dengan menambahkan kode pada ```views.py``` seperti berikut: <br>
        ```python
        def show_xml_by_id(request, id):
            data = Operator.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
        ```
    - Membuat fungsi untuk mengembalikan data dari suatu ID tertentu dalam bentuk JSON dengan menambahkan kode pada ```views.py``` seperti berikut: <br>
        ```python
        def show_json_by_id(request, id):
            data = Operator.objects.filter(pk=id)
            return HttpResponse(serializers.serialize("json", data), content_type="application/json")
        ```
- [x] Membuat routing URL untuk masing-masing ```views``` yang telah ditambahkan pada poin 2. <br>
    - Memodifikasi ```urls.py``` pada folder ```main``` menjadi seperti ini:
        ```python
        from django.urls import path
        from main.views import show_html, show_json, show_json_by_id, show_main, create_operator, show_xml, show_xml_by_id

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
            path('create-operator', create_operator, name='create_operator'),
            path('xml/', show_xml, name='show_xml'),
            path('html/', show_html, name='show_html'),
            path('json/', show_json, name='show_json'),
            path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
            path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
        ]
        ```
- [x] Menjawab beberapa pertanyaan berikut pada ```README.md``` pada root folder. <br>
    - [x] Apa perbedaan antara form ```POST``` dan form ```GET``` dalam Django? <br>
        **Jawab:** <br>
        Form pada Django dikembalikan dengan menggunakan metode POST, di mana browser membundel data formulir, mengkodekannya untuk transmisi, mengirimkannya ke server, dan kemudian menerima kembali responsnya. Sebaliknya, GET, menggabungkan data yang dikirimkan ke dalam sebuah string, dan menggunakannya untuk membuat URL. <br><br>
    - [x] Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data? <br>
        **Jawab:** <br>
        JSON merupakan format penukaran data secara terbuka yang dapat dibaca dengan mudah oleh manusia maupun mesin atau komputer. JSON memiliki sifat yang independen dari setiap bahasa pemrograman serta merupakan output API yang umum dalam berbagai aplikasi. XML adalah bahasa markah yang menyediakan aturan untuk menentukan jenis data. XML sendiri menggunakan tanda-tanda untuk membedakan atribut dengan data yang aktual. HTML merupakan bahasa markah sama seperti XML tetapi dimanfaatkan untuk menafsirkan dan menulis data seperti teks, gambar, dan bahan lainnya ke dalam halaman web. <br><br>
    - [x] Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern? <br>
        **Jawab:** <br>
        Karena JSON lebih mudah dibaca baik oleh manusia maupun mesin atau komputer serta JSON merupakan opsi yang lebih baru, lebih fleksibel, dan lebih populer ketimbang dengan opsi yang lain. <br><br>
    - [x] Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)! <br>
        **Jawab:** <br>
        Sudah dijelaskan di atas. <br>
- [x] Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam ```README.md```. <br>
    ![html2](/doks_md/html2.png) <br>
    ![html](/doks_md/html.png) <br>
    ![json](/doks_md/json.png) <br>
    ![json2](/doks_md/json2.png) <br>
    ![xml](/doks_md/xml.png) <br>
    ![xml2](/doks_md/xml2.png) <br>
- [x] Melakukan ```add```-```commit```-```push``` ke GitHub. <br>

# PBP Tugas 4
## Checklist Tugas
Checklist untuk tugas ini adalah sebagai berikut: <br>
- [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar. <br>
    - Menyalakan Python virtual environment. <br>
    - Menambahkan beberapa kode serta import di dalam ```main/views.py``` seperti function register, login, logout <br>
        ```python
        import datetime
        from django.http import HttpResponseRedirect
        from django.urls import reverse
        from django.contrib.auth.decorators import login_required
        from django.contrib.auth import logout
        from django.contrib.auth import authenticate, login
        from django.shortcuts import redirect
        from django.contrib.auth.forms import UserCreationForm
        from django.contrib import messages  
        from django.shortcuts import render
        from django.http import HttpResponseRedirect
        from main.forms import OperatorForm
        from django.urls import reverse
        from main.models import Operator
        from django.http import HttpResponse
        from django.core import serializers

        ...

        def logout_user(request):
            logout(request)
            response = HttpResponseRedirect(reverse('main:login'))
            response.delete_cookie('last_login')
            return response

        def register(request):
            form = UserCreationForm()

            if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Your account has been successfully created!')
                    return redirect('main:login')
            context = {'form':form}
            return render(request, 'register.html', context)

        def login_user(request):
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    response = HttpResponseRedirect(reverse("main:show_main")) 
                    response.set_cookie('last_login', str(datetime.datetime.now()))
                    return response
                else:
                    messages.info(request, 'Sorry, incorrect username or password. Please try again.')
            context = {}
            return render(request, 'login.html', context)

        ...
        ```
    - Menambahkan file HTML di dalam ```main/templates``` berupa ```login.html``` dan ```register.html```. <br>
        - ```login.html``` : <br>
            ```html
            {% extends 'base.html' %}

            {% block meta %}
                <title>LOGIN</title>
            {% endblock meta %}

            {% block content %}

            <div class = "login">

                <h1>Login</h1>

                <form method="POST" action="">
                    {% csrf_token %}
                    <table>
                        <tr>
                            <td>Username: </td>
                            <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                        </tr>
                                
                        <tr>
                            <td>Password: </td>
                            <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                        </tr>

                        <tr>
                            <td></td>
                            <td><input class="btn login_btn" type="submit" value="Login"></td>
                        </tr>
                    </table>
                </form>

                {% if messages %}
                    <ul>
                        {% for message in messages %}
                            <li>{{ message }}</li>
                        {% endfor %}
                    </ul>
                {% endif %}     
                    
                Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

            </div>

            {% endblock content %}
            ```
        - ```register.html``` : <br>
            ```html
            {% extends 'base.html' %}

            {% block meta %}
                <title>REGISTER</title>
            {% endblock meta %}

            {% block content %}  

            <div class = "login">
                
                <h1>Register</h1>  

                    <form method="POST" >  
                        {% csrf_token %}  
                        <table>  
                            {{ form.as_table }}  
                            <tr>  
                                <td></td>
                                <td><input type="submit" name="submit" value="Daftar"/></td>  
                            </tr>  
                        </table>  
                    </form>

                {% if messages %}  
                    <ul>   
                        {% for message in messages %}  
                            <li>{{ message }}</li>  
                            {% endfor %}  
                    </ul>   
                {% endif %}

            </div>  

            {% endblock content %}
            ```
    - Menambahkan beberapa kode di ```main/urls.py``` <br>
        ```python
        from django.urls import path
        from main.views import (show_html, show_json, show_json_by_id, show_main, create_operator, 
                                show_xml, show_xml_by_id, register, login_user, logout_user,
                                add_primary_ammo_amount, add_secondary_ammo_amount, dec_primary_ammo_amount,
                                dec_secondary_ammo_amount, remove_operator)

        app_name = 'main'

        urlpatterns = [
            ...
            path('register/', register, name='register'),
            path('login/', login_user, name='login'),
            path('logout/', logout_user, name='logout'),
        ]
        ```
    - Menambahkan tombol logout di dalam main page dengan menambahkan kode pada ```main/templates/main.html``` setelah hyperlink tag untuk Add New Operator <br>
        ```html
        ...
        <a href="{% url 'main:logout' %}">
            <button>
                Logout
            </button>
        </a>
        ...
        ```
    - Menambahkan kode ini di dalam ```main/views.py``` untuk merestriksi akses ke halaman main tanpa login <br>
        ```python
        ...
        @login_required(login_url='/login')
        def show_main(request):
        ...
        ```
- [x] Menghubungkan model Operator dengan User.
    - Menambahkan kode pada ```main/models.py``` <br>
        ```python
        from django.db import models
        from django.core.validators import MinValueValidator, MaxValueValidator
        from django.contrib.auth.models import User

        class Operator(models.Model):
            user = models.ForeignKey(User, on_delete=models.CASCADE)
            name = models.CharField(max_length=255)
            unit = models.CharField(max_length=255)
            primary_weapon = models.CharField(max_length=255)
            secondary_weapon = models.CharField(max_length=255)
            primary_weapon_ammo_amount = models.IntegerField()
            secondary_weapon_ammo_amount = models.IntegerField()
            armor = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)])
            speed = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)]) 
            description = models.TextField()
            price = models.IntegerField()
        ```
    - Memodifikasi kode pada ```main/views.py``` <br>
        ```python
        def create_operator(request):
            form = OperatorForm(request.POST or None)

            if form.is_valid() and request.method == "POST":
                product = form.save(commit=False)
                product.user = request.user
                product.save()
                return HttpResponseRedirect(reverse('main:show_main'))
            
            context = {"form": form}
            return render(request, "create_operator.html", context)
        ```
    - Memodifikasi fungsi show_main pada ```main/views.py``` <br>
        ```python
        @login_required(login_url='/login')
        def show_main(request):
            operators = Operator.objects.filter(user=request.user)
            roster_size = len(operators)
            roster_size_message = f"You have {roster_size} operator(s) in your roster"

            context = {
                'creator': request.user.username,
                ...
        ```
    - Menyimpan dan melakukan migrasi dengan ```python manage.py makemigrations``` <br>
    - Jika muncul error saat melakukan migrasi model, maka pilih 1 untuk menetapkan default value untuk field user pada semua row yang telah dibuat pada basis data. <br>
    - Mengetik angka 1 lagi untuk menetapkan user dengan ID 1 (yang sudah dibuat sebelumnya) pada model yang sudah ada. <br>
    - Lakukan ```python manage.py migrate``` <br>
- [x] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi. <br>
    - Menambahkan import pada ```main/views.py``` di bagian paling atas <br>
        ```python
        import datetime
        from django.http import HttpResponseRedirect
        from django.urls import reverse
        ```
    - Memodifikasi fungsi login_user pada ```main/views.py``` <br>
        ```python
        def login_user(request):
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    response = HttpResponseRedirect(reverse("main:show_main")) 
                    response.set_cookie('last_login', str(datetime.datetime.now()))
                    return response
                else:
                    messages.info(request, 'Sorry, incorrect username or password. Please try again.')
            context = {}
            return render(request, 'login.html', context)
        ```
    - Memodifikasi fungsi show_main pada ```main/views.py``` <br>
        ```python
        @login_required(login_url='/login')
        def show_main(request):
            operators = Operator.objects.filter(user=request.user)
            roster_size = len(operators)
            roster_size_message = f"You have {roster_size} operator(s) in your roster"

            context = {
                'creator': request.user.username,
                'class': 'PBP C',
                'operators': operators,
                'roster_size': roster_size_message,
                'last_login': request.COOKIES['last_login']
            }

            return render(request, "main.html", context)
        ```
    - Memodifikasi file ```main/templates/main.html``` dengan menambahkan potongan kode di antara tabel dan tombol logout untuk menampilkan data last login. <br>
        ```python
        ...
        <h5>Sesi terakhir login: {{ last_login }}</h5>
        ...
        ```

**BONUS** <br>
Special thanks To Faris Zhafir Faza for teaching me on how to do this. <br>
- [x] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal. <br>
    ![hokum](/doks_md/hokum.png) <br>
    ![dhn](/doks_md/dhn.png) <br>
- [x] Tambahkan tombol dan fungsi untuk menambahkan amount suatu objek sebanyak satu dan tombol untuk mengurangi jumlah stok suatu objek sebanyak satu.
    - Menambahkan function-function berikut di ```main/views.py``` <br>
        ```python
        ...

        def add_primary_ammo_amount(request, operator_id):
            if request.method == 'POST' and 'Increment' in request.POST:
                operator = Operator.objects.get(id=operator_id)
                operator.primary_weapon_ammo_amount += 1
                operator.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        def dec_primary_ammo_amount(request, operator_id):
            if request.method == 'POST' and 'Decrement' in request.POST:
                operator = Operator.objects.get(id=operator_id)
                operator.primary_weapon_ammo_amount -= 1
                operator.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        def add_secondary_ammo_amount(request, operator_id):
            if request.method == 'POST' and 'Increment' in request.POST:
                operator = Operator.objects.get(id=operator_id)
                operator.secondary_weapon_ammo_amount += 1
                operator.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        ...

        def dec_secondary_ammo_amount(request, operator_id):
            if request.method == 'POST' and 'Decrement' in request.POST:
                operator = Operator.objects.get(id=operator_id)
                operator.secondary_weapon_ammo_amount -= 1
                operator.save()
            return HttpResponseRedirect(reverse('main:show_main'))
        
        ...
        ```
    - Memodfikasi ```main/urls.py``` <br>
        ```python
        from django.urls import path
        from main.views import (show_html, show_json, show_json_by_id, show_main, create_operator, 
                                show_xml, show_xml_by_id, register, login_user, logout_user,
                                add_primary_ammo_amount, add_secondary_ammo_amount, dec_primary_ammo_amount,
                                dec_secondary_ammo_amount, remove_operator)

        app_name = 'main'

        urlpatterns = [
            ...
            path('add_primary_ammo_amount/<int:operator_id>/', add_primary_ammo_amount, name='add_primary_ammo_amount'),
            path('add_secondary_ammo_amount/<int:operator_id>/', add_secondary_ammo_amount, name='add_secondary_ammo_amount'),
            path('dec_primary_ammo_amount/<int:operator_id>/', dec_primary_ammo_amount, name='dec_primary_ammo_amount'),
            path('dec_secondary_ammo_amount/<int:operator_id>/', dec_secondary_ammo_amount, name='dec_secondary_ammo_amount'),
            ....
        ]
        ```
    - Menambahkan kode berikut di dalam ```main/templates/main.html``` <br>
        ```python
        ...

            <td>{{ operator.description }}</td>
            <td><center>{{ operator.price }}</center></td>
            <td><center>
                <form action="{% url 'main:add_primary_ammo_amount' operator.id %}" method="post">
                    {% csrf_token %}
                    <button type="submit" name="Increment">Add</button>
                </form>
            </td></center>
            <td><center>
                <form action="{% url 'main:add_secondary_ammo_amount' operator.id %}" method="post">
                    {% csrf_token %}
                    <button type="submit" name="Increment">Add</button>
                </form></center>
            </td>
            <td><center>
                <form action="{% url 'main:dec_primary_ammo_amount' operator.id %}" method="post">
                    {% csrf_token %}
                    <button type="submit" name="Decrement">Decrease</button>
                </form>
            </td></center>
            <td><center>
                <form action="{% url 'main:dec_secondary_ammo_amount' operator.id %}" method="post">
                    {% csrf_token %}
                    <button type="submit" name="Decrement">Decrease</button>
                </form>
            </td></center>
        
        ...
        ```
- [x] Tambahkan tombol dan fungsi untuk menghapus suatu objek dari inventori. <br>
    - Menambahkan function berikut di ```main/views.py``` <br>
        ```python
        def remove_operator(request, operator_id):
            if request.method == 'POST' and 'Remove' in request.POST:
                operator = Operator.objects.get(id=operator_id)
                operator.delete()
            return HttpResponseRedirect(reverse('main:show_main'))
        ```
    - Memodfikasi ```main/urls.py``` <br>
        ```python
        from django.urls import path
        from main.views import (show_html, show_json, show_json_by_id, show_main, create_operator, 
                                show_xml, show_xml_by_id, register, login_user, logout_user,
                                add_primary_ammo_amount, add_secondary_ammo_amount, dec_primary_ammo_amount,
                                dec_secondary_ammo_amount, remove_operator)

        app_name = 'main'

        urlpatterns = [
            ...
            path('remove_operator/<int:operator_id>/', remove_operator, name='remove_operator'),
            ...
        ]
        ```
    - Menambahkan kode berikut di dalam ```main/templates/main.html``` <br>
        ```python
        ...

            <td>{{ operator.description }}</td>
            <td><center>{{ operator.price }}</center></td>
            <td><center>
                <form action="{% url 'main:add_primary_ammo_amount' operator.id %}" method="post">
                    {% csrf_token %}
                    <button type="submit" name="Increment">Add</button>
                </form>
            </td></center>
            <td><center>
                <form action="{% url 'main:add_secondary_ammo_amount' operator.id %}" method="post">
                    {% csrf_token %}
                    <button type="submit" name="Increment">Add</button>
                </form></center>
            </td>
            <td><center>
                <form action="{% url 'main:dec_primary_ammo_amount' operator.id %}" method="post">
                    {% csrf_token %}
                    <button type="submit" name="Decrement">Decrease</button>
                </form>
            </td></center>
            <td><center>
                <form action="{% url 'main:dec_secondary_ammo_amount' operator.id %}" method="post">
                    {% csrf_token %}
                    <button type="submit" name="Decrement">Decrease</button>
                </form>
            </td></center>
            <td><center>
                <form action="{% url 'main:remove_operator' operator.id %}" method="post">
                    {% csrf_token %}
                    <button type="submit" name="Remove">Remove</button>
                </form>
            </td></center>
        ...
        ```
- [x] Menjawab beberapa pertanyaan berikut pada ```README.md``` pada root folder (silakan modifikasi ```README.md``` yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas). <br>
    - [x] Apa itu ```Django UserCreationForm```, dan jelaskan apa kelebihan dan kekurangannya? <br>
        **Jawab:** <br>
        UserCreationForm adalah impor formulir bawaan yang memudahkan pembuatan formulir pendaftaran pengguna dalam aplikasi web. Dengan formulir ini, pengguna baru dapat mendaftar dengan mudah di situs web kita tanpa harus menulis kode dari awal. Salah satu kekurangan dari UserCreationForm adalah tidak memiliki field untuk Email. <br>
    - [x] Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting? <br>
        **Jawab:** <br>
        **Autentikasi:** <br>
        1. Autentikasi adalah proses verifikasi identitas pengguna. Ini digunakan untuk memastikan bahwa pengguna yang mencoba mengakses aplikasi adalah pengguna yang mereka klaim. <br>
        2. Biasanya, autentikasi melibatkan validasi kombinasi nama pengguna (username) dan kata sandi (password) yang dimasukkan oleh pengguna saat login. <br>
        3. Django memiliki sistem autentikasi bawaan yang menyediakan metode otentikasi yang aman, termasuk otentikasi berdasarkan database pengguna (user-based) atau otentikasi eksternal seperti OAuth. <br>

        <br>

        **Otorisasi:** <br>
        1. Otorisasi berkaitan dengan apa yang diizinkan atau tidak diizinkan untuk dilakukan oleh pengguna setelah mereka berhasil diotentikasi. <br>
        2. Ini adalah tahap berikutnya setelah autentikasi dan berfokus pada pengaturan izin dan hak akses pengguna dalam aplikasi. <br>
        3. Django menggunakan sistem otorisasi berbasis peran (role-based), di mana pengguna diberikan peran (role) seperti "pengguna biasa" atau "administrator," dan kemudian izin (permissions) ditentukan berdasarkan peran tersebut. Ini memungkinkan pengelolaan akses ke berbagai bagian dari aplikasi. <br>

        <br>

        **Mengapa keduanya penting?** <br>
        1. Autentikasi penting karena melindungi aplikasi dari akses yang tidak sah. Tanpa autentikasi yang kuat, seseorang dapat dengan mudah menyusup ke dalam sistem dan melakukan tindakan yang tidak diizinkan. <br>
        2. Otorisasi penting karena memungkinkan pengontrolan granular terhadap tindakan yang dapat dilakukan oleh pengguna yang sudah diotentikasi. Ini memastikan bahwa pengguna hanya dapat mengakses atau melakukan operasi yang sesuai dengan peran atau izin yang mereka miliki dalam aplikasi. <br>
    - [x] Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna? <br>
        **Jawab:** <br>
        Cookies adalah bagian kecil data yang disimpan di komputer pengguna saat mereka mengunjungi sebuah situs web. Cookies digunakan dalam konteks aplikasi web untuk menyimpan informasi pada sisi klien (browser pengguna) yang dapat digunakan oleh server web saat pengguna melakukan permintaan berikutnya ke situs tersebut. Salah satu penggunaan utama cookies adalah untuk mengelola data sesi pengguna. <br>

        <br>
        Django, sebagai kerangka kerja web Python, menyediakan dukungan bawaan untuk mengelola cookies dan data sesi pengguna. Berikut adalah bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna: <br>
        1. Membuat Session Cookies: Saat pengguna pertama kali mengakses situs web Django, server akan membuat cookie sesi baru dan mengirimkannya ke browser pengguna. Cookie ini berisi ID sesi unik yang terkait dengan sesi pengguna. <br>
        2. Menyimpan Data Sesuai ID Sesi: Data sesi pengguna disimpan di sisi server, bukan di cookie itu sendiri. Data ini seringkali berisi informasi seperti informasi login, preferensi pengguna, keranjang belanja, dan sebagainya. <br>
        3. Mengelola Data Sesuai ID Sesi: Setiap kali pengguna membuat permintaan ke situs web yang menggunakan sesi, Django akan mengidentifikasi pengguna berdasarkan ID sesi yang terkandung dalam cookie. Ini memungkinkan server untuk mengambil data sesi yang sesuai dari penyimpanan sesi dan membuatnya tersedia dalam kode aplikasi untuk penggunaan selanjutnya. <br>
        4. Meng-update Data Sesuai Permintaan: Selama pengguna berinteraksi dengan situs web, data sesi dapat diperbarui atau diperluas sesuai dengan kebutuhan aplikasi. Django menyediakan API untuk menyimpan dan mengambil data sesi ini dalam kode aplikasi kita. <br>
        5. Mengakhiri Sesuai Permintaan: Ketika sesi pengguna selesai (misalnya, pengguna keluar atau sesi kedaluwarsa), data sesi dapat dihapus dari penyimpanan sesi server, dan cookie sesi pada browser pengguna dapat dihapus. <br>
    - [x] Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? <br>
        **Jawab:** <br>
        Penggunaan cookies dalam pengembangan web dapat menjadi alat yang aman, tetapi juga memiliki risiko potensial yang perlu diwaspadai. Di bawah ini adalah beberapa pertimbangan terkait dengan keamanan cookies: <br>
        1. Cross-Site Scripting (XSS): Cookies dapat menjadi sasaran serangan XSS jika data dalam cookies diambil tanpa sanitasi atau validasi yang cukup. Ini dapat mengizinkan penyerang untuk mencuri atau memanipulasi data cookies pengguna. <br>
        2. Man in the Middle (MitM) Attacks: Cookies yang tidak dienkripsi rentan terhadap serangan MitM, di mana penyerang dapat mencuri atau memodifikasi cookies saat data dikirimkan dari server ke browser pengguna. <br>
        3. Session Fixation: Penyerang dapat mencoba menetapkan ID sesi mereka sendiri kepada pengguna dengan tujuan untuk mencuri sesi pengguna yang telah diotentikasi. <br>
    - [x] Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). <br>
        **Jawab:** <br>
        Sudah dijelaskan di atas <br>
- [x] Melakukan add-commit-push ke GitHub.

# PBP Tugas 5
## Checklist Tugas
Checklist untuk tugas ini adalah sebagai berikut: <br>
- [x] Kustomisasi desain pada templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut <br>
    - Install tailwind: <br>
        https://django-tailwind.readthedocs.io/en/latest/installation.html <br>
    - [x] Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin. <br>
        - Memodifikasi dan menambahkan file-file HTML dengan styling. <br>
            - ```templates\base.html``` <br>
                ```html
                {% load static tailwind_tags %}

                <!DOCTYPE html>
                <html lang="en">
                    <head>
                        <meta charset="UTF-8" />
                        <meta http-equiv="X-UA-Compatible" content="IE=edge">
                        <meta
                            name="viewport"
                            content="width=device-width, initial-scale=1.0"
                        />

                        {% block meta %}
                        {% endblock meta %}
                        {% tailwind_css %}
                    </head>

                    <body class="bg-gray-500">
                        <div>
                            {% block content %}
                            {% endblock content %}
                        </div>
                    </body>    
                </html>
                ```
            - ```login.html``` <br>
                ```html
                {% extends 'base.html' %}

                {% block meta %}
                    <title>LOGIN</title>
                {% endblock meta %}

                {% block content %}

                <div class="login">
                    <form method="POST" action="">
                        {% csrf_token %}
                        <div class="flex justify-center items-center h-screen bg-gray-600">
                            <div class="w-96 p-6 shadow-lg bg-white rounded-md">
                                <h1 class="text-3xl block text-center font-semibold"><i class="fa-solid fa-user"></i> Login</h1>
                                <hr class="mt-3">
                                <div class="mt-3">
                                    <label for="username" class="block text-base mb-2">Username</label>
                                    <input type="text" name="username" class="border w-full text-base px-2 py-1 focus:outline-none focus:ring-0 focus:border-gray-600" placeholder="Enter Username..." />
                                </div>
                                <div class="mt-3">
                                    <label for="password" class="block text-base mb-2">Password</label>
                                    <input type="password" name="password" class="border w-full text-base px-2 py-1 focus:outline-none focus:ring-0 focus:border-gray-600" placeholder="Enter Password..." />
                                </div>
                                {% if messages %}
                                    <ul class="mt-3">
                                        {% for message in messages %}
                                            <li class="text-red-600">{{ message }}</li>
                                        {% endfor %}
                                    </ul>
                                {% endif %}
                                <div class="mt-3 flex justify-between items-center">
                                    <div>
                                        <p>Don't have an account yet?</p>
                                    </div>
                                    <div>
                                        <a href="{% url 'main:register' %}" class="text-blue-600 font-semibold">Register now!</a>
                                    </div>
                                </div>
                                <div class="mt-5">
                                    <button value="Login" type="submit" class="border-2 border-green-700 bg-green-700 text-white py-1 w-full rounded-md hover:bg-transparent hover:text-green-700 font-semibold"><i class="fa-solid fa-right-to-bracket"></i>&nbsp;&nbsp;Login</button>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>

                {% endblock content %}
                ```
            - ```register.html```
                ```html
                {% extends 'base.html' %}

                {% block meta %}
                    <title>REGISTER</title>
                {% endblock meta %}

                {% block content %}  

                <div class="login">
                    <form method="POST" action="">
                        {% csrf_token %}
                        <div class="flex justify-center items-center h-screen bg-gray-600">
                            <div class="w-96 p-6 shadow-lg bg-white rounded-md">
                                <h1 class="text-3xl block text-center font-semibold"><i class="fa-solid fa-user"></i> Register</h1>
                                <hr class="mt-3">
                                {% for field in form %}
                                <div class="mt-3">
                                    {% if field.errors %}
                                    <ul class="block text-base mb-2 list-disc mt-3">
                                        {% for error in field.errors %}
                                        <li class="text-red-600">{{ error }}</li>
                                        {% endfor %}
                                    </ul>
                                    {% endif %}
                                    <p class="block text-base mb-2">{{ field.label_tag }}</p>
                                    <p class="w-full text-base px-2 py-1 focus:outline-none focus:ring-0 focus:border-gray-600" >
                                        {{ field }}
                                    </p>
                                </div>
                                {% endfor %}
                                {% if messages %}
                                    <ul class="mt-3">
                                        {% for message in messages %}
                                            <li class="text-red-600">{{ message }}</li>
                                        {% endfor %}
                                    </ul>
                                {% endif %}
                                <div class="mt-3 flex justify-between items-center">
                                    <div>
                                        <p>Already have an account?</p>
                                    </div>
                                    <div>
                                        <a href="{% url 'main:login' %}" class="text-blue-600 font-semibold">Login now!</a>
                                    </div>
                                </div>
                                <div class="mt-5">
                                    <button value="Login" type="submit" class="border-2 border-green-700 bg-green-700 text-white py-1 w-full rounded-md hover:bg-transparent hover:text-green-700 font-semibold"><i class="fa-solid fa-right-to-bracket"></i>&nbsp;&nbsp;Register</button>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>

                {% endblock content %}
                ```
            - ```navbar.html```
                ```html
                <header class="bg-gray-400">
                <nav class="flex justify-between items-center w-[92%] mx-auto">
                    <div>
                        <img class="w-36 h-14 cursor-pointer mt-2 mb-2" src="https://cdn2.steamgriddb.com/file/sgdb-cdn/logo/90664f7d1cde0398e10c9466ef495b89.png" alt="...">
                    </div>
                    <div
                        class="nav-links duration-500 md:static absolute md:min-h-fit min-h-[60vh] left-0 top-[-100%] md:w-auto  w-full flex items-center px-5">
                        <ul class="flex md:flex-row flex-col md:items-center md:gap-[4vw] gap-8">
                        </ul>
                    </div>
                    <div class="flex items-center gap-6">
                        <a href="{% url 'main:logout' %}" class="bg-[#cc3f3f] text-white px-5 py-2 rounded-full hover:bg-[#ec8e87]">Logout</a>
                    </div>
                </header>
                ```
            - ```create_operator.html``` <br>
                ```html
                {% extends 'base.html' %}

                {% block meta %}
                    <title>CREATE OPERATOR</title>
                {% endblock meta %}

                {% block content %}
                <div class="px-4 my-7 ml-7">
                <h1 class="text-2xl font-bold font-sans mb-5">Add Operator</h1>

                <form method="POST">
                    {% csrf_token %}
                    <table>
                    {{ form.as_table }}
                    <tr>
                        <td></td>
                        <td>
                        <input class="bg-[#3870ff] text-white mt-5 px-5 py-2 rounded-full hover:bg-[#87aaec]" type="submit" value="Add Operator">
                        </td>
                    </tr>
                    </table>
                </form>
                </div>

                {% endblock %}
                ```
    - [x] Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card. <br>
        - Memodifikasi ```main.html``` dengan styling dan juga mengerjakan bonus. <br>
            - ```main.html``` <br>
                ```html
                {% extends 'base.html' %}

                {% block meta %}
                    <title>ROSTER</title>
                {% endblock meta %}

                {% block content %}

                {% include 'navbar.html' %}

                {% comment %} Shout out to Faris Zhafir Faza for helping me {% endcomment %}
                <div class="px-4 my-7 ml-7">
                    <h1 class="text-2xl font-bold font-sans">Greetings Officer <span class="text-red-500">{{ creator }}</span> from {{ class }}!</h1>
                    <div class="flex justify-between mt-4">
                        {% if operators %}
                        <h1 class="font-extrabold text-2xl text-black">Operator Roster</h1>
                        {% else %}
                        <h1 class="font-extrabold text-2xl text-black">Add Operator</h1>
                        {% endif %}
                        <a href="{% url 'main:create_operator' %}" class="flex w-fit justify-self-end text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:ring-green-300 font-medium rounded-lg text-sm p-4 mr-2 mb-2 focus:outline-none">
                            <button>
                            Add New Operator
                            </button>
                        </a>
                    </div>
                    <div class="flex flex-wrap justify-center">
                        {% for operator in operators %}
                        <div class="w-[300px] m-4 h-[580px] p-6 {% if forloop.last %} bg-blue-200 {% else %}bg-white{% endif %} border border-gray-200 rounded-lg shadow-xl">
                            <div class="flex justify-between">
                                <h5 class="mb-2 text-xl font-bold tracking-tight text-gray-900 ">{{operator.name}}</h5>
                                <form action="{% url 'main:remove_operator' operator.id %}" method="post">
                                    {% csrf_token %}
                                    <button type="submit" name="Remove" class="btn btn-danger focus:outline-none text-white bg-red-600 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-2 py-1.5 mb-2">Delete</button>
                                </form>
                            </div>
                            <p class="my-3 font-normal text-gray-700 ">{{operator.description}}</p>
                            <div class="flex justify-between mt-2 mb-2">
                                <p class="font-bold text-gray-900">{{operator.price}} renown</p>
                            </div>
                            <div class="flex justify-between mx-2 mt-2 mb-2">
                                <a><center>{{ operator.primary_weapon_ammo_amount }} Primary Weapon Amount</center></a>
                                <a><center>{{ operator.secondary_weapon_ammo_amount }} Secondary Weapon Amount</center></a>
                            </div>
                            <div class="flex justify-end mx-2 mt-2 mb-2">
                                <form action="{% url 'main:add_primary_ammo_amount' operator.id %}" method="post">
                                    {% csrf_token %}
                                    <button type="submit" name="Increment" class="btn btn-primary text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-2 py-1.5 mr-2 mb-2 focus:outline-none">+ Primary</button>
                                </form>
                                <form action="{% url 'main:add_secondary_ammo_amount' operator.id %}" method="post">
                                    {% csrf_token %}
                                    <button type="submit" name="Increment" class="btn btn-primary text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-2 py-1.5 mr-2 mb-2 focus:outline-none">+ Secondary</button>
                                </form>
                            </div>
                            <div class="flex justify-end mx-2 mt-2 mb-2">
                                <form action="{% url 'main:dec_primary_ammo_amount' operator.id %}" method="post">
                                    {% csrf_token %}
                                    <button type="submit" name="Decrement" class="focus:outline-none text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-2 py-1.5 mr-2 mb-2">- Primary</button>
                                </form>
                                <form action="{% url 'main:dec_secondary_ammo_amount' operator.id %}" method="post">
                                    {% csrf_token %}
                                    <button type="submit" name="Decrement" class="focus:outline-none text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-2 py-1.5 mr-2 mb-2">- Secondary</button>
                                </form>
                            </div>
                        </div>
                        {% endfor %}
                    </div>
                </div>
                    
                {% endblock content %}
                ```
- [x] Menjawab beberapa pertanyaan berikut pada ```README.md``` pada root folder (silakan modifikasi ```README.md``` yang telah kamu buat sebelumnya; tambahkan subjudul untuk setiap tugas). <br>
    - [x] Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya. <br>
    **Jawab:** <br>
        Element Selector: <br>
        Element Selector memungkinkan kita mengubah properti untuk semua elemen yang memiliki tag HTML yang sama. <br>
        Kita dapat menggunakan element sebagai selector dalam file CSS. Element selector menggunakan format [id_name] (tanpa diawali oleh sebuah simbol). <br>
        Selektor elemen dalam CSS digunakan untuk memilih elemen di dalam elemen, yaitu menggabungkan dua selektor sehingga elemen yang cocok dengan selektor kedua akan dipilih jika elemen tersebut memiliki elemen leluhur yang cocok dengan selektor pertama. <br>

        <br>
        ID Selector: <br>
        ID selector menggunakan ID pada tag sebagai selector-nya. ID bersifat unik dalam satu halaman web. ID dapat ditambahkan pada halaman template HTML. Kemudian, kita dapat menggunakan ID tersebut sebagai selector dalam file CSS. ID selector menggunakan format #[id_name] (selalu diawali #). <br>
        Kita dapat menggunakan pemilih ID pada judul atau gambar, tombol, dan elemen HTML lainnya. <br>

        <br>
        Class Selector: <br>
        Class Selector memungkinkan kita untuk mengelompokkan elemen dengan karakteristik yang sama. Kemudian, kita dapat menggunakan Class tersebut sebagai selector dalam file CSS. Kemudian, kita dapat menggunakan Class tersebut sebagai selector dalam file CSS. Class selector menggunakan format .[class_name] (diawali .) Class selector digunakan untuk memilih semua elemen yang termasuk dalam atribut kelas tertentu. <br><br>

    - [x] Jelaskan HTML5 Tag yang kamu ketahui <br>
    **Jawab:** <br>
        ```<!--...-->```   Specifies a comment<br>
        ```<!DOCTYPE>```   Specifies the document type<br>
        ```<a>```   Specifies an anchor<br>
        ```<abbr>```   Specifies an abbreviation<br>
        ```<acronym>```   Deprecated:Specifies an acronym<br>
        ```<address>```   Specifies an address element<br>
        ```<applet>```   Deprecated: Specifies an applet<br>
        ```<area>```   Specifies an area inside an image map<br>
        ```<article>```   New Tag: Specifies an independent piece of content of a document, such as a blog entry or newspaper article<br>
        ```<aside>```   New Tag:Specifies a piece of content that is only slightly related to the rest of the page.<br>
        ```<audio>```   New Tag:Specifies an audio file.<br>
        ```<base>```   Specifies a base URL for all the links in a page<br>
        ```<basefont>```   Deprecated: Specifies a base font<br>
        ```<bdo>```   Specifies the direction of text display<br>
        ```<bgsound>```   Specifies the background music<br>
        ```<blink>```   Specifies text which blinks<br>
        ```<blockquote>```   Specifies a long quotation<br>
        ```<body>```   Specifies the body element<br>
        ```<br>```   Inserts a single line break<br>
        ```<button>```   Specifies a push button<br>
        ```<canvas>```   New Tag:This is used for rendering dynamic bitmap graphics on the fly, such as graphs or games.<br>
        ```<caption>```   Specifies a table caption<br>
        ```<center>```   Deprecated: Specifies centered text<br>
        ```<col>```   Specifies attributes for table columns<br>
        ```<colgroup>```   Specifies groups of table columns<br>
        ```<command>```   New Tag:Specifies a command the user can invoke.<br>
        ```<comment>```   Puts a comment in the document<br>
        ```<datalist>```   New Tag:Together with the a new list attribute for input can be used to make comboboxes<br>
        ```<dd>```   Specifies a definition description<br>
        ```<del>```   Specifies deleted text<br>
        ```<details>```   New Tag:Specifies additional information or controls which the user can obtain on demand.<br>
        ```<dir>```   Deprecated: Specifies a directory list<br>
        ```<div>```   Specifies a section in a document<br>
        ```<dl>```   Specifies a definition list<br>
        ```<dt>```   Specifies a definition term<br>
        ```<embed>```   New Tag:Defines external interactive content or plugin.<br>
        ```<fieldset>```   Specifies a fieldset<br>
        ```<figure>```   New Tag:Specifies a piece of self-contained flow content, typically referenced as a single unit from the main flow of the document.<br>
        ```<b>```   Specifies bold text<br>
        ```<big>```   Deprecated:Specifies big text<br>
        ```<i>```   Specifies italic text<br>
        ```<small>```   Specifies small text<br>
        ```<tt>```   Deprecated:Specifies teletype text<br>
        ```<font>```   Deprecated: Specifies text font, size, and color<br>
        ```<footer>```   New Tag:Specifies a footer for a section and can contain information about the author, copyright information, et cetera.<br>
        ```<form>```  Specifies a form<br>
        ```<frame>```   Deprecated:Specifies a sub window (a frame)<br>
        ```<frameset>```   Deprecated:Specifies a set of frames<br>
        ```<head>```   Specifies information about the document<br>
        ```<header>```   New Tag:Specifies a group of introductory or navigational aids.<br>
        ```<hgroup>```   New Tag:Specifies the header of a section.<br>
        ```<h1>``` to ```<h6>```   Specifies header 1 to header 6<br>
        ```<hr>```   Specifies a horizontal rule<br>
        ```<html>```   Specifies an html document<br>
        ```<isindex>```   Deprecated: Specifies a single-line input field<br>
        ```<iframe>```   Specifies an inline sub window (frame)<br>
        ```<ilayer>```   Specifies an inline layer<br>
        ```<img>```   Specifies an image<br>
        ```<input>```  Specifies an input field<br>
        ```<ins>```   Specifies inserted text<br>
        ```<keygen>```   New Tag:Specifies control for key pair generation.<br>
        ```<keygen>```   Generate key information in a form<br>
        ```<label>```   Specifies a label for a form control<br>
        ```<layer>```   Specifies a layer<br>
        ```<legend>```   Specifies a title in a fieldset<br>
        ```<li>```   Specifies a list item<br>
        ```<link>```   Specifies a resource reference<br>
        ```<map>```   Specifies an image map<br>
        ```<mark>```   New Tag:Specifies a run of text in one document marked or highlighted for reference purposes, due to its relevance in another context.<br>
        ```<marquee>```   Create a scrolling-text marquee<br>
        ```<menu>```   Deprecated: Specifies a menu list<br>
        ```<meta>```   Specifies meta information<br>
        ```<meter>```   New Tag:Specifies a measurement, such as disk usage.<br>
        ```<multicol>```   Specifies a multicolumn text flow<br>
        ```<nav>```   New Tag:Specifies a section of the document intended for navigation.<br>
        ```<nobr>```   No breaks allowed in the enclosed text<br>
        ```<noembed>```   Specifies content to be presented by browsers that do not support the <embed>tag<br>
        ```<noframes>```   Deprecated:Specifies a noframe section<br>
        ```<noscript>```   Specifies a noscript section<br>
        ```<object>```   Specifies an embedded object<br>
        ```<ol>```   Specifies an ordered list<br>
        ```<optgroup>```   Specifies an option group<br>
        ```<option>```   Specifies an option in a drop-down list<br>
        ```<output>```   New Tag:Specifies some type of output, such as from a calculation done through scripting.<br>
        ```<p>```   Specifies a paragraph<br>
        ```<param>```   Specifies a parameter for an object<br>
        ```<cite>```   Specifies a citation<br>
        ```<code>```   Specifies computer code text<br>
        ```<dfn>```   Specifies a definition term<br>
        ```<em>```   Specifies emphasized text<br>
        ```<kbd>```   Specifies keyboard text<br>
        ```<samp>```   Specifies sample computer code<br>
        ```<strong>```   Specifies strong text<br>
        ```<var>```   Specifies a variable<br>
        ```<plaintext>```   Deprecated: Render the remainder of the document as preformatted plain text<br>
        ```<pre>```   Specifies preformatted text<br>
        ```<progress>```   New Tag:Specifies a completion of a task, such as downloading or when performing a series of expensive operations.<br>
        ```<q>```   Specifies a short quotation<br>
        ```<ruby>```   New Tag:Together with ```<rt>``` and ```<rp>``` allow for marking up ruby annotations.<br>
        ```<script>```   Specifies a script<br>
        ```<section>```   New Tag:Represents a generic document or application section.<br>
        ```<select>```   Specifies a selectable list<br>
        ```<spacer>```   Specifies a white space<br>
        ```<span>```   Specifies a section in a document<br>
        ```<s>```   Deprecated: Specifies strikethrough text<br>
        ```<strike>```   Deprecated: Specifies strikethrough text<br>
        ```<style>```   Specifies a style definition<br>
        ```<sub>```   Specifies subscripted text<br>
        ```<sup>```   Specifies superscripted text<br>
        ```<table>```   Specifies a table<br>
        ```<tbody>```   Specifies a table body<br>
        ```<td>```   Specifies a table cell<br>
        ```<textarea>```   Specifies a text area<br>
        ```<tfoot>```   Specifies a table footer<br>
        ```<th>```   Specifies a table header<br>
        ```<thead>```   Specifies a table header<br>
        ```<time>```   New Tag:Specifies a date and/or time.<br>
        ```<title>```   Specifies the document title<br>
        ```<tr>```  Specifies a table row<br>
        ```<u>```   Deprecated: Specifies underlined text<br>
        ```<ul>```   Specifies an unordered list<br>
        ```<video> ```  New Tag:Specifies a video file.<br>
        ```<wbr>```   New Tag:Specifies a line break opportunity.<br>
        ```<wbr>```   Indicate a potential word break point within a ```<nobr>``` section<br>
        ```<xmp>```   Deprecated: Specifies preformatted text<br><br>
    - [x] Jelaskan perbedaan antara margin dan padding. <br>
    **Jawab:** <br>
        Margin dan padding adalah dua properti dalam CSS yang digunakan untuk mengatur ruang di sekitar elemen HTML. Meskipun keduanya digunakan untuk mengatur tata letak elemen, mereka memiliki tujuan yang berbeda dan diterapkan dengan cara yang berbeda: <br>
            1. **Margin** <br>
                - Margin adalah ruang di luar elemen HTML, yang berarti ia mengontrol jarak antara elemen tersebut dan elemen-elemen lain di sekitarnya. <br>
                - Margin digunakan untuk menciptakan ruang tambahan di luar elemen untuk mengatur jarak antara elemen tersebut dan elemen-elemen tetangganya, baik horizontal maupun vertikal. <br>
                - Margin juga digunakan untuk mengatur pusat elemen di tengah halaman dengan menggunakan ```margin: auto;```. <br>
            2. **Padding** <br>
                - Padding adalah ruang di dalam elemen HTML, yang berarti ia mengontrol jarak antara konten elemen dan batas elemen tersebut. <br>
                - Padding digunakan untuk memberikan ruang antara konten elemen dan batas elemen, sehingga tidak memengaruhi jarak antara elemen tersebut dan elemen-elemen lain di sekitarnya. <br>
                - Padding sering digunakan untuk mengatur tampilan elemen dalam elemen kotak atau mengatur tampilan elemen teks. <br> <br>
    - [x] Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya? <br>
    **Jawab:** <br>
        Tailwind CSS dan Bootstrap adalah dua framework CSS yang berbeda dalam pendekatan dan gaya pengembangan. Bootstrap menyediakan sejumlah komponen siap pakai dengan desain yang sudah ditentukan, sementara Tailwind adalah alat yang lebih rendah tingkatnya, memungkinkan pengembang untuk menyesuaikan setiap gaya komponen secara langsung dalam kode HTML. Bootstrap cocok digunakan ketika kita perlu mengembangkan dengan cepat dan ingin desain yang konsisten tanpa banyak penyesuaian. Di sisi lain, Tailwind menjadi pilihan yang baik jika kita ingin total kontrol atas desain kita atau jika proyek kita memiliki tuntutan kustomisasi yang tinggi, meskipun ini dapat memerlukan lebih banyak waktu untuk mengimplementasikannya. <br><br>
    - [x] Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). <br>
    **Jawab:** <br>
    Sudah dijelaskan di atas. <br>

# PBP Tugas 6
- Jelaskan perbedaan antara asynchronous programming dengan synchronous programming. <br>
    **Jawab:** <br>
    1. Synchronous Programming: <br>
        - Dalam synchronous programming, tugas-tugas dieksekusi secara berurutan, satu per satu. Artinya, ketika satu tugas sedang berjalan, program akan menunggu hingga tugas tersebut selesai sebelum menjalankan tugas berikutnya. <br>
        - Ini cocok untuk tugas-tugas yang cepat dan tidak memerlukan banyak waktu pemrosesan. <br>
        - Jika ada tugas yang memerlukan waktu lama, seperti mengambil data dari database atau mengunduh file dari internet, maka program akan mengalami blocking, di mana program tidak akan merespons input atau menjalankan tugas lain sampai tugas yang sedang berlangsung selesai. <br>
    2. Asynchronous Programming: <br>
        - Dalam asynchronous programming, tugas-tugas dieksekusi secara bersamaan atau non-blokir. Artinya, program tidak harus menunggu tugas yang satu selesai sebelum menjalankan tugas lainnya. <br>
        - Ini sangat berguna dalam situasi di mana ada banyak tugas yang memerlukan waktu lama atau menunggu sumber daya eksternal seperti jaringan atau database. <br>
        - Untuk mengimplementasikan asynchronous programming, biasanya digunakan konsep seperti callback, promise, atau async/await dalam bahasa pemrograman seperti JavaScript. <br> <br>
    Contoh perbedaannya dalam konteks web development: <br>
        - **Synchronous**: Ketika seorang pengguna mengklik tombol untuk mengunduh file besar dari server, antarmuka pengguna akan membeku (freeze) sampai file tersebut selesai diunduh. Selama itu, pengguna tidak dapat berinteraksi dengan aplikasi. <br>
        - **Asynchronous**: Dalam kasus yang sama, jika aplikasi web menggunakan asynchronous programming, pengguna masih dapat berinteraksi dengan antarmuka pengguna tanpa terpengaruh oleh proses pengunduhan. Proses pengunduhan akan berjalan di belakang layar, dan pengguna dapat melanjutkan berinteraksi dengan aplikasi tanpa adanya pembekuan antarmuka. <br><br>
- Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini. <br>
    **Jawab:** <br>
    Paradigma event-driven programming adalah salah satu pendekatan dalam pemrograman yang berfokus pada interaksi dan merespons kejadian atau peristiwa (events) yang terjadi dalam sistem atau aplikasi. Dalam konteks JavaScript dan AJAX (Asynchronous JavaScript and XML), paradigma ini sangat umum digunakan karena banyak tugas yang melibatkan interaksi dengan pengguna atau komunikasi dengan server web melalui asinkronus. <br> <br>
    Maksud dari paradigma event-driven programming adalah sebagai berikut: <br>
        1. **Berbasis Kejadian (Event-Based)**: Aplikasi yang dibangun dengan paradigma ini menunggu kejadian atau peristiwa tertentu untuk terjadi, seperti klik tombol, input pengguna, atau respons dari server, lalu meresponsnya dengan menjalankan kode yang sesuai. <br>
        2. **Non-Blokir (Non-Blocking)**: Paradigma ini memungkinkan aplikasi untuk tetap merespons terhadap kejadian lainnya tanpa harus menunggu penyelesaian dari kejadian tertentu yang sedang berlangsung. Ini sangat berguna dalam situasi asinkronus seperti komunikasi dengan server. <br><br>
    ```java
    document.getElementById('load-button').addEventListener('click', function() {
    // Kode yang akan dijalankan saat tombol "Muat Data" diklik
    // Misalnya, mengirim permintaan AJAX ke server
    });
    ```
- Jelaskan penerapan asynchronous programming pada AJAX. <br>
    **Jawab:** <br>
    Penerapan asynchronous programming pada AJAX (Asynchronous JavaScript and XML) adalah salah satu aspek fundamental dalam penggunaan AJAX dalam pengembangan web. Dalam konteks AJAX, asynchronous programming memungkinkan permintaan data ke server web dan pemrosesan respons server dilakukan secara non-blokir, sehingga halaman web tetap responsif dan tidak mengalami pembekuan saat menunggu respons dari server. Berikut adalah cara asynchronous programming diterapkan pada AJAX: <br>
    1. **Menggunakan Objek XMLHttpRequest atau Fetch API:** <br>
        - Biasanya, dalam asynchronous programming dengan AJAX, kita akan menggunakan objek XMLHttpRequest atau Fetch API (lebih modern) untuk mengirim permintaan ke server dan menerima respons. <br>
        - Contoh penggunaan Fetch API dalam JavaScript modern: <br>
            ```java
            fetch('https://example.com/data')
            .then(response => {
                if (!response.ok) {
                throw new Error('Terjadi kesalahan saat mengambil data.');
                }
                return response.json();
            })
            .then(data => {
                // Lakukan sesuatu dengan data yang diterima dari server
            })
            .catch(error => {
                // Tangani kesalahan jika ada
            });
            ```
    2. **Menggunakan Callback, Promise, atau async/await:** <br>
        - Biasanya, kita akan menggunakan callback, promise, atau async/await untuk menangani respons dari server dan menghindari pembekuan (blocking) antarmuka pengguna. <br>
        - Contoh penggunaan promise dengan Fetch API: <br>
            ```java
            function fetchData() {
            return fetch('https://example.com/data')
                .then(response => {
                if (!response.ok) {
                    throw new Error('Terjadi kesalahan saat mengambil data.');
                }
                return response.json();
                });
            }

            fetchData()
            .then(data => {
                // Lakukan sesuatu dengan data yang diterima dari server
            })
            .catch(error => {
                // Tangani kesalahan jika ada
            });
            ```
    3. **Menangani Respons Asynchronously:** <br>
        - Dalam asynchronous programming, kode kita akan tetap melanjutkan eksekusi tanpa harus menunggu respons dari server. Ini memungkinkan interaksi pengguna dengan halaman web tetap lancar sementara data dari server diambil dan diproses secara asinkron. <br>
        - Setelah respons dari server diterima, kita dapat memanipulasi DOM atau menjalankan tindakan lainnya sesuai dengan data yang diterima. <br><br>
- Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan. <br>
    **Jawab:** <br>
    Penerapan AJAX dengan menggunakan Fetch API dan jQuery adalah dua pendekatan yang berbeda dalam mengatasi permintaan asinkron ke server dalam pengembangan web. <br> <br>
    **Fetch API:** <br>
        1. **Native:** Fetch API adalah bagian dari standar JavaScript ECMAScript, yang berarti ia merupakan bagian bawaan dari bahasa JavaScript modern. Kita tidak perlu mengunduh atau memasang perpustakaan tambahan untuk menggunakannya. <br>
        2. **Lebih Ringan:** Fetch API cenderung lebih ringan dibandingkan dengan jQuery. Ini dapat menghemat bandwidth dan memuat halaman lebih cepat karena tidak memerlukan penambahan perpustakaan eksternal. <br>
        3. **Promises:** Fetch API menggunakan konsep promise, yang memungkinkan kita mengelola tugas asinkron dengan cara yang lebih bersih dan mudah dipahami. Ini membuat kode kita lebih mudah dibaca. <br>
        4. **Fleksibilitas:** Fetch API memberikan kita lebih banyak fleksibilitas dalam mengelola permintaan dan respons HTTP, dan dapat berintegrasi dengan baik dengan teknologi terbaru seperti async/await. <br> <br>
    **jQuerry:** <br>
        1. **Kompatibilitas:** jQuery adalah perpustakaan yang telah ada sejak lama dan kompatibel dengan banyak browser yang lebih tua. Ini bisa bermanfaat jika kita harus mendukung browser lama. <br>
        2. **Abstraksi yang Kuat:** jQuery menyediakan abstraksi yang kuat untuk AJAX, yang bisa membuat kode lebih pendek dan lebih mudah digunakan untuk tugas-tugas sederhana. <br>
        3. Plugin Ekstensif: jQuery memiliki banyak plugin yang tersedia, termasuk plugin AJAX yang memperluas fungsionalitasnya. Ini bisa sangat berguna jika kita membutuhkan fitur-fitur khusus. <br> <br>
    **Pendapat Pribadi:** <br>
    - Jika kita mengembangkan aplikasi modern dan ingin memaksimalkan performa serta menghindari penggunaan perpustakaan eksternal yang tidak diperlukan, Fetch API adalah pilihan yang baik. Ini lebih ringan, lebih modern, dan lebih bersih dalam hal manajemen tugas asinkron. <br>
    - Namun, jika kita bekerja dengan proyek yang harus mendukung browser lama atau ingin memanfaatkan abstraksi yang kuat dan plugin yang telah ada, maka menggunakan jQuery mungkin lebih sesuai. <br> <br>
- Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). <br>
    **Jawab:** <br>
    - AJAX GET
        Membuang kode Card yang sebelumnya dibuat dan menambahkan ini sebagai penggantinya. <br>
        ```html
        <div id="operator_card" class="flex flex-wrap justify-center"></div>
        ```
        Menambahkan function untuk mendapatkan operator dalam bentuk json dalam views.py. <br>
        ```python
        def get_operator_json(request):
            operator_item = Operator.objects.filter(user=request.user)
            return HttpResponse(serializers.serialize('json', operator_item))
        ```

        Menambahkan URL function tersebut ke dalam urls.py. <br>
        ```python
        ...
        path('get-operator/', get_operator_json, name='get_operator_json'),
        ...
        ```

        Menambahkan script AJAX getter untuk mendapatkan operator. <br>
        ```java
        async function getOperators() {
            return fetch("{% url 'main:get_operator_json' %}").then((res) => res.json())
        }
        ```

        Menambahkan script AJAX untuk menampilkan operator-operator sekaligus refresh. <br>
        ```java
        async function refreshOperators() {
            document.getElementById("operator_card").innerHTML = ""
            const operators = await getOperators()
            if(operators.length > 0){
                messageText.textContent = "Operator Roster";
            }else{
                messageText.textContent = "Add Operator";
            }
            let htmlString = ``
            operators.forEach((operator, index, array) => {
                const isLastOperator = index === array.length - 1;
                htmlString += `\n
                <div id="operator_card" class="w-[300px] m-4 h-[580px] p-6 ${isLastOperator ? 'bg-blue-200' : 'bg-white'} border border-gray-200 rounded-lg shadow-xl">
                    <div class="flex justify-between">
                        <h5 class="mb-2 text-xl font-bold tracking-tight text-gray-900 ">${operator.fields.name}</h5>
                        <a>
                            <button type="submit" onclick="deleteOperator(${operator.pk}); return false;" class="btn btn-danger focus:outline-none text-white bg-red-600 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-2 py-1.5 mb-2">Remove</button>
                        </a>
                    </div>
                    <p class="my-3 font-normal text-gray-700 ">${operator.fields.description}</p>
                    <div class="flex justify-between mt-2 mb-2">
                        <p class="font-bold text-gray-900">${operator.fields.price} renown</p>
                    </div>
                    <div class="flex justify-between mx-2 mt-2 mb-2">
                        <a><center>${operator.fields.primary_weapon} : ${operator.fields.primary_weapon_ammo_amount}</center></a>
                        <a><center>${operator.fields.secondary_weapon} : ${operator.fields.secondary_weapon_ammo_amount}</center></a>
                    </div>
                    <div class="flex justify-end mx-2 mt-2 mb-2">
                        <a href="/add-primary-ammo-amount/${operator.pk}">
                            <button type="button" class="btn btn-primary text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-2 py-1.5 mr-2 mb-2 focus:outline-none">+ Primary</button>
                        </a>
                        <a href="/add-secondary-ammo-amount/${operator.pk}">
                            <button type="button" class="btn btn-primary text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-2 py-1.5 mr-2 mb-2 focus:outline-none">+ Secondary</button>
                        </a>
                    </div>
                    <div class="flex justify-end mx-2 mt-2 mb-2">
                        <a href="/dec-primary-ammo-amount/${operator.pk}">
                            <button type="button" class="focus:outline-none text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-2 py-1.5 mr-2 mb-2">- Primary</button>
                        </a>
                        <a href="/dec-secondary-ammo-amount/${operator.pk}">
                            <button type="button" class="focus:outline-none text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:ring-red-300 font-medium rounded-lg text-sm px-2 py-1.5 mr-2 mb-2">- Secondary</button>
                        </a>
                    </div>
                </div>
                ` 
            })
            document.getElementById("operator_card").innerHTML = htmlString
        }

        refreshOperators()
        ```
    - AJAX POST
        Membuat modals form. <br>
        ```html
        <div id="modal" tabindex="-1" aria-hidden="true" class="fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-[calc(100%-1rem)] max-h-full">
            <div class="relative w-full max-w-md max-h-full">
                <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
                    <button type="button" class="absolute top-3 right-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ml-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white" data-modal-hide="modal">
                        <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"/>
                        </svg>
                        <span class="sr-only">Close</span>
                    </button>
                    <div class="px-6 py-6 lg:px-8">
                        <h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">Create operator</h3>
                        <form class="space-y-6" id="form" onsubmit="return false;">
                            {% csrf_token %}
                            <div>
                                <label for="name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Name</label>
                                <input type="text" name="name" id="name" class="form-control border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 " placeholder="Operator" required>
                            </div>
                            <div>
                                <label for="unit" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Unit</label>
                                <input type="text" name="unit" id="unit" class="form-control border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 " placeholder="GSG-9" required>
                            </div>
                            <div>
                                <label for="primary_weapon" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Primary Weapon</label>
                                <input type="text" name="primary_weapon" id="primary_weapon" class="form-control border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 " placeholder="M4A1" required>
                            </div>
                            <div>
                                <label for="primary_weapon_ammo_amount" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Primary Ammo</label>
                                <input type="number" name="primary_weapon_ammo_amount" id="primary_weapon_ammo_amount" class="form-control bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 " placeholder="300" required>
                            </div>
                            <div>
                                <label for="secondary_weapon" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Secondary Weapon</label>
                                <input type="text" name="secondary_weapon" id="secondary_weapon" class="form-control border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 " placeholder="P12" required>
                            </div>
                            <div>
                                <label for="secondary_weapon_ammo_amount" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Secondary Ammo</label>
                                <input type="number" name="secondary_weapon_ammo_amount" id="secondary_weapon_ammo_amount" class="form-control bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 " placeholder="300" required>
                            </div>
                            <div>
                                <label for="armor" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Armor</label>
                                <input type="number" name="armor" id="armor" class="form-control bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 " placeholder="2" required>
                            </div>
                            <div>
                                <label for="speed" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Speed</label>
                                <input type="number" name="speed" id="speed" class="form-control bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 " placeholder="2" required>
                            </div>
                            <div>
                                <label for="description" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Description</label>
                                <textarea type="text" name="description" id="description" class="form-control border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 " placeholder="The operator is..." required></textarea>
                            </div>
                            <div>
                                <label for="price" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Price</label>
                                <input type="number" name="price" id="price" class="form-control bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 " placeholder="12500" required>
                            </div>
                            <button type="button" id="button_add" class="w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center" data-modal-hide="modal">Add Operator</button>
                            <button type="button" class="w-full text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center " data-modal-hide="modal">Cancel</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        ```

        Mengubah button add operator untuk membuka modal form. <br>
        ```html
        <div class="flex justify-between" id="msgcontainer">
            <h1 id="msgtext" class="font-extrabold text-2xl mt-3 text-black"></h1>
            <div class="flex">
                <a class="flex w-fit justify-self-end text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm p-4 mr-2 mb-2 focus:outline-none">
                    <button data-modal-target="modal" data-modal-toggle="modal" type="button">
                        Create operator
                    </button>
                </a>
            </div>
        </div>
        ```

        Membuat function add_operator_ajax di dalam views.py. <br>
        ```python
        @csrf_exempt
        def add_operator_ajax(request):
            if request.method == 'POST':
                name = request.POST.get("name")
                price = request.POST.get("price")
                unit = request.POST.get("unit")
                primary_weapon = request.POST.get("primary_weapon")
                secondary_weapon = request.POST.get("secondary_weapon")
                primary_weapon_ammo_amount = request.POST.get("primary_weapon_ammo_amount")
                secondary_weapon_ammo_amount = request.POST.get("secondary_weapon_ammo_amount")
                armor = request.POST.get("armor")
                speed = request.POST.get("speed")
                description = request.POST.get("description")
                price = request.POST.get("price")
                user = request.user

                new_operator = Operator(name=name, 
                                    price=price,
                                    unit=unit,
                                    primary_weapon=primary_weapon,
                                    secondary_weapon=secondary_weapon,
                                    primary_weapon_ammo_amount=primary_weapon_ammo_amount,
                                    secondary_weapon_ammo_amount=secondary_weapon_ammo_amount,
                                    armor=armor,
                                    speed=speed,
                                    description=description, 
                                    user=user)
                new_operator.save()

                return HttpResponse(b"CREATED", status=201)

            return HttpResponseNotFound()
        ```

        Menambahkan URL untuk add_operator_ajax dalam urls.py. <br>
        ```python
        ...
        path('create-operator-ajax/', add_operator_ajax, name='add_operator_ajax'),
        ...
        ```

        Membuat script AJAX untuk add operator. <br>
        ```java
        function addOperator() {
            fetch("{% url 'main:add_operator_ajax' %}", {
                method: "POST",
                body: new FormData(document.querySelector('#form'))
            }).then(() => {
                refreshOperators();
                updateRosterSize();})

            document.getElementById("form").reset()
            return false
        }
        ```
    - Menjalankan ```python manage.py collectstatic```. Perintah ini bertujuan untuk mengumpulkan file static dari setiap aplikasi kamu ke dalam suatu folder yang dapat dengan mudah disajikan pada produksi. <br>