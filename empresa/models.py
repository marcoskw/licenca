from django.db import models

# Create your models here.
class Empresa(models.Model):
    nome_empresa = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=14)
    logo = models.FileField(upload_to='logo')
    endereco = models.CharField(max_length=150)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=255, blank=True)
    bairro = models.CharField(max_length=75)
    cidade = models.CharField(max_length=75)
    uf = models.CharField(max_length=2)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=254)
    site = models.URLField()

    def __str__(self):
        return self.nome_empresa
    
class Setor(models.Model):
    empresa = models.ForeignKey(Empresa, null=True, on_delete=models.DO_NOTHING)
    nome_setor = models.CharField(max_length=150)
