from django.shortcuts import render
from django.http import HttpResponse
from empresa.models import Setor
from .models import Usuario

# Create your views here.
def cadastrar_usuario(request):
    setores = Setor.objects.all()
    if request.method == "GET":
        return render(request, 'cadastrar_usuario.html', {
            'setores': setores,
            'status': Usuario.status_choices
        })
    