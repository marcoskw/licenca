from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    current_time = datetime.now()
    if request.user.is_authenticated:
        first_name = request.user.first_name
        last_name = request.user.last_name
        
        context = {
            'current_time': current_time,
            'first_name': first_name,
            'last_name': last_name,
        }
    return render(request, 'home.html', context)

def sobre(request):
    return render(request, 'sobre.html')

def parametros(request):
    return render(request, 'parametros.html')