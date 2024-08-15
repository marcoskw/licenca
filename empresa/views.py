from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def cadastrar_empresa(request):
    if request.method == "GET":
        return render(request, 'cadastrar_empresa.html')
    
def cadastrar_setor(request):
    if request.method == "GET":
        return render(request, 'cadastrar_setor.html')
        