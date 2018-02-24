from django.conf.urls import url
from django.contrib import admin
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'home/', views.homepage),
    url(r'orders/', views.orders),
    url(r'menu/', views.menu),
    url(r'about/', views.about),
    url(r'admin/', admin.site.urls),
    url(r'^$', login),
    url(r'create/', views.create),
    url(r'accounts/profile', views.Profile),
    url(r'order_info/', views.order_info),
]
