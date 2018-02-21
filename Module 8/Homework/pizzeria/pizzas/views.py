from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . import models
from . import forms


# Create your views here.

# Homepage View
def homepage(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = forms.FullName(request.POST)
        form_second = forms.PizzaType(request.POST)
        # check whether it's valid:
        if form_second.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            task = form_second.save(commit=False)
            task.usern = request.user
            task.save()
            return HttpResponseRedirect('/orders/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.FullName()
        form_second = forms.PizzaType()

    context = {
        "orders": "Please Enter Your Order Here:",
        "names": "Please Enter Your Full Name Here:",
        "intro_description": "We Hope Your Day is Full of cheese, sauce, and good times!",
        "form": form,
        "form_second": form_second
    }

    return render(request, 'home/home.html', context)


# Orders View
def orders(request):
    context = {}
    return render(request, 'orders/orders.html', context)


# Menu View
def menu(request):
    context = {}
    return render(request, 'menu/menu.html', context)


# About View
def about(request):
    context = {}
    return render(request, 'about/about.html', context)
