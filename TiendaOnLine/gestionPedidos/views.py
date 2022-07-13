from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Product

# Create your views here.
def busqueda_productos(request):
    
    return render(request, 'busqueda_productos.html')


def buscar(request):
    
    if request.GET["prd"]:
        
      
      articulo=request.GET["prd"]
      articulos = Product.objects.filter(name__icontains= articulo)
  
      return render(request,'resultado.html',{"Producto":articulos,"query":articulo})
       
    else:
        mensaje= "No se ha introducido ningun articulo"
    
    return HttpResponse(mensaje)
    
    