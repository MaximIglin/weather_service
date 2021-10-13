from django.http import response
from django.test import TestCase
from .models import City, UserRequest
import pytz
import datetime

from .services import get_weather, get_all_cities, get_all_users_requests, create_weather_info


class TestServices(TestCase):

    def setUp(self) -> None:
        city_1 = City.objects.create(name="Moscow")
        city_2 = City.objects.create(name="London")
        city_1.save()
        city_2.save()

        response_api_1 = get_weather("Moscow")
        response_api_2 = get_weather("London")
        weather_info_1 = create_weather_info(response_api_1)
        weather_info_2 = create_weather_info(response_api_2)

        user_request_1 = UserRequest()
        user_request_1.city = City.objects.get(name=city_1.name)
        user_request_1.weather = f'Температура:{weather_info_1["tempreture"]}. Ветер: {weather_info_1["wind"]}м/с. Влажность:{weather_info_1["humidity"]}%'
        user_request_1.time = datetime.datetime.now().replace(
            tzinfo=pytz.timezone("UTC")).astimezone(tz=pytz.timezone("Europe/Moscow"))
        user_request_1.save()

        user_request_2 = UserRequest()
        user_request_2.city = City.objects.get(name=city_2.name)
        user_request_2.weather = f'Температура:{weather_info_2["tempreture"]}. Ветер: {weather_info_2["wind"]}м/с. Влажность:{weather_info_2["humidity"]}%'
        user_request_2.time = datetime.datetime.now().replace(
            tzinfo=pytz.timezone("UTC")).astimezone(tz=pytz.timezone("Europe/Moscow"))
        user_request_2.save()

    def test_get_all_cities(self):
        cities = City.objects.all()
        cities_from_func = get_all_cities()
        self.assertQuerysetEqual(cities, cities_from_func)

    def test_get_all_user_requests(self):
        us_requests = UserRequest.objects.all()
        us_requests_from_func = get_all_users_requests()
        self.assertQuerysetEqual(us_requests, us_requests_from_func)

    def test_get_weather(self):
        city = "Moscow"
        response = get_weather(city)
        self.assertEqual(city, response["name"]) 

    def test_create_weather_info(self):
        city = "Moscow"
        response = get_weather(city)
        weather_info = create_weather_info(response)
        correct_keys = ["tempreture", "wind", "city", "icon", "humidity"]
        for key in correct_keys:
            self.assertIn(key, weather_info.keys())
