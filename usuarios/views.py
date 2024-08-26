from django.shortcuts import render, redirect
from django.http import HttpResponse
from empresa.models import Setor
from .models import Usuario
from django.contrib import messages
from django.contrib.messages import constants


# Create your views here.
def cadastrar_usuario(request):
    setores = Setor.objects.all()
    
    if request.method == "GET":
        return render(request, 'cadastrar_usuario.html', {
            'setores': setores,
            'status': Usuario.status_choices
        })

    elif request.method == "POST":
        nome_usuario = request.POST.get('nome_usuario')
        setor_id = request.POST.get('setor')
        email = request.POST.get('email')
        status = "ATV"
        setor = Setor.objects.get(id=setor_id)

        usuario = Usuario(
            nome_usuario=nome_usuario,
            setor=setor,
            email=email,
            status=status,
        )
        
        try:
            usuario.save()
            messages.add_message(request, constants.SUCCESS, 'Usuário criado com sucesso')
        except Exception as e:
            print(e)  
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
        
        return redirect('/usuarios/cadastrar_usuario')
    
def listar_usuarios(request):
    if request.method == "GET":
        usuarios = Usuario.objects.order_by('id')
        
    return render(request, 'listar_usuarios.html', {'usuarios': usuarios})