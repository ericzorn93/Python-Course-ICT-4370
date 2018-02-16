from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.Home),
    url(r'bonds', views.Bonds),
    url(r'investors', views.Investors)
]