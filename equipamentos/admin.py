from django.contrib import admin

from equipamentos.models import TipoEquipamento, Marca, Software, Computador
from equipamentos.models import LicencaSoftware, SistemaOperacional, Equipamento


# Register your models here.
admin.site.register(TipoEquipamento)
admin.site.register(Marca)
admin.site.register(Software)
admin.site.register(LicencaSoftware)
admin.site.register(SistemaOperacional)
admin.site.register(Equipamento)
admin.site.register(Computador)
