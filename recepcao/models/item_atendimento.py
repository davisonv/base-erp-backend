"""Model dos itens do atendimento"""
from django.db import models


class ItemAtendimentoModel(models.Model):
    id_item_atendimento = models.AutoField(primary_key=True)
    id_item_servico = models.ForeignKey("servicos.ServicosModel", on_delete=models.DO_NOTHING)
    id_atendimento =  models.ForeignKey("recepcao.AtendimentoModel", on_delete=models.DO_NOTHING)