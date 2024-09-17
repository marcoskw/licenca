from django.urls import path
from . import views

urlpatterns = [
    path('', views.wiki_lista, name="wiki_lista"),
    path('post_detalhe/<int:id>/', views.post_detalhe, name='post_detalhe'),
]