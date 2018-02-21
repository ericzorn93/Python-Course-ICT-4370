from django import forms
from .models import Pizza, Toppings


class FullName(forms.Form):
    # name = forms.CharField(label='Please Enter Your Full Name', max_length=100)

    class Meta:
        model = Pizza
        fields = ('name')


class PizzaType(forms.Form):
    name = forms.CharField(label='Please Enter Your Full Name', max_length=100)
    topping = forms.CharField(label='Please Enter the kind of pizza of topping you would like', max_length=200)
