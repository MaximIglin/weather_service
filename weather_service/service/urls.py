from django.conf.urls import include
from django.urls import path
from .views  import get_index_page


urlpatterns = [
    path('', get_index_page, name="home"),
    path('', include('service.router'))
]