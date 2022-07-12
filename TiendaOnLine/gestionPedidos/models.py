from datetime import date
from unicodedata import name
from django.db import models

# Create your models here.Cli

class Client(models.Model):
    name = models.CharField(max_length=50,verbose_name='Nombre')
    surname = models.CharField(max_length=50,verbose_name='Apellido')
    email = models.EmailField(max_length=50,verbose_name='Email')
    phone = models.CharField(max_length=12,verbose_name='Telefono')
    address = models.CharField(max_length=50,verbose_name='Direccion')
    city = models.CharField(max_length=20,verbose_name  = 'Ciudad')
    country = models.CharField(blank=True,null=True,max_length=20,verbose_name='Pais')
    date_created = models.DateField(default=date.today,verbose_name='Fecha de creacion')
    date_updated = models.DateField(default=date.today,verbose_name='Fecha de actualizacion')
    
        
    def __str__(self):
        return ' id %s client %s  %s' % (self.id,self.name,self.surname)
class Product(models.Model):
    name = models.CharField(max_length=50,verbose_name='producto')
    description = models.CharField(max_length=50,verbose_name='Descripcion')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    date_created = models.DateField(default=date.today,verbose_name='Fecha de creacion')
    date_updated = models.DateField(default=date.today,verbose_name='Fecha de actualizacion')
    
    def __str__(self):
        return 'Produc: %s  %s  %s  %s %s %s' % (self.id, self.name, self.description, self.price, self.date_created, self.date_updated)
    
class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_created = models.DateField(default=date.today)
    date_updated = models.DateField(default=date.today)
    order_status = models.BooleanField(default=False)
    
    def __str__(self):
        return ' %s  %s  %s  %s  %s' % (self.id, self.client, self.date_created, self.date_updated, self.order_status)
        
    