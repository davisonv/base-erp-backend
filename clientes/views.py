# REST
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# MODELS
from .models import ClientesModel

# SERIALIZERS
from .serializer import ClientesSerializer

# GENERICS
from util.generics_views import CustomGenericAPIView


class ClientesListAPIView(generics.ListAPIView, CustomGenericAPIView):
    """View que lista os clientes com dados completos."""
    
    serializer_class = ClientesSerializer
    
    def get_queryset(self):
        nome = self.request.query_params.get("nome")
        
        if nome:
            queryset = ClientesModel.objects.filter(nome__contains=nome)
        else:
            queryset = ClientesModel.objects.all()
        
        return queryset
    
    
class ClienteCreateAPIView(generics.CreateAPIView, CustomGenericAPIView):
    """View que adiciona um novo cliente."""
    queryset = ClientesModel.objects.all()
    serializer_class = ClientesSerializer
    
    
class ClienteRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView, CustomGenericAPIView):
    queryset = ClientesModel.objects.all()
    serializer_class = ClientesSerializer
    

