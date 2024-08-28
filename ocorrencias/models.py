from django.db import models
from usuarios.models import Usuario, Setor

# Create your models here.
class OcorrenciaUsuario(models.Model):
    tipo_ocorrencia_choices = (
        ('1', 'INATIVAR USUÁRIO'),               
        ('2', 'TROCAR USUÁRIO DE SETOR'),
    )
    tipo_ocorrencia = models.CharField(max_length=1, choices=tipo_ocorrencia_choices)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, blank=True)
    setor = models.ForeignKey(Setor, on_delete=models.DO_NOTHING, null=True, blank=True)
    observacoes = models.TextField(blank=True)

    
"""
class OcorrenciaComputador(models.Model):
    pass
"""