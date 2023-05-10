from django.db import models
from datetime import date


# Create your models here.


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField(default=date.today())
    quantity = models.IntegerField()
    customer_id = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
