from django.urls import path

from .views import (
    AtendimentoListAPIView,
    AtendimentoCreateAPIView,
    AtendimentoRetriveUpdateDestroyAPIView,
    SelectAtendenteAPIview,
    SelectServicoAPIview,
)

urlpatterns = [
    path('lista_atendimentos/', AtendimentoListAPIView.as_view(), name='lista_atendimentos'),
    path('novo_atendimento/', AtendimentoCreateAPIView.as_view(), name='novo_atendimento'),
    path('atendimento/<uuid:pk>/', AtendimentoRetriveUpdateDestroyAPIView.as_view(), name='atendimento'),
    path('atendente_select/', SelectAtendenteAPIview.as_view(), name='atendente_select'),
    path('servico_select/', SelectServicoAPIview.as_view(), name='servico_select'),
    
    
    
    
    
]