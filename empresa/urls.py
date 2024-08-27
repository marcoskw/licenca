from django.urls import path
from . import views

urlpatterns = [
    # empresa
    path('cadastrar_empresa/', views.cadastrar_empresa, name="cadastrar_empresa"),
    path('listar_empresas/', views.listar_empresas, name="listar_empresas"),
    # setor
    path('cadastrar_setor/', views.cadastrar_setor, name="cadastrar_setor"),
    path('listar_setores/', views.listar_setores, name="listar_setores")
]