from django.urls import path
from . import views

urlpatterns = [
    # empresa
    path('cadastrar_empresa/', views.cadastrar_empresa, name="cadastrar_empresa"),
    path('listar_empresas/', views.listar_empresas, name="listar_empresas"),
    path('detalhes/<int:id>/', views.detalhes_empresa, name='detalhes_empresa'),
    # setor
    path('cadastrar_setor/', views.cadastrar_setor, name="cadastrar_setor"),
    path('listar_setores/', views.listar_setores, name="listar_setores"),

    # Operador
    path('cadastrar_operador/', views.cadastrar_operador, name="cadastrar_operador"),
    path('listar_operadores/', views.listar_operadores, name="listar_operadores"),
]