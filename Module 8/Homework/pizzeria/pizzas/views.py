from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from pizzas.models import Pizza, Toppings
from . import forms
import datetime as dt
import time

from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

# Create your views here.

# Homepage View
def homepage(request):
    """Renders Homepage and Correct Django Forms, rendered from models"""

    # Pizza Names
    pizza_name_form = forms.FullNameForm(request.POST)
    if pizza_name_form.is_valid():
        pizza_name_form.save()

    # Topping Names
    toppings_form = forms.ToppingForm(request.POST)
    if toppings_form.is_valid():
        toppings_form.save()

    context = {
        "orders": "Please Enter Your Order Here:",
        "names": "Please Enter Your Full Name Here:",
        "intro_description": "We Hope Your Day is Full of cheese, sauce, and good times!",
        "pizza_name_form": pizza_name_form,
        "toppings_form": toppings_form,
    }

    return render(request, 'home/home.html', context)


# Orders View
def orders(request):
    all_toppings = Toppings.objects.all()
    all_names = Pizza.objects.all()
    context = {
        "all_toppings": all_toppings,
        "all_names": all_names,
    }

    return render(request, 'orders/orders.html', context)


# Menu View
def menu(request):
    """Displays Menu Items from DB to the UI"""

    context = {
        "menu_items": [
            "Custom Pizza Toppings",
            "Pepperoni",
            "Sausage",
            "Philly Cheese Steak",
            "Chicken Bacon Philly",
            "The Works",
            "Spicy Italian Pepperoni",
            "Hawaiian Chicken",
            "Spinach Carbonara",
            "Extra Veggies",
            "Cheese Pizza",
            "Original Breadsticks",
            "Cheesy Garlic Bread",
            "BBQ Wings",
            "Hot Wings",
            "Chocolate Brownie",
            "Chocolate Chip Cookie",
            "Sugar Cookie",
            "Coca-Cola",
            "Mountain Dew",
            "Fanta",
            "Dasani Water"
        ]
    }
    return render(request, 'menu/menu.html', context)



# About View
def about(request):
    """UI View of the About Page"""
    context = {}
    return render(request, 'about/about.html', context)



# Create User View
def create(request):
    """Create User Form"""

    if request.method == "POST":
        user_creation_form = UserCreationForm(request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            context = {"form": user_creation_form}
            return redirect('login_user/login_user.html')
    else:
        user_creation_form = UserCreationForm()
        context = {"form": user_creation_form}
        return render(request, 'create_user/create_user.html', context)


# Login User
def login(request):
    """Login User Form"""

    if request.method == "POST":
        user_login_form = AuthenticationForm(request.POST)
        if user_login_form.is_valid():
            username = user_login_form.cleaned_data.get('username')
            password = user_login_form.cleaned_data.get('password')
            authenticate(username=username, password=password)
            return redirect("home/home.html")
    else:
        user_login_form = AuthenticationForm()
        context = {"user_login_form": user_login_form}
        return render(request, 'login_user/login_user.html', context)


# Shows Profile
def Profile(request):
    """Displays Profile To The User"""
    session_key = request.session.session_key
    session = Session.objects.get(session_key=session_key)
    uid = session.get_decoded().get('_auth_user_id')
    user = User.objects.get(pk=uid)

    context = {
        "hello": "Hello",
        "current_user": user,
        "current_date": dt.datetime.now().strftime("%m/%d/%Y"),
        "current_time": dt.datetime.now()
    }

    return render(request, 'accounts/profile/profile.html', context)


# Defines Order Information
def order_info(request):
    context = {}
    return render(request, 'order_info.html', context)