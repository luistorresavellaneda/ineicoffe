from django.shortcuts import render
from django.http import HttpResponse
from productos.models import Producto
from django.views.generic import TemplateView, ListView
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


class CartaProductos(TemplateView):
    template_name = 'carta_productos.html'

    def get_context_data(self, **kwargs):
        context = super(CartaProductos, self).get_context_data(**kwargs)
        context.update({
            'titulo': 'CARTA DEL DIA',
            'productos': Producto.objects.all(),
        })

        return context

class ProductoLista(ListView):
    template_name = 'productos_lista.html'
    model = Producto
    context_object_name = 'productos'

    def get_queryset(self):
        categoria = self.kwargs.get('categoria')
        if(categoria is None):
            return Producto.objects.all()
        else:
            return Producto.objects.all(categoria_id=categoria)

    def get_context_data(self, **kwargs):
        context = super(ProductoLista, self).get_context_data(**kwargs)
        context.update({
            'titulo': 'CARTA DEL DIA',
        })

        return context