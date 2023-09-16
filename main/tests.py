from django.test import TestCase, Client

class mainTest(TestCase):
    # Uji apakah halaman utama eksis
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    # Uji apakah halaman utama menggunakan template main.html
    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    # Uji apakah header yang digunakan sesuai
    def test_table_has_correct_headers(self):
        response = Client().get('')
        self.assertContains(response, '<th>Name</th>', html=True)
        self.assertContains(response, '<th>Unit</th>', html=True)
        self.assertContains(response, '<th>Primary weapon</th>', html=True)
        self.assertContains(response, '<th>Secondary weapon</th>', html=True)
        self.assertContains(response, '<th>Primary weapon ammo</th>', html=True)
        self.assertContains(response, '<th>Secondary weapon ammo</th>', html=True)
        self.assertContains(response, '<th>Armor</th>', html=True)
        self.assertContains(response, '<th>Speed</th>', html=True)
        self.assertContains(response, '<th>Description</th>', html=True)
        self.assertContains(response, '<th>Price</th>', html=True)

    # Uji apakah data yang ditampilkan sesuai
    def test_table_row_contains_data(self):
        data = {
            'creator': 'Dimas Herjunodarpito Notoprayitno',
            'student_id': '2206081282',
            'class': 'PBP C'
        }
        response = Client().get('')
        for value in data.values():
            self.assertContains(response, f'<p>{value}</p>', html=True)