from datetime import datetime
from django.shortcuts import redirect, render
from equipamentos.models import Computador
from ocorrencias.models import OcorrenciaUsuario, OcorrenciaComputador
from usuarios.models import Usuario, Setor

from django.contrib import messages
from django.contrib.messages import constants

# Usuários
def ocorrencias_usuarios(request): 
    return render(request, 'ocorrencias_usuarios.html')

def inativar_usuario(request):
    usuarios = Usuario.objects.all()

    if request.method == "GET":
        return render(request,'inativar_usuario.html', {'usuarios': usuarios})

    elif request.method == "POST":
        usuario_selecionado = request.POST.get('usuario')
        observacoes = request.POST.get('observacoes')
        tipo_ocorrencia = 1
        usuario = Usuario.objects.get(id=usuario_selecionado)
        data = datetime.now()

        ocorrencia = OcorrenciaUsuario(
            tipo_ocorrencia=tipo_ocorrencia,
            usuario=usuario,
            data=data,
            setor=None,
            observacoes=observacoes,
        )

        try:
            usuario.status = 'INT'
            ocorrencia.save()
            usuario.save()

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('inativar_usuario')   
        
        messages.add_message(request, constants.SUCCESS, 'Ocorrencia criada com sucesso')
        return redirect('inativar_usuario')   

def atualizar_setor_usuario(request):
    usuarios = Usuario.objects.all()
    setores = Setor.objects.all()

    if request.method == "GET":
        return render(request,'atualizar_setor_usuario.html', {
            'usuarios': usuarios,
            'setores': setores})

    elif request.method == "POST":
        usuario_selecionado = request.POST.get('usuario')
        observacoes = request.POST.get('observacoes')
        setor_id= request.POST.get('setor_novo')
        tipo_ocorrencia = 2
        usuario = Usuario.objects.get(id=usuario_selecionado)
        setor = Setor.objects.get(id=setor_id)

        ocorrencia = OcorrenciaUsuario(
            tipo_ocorrencia=tipo_ocorrencia,
            usuario=usuario,
            setor=setor,
            observacoes=observacoes,
        )

        try:
            usuario.setor = setor
            ocorrencia.save()
            usuario.save()

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('atualizar_setor_usuario')   
        
        messages.add_message(request, constants.SUCCESS, 'Ocorrencia criada com sucesso')
        return redirect('atualizar_setor_usuario')   

def listar_ocorrencias_usuarios(request):
    ocorrencias = OcorrenciaUsuario.objects.all()

    tipo_ocorrencia_choices = dict(OcorrenciaUsuario.tipo_ocorrencia_choices)
    
    if request.method == "GET":  
        return render(request, 'listar_ocorrencias_usuarios.html', {
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
            usuario=None       
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

def trocar_computador_usuario(request):
    computadores = Computador.objects.all()
    usuarios = Usuario.objects.all()

    if request.method == "GET":
        return render(request,'trocar_computador_usuario.html', {
            'computadores': computadores,
            'usuarios': usuarios})
    
    elif request.method == "POST":

        computador_id = request.POST.get('computador')
        usuario_id = request.POST.get('usuario')
        observacoes = request.POST.get('observacoes')    

        tipo_ocorrencia = 2
        computador = Computador.objects.get(id=computador_id)         
        usuario = Usuario.objects.get(id=usuario_id)
        data = datetime.now()

        ocorrencia = OcorrenciaComputador(
            tipo_ocorrencia=tipo_ocorrencia,
            computador=computador,
            data=data,
            observacoes=observacoes,
            usuario=usuario,
        )

        try:
            computador.usuario = usuario
            ocorrencia.save()
            computador.save()

        except Exception as e:
            print(f"Erro: {e}")
            print(ocorrencia, computador)
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('trocar_computador_usuario')   
        
        messages.add_message(request, constants.SUCCESS, 'Ocorrência criada com sucesso')
        return redirect('trocar_computador_usuario')   

def listar_ocorrencias_equipamentos(request):
    ocorrencias = OcorrenciaComputador.objects.all()

    tipo_ocorrencia_choices = dict(OcorrenciaComputador.tipo_ocorrencia_choices)
    
    if request.method == "GET":  
        return render(request, 'listar_ocorrencias_equipamentos.html', {
            'ocorrencias': ocorrencias, 
            'tipo_ocorrencia_choices': tipo_ocorrencia_choices})
