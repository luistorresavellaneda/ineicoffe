from django.contrib import admin
from .models import Contacto
# Register your models here.

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('id', 'primer_nombre', 'apellido_paterno', 'asunto')
    readonly_fields = ('tipo_sugerencia', 'primer_nombre', 'segundo_nombre', 'apellido_paterno', 'apellido_materno', 'asunto', 'contenido')

    def has_add_permission(self, request):
        return False