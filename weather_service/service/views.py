from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
import requests
from rest_framework.views import APIView

from .services import add_user_request_instance, create_weather_info

from .forms import CityForm


def get_index_page(request):
    """This function is render index-page"""

    api_key = "bd28fbbbdaa30d7ce0da8150e9ad3653"
    context = {}

    form = CityForm(request.POST)
    context["form"] = form

    if request.method == 'POST':
        if form.is_valid():
            try:
                city = form.cleaned_data['name']
                uri = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
                response_api = requests.get(uri).json()
                weather_info = create_weather_info(response_api)
                context["info"] = weather_info
                add_user_request_instance(city, weather_info)
                form = CityForm()
            except ObjectDoesNotExist:
                form.save()
                add_user_request_instance(city, weather_info)
                form = CityForm()
            except KeyError:
                context["error"] = "Город не найден"
                form = CityForm()

    form = CityForm()
    return render(request, "index.html", context)

        
