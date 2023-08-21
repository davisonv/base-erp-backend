"""Serielizers de atendimento."""
from rest_framework import serializers
from django.contrib.auth import get_user_model

from ..models.atendimento import AtendimentoModel
from servicos.models import ServicosModel
from clientes.models import ClientesModel


class AtendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtendimentoModel
        fields = '__all__'
        

class ClienteAtendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientesModel
        fields = 'nome',


class ServicoAtendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicosModel
        fields = 'nome_servico',


class AtendenteAtendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = 'first_name',


class AtendimentoListSerializer(serializers.ModelSerializer):
    # cliente_nome = ClienteAtendimentoSerializer(many=True, read_only=True)
    # servico_nome = ServicoAtendimentoSerializer(many=True, read_only=True)
    # atendente_nome = AtendenteAtendimentoSerializer(many=True, read_only=True)
    
    class Meta:
        model = AtendimentoModel
        fields = [
            'id_atendimento', 
            # 'servico',
            'valor', 
            'valor_desconto', 
            'valor_adicional', 
            'atendente', 
            'cliente', 
            'data_hora_atendimento', 
            'status',
            'nome_cliente',
            'nome_servico',
            'nome_atendente',
            'servicos',
        ]


class SelectAtendenteSerializer(serializers.ModelSerializer):
    value = serializers.ReadOnlyField(source='id')
    label = serializers.ReadOnlyField(source='username')
    
    
    class Meta:
        model = get_user_model()
        fields = 'value', 'label',
        

class SelectServicoSerializer(serializers.ModelSerializer):
    value = serializers.ReadOnlyField(source='id_servico')
    label = serializers.ReadOnlyField(source='nome_servico')
    
    
    class Meta:
        model = ServicosModel()
        fields = 'value', 'label',
  
