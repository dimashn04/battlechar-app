# PBP Tugas 01
**BattleChar-App**<br>
**Link:** https://battlechar.adaptable.app/main/ <br>
Dimas Herjunodarpito Notoprayitno<br>
2206081282<br>
PBP C<br>

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
        <br>
    - Menguji apakah proyek telah berhasil dibuat dengan ```./manage.py runserver``` <br>
- [x] Membuat aplikasi dengan nama ```main``` pada proyek tersebut. <br>
- [x] Melakukan routing pada proyek agar dapat menjalankan aplikasi ```main```. <br>
- [x] Membuat model pada aplikasi ```main``` dengan nama ```Item``` dan memiliki atribut wajib sebagai berikut. <br>
    - ```name``` sebagai nama item dengan tipe ```CharField```. <br>
    - ```amount``` sebagai jumlah item dengan tipe ```IntegerField```. <br>
    - ```description``` sebagai deskripsi item dengan tipe ```TextField```. <br>
- [x] Membuat sebuah fungsi pada ```views.py``` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu. <br>
- [x] Membuat sebuah routing pada ```urls.py``` aplikasi main untuk memetakan fungsi yang telah dibuat pada ```views.py```. <br>
- [x] Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet. <br>
- [x] Membuat sebuah ```README.md``` yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut. <br>
    - Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial). <br>
    Jawab: <br>