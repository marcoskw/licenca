from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import SistemaOperacional,Software,TipoEquipamento, Setor, Computador, Marca
from usuarios.models import Usuario

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

def listar_marcas(request):
    if request.method == "GET":
        marcas = Marca.objects.order_by('id')
        
    return render(request, 'listar_marcas.html', {'marcas': marcas})

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
    
def listar_softwares(request):
    if request.method == "GET":
        softwares = Software.objects.order_by('id')
    
    return render(request, 'listar_softwares.html', {'softwares':softwares})

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
    
def listar_sistemas_operacionais(request):
    if request.method == "GET":
        sos = SistemaOperacional.objects.order_by('id')

    return render(request, 'listar_sistemas_operacionais.html', {'sos': sos})

def cadastrar_computador(request):
    empresas = Empresa.objects.all()
    setores = Setor.objects.all()
    usuarios = Usuario.objects.all()
    tipo_equipamentos = TipoEquipamento.objects.all()
    marcas = Marca.objects.all()
    sistemas_operacionais = SistemaOperacional.objects.all()
    softwares = Software.objects.all()

    if request.method == "GET":
        return render(request, 'cadastrar_computador.html', {
            'empresas': empresas,
            'setores':setores,
            'usuarios': usuarios,
            'tipo_equipamentos': tipo_equipamentos,
            'marcas': marcas,
            'status': Usuario.status_choices,
            'tipo_armazenamentos': Computador.tipo_armazenamento_choices,
            'sistemas_operacionais': sistemas_operacionais,
            'softwares': softwares,
        })
    
    elif request.method == "POST":
        setor_id = request.POST.get('setor')
        nome_rede = request.POST.get('nome_rede')
        status = 'ATV'
        usuario_id = request.POST.get('usuario')
        tipo_equipamento_id = request.POST.get('tipo_equipamento')
        marca_id = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        serial_number = request.POST.get('serial_number')
        processador = request.POST.get('processador')
        memoria = request.POST.get('memoria')
        armazenamento = request.POST.get('armazenamento')
        tipo_armazenamento = request.POST.get('tipo_armazenamento') 
        sistema_operacional_id = request.POST.get('sistema_operacional')
        so_serial_vbs = request.POST.get('so_serial_vbs')
        so_serial_cmd = request.POST.get('so_serial_cmd')
        nf_computador = request.FILES.get('nf_computador')
        nf_sistema_operacional = request.FILES.get('nf_sistema_operacional')
        observacoes = request.POST.get('observacoes')

        setor = Setor.objects.get(id=setor_id)
        usuario = Usuario.objects.get(id=usuario_id)
        tipo_equipamento = TipoEquipamento.objects.get(id=tipo_equipamento_id)
        marca = Marca.objects.get(id=marca_id)
        sistema_operacional = SistemaOperacional.objects.get(id=sistema_operacional_id)

        try:   
            computador = Computador(
                setor=setor,
                nome_rede=nome_rede,
                status=status,
                usuario=usuario,
                tipo_equipamento=tipo_equipamento,
                marca=marca,
                modelo=modelo,
                serial_number=serial_number,
                processador=processador,
                memoria=memoria,
                armazenamento=armazenamento,
                tipo_armazenamento=tipo_armazenamento,
                sistema_operacional=sistema_operacional,
                so_serial_vbs=so_serial_vbs,
                so_serial_cmd=so_serial_cmd,
                nf_computador=nf_computador,
                nf_sistema_operacional=nf_sistema_operacional,
                observacoes=observacoes,
                )
            
            computador.save()

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/equipamentos/cadastrar_computador') 
        
        messages.add_message(request, constants.SUCCESS, 'Sistema Operacional criado com sucesso')
        return redirect('/equipamentos/cadastrar_computador') 
