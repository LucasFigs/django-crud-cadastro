# app_cad_usuarios/views.py
from django.shortcuts import render, redirect
from .models import Usuario

# View para CRIAR e LER usuários
def home(request):
    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.email = request.POST.get('email')
        novo_usuario.ativo = request.POST.get('ativo') == 'on'
        novo_usuario.save()
        return redirect('home')

    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/home.html', {'usuarios': usuarios})

# View para EDITAR um usuário
def edit_usuario(request, id):
    usuario = Usuario.objects.get(id=id)

    if request.method == 'POST':
        usuario.nome = request.POST.get('nome')
        usuario.idade = request.POST.get('idade')
        usuario.email = request.POST.get('email')
        usuario.ativo = request.POST.get('ativo') == 'on'
        usuario.save()
        return redirect('home')

    return render(request, 'usuarios/edit.html', {'usuario': usuario})

# View para DELETAR um usuário
def delete_usuario(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('home')