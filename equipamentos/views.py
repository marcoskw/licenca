from django.shortcuts import get_object_or_404, render, redirect
from .models import SistemaOperacional,Software, SoftwareComputador,TipoEquipamento, Setor, Computador, Marca

from empresa.models import Empresa, Operador, Setor
from django.contrib import messages
from django.contrib.messages import constants


# MARCAS
def cadastrar_marca(request):
    if not request.user.is_authenticated:
        return redirect('/login')
        
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
    if not request.user.is_authenticated:
        return redirect('/login')
        
    if request.method == "GET":
        marcas = Marca.objects.order_by('id')
        
    return render(request, 'listar_marcas.html', {'marcas': marcas})


# SOFTWARES
def cadastrar_software(request):
    if not request.user.is_authenticated:
        return redirect('/login')
        
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
    if not request.user.is_authenticated:
        return redirect('/login')
        
    if request.method == "GET":
        softwares = Software.objects.order_by('id')
    
    return render(request, 'listar_softwares.html', {'softwares':softwares})


# SISTEMAS OPERACIONAIS
def cadastrar_sistema_operacional(request):
    if not request.user.is_authenticated:
        return redirect('/login')
        
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
    if not request.user.is_authenticated:
        return redirect('/login')
        
    if request.method == "GET":
        sos = SistemaOperacional.objects.order_by('id')

    return render(request, 'listar_sistemas_operacionais.html', {'sos': sos})


# COMPUTADORES
def cadastrar_computador(request):
    if not request.user.is_authenticated:
        return redirect('/login')
        
    empresas = Empresa.objects.all()
    setores = Setor.objects.all()
    operadores = Operador.objects.all()
    tipo_equipamentos = TipoEquipamento.objects.all()
    marcas = Marca.objects.all()
    sistemas_operacionais = SistemaOperacional.objects.all()
    softwares = Software.objects.all()

    if request.method == "GET":
        return render(request, 'cadastrar_computador.html', {
            'empresas': empresas,
            'setores':setores,
            'operadores': operadores,
            'tipo_equipamentos': tipo_equipamentos,
            'marcas': marcas,
            'status': Operador.status_choices,
            'tipo_armazenamentos': Computador.tipo_armazenamento_choices,
            'sistemas_operacionais': sistemas_operacionais,
            'softwares': softwares,
        })
    
    elif request.method == "POST":
        setor_id = request.POST.get('setor')
        nome_rede = request.POST.get('nome_rede')
        status = 'ATV'
        operador_id = request.POST.get('operador')
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

        software_id = request.POST.get('software')
        serial_software = request.POST.get('serial_software')
        nf_software = request.FILES.get('nf_software')

        setor = Setor.objects.get(id=setor_id)
        operador = Operador.objects.get(id=operador_id)
        tipo_equipamento = TipoEquipamento.objects.get(id=tipo_equipamento_id)
        marca = Marca.objects.get(id=marca_id)
        sistema_operacional = SistemaOperacional.objects.get(id=sistema_operacional_id)
        software = Software.objects.get(id=software_id)


        try:   
            computador = Computador(
                setor=setor,
                nome_rede=nome_rede,
                status=status,
                operador=operador,
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
            
            software_computador = SoftwareComputador(
                computador = computador,
                software = software,
                serial=serial_software,
                nf_software=nf_software,
            )
            computador.save()
            software_computador.save()

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/equipamentos/cadastrar_computador') 
        
        messages.add_message(request, constants.SUCCESS, 'Computador criado com sucesso')
        return redirect('/equipamentos/cadastrar_computador') 

def listar_computadores(request):
    if not request.user.is_authenticated:
        return redirect('/login')
        
    if request.method == "GET":
        computadores = Computador.objects.order_by('nome_rede')
    return render(request, 'listar_computadores.html', {'computadores':computadores})

def detalhe_computador(request, id):
    computador = get_object_or_404(Computador, id=id)
    softwares_computador = SoftwareComputador.objects.filter(computador=computador)


    return render(request, 'detalhe_computador.html', {
        'computador': computador, 
        'softwares_computador': softwares_computador})