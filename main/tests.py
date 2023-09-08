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