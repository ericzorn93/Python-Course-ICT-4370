from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from pizzas.models import Pizza, Toppings
from . import forms


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
