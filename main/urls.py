from django.urls import path
from main.views import (show_html, show_json, show_json_by_id, show_main, create_operator, 
                        show_xml, show_xml_by_id, register, login_user, logout_user,
                        add_primary_ammo_amount, add_secondary_ammo_amount, dec_primary_ammo_amount,
                        dec_secondary_ammo_amount, remove_operator)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-operator', create_operator, name='create_operator'),
    path('add_primary_ammo_amount/<int:operator_id>/', add_primary_ammo_amount, name='add_primary_ammo_amount'),
    path('add_secondary_ammo_amount/<int:operator_id>/', add_secondary_ammo_amount, name='add_secondary_ammo_amount'),
    path('dec_primary_ammo_amount/<int:operator_id>/', dec_primary_ammo_amount, name='dec_primary_ammo_amount'),
    path('dec_secondary_ammo_amount/<int:operator_id>/', dec_secondary_ammo_amount, name='dec_secondary_ammo_amount'),
    path('remove_operator/<int:operator_id>/', remove_operator, name='remove_operator'),
    path('xml/', show_xml, name='show_xml'),
    path('html/', show_html, name='show_html'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]