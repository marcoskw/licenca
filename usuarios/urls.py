from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_usuario/', views.cadastrar_usuario, name="cadastrar_usuario"),
    path('listar_usuarios/', views.listar_usuarios, name="listar_usuarios")
]