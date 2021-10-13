from django.db import models


class City(models.Model):
    """This model for all cities in our app"""
    name = models.CharField("Название города", max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        db_table = "city"
        verbose_name = "Города"


class UserRequest(models.Model):
    """This model is describe all user's requests in our service"""
    city = models.ForeignKey(City, verbose_name="Город",
                             on_delete=models.CASCADE, related_name="users_requests")
    weather = models.CharField("Погода", max_length=150)
    time = models.DateTimeField(verbose_name="Время запроса")

    def __str__(self):
        return f"{self.city}: {self.time}"

    class Meta:
        ordering = ['id']
        db_table = "UsersRequests"
        verbose_name = "Запросы пользователей"
