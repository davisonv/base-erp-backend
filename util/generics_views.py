"""Arquivo com classes genericas customizadas."""

from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import GenericAPIView

class CustomGenericAPIView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    