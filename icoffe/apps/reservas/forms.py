from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    dni = forms.CharField(max_length=8, min_length=8, required=True)
    ambiente = forms.CharField(max_length=10)

    class Meta:
        model = Reserva
        fields = ('nombres', 'apellidos', 'dni')