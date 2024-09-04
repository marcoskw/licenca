from django.urls import path
from . import views

urlpatterns = [
    # Operadores
    path('login/', views.login, name="login"),
    path('usuarios/cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),]