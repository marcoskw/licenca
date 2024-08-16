from django.urls import path
from . import views

urlpatterns = [
    # marca
    path('cadastrar_marca/', views.cadastrar_marca, name="cadastrar_marca"),

    # software
    path('cadastrar_software/', views.cadastrar_software, name="cadastrar_software")
]