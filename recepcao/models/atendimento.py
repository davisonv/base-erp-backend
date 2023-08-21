"""Model de atendimento"""
from django.db import models

import uuid

class AtendimentoModel(models.Model):
    
    STATUS_CHOICES = (
        ("A", "Aberto"),
        ("F", "Finalizado"),
        ("C", "Cancelado"),
    )
    
    id_atendimento = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # atendimento_servicos = models.ForeignKey("recepcao.ItemAtendimentoModel", on_delete=models.DO_NOTHING)
    valor = models.FloatField(blank=False, null=False, default=0.00)
    valor_desconto = models.FloatField(blank=False, null=False, default=0.00)
    valor_adicional = models.FloatField(blank=False, null=False, default=0.00)
    atendente = models.ForeignKey("usuarios.User", on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey("clientes.ClientesModel", on_delete=models.DO_NOTHING)
    data_hora_atendimento = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, blank=False, null=False, default='A')
    
    
    @property
    def nome_servico(self):
        return self.servico.nome_servico
    
    @property
    def nome_cliente(self):
        return self.cliente.nome
    
    @property
    def nome_atendente(self):
        return self.atendente.first_name
    
    @property
    def servicos(self):
        from recepcao.models import ItemAtendimentoModel
        
        res = (
            ItemAtendimentoModel
            .objects
            .select_related('id_item_servico')
            .filter(id_atendimento=self.id_atendimento).values('id_item_servico__nome_servico', 'id_item_servico', 'id_item_atendimento')
        )
        
        return res
        