from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.homepage),
    url(r'orders/', views.orders),
    url(r'menu/', views.menu),
    url(r'about/', views.about),
]
