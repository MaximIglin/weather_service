from django.urls import path
from .api import CityApi, UserRequestApi

urlpatterns = [
    path('api/city', CityApi.as_view()),
    path('api/city_weather', UserRequestApi.as_view())
]