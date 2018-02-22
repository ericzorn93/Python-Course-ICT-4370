from django.contrib import admin
from .models import Pizza, Toppings

# Register your models here.


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    pass


@admin.register(Toppings)
class ToppingsAdmin(admin.ModelAdmin):
    pass