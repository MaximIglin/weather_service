from django.db.models import fields
from django.forms import ModelForm
from django.forms import widgets


from .models import City


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            "name": widgets.Input(attrs={
                'class': 'form-control'
            })}
        labels = {
            'name':""
        }
