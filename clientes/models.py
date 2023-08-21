"""Model do cadastro dos clientes."""
from django.db import models

class ClientesModel(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, blank=False)
    data_nascimento = models.DateField(blank=False)
    telefone = models.CharField(max_length=20)
    ultimo_atendimento = models.DateField(blank=True, null=True)
    ativo = models.BooleanField(null=False, blank=False, default=True)
    
