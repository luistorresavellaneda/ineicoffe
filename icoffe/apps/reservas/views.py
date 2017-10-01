from django.shortcuts import render
from django.views.generic import FormView, DetailView
from django.urls import reverse
from .models import Reserva
from .forms import ReservaForm
# Create your views here.

class ReservaView(FormView):
    template_name = 'reservas/reserva.html'
    form_class = ReservaForm

    def get_success_url(self):
        return reverse('reserva:detalle', {"pk":self.detalle_reserva})

class DetalleReservaView(DetailView):
    model = Reserva
    template_name = 'reservas/detalle_reserva.html'
