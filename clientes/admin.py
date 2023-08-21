from django.contrib import admin
from .models import ClientesModel

class ClientesAdminConfig(admin.ModelAdmin):
    ...
    
    

admin.site.register(ClientesModel, ClientesAdminConfig)