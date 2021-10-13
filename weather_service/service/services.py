from .models import City, UserRequest
import datetime
import pytz


def get_all_cities():
    """This function is return all cities in database"""
    cities = City.objects.all()
    return cities


def create_weather_info(response_api):
    weather_info = {
        "tempreture": round((response_api["main"]["temp"]-273), 3),
        "wind": response_api["wind"]["speed"],
        "city": response_api["name"],
        "icon": f'https://api.openweathermap.org/img/w/{response_api["weather"][0]["icon"]}.png',
        "humidity": response_api["main"]["humidity"]
    }
    return weather_info


def add_user_request_instance(city, weather_info):
    user_request = UserRequest()
    user_request.city = City.objects.get(name=city)
    user_request.weather = f'Температура:{weather_info["tempreture"]}. Ветер: {weather_info["wind"]}м/с. Влажность:{weather_info["humidity"]}%'
    user_request.time = datetime.datetime.now().replace(tzinfo=pytz.timezone("UTC")).astimezone(tz=pytz.timezone("Europe/Moscow"))
    user_request.save()
