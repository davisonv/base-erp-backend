from django.urls import path

from .views import (ServicosListAPIView, ServicoCreateAPIView, ServicoRetriveUpdateDestroyAPIView)

urlpatterns = [
    path('lista_servicos/', ServicosListAPIView.as_view(), name='lista_servicos'),
    path('novo_servico/', ServicoCreateAPIView.as_view(), name='lista_servicos'),
    path('servico/<int:pk>/', ServicoRetriveUpdateDestroyAPIView.as_view(), name='lista_servicos'),
]