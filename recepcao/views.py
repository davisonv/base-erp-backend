from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.db import transaction


# MODELS
from .models import AtendimentoModel, ItemAtendimentoModel
from servicos.models import ServicosModel

# SERIALIZERS
from .serializers.atendimento import AtendimentoSerializer, SelectAtendenteSerializer, SelectServicoSerializer, AtendimentoListSerializer

# GENERICS
from util.generics_views import CustomGenericAPIView

class AtendimentoCreateAPIView(CustomGenericAPIView):
    """View que adiciona um novo atendimento."""

    def post(self, request, *args, **kwargs):
        
        data=request.data
        servicos = [item['id_servico'] for item in data["atendimento_items"]]
        valores_servicos = (
            ServicosModel.objects
                .filter(id_servico__in=servicos).values_list('id_servico', 'valor_servico')
        )
        v = dict(valores_servicos)
        
        valor_total = sum([v[servico] for servico in servicos]) - data['atendimento'].get('valor_desconto', 0)        
        data['atendimento']['valor'] = valor_total
        serializer = AtendimentoSerializer(data=data['atendimento'])
        
        @transaction.atomic
        def cria_servico_e_seus_itens():
            atendimento = serializer.save()
            
            ItemAtendimentoModel.objects.bulk_create(
                [ItemAtendimentoModel(id_atendimento=atendimento, id_item_servico=ServicosModel.objects.get(**item)) for item in data["atendimento_items"]]
            )
            
            
        if serializer.is_valid():
            try:
                cria_servico_e_seus_itens()
                return Response(status=status.HTTP_201_CREATED)
            except Exception as e:
                raise e
        else:
            return Response({'message':'Ocorreu um erro ao salvar o atendimento, verifique os campos e tente novamente.'}, status=status.HTTP_400_BAD_REQUEST)
            
        
        
        

class AtendimentoListAPIView(generics.ListAPIView, CustomGenericAPIView):
    """View que lista os atendimentos."""
    queryset = AtendimentoModel.objects.all()
    serializer_class = AtendimentoListSerializer
    filterset_fields = ['data_hora_atendimento', 'atendente']
    ordering = ('data_hora_atendimento',)
    

class AtendimentoRetriveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView, CustomGenericAPIView):
    queryset = AtendimentoModel.objects.all()
    serializer_class = AtendimentoSerializer
    

class SelectAtendenteAPIview(generics.ListAPIView, CustomGenericAPIView):
    """Select api para trazer os possiveis barbeiros para o atendimento."""
    serializer_class = SelectAtendenteSerializer
    pagination_class = None
  
    def get_queryset(self):
        User = get_user_model()
        return User.objects.filter(funcao="B")
    

class SelectServicoAPIview(generics.ListAPIView, CustomGenericAPIView):
    """Select api para trazer os possiveis barbeiros para o atendimento."""
    serializer_class = SelectServicoSerializer
    pagination_class = None
    queryset = ServicosModel.objects.all()
    
  
  
  