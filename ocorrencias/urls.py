from django.urls import path
from . import views

urlpatterns = [
    # Usuários
    path('inativar_usuario/', views.inativar_usuario, name="inativar_usuario"),
]