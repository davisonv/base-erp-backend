from rest_framework import generics

# MODELS
from .models import ServicosModel

# SERIALIZERS
from .serializer import ServicosSerializer

# GENERICS
from util.generics_views import CustomGenericAPIView

class ServicosListAPIView(generics.ListAPIView, CustomGenericAPIView):
    serializer_class = ServicosSerializer

    def get_queryset(self):
        nome_servico = self.request.query_params.get("nome_servico")
        
        if nome_servico:
            queryset = ServicosModel.objects.filter(nome_servico__contains=nome_servico)
        else:
            queryset = ServicosModel.objects.all()
        
        return queryset
        
        
    

class ServicoCreateAPIView(generics.CreateAPIView, CustomGenericAPIView):
    """View que adiciona um novo serviço."""
    queryset = ServicosModel.objects.all()
    serializer_class = ServicosSerializer
    
    
class ServicoRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView, CustomGenericAPIView):
    queryset = ServicosModel.objects.all()
    serializer_class = ServicosSerializer