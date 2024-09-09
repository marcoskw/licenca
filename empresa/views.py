from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from django.db.models import Q
from .models import Contato, Empresa, Operador, Setor

# Empresa
def cadastrar_empresa(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    
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
     
def listar_empresas(request):
    if not request.user.is_authenticated:
        return redirect('/login')
        
    if request.method == "GET":
        empresas = Empresa.objects.order_by('id')
        
    return render(request, 'listar_empresas.html', {'empresas': empresas})    

def detalhes_empresa(request, id):
    empresa = get_object_or_404(Empresa, id=id)
    return render(request, 'detalhes_empresa.html', {'empresa': empresa})


# Setor
def cadastrar_setor(request):
    if not request.user.is_authenticated:
        return redirect('/login')
        
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

def listar_setores(request):
    if not request.user.is_authenticated:
        return redirect('/login')
        
    if request.method == "GET":
        setores = Setor.objects.order_by('id')
        
    return render(request, 'listar_setores.html', {'setores': setores})


# Operador
def cadastrar_operador(request):
    if not request.user.is_authenticated:
        return redirect('/login')
        
    setores = Setor.objects.all()
    
    if request.method == "GET":
        return render(request, 'cadastrar_operador.html', {
            'setores': setores,
            'status': Operador.status_choices
        })

    elif request.method == "POST":
        nome_operador = request.POST.get('nome_operador')
        setor_id = request.POST.get('setor')
        email = request.POST.get('email')
        status = "ATV"
        setor = Setor.objects.get(id=setor_id)

        operador = Operador(
            nome_operador=nome_operador,
            setor=setor,
            email=email,
            status=status,
        )
        
        try:
            operador.save()
            messages.add_message(request, constants.SUCCESS, 'Operador criado com sucesso')
        except Exception as e:
            print(e)  
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
        
        return redirect('cadastrar_operador')
    
def listar_operadores(request):
    if not request.user.is_authenticated:
        return redirect('/login')
        
    if request.method == "GET":
        operadores = Operador.objects.order_by('id')
        
    return render(request, 'listar_operadores.html', {'operadores': operadores})

# Contato
def cadastrar_contato(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    
    empresas = Empresa.objects.all()
    setores = Setor.objects.all()


    if request.method == "GET":
        return render(request, 'cadastrar_contato.html', {
            'empresas': empresas,
            'setores': setores,
            'status': Contato.status_choices
        })
    elif request.method == "POST":
        nome_contato = request.POST.get('nome_contato')
        empresa_id = request.POST.get('empresa')
        setor_id = request.POST.get('setor')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        status = "ATV"
        observacoes = request.POST.get('observacoes')

        empresa = Empresa.objects.get(id=empresa_id)
        setor = Setor.objects.get(id=setor_id)

        contato = Contato(
            nome_contato=nome_contato,
            empresa=empresa,
            setor=setor,
            email=email,
            telefone=telefone,
            status=status,
            observacoes=observacoes,
        )

        try:
            contato.save()
            messages.add_message(request, constants.SUCCESS, 'Contato criado com Sucesso')
        except Exception as e:
            print(e)
            messages.add_message(request, constants.ERROR, 'Erro interno no sistema')
    return redirect('cadastrar_contato')

def listar_contatos(request):
    if not request.user.is_authenticated:
        return redirect('/login')
        
    if request.method == "GET":
        contatos = Contato.objects.order_by('id')
        
    return render(request, 'listar_contatos.html', {'contatos': contatos})

def buscar_contatos(request):
    termo = request.GET.get('q')
    contatos = Contato.objects.all()

    if termo:
        contatos = contatos.filter(
            Q(nome_contato__icontains=termo) | 
            Q(empresa__nome_empresa__icontains=termo) | 
            Q(setor__nome_setor__icontains=termo)
        )

    return render(request, 'listar_contatos.html', {'contatos': contatos})
