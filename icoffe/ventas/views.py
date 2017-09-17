from django.shortcuts import render
from django.http import HttpResponse
from productos.models import Producto

# Create your views here.

#vista de funcion basica
def demovista(request):
    return HttpResponse('Prueba')

#vista de funcion con template
def demo_orden(request):
    template = 'demo.html'
    context = {
        'titulo': 'titulo de la pagina',
        'texto' : 'aaaaaaaaaaa',
    }
    return render(request, template, context)

def carta_productos(request):
    template = 'carta_productos.html'
    context = {
        'titulo': 'CARTA DEL DIA',
        'productos' : Producto.objects.all(),
    }
    return render(request, template, context)