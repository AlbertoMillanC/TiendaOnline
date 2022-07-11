from datetime import date
from unicodedata import name
from django.db import models

# Create your models here.Cli

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
    
    def __str__(self):
        return 'the client is %s the surname is %s the email is %s the phone is %s the address is %s the city is %s the country is %s the date created is %s the date updated is %s' % (self.name, self.surname, self.email, self.phone, self.address, self.city, self.country, self.date_created, self.date_updated)

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateField(default=date.today)
    date_updated = models.DateField(default=date.today)
    
    def __str__(self):
        return 'the product is %s the description is %s the price is %s the date created is %s the date updated is %s' % (self.name, self.description, self.price, self.date_created, self.date_updated)
    
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateField(default=date.today)
    date_updated = models.DateField(default=date.today)
    order_status = models.BooleanField(default=False)
    
    def __str__(self):
        return 'the order is %s the client is %s the date created is %s the date updated is %s the order status is %s' % (self.id, self.client, self.date_created, self.date_updated, self.order_status)
        
    