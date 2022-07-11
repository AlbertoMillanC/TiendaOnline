from datetime import date
from unicodedata import name
from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    date_created = models.DateField(default=date.today)
    date_updated = models.DateField(default=date.today)

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateField(default=date.today)
    date_updated = models.DateField(default=date.today)
    
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateField(default=date.today)
    date_updated = models.DateField(default=date.today)
    order_status = models.BooleanField(default=False)
    
    
    