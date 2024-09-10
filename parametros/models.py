from django.db import models
from empresa.models import Empresa

# Create your models here.
class ParametrosEmpresa(models.Model):
    empresa = models.ForeignKey(Empresa, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.empresa.nome_empresa