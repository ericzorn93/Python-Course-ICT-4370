from django.conf.urls import url
from django.contrib import admin
from . import views
from . models import Pizza, Toppings
from django.contrib.auth.views import login
from django.views.generic import DetailView, ListView

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
    url(r'^orders/(?P<pk>\d+)/$', DetailView.as_view(model=Toppings, template_name="orders/specific_order.html")),
]
