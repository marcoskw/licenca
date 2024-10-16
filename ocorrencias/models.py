from django.db import models
from django.utils import timezone

from empresa.models import Operador, Setor
from equipamentos.models import Computador

# Create your models here.
class OcorrenciaOperador(models.Model):
    tipo_ocorrencia_choices = (
        ('1', 'INATIVAR OPERADOR'),               
        ('2', 'TROCAR OPERADOR DE SETOR'),
    )
    data = models.DateTimeField(default=timezone.now)
    tipo_ocorrencia = models.CharField(max_length=1, choices=tipo_ocorrencia_choices)
    operador = models.ForeignKey(Operador, on_delete=models.DO_NOTHING, blank=True)
    setor = models.ForeignKey(Setor, on_delete=models.DO_NOTHING, null=True, blank=True)
    observacoes = models.TextField(blank=True)

    
class OcorrenciaComputador(models.Model):
    tipo_ocorrencia_choices = (
        ('1', 'INATIVAR COMPUTADOR'),               
        ('2', 'TROCAR OPERADOR DE COMPUTADOR'),
        ('3', 'ADICIONAR NOVO SOFTWARE EM UM COMPUTADOR'),  
        ('4', 'ATUALIZAR NOME DO COMPUTADOR'),                 
    )
    data = models.DateTimeField(default=timezone.now)
    tipo_ocorrencia = models.CharField(max_length=1, choices=tipo_ocorrencia_choices)
    computador = models.ForeignKey(Computador, on_delete=models.DO_NOTHING, blank=True)
    operador = models.ForeignKey(Operador, on_delete=models.DO_NOTHING, blank=True, null=True)
    setor = models.ForeignKey(Setor, on_delete=models.DO_NOTHING, null=True, blank=True)
    observacoes = models.TextField(blank=True)    
    