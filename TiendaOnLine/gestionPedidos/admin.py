from re import A
from django.contrib import admin
from gestionPedidos.models import Client,Product,Order

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id','name','surname','email','phone','address','city','country','date_created','date_updated')
    search_fields = ('id','name','surname','email','phone','address','city','country','date_created','date_updated')
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','description','price','date_created','date_updated')
    search_fields = ('id','name','description','price','date_created','date_updated')
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','client','date_created','date_updated','order_status')
    search_fields = ('id','client','date_created','date_updated','order_status')


admin.site.register(Client,ClientAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)




