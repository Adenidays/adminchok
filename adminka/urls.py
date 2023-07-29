from django.urls import path
from adminka.views import add_product, start_page, edit_product

app_name = 'adminka'

urlpatterns = [
    path('', start_page, name='start_page'),
    path('edit_product/<int:product_id>/', edit_product, name='name_product'),
    path('add_product/', add_product, name='add_product'),
]