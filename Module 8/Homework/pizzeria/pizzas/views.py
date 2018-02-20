from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    context = {
        "orders": "Please Enter Your Order Here:",
        "names": "Please Enter Your Full Name Here:",
        "intro_description": "We Hope Your Day is Full of cheese, sauce, and good times!",
    }
    return render(request, 'home/home.html', context)


def orders(request):
    context = {}
    return render(request, 'orders/orders.html', context)


def menu(request):
    context = {}
    return render(request, 'menu/menu.html', context)


def about(request):
    context = {}
    return render(request, 'about/about.html', context)
