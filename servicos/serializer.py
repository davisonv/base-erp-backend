"""Serielizers do modulo de cadastro de servicos."""
from rest_framework import serializers

from .models import ServicosModel

class ServicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicosModel
        fields = '__all__'