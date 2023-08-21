from .serializers import UsuarioCreateSerializer, UsuarioUpdateGetSerializer, UsuarioUpdateSerializer, UsuarioListSerializer
from django.contrib.auth import get_user_model

from rest_framework import generics

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

# GENERICS
from util.generics_views import CustomGenericAPIView

from .serializers import CustomTokenObtainPairSerializer

# MODELS
from .models import User

class UsuarioUpdateRetrieveDestroyAPIView(generics.RetrieveUpdateDestroyAPIView, CustomGenericAPIView):
    serializer_class = UsuarioUpdateGetSerializer
    
    def get_queryset(self):
        User = get_user_model()
        qs = User.objects.all()
        return qs


class UsuarioCreateAPIView(generics.CreateAPIView, CustomGenericAPIView):
    serializer_class = UsuarioCreateSerializer
    
    def get_queryset(self):
        User = get_user_model()
        qs = User.objects.all()
        return qs

class UpdateUsuariosSenhaAPIView(generics.UpdateAPIView,CustomGenericAPIView):
    serializer_class = UsuarioUpdateSerializer
    http_method_names = ['patch']
    
    def get_queryset(self):
        User = get_user_model()
        qs = User.objects.all()
        return qs

class UsuarioListAPIView(generics.ListAPIView, CustomGenericAPIView):
    serializer_class = UsuarioListSerializer
    
    def get_queryset(self):
        User = get_user_model()

        first_name = self.request.query_params.get("first_name")
        
        if first_name:
            queryset = User.objects.filter(first_name__contains=first_name)
        else:
            queryset = User.objects.all()
        
        return queryset


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer