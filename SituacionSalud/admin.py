from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(EstablecimientoSalud)
admin.site.register(Zona)
admin.site.register(NivelEconomico)
admin.site.register(Seguro)
admin.site.register(Cie)
admin.site.register(Distrito)
admin.site.register(Sexo)
admin.site.register(SituacionSalud)
admin.site.register(TipoGrupoEnf2)
admin.site.register(Gruponenf2)
admin.site.register(RangoEdad)
admin.site.register(Poblacion)


#class CieAdmin(admin.ModelAdmin):
 #   def get_queryset(self, request):
  #      queryset = Cie.objects.all().order_by('codigo')
   #     return queryset


#admin.site.register(Cie, CieAdmin)
