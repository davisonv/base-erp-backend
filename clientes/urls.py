from django.urls import path

from .views import (
    ClientesListAPIView,
    ClienteCreateAPIView,
    ClienteRetriveUpdateDestroyAPIView,
)

urlpatterns = [
    path('lista_clientes/', ClientesListAPIView.as_view(), name='lista_clientes'),
    path('novo_cliente/', ClienteCreateAPIView.as_view(), name='novo_cliente'),
    path('cliente/<int:pk>/', ClienteRetriveUpdateDestroyAPIView.as_view(), name='cliente'),
    
    
    
]