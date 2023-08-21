"""Serielizers do modulo de cadastro de clientes."""
from rest_framework import serializers

from .models import ClientesModel

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientesModel
        fields = '__all__'