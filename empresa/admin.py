from django.contrib import admin

from empresa.models import Empresa, Setor

# Register your models here.
admin.site.register(Empresa)
admin.site.register(Setor)