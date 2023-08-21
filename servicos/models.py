from django.db import models

class ServicosModel(models.Model):
  id_servico = models.AutoField(primary_key=True)
  nome_servico = models.CharField(max_length=50, blank=False, null=False)
  descricao_servico = models.CharField(max_length=100, blank=True, null=True)
  valor_servico = models.FloatField(blank=False, null=False, default=0.00)
  ativo = models.BooleanField(null=False, blank=False, default=True)
  
