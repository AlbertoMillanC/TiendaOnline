from multiprocessing.connection import Client
from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Client, Product, Order
from gestionPedidos.forms import contactoforms

def busqueda_productos(request):

    return render(request, 'busqueda_productos.html')


def buscar(request):

    if request.GET["prd"]:

      articulo = request.GET["prd"]

      if len(articulo) > 20:

         mensaje = "El articulo no puede tener mas de 20 caracteres"
      else:

         articulos = Product.objects.filter(name=articulo)

         return render(request, 'resultado.html', {"Product": articulos, "query": articulo})

    else:
        mensaje = "No se ha introducido ningun articulo"

    return HttpResponse(mensaje)


""""def contacto(request):

    if request.method == 'POST':

        return render(request, 'gracias.html', {'mensaje': 'Mensaje enviado correctamente'})

    return render(request, 'contacto.html')"""

def contacto(request):
    
    if request.method == 'POST':
        form = contactoforms(request.POST)
        
        if form.is_valid():
            
            infForm = form.cleaned_data
            
            send_mail(infForm['asunto'], infForm['mensaje'], infForm['email'], 
            infForm.get('email', ''),['yamarteatro@gmail.com'],)
            
            return render(request, 'gracias.html')
    else:
        form = contactoforms()
        
    return render(request, 'formulario_contacto.html', {'form': form})
    
    
    
            
            
