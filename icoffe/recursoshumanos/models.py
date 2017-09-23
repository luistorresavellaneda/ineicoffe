from django.db import models

# Create your models here.
class Personal(models.Model):
    CARGO_LISTA = {
        (1, 'Mozos'),
        (2, 'Cajero'),
    }
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.PositiveIntegerField(choices=CARGO_LISTA)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    fecha_modificado = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Personal"
        verbose_name_plural = "Personal"