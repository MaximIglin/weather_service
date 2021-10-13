import datetime
import pytz
import requests

from django.db.models.query import QuerySet

from .models import City, UserRequest


def get_all_cities() -> QuerySet:
    """This function is return all cities in database"""
    cities = City.objects.all()
    return cities


def get_all_users_requests() -> QuerySet:
    """This function is return queryset with all users requests"""
    users_requests = UserRequest.objects.all()
    return users_requests


def get_weather(city: str) -> dict:
    """This function is return weather from API"""
    api_key = "bd28fbbbdaa30d7ce0da8150e9ad3653"
    uri = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response_api = requests.get(uri).json()
    return response_api


def create_weather_info(response_api: dict) -> dict:
    """This function is collect dictionary with weather information"""
    weather_info = {
        "tempreture": round((response_api["main"]["temp"]-273), 3),
        "wind": response_api["wind"]["speed"],
        "city": response_api["name"],
        "icon": f'https://api.openweathermap.org/img/w/{response_api["weather"][0]["icon"]}.png',
        "humidity": response_api["main"]["humidity"]
    }
    return weather_info


def add_user_request_instance(city: str, weather_info: dict):
    user_request = UserRequest()
    user_request.city = City.objects.get(name=city)
    user_request.weather = f'Температура:{weather_info["tempreture"]}. Ветер: {weather_info["wind"]}м/с. Влажность:{weather_info["humidity"]}%'
    user_request.time = datetime.datetime.now().replace(
        tzinfo=pytz.timezone("UTC")).astimezone(tz=pytz.timezone("Europe/Moscow"))
    user_request.save()
    return user_request
