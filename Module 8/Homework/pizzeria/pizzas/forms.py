from django.forms import ModelForm
from .models import Pizza, Toppings
from django.contrib.auth.models import User
from django import forms


class FullNameForm(ModelForm):
    class Meta:
        model = Pizza
        fields = ['name']


class ToppingForm(ModelForm):
    class Meta:
        model = Toppings
        fields = ['pizza', 'name']


# Create User Signup Form
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
