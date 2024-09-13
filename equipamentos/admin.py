from django.contrib import admin

from equipamentos.models import TipoEquipamento, Marca, Software, Computador
from equipamentos.models import SistemaOperacional, Equipamento, SoftwareComputador

class SoftwareComputadorAdmin(admin.ModelAdmin):
    list_display = (
        'computador',
        'software',
        'serial',
        'numero_nota_software',
        'nf_software'
    )

# Register your models here.
admin.site.register(TipoEquipamento)
admin.site.register(SoftwareComputador, SoftwareComputadorAdmin)
admin.site.register(Marca)
admin.site.register(Software)
admin.site.register(SistemaOperacional)
admin.site.register(Equipamento)
admin.site.register(Computador)
