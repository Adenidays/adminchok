from django.urls import path
from user.views import user_start_page, product_details

app_name = 'user'

urlpatterns = [
    path('', user_start_page, name='user_start_page'),
    path('<int:product_id>/', product_details, name='prodd')
]