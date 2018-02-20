from django.db import models


# Create your models here.
class Pizza(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)


class Toppings(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
