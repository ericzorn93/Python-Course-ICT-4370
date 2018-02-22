from django import forms
from django.forms import ModelForm
from .models import Pizza, Toppings


class FullNameForm(ModelForm):
    class Meta:
        model = Pizza
        fields = ['name']


class ToppingForm(ModelForm):
    class Meta:
        model = Toppings
        fields = ['pizza', 'name']
