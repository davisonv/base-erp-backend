from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    FUNCAO_CHOICES = (
        ("A", "Administrador"),
        ("S", "Superusuario"),
        ("B", "Barbeiro"),
        ("R", "Recepcionista")
    )
    
    funcao = models.CharField(max_length=25, choices=FUNCAO_CHOICES, blank=False, null=False)
