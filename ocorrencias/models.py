from django.db import models
from django.utils import timezone

from usuarios.models import Usuario, Setor
from equipamentos.models import Computador

# Create your models here.
class OcorrenciaUsuario(models.Model):
    tipo_ocorrencia_choices = (
        ('1', 'INATIVAR USUÁRIO'),               
        ('2', 'TROCAR USUÁRIO DE SETOR'),
    )
    data = models.DateTimeField(default=timezone.now)
    tipo_ocorrencia = models.CharField(max_length=1, choices=tipo_ocorrencia_choices)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, blank=True)
    setor = models.ForeignKey(Setor, on_delete=models.DO_NOTHING, null=True, blank=True)
    observacoes = models.TextField(blank=True)

    
class OcorrenciaComputador(models.Model):
    tipo_ocorrencia_choices = (
        ('1', 'INATIVAR COMPUTADOR'),               
        ('2', 'TROCAR COMPUTADOR DE USUARIO'),
        ('3', 'RECOLHER COMPUTADOR PARA T.I.'),  
        ('4', 'ATUALIZAR SISTEMA OPERACIONAL'),
        ('5', 'ATUALIZAR SOFTWARE'),                     
    )
    data = models.DateTimeField(default=timezone.now)
    tipo_ocorrencia = models.CharField(max_length=1, choices=tipo_ocorrencia_choices)
    computador = models.ForeignKey(Computador, on_delete=models.DO_NOTHING, blank=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, blank=True, null=True,)
    setor = models.ForeignKey(Setor, on_delete=models.DO_NOTHING, null=True, blank=True)
    observacoes = models.TextField(blank=True)    