from multiprocessing.connection import Client
from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Client,Product,Order

# Create your views here.
def busqueda_productos(request):
    
    return render(request, 'busqueda_productos.html')


def buscar(request):
    
    if request.GET["prd"]:
        
      
      articulo=request.GET["prd"]
      
      if len(articulo)>20:
         
         mensaje="El articulo no puede tener mas de 20 caracteres"
      else:
      
         articulos = Product.objects.filter(name= articulo)
  
         return render(request,'resultado.html',{"Product":articulos,"query":articulo})
       
    else:
        mensaje= "No se ha introducido ningun articulo"
    
    return HttpResponse(mensaje)
    
    