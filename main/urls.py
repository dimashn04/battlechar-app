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