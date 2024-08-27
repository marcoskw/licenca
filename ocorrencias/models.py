from django.db import models
from usuarios.models import Usuario, Setor

# Create your models here.
class OcorrenciaUsuario(models.Model):
    tipo_ocorrencia_choices = (
        ('INATIVAR USUÁRIO', '1'),               
        ('TROCAR USUÁRIO DE SETOR', '2'),
    )


"""
class OcorrenciaComputador(models.Model):
    pass
"""