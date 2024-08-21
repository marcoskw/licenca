from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Computador, Equipamento,LicencaSoftware, Marca
from .models import SistemaOperacional,Software,TipoEquipamento, Setor
from empresa.models import Empresa, Setor
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.
def cadastrar_marca(request):
    if request.method == "GET":
        return render(request,'cadastrar_marca.html')
    
    elif request.method == "POST":
        nome_marca = request.POST.get('nome_marca')

        try:
            marca = Marca(nome_marca=nome_marca)

            marca.save()

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/equipamentos/cadastrar_marca') 
        
        messages.add_message(request, constants.SUCCESS, 'Marca criada com sucesso')
        return redirect('/equipamentos/cadastrar_marca')

def cadastrar_software(request):
    if request.method == "GET":
        return render(request,'cadastrar_software.html')
    
    elif request.method == "POST":
        nome_software = request.POST.get('nome_software')

        try:
            software = Software(nome_software=nome_software)

            software.save()

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/equipamentos/cadastrar_software') 
        
        messages.add_message(request, constants.SUCCESS, 'Software criado com sucesso')
        return redirect('/equipamentos/cadastrar_software')
    
def cadastrar_sistema_operacional(request):
    if request.method == "GET":
        return render(request,'cadastrar_sistema_operacional.html')
    
    elif request.method == "POST":
        nome_sistema_operacional = request.POST.get('nome_sistema_operacional')

        try:
            sistema_operacional = SistemaOperacional(nome_sistema_operacional=nome_sistema_operacional)

            sistema_operacional.save()

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/equipamentos/cadastrar_sistema_operacional') 
        
        messages.add_message(request, constants.SUCCESS, 'Sistema Operacional criado com sucesso')
        return redirect('/equipamentos/cadastrar_sistema_operacional')
    
def cadastrar_computador(request):
    empresas = Empresa.objects.all()
    setores = Setor.objects.all()
    
    if request.method == "GET":
        return render(request, 'cadastrar_computador.html', {
            'empresas': empresas,
            'setores':setores
        } ) 