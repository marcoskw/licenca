from django.urls import path
from . import views

urlpatterns = [
    # marca
    path('cadastrar_marca/', views.cadastrar_marca, name="cadastrar_marca"),
    path('listar_marcas/', views.listar_marcas, name="listar_marcas"),

    # software
    path('cadastrar_software/', views.cadastrar_software, name="cadastrar_software"),
    path('listar_softwares/', views.listar_softwares, name="listar_softwares"),

    # sistema operacional
    path('cadastrar_sistema_operacional/', views.cadastrar_sistema_operacional, name="cadastrar_sistema_operacional"),
    path('listar_sistemas_operacionais/', views.listar_sistemas_operacionais, name="listar_sistemas_operacionais"),
    # computador
    path('cadastrar_computador/', views.cadastrar_computador, name="cadastrar_computador")
]