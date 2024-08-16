from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants

from .models import Empresa, Setor

# Create your views here.
def cadastrar_empresa(request):
    if request.method == "GET":
            return render(request, 'cadastrar_empresa.html')
            
    elif request.method == "POST":
        nome_empresa = request.POST.get('nome_empresa')
        cnpj = request.POST.get('cnpj')
        logo = request.FILES.get('logo')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        site = request.POST.get('endereco')
        endereco = request.POST.get('endereco')
        numero = request.POST.get('numero')
        complemento = request.POST.get('complemento')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        uf = request.POST.get('uf')

        try:
            empresa = Empresa(
                nome_empresa=nome_empresa,
                cnpj=cnpj,
                logo=logo,
                telefone=telefone,
                email=email,
                site=site,
                endereco=endereco,
                numero=numero,
                complemento=complemento,
                bairro=bairro,
                cidade=cidade,
                uf=uf
            )
            empresa.save()
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/empresa/cadastrar_empresa') 

        messages.add_message(request, constants.SUCCESS, 'Empresa criada com sucesso')
        return redirect('/empresa/cadastrar_empresa')
     
    
def cadastrar_setor(request):
    empresas = Empresa.objects.all()
    setor = Setor()

    if request.method == "GET":
        return render(request, 'cadastrar_setor.html', {'empresas': empresas} )
    
    elif request.method == "POST":
        empresa_id = request.POST.get('empresa')
        nome_setor = request.POST.get('nome_setor')
 
    try:
        setor = Setor(
            nome_setor=nome_setor,
            empresa_id=empresa_id,
        )

        setor.save()
    except:
        messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
        return redirect('/empresa/cadastrar_setor') 

    messages.add_message(request, constants.SUCCESS, 'Setor criada com sucesso')
    return redirect('/empresa/cadastrar_setor')