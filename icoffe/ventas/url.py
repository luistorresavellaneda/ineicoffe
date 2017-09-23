from django.conf.urls import url
from .views import demovista, demo_orden, carta_productos, CartaProductos, ProductoLista

urlpatterns = [
    url(r'^$', demovista),
    url(r'^demorden/$', demo_orden),
    url(r'^carta/$', CartaProductos.as_view()),
    url(r'^lista/(?P<categoria>[1-9]?/?)$', ProductoLista.as_view()),
]