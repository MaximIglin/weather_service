from rest_framework.serializers import ModelSerializer, StringRelatedField

from .models import UserRequest, City


class CitySerializer(ModelSerializer):
    """Serializer for city model"""
    users_requests = StringRelatedField(many=True, read_only=True)

    class Meta:
        model = City
        fields = ["id", "name", "users_requests"]


class UsersRequestsSerializer(ModelSerializer):
    """Serializer for users requests model"""
    class Meta:
        model = UserRequest
        fields = ["id", "city", "weather", "time"]
    def to_representation(self, instance):
        rep = super(UsersRequestsSerializer, self).to_representation(instance)
        rep['city'] = instance.city.name
        return rep   
