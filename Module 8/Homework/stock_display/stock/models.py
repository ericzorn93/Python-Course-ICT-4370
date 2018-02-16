from django.db import models


# Create your models here.
class Stock(models.Model):
    id = models.IntegerField(primary_key=True)
    symbol = models.CharField(max_length=10)
    shares = models.IntegerField()
    purchase_price = models.DecimalField(decimal_places=1, max_digits=20)
    current_price = models.DecimalField(decimal_places=1, max_digits=20)
    purchase_date = models.CharField(max_length=9)

    def __str__(self):
        return self.symbol + " - " + str(self.shares)


class Bond(models.Model):
    id = models.IntegerField(primary_key=True)
    symbol = models.CharField(max_length=10)
    shares = models.IntegerField()
    coupon = models.DecimalField(decimal_places=1, max_digits=20)
    yield_amt = models.DecimalField(decimal_places=1, max_digits=9)

    def __str__(self):
        return self.symbol + " - " + str(self.shares)
