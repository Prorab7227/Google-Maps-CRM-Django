# urls.py
from django.urls import path

from .views import *

urlpatterns = [
    # Basic
    path('', index, name='index'),
    path('list/<str:category_name>/', categoty_list_place, name='categoty_list_place'),
    path('info/<str:name_slug>/', place_full_info, name='place_full_info'),
]