from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homepage(request):
    context = {"hello": 1}
    return render(request, 'home/home.html', context)


def aboutpage(request):
    return HttpResponse("About Page")
