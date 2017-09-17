from django.contrib import admin
from .models import Ambiente, Mesa
# Register your models here.

class MesaInline(admin.TabularInline):
    model = Mesa
    extra = 0

@admin.register(Ambiente)
class AmbienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tipo', 'descripcion_corta')
    list_editable = ('tipo', )
    list_display_links = ('id', 'nombre', )
    list_filter = ('tipo', )
    search_fields = ('nombre', )
    inlines = [MesaInline]  #agregar mesas junto con el ambiente

    def descripcion_corta(self, modelo):
        if modelo.descripcion == '':
            return '---'
        else:
            return modelo.descripcion[:20]

    descripcion_corta.short_description = 'DESCRIPCION'

'''
@admin.register(Mesa)
class MesaAdmin(admin.ModelAdmin):
    pass
'''