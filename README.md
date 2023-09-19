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
    ![html](/doks_md/html.png) <br>
    ![json](/doks_md/json.png) <br>
    ![json2](/doks_md/json2.png) <br>
    ![xml](/doks_md/xml.png) <br>
    ![xml2](/doks_md/xml2.png) <br>
- [x] Melakukan ```add```-```commit```-```push``` ke GitHub. <br>