from django.contrib import admin
from .models import User

class UsuariosAdminConfig(admin.ModelAdmin):
    ...

admin.site.register(User, UsuariosAdminConfig)