from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

from .serializers import CitySerializer, UsersRequestsSerializer
from .services import (get_all_cities,
                       get_all_users_requests,
                       get_weather, create_weather_info, add_user_request_instance)
from .models import City


class CityApi(APIView):
    """This api for all cities"""

    def get(self, request):
        queryset = get_all_cities()
        serializer = CitySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRequestApi(APIView):
    """This api for get or add city"""

    def get(self, request):
        queryset = get_all_users_requests()
        serializer = UsersRequestsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        city = self.request.data["city"]
        try:
            response_api = get_weather(city)
            weather_info = create_weather_info(response_api)
            users_request = add_user_request_instance(city, weather_info)
            serializer = UsersRequestsSerializer(users_request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ObjectDoesNotExist:
            new_city = City.objects.create(name=city)
            new_city.save()
            users_request = add_user_request_instance(city, weather_info)
            serializer = UsersRequestsSerializer(users_request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)   
        except KeyError:
            return Response({"ERROR":"Город не найден"}, status=status.HTTP_400_BAD_REQUEST)             
    
