from django.shortcuts import redirect, render
from ocorrencias.models import OcorrenciaUsuario
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


        ocorrencia = OcorrenciaUsuario(
            tipo_ocorrencia=tipo_ocorrencia,
            usuario=usuario,
            setor=None,
            observacoes=observacoes,
        )

        try:
            usuario.status = 'INT'
            ocorrencia.save()
            usuario.save()

        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/ocorrencias/inativar_usuario')   
        
        messages.add_message(request, constants.SUCCESS, 'Ocorrencia criada com sucesso')
        return redirect('/ocorrencias/inativar_usuario')   

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
