from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
from main.views import register 
from main.views import logout_user
from main.views import edit_product, get_product_json, add_product_ajax
from main.views import increase_product, decrease_product, delete_product, create_product_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('increase_product/<int:id>', increase_product, name='increase_product'),
    path('decrease_product/<int:id>', decrease_product, name='decrease_product'),
    path('delete_product/<int:id>', delete_product, name='delete_product'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]