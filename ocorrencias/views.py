from datetime import datetime
from django.shortcuts import redirect, render
from equipamentos.models import Computador
from ocorrencias.models import OcorrenciaOperador, OcorrenciaComputador
from empresa.models import Operador, Setor

from django.contrib import messages
from django.contrib.messages import constants

# Operadores
def ocorrencias_operadores(request): 
    return render(request, 'ocorrencias_operadores.html')

def inativar_operador(request):
    operadores = Operador.objects.all()

    if request.method == "GET":
        return render(request,'inativar_operador.html', {'operadores': operadores})

    elif request.method == "POST":
        operador_selecionado = request.POST.get('operador')
        observacoes = request.POST.get('observacoes')
        tipo_ocorrencia = 1
        operador = Operador.objects.get(id=operador_selecionado)
        data = datetime.now()

        ocorrencia = OcorrenciaOperador(
            tipo_ocorrencia=tipo_ocorrencia,
            operador=operador,
            data=data,
            setor=None,
            observacoes=observacoes,
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
    ocorrencias = OcorrenciaOperador.objects.all()

    tipo_ocorrencia_choices = dict(OcorrenciaOperador.tipo_ocorrencia_choices)
    
    if request.method == "GET":  
        return render(request, 'listar_ocorrencias_operadores.html', {
            'ocorrencias': ocorrencias, 
            'tipo_ocorrencia_choices': tipo_ocorrencia_choices})


# Equipamentos
def ocorrencias_equipamentos(request):
    return render(request, 'ocorrencias_equipamentos.html')

def inativar_computador(request):

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
    computadores = Computador.objects.all()
    operadores = Operador.objects.all()

    if request.method == "GET":
        return render(request,'trocar_computador_operadores.html', {
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
    ocorrencias = OcorrenciaComputador.objects.all()

    tipo_ocorrencia_choices = dict(OcorrenciaComputador.tipo_ocorrencia_choices)
    
    if request.method == "GET":  
        return render(request, 'listar_ocorrencias_equipamentos.html', {
            'ocorrencias': ocorrencias, 
            'tipo_ocorrencia_choices': tipo_ocorrencia_choices})
