from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.http import HttpResponseRedirect
from wiki.models import Post

# Create your views here.
def wiki_lista(request):
    if not request.user.is_authenticated:
        return redirect('/login')    
    
    if request.method == "GET":
        posts = Post.objects.order_by('id')
        return render(request,'lista_wiki.html', {'posts': posts})

def adicionar_post(request):
    url = reverse('admin:wiki/post/')
    return HttpResponseRedirect(url)

def post_detalhe(request, id):
    if not request.user.is_authenticated:
        return redirect('/login')   
         
    post = get_object_or_404(Post, id=id)
    
    return render(request, 'post_detalhe.html', {'post': post})