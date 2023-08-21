"""Serielizers de item_atendimento."""
from rest_framework import serializers
from ..models import ItemAtendimentoModel


class ItemAtendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemAtendimentoModel
        fields = '__all__'