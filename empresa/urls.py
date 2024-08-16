from django.urls import path
from . import views

urlpatterns = [
    #empresa
    path('cadastrar_empresa/', views.cadastrar_empresa, name="cadastrar_empresa"),
    path('cadastrar_setor/', views.cadastrar_setor, name="cadastrar_setor"),
]