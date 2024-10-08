from django.shortcuts import render, redirect
from datetime import datetime
from datetime import timedelta
from equipamentos.models import Computador
from parametros.models import ParametrosEmpresa

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    
    computadores_verificacao = Computador.objects.filter(status="ATV").order_by('proxima_verificacao')[:5]
    
    current_time = datetime.now()
    if request.user.is_authenticated:
        first_name = request.user.first_name
        last_name = request.user.last_name
        
        context = {
            'current_time': current_time,
            'first_name': first_name,
            'last_name': last_name,
            'computadores_verificacao':computadores_verificacao,
        }
    return render(request, 'home.html', context)

def sobre(request):
    if not request.user.is_authenticated:
        return redirect('/login')
            
    return render(request, 'sobre.html')

def parametros(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    
    empresa = ParametrosEmpresa.objects.get(id=1)

    return render(request, 'parametros.html', {'empresa': empresa})