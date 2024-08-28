from django.shortcuts import redirect, render
from ocorrencias.models import OcorrenciaUsuario
from usuarios.models import Usuario

from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.
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
