from django.urls import path
from . import views

urlpatterns = [
    # Usuários
    path('ocorrencias_usuarios/', views.ocorrencias_usuarios, name="ocorrencias_usuarios"),
    path('ocorrencias_usuarios/inativar_usuario/', views.inativar_usuario, name="inativar_usuario"),
    path('ocorrencias_usuarios/atualizar_setor_usuario/', views.atualizar_setor_usuario, name='atualizar_setor_usuario'),
    
    # Equipamentos
    path('ocorrencias_equipamentos/', views.ocorrencias_equipamentos, name="ocorrencias_equipamentos"),

]