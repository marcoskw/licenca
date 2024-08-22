from django.db import models
from empresa.models import Setor

# Create your models here.
class Usuario(models.Model):
    status_choices = (
        ('ATV', 'Ativo'),
        ('INT', 'Inativo'),
        ('AFT', 'Afastado'),
    )
    nome_usuario = models.CharField(max_length=150)
    setor = models.ForeignKey(Setor, on_delete=models.DO_NOTHING)
    email = models.EmailField(null=True, blank=True)
    status = models.CharField(max_length=3, choices=status_choices, default=('ATV'))
