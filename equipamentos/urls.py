from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_equipamento/', views.cadastrar_equipamento, name="cadastrar_equipamento"),
]