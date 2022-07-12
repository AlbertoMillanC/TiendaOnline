from django.shortcuts import render

# Create your views here.
def busqueda_productos(request):
    return render(request, 'busqueda_productos.html')
    