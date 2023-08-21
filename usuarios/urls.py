from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

from .views import (
    UsuarioCreateAPIView,
    UsuarioUpdateRetrieveDestroyAPIView,
    UpdateUsuariosSenhaAPIView,
    UsuarioListAPIView,
    CustomTokenObtainPairView
)

from django.urls import path


urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('registrar/', UsuarioCreateAPIView.as_view(), name='registrar'),
    path('<int:pk>/', UsuarioUpdateRetrieveDestroyAPIView.as_view(), name='usuario_ver_apagar_editar'),
    path('<int:pk>/alterar_senha/', UpdateUsuariosSenhaAPIView.as_view(), name='alterar_senha'),
    path('lista_usuarios/', UsuarioListAPIView.as_view(), name='lista_usuarios'),
    
]