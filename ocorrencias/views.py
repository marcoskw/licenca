from datetime import datetime
from django.shortcuts import redirect, render
from equipamentos.models import Computador, Software, SoftwareComputador
from ocorrencias.models import OcorrenciaOperador, OcorrenciaComputador
from empresa.models import Operador, Setor

from django.contrib import messages
from django.contrib.messages import constants

# Operadores
def ocorrencias_operadores(request): 
    if not request.user.is_authenticated:
        return redirect('/login')
    
    return render(request, 'ocorrencias_operadores.html')

def inativar_operador(request):
    if not request.user.is_authenticated:
        return redirect('/login')
        
    operadores = Operador.objects.all()

    if request.method == "GET":
        return render(request,'inativar_operador.html', {'operadores': operadores})

    elif request.method == "POST":
        operador_selecionado = request.POST.get('operador')
        observacoes = request.POST.get('observacoes')
        tipo_ocorrencia = 1
        operador = Operador.objects.get(id=operador_selecionado)
        data = datetime.now()
        usuario = request.user

        ocorrencia = OcorrenciaOperador(
            data=data,
            usuario=usuario,
            tipo_ocorrencia=tipo_ocorrencia,
            operador=operador,
            observacoes=f'O Operador {operador.nome_operador} - ID:{operador.id} foi inativado. \n {usuario} colocou como observação: {observacoes}. Data: {data}',
        )

        try:
            operador.status = 'INT'
            ocorrencia.save()
            operador.save()

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('inativar_operador')   
        
        messages.add_message(request, constants.SUCCESS, 'Ocorrencia criada com sucesso')
        return redirect('inativar_operador')   

def atualizar_setor_operador(request):
    if not request.user.is_authenticated:
        return redirect('/login')
            
    operadores = Operador.objects.all()
    setores = Setor.objects.all()

    if request.method == "GET":
        return render(request,'atualizar_setor_operador.html', {
            'operadores': operadores,
            'setores': setores})

    elif request.method == "POST":
        operador_selecionado = request.POST.get('operador')
        observacoes = request.POST.get('observacoes')
        setor_id= request.POST.get('setor_novo')
        tipo_ocorrencia = 2
        operador = Operador.objects.get(id=operador_selecionado)
        setor = Setor.objects.get(id=setor_id)

        ocorrencia = OcorrenciaOperador(
            tipo_ocorrencia=tipo_ocorrencia,
            operador=operador,
            setor=setor,
            observacoes=observacoes,
        )

        try:
            operador.setor = setor
            ocorrencia.save()
            operador.save()

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('atualizar_setor_operador')   
        
        messages.add_message(request, constants.SUCCESS, 'Ocorrencia criada com sucesso')
        return redirect('atualizar_setor_operador')   

def listar_ocorrencias_operadores(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    
    ocorrencias = OcorrenciaOperador.objects.all()

    tipo_ocorrencia_choices = dict(OcorrenciaOperador.tipo_ocorrencia_choices)
    
    if request.method == "GET":  
        return render(request, 'listar_ocorrencias_operadores.html', {
            'ocorrencias': ocorrencias, 
            'tipo_ocorrencia_choices': tipo_ocorrencia_choices})


# Equipamentos
def ocorrencias_equipamentos(request):
    if not request.user.is_authenticated:
        return redirect('/login')
            
    return render(request, 'ocorrencias_equipamentos.html')

def inativar_computador(request):
    if not request.user.is_authenticated:
        return redirect('/login')
        
    computadores = Computador.objects.all()
    if request.method == "GET":
        return render(request,'inativar_computador.html', {'computadores': computadores})

    elif request.method == "POST":
        computador_id = request.POST.get('computador')
        observacoes = request.POST.get('observacoes')
        tipo_ocorrencia = 1
        computador = Computador.objects.get(id=computador_id)
        data = datetime.now()

        ocorrencia = OcorrenciaComputador(
            tipo_ocorrencia=tipo_ocorrencia,
            computador=computador,
            data=data,
            observacoes=observacoes,
            operador=None       
        )

        try:
            computador.status = 'INT'
            ocorrencia.save()
            computador.save()
        except Exception as e:
            print(f"Erro: {e}")
            print(ocorrencia, computador)
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('inativar_computador')   
    
        messages.add_message(request, constants.SUCCESS, 'Ocorrência criada com sucesso')
        return redirect('inativar_computador')   

def trocar_computador_operador(request):
    if not request.user.is_authenticated:
        return redirect('/login')
            
    computadores = Computador.objects.all()
    operadores = Operador.objects.all()

    if request.method == "GET":
        return render(request,'trocar_computador_operador.html', {
            'computadores': computadores,
            'operadores': operadores})
    
    elif request.method == "POST":

        computador_id = request.POST.get('computador')
        operador_id = request.POST.get('operador')
        observacoes = request.POST.get('observacoes')    

        tipo_ocorrencia = 2
        computador = Computador.objects.get(id=computador_id)         
        operador = Operador.objects.get(id=operador_id)
        data = datetime.now()

        ocorrencia = OcorrenciaComputador(
            tipo_ocorrencia=tipo_ocorrencia,
            computador=computador,
            data=data,
            observacoes=observacoes,
            operador=operador,
        )

        try:
            computador.operador = operador
            ocorrencia.save()
            computador.save()

        except Exception as e:
            print(f"Erro: {e}")
            print(ocorrencia, computador)
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('trocar_computador_operador')   
        
        messages.add_message(request, constants.SUCCESS, 'Ocorrência criada com sucesso')
        return redirect('trocar_computador_operador')   

def listar_ocorrencias_equipamentos(request):
    if not request.user.is_authenticated:
        return redirect('/login')
            
    ocorrencias = OcorrenciaComputador.objects.all()

    tipo_ocorrencia_choices = dict(OcorrenciaComputador.tipo_ocorrencia_choices)
    
    if request.method == "GET":  
        return render(request, 'listar_ocorrencias_equipamentos.html', {
            'ocorrencias': ocorrencias, 
            'tipo_ocorrencia_choices': tipo_ocorrencia_choices})

def adicionar_software_em_um_computador(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    computadores = Computador.objects.all()
    softwares = Software.objects.all()

    if request.method == "GET":
        context = {
            'computadores': computadores,
            'softwares': softwares,
        }

        return render(request,'adicionar_software_em_um_computador.html', context)
    
    elif request.method == "POST":
        computador_id = request.POST.get('computador')
        software_id = request.POST.get('software_id')
        serial = request.POST.get('serial')
        numero_nota_fiscal_software = request.POST.get('numero_nota_fiscal_software')
        nf_software = request.FILES.get('nf_software')
        observacoes = request.POST.get('observacoes')    
        tipo_ocorrencia = 3
        computador = Computador.objects.get(id=computador_id)         
        software = Software.objects.get(id=software_id)
        data = datetime.now()

        software_computador = SoftwareComputador(
            computador = computador,
            software = software,
            serial = serial,
            numero_nota_software = numero_nota_fiscal_software,
            nf_software = nf_software
        )


        ocorrencia = OcorrenciaComputador(
            tipo_ocorrencia=tipo_ocorrencia,
            computador=computador,
            data=data,
            observacoes=f'Adicionado ao computador {computador_id}, o software {software.nome_software}. Serial: {serial}, Nota: {numero_nota_fiscal_software}. Usuário colocou como observação: {observacoes}',
        )

        try:
            software_computador.save()
            ocorrencia.save()

        except Exception as e:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('listar_ocorrencias_equipamentos')   
        
        messages.add_message(request, constants.SUCCESS, 'Ocorrência criada com sucesso')
        return redirect('listar_ocorrencias_equipamentos')   
    
def atualizar_nome_maquina(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    computadores = Computador.objects.all()

    if request.method == "GET":
        context = {
            'computadores': computadores,
        }
        return render(request,'atualizar_nome_maquina.html', context)
    
    elif request.method == "POST":
        tipo_ocorrencia = 4
        computador_id = request.POST.get('computador')
        novo_nome_rede = request.POST.get('novo_nome_rede')
        observacoes = request.POST.get('observacoes')
        computador = Computador.objects.get(id=computador_id)
        antigo_nome_rede = computador.nome_rede
        data = datetime.now()

        computador.nome_rede=novo_nome_rede

        ocorrencia = OcorrenciaComputador(
            tipo_ocorrencia=tipo_ocorrencia,
            computador=computador,
            data=data,
            observacoes=f'Alterado o computador com id:{computador_id}, nome da rede de {antigo_nome_rede} para {novo_nome_rede}. Usuário colocou como observação: {observacoes}',
        )

        try:
            computador.save()
            ocorrencia.save()

        except Exception as e:
            messages.add_message(request, constants.ERROR, f'Erro interno do sistema: {e}')
            return redirect('atualizar_nome_maquina')   
        
        messages.add_message(request, constants.SUCCESS, 'Ocorrência criada com sucesso')
        return redirect('atualizar_nome_maquina')   