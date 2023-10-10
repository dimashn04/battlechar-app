from django.urls import path
from main.views import (add_operator_ajax, delete_operator_ajax, edit_operator, get_operator_json, show_html, show_json, show_json_by_id, show_main, create_operator, 
                        show_xml, show_xml_by_id, register, login_user, logout_user,
                        add_primary_ammo_amount, add_secondary_ammo_amount, dec_primary_ammo_amount,
                        dec_secondary_ammo_amount, remove_operator)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-operator', create_operator, name='create_operator'),
    path('add-primary-ammo-amount/<int:operator_id>/', add_primary_ammo_amount, name='add_primary_ammo_amount'),
    path('add-secondary-ammo-amount/<int:operator_id>/', add_secondary_ammo_amount, name='add_secondary_ammo_amount'),
    path('dec-primary-ammo-amount/<int:operator_id>/', dec_primary_ammo_amount, name='dec_primary_ammo_amount'),
    path('dec-secondary-ammo-amount/<int:operator_id>/', dec_secondary_ammo_amount, name='dec_secondary_ammo_amount'),
    path('remove-operator/<int:operator_id>/', remove_operator, name='remove_operator'),
    path('xml/', show_xml, name='show_xml'),
    path('html/', show_html, name='show_html'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('get-operator/', get_operator_json, name='get_operator_json'),
    path('create-operator-ajax/', add_operator_ajax, name='add_operator_ajax'),
    path('edit-operator/<int:id>', edit_operator, name='edit_operator'),
    path('delete-operator-ajax/<int:operator_id>/', delete_operator_ajax, name='delete_operator_ajax'),
]