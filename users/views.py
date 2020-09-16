from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#from .forms import FormularioRegistro
#from .forms import FormularioLogin, AtualizarUsuarioInfo, AtualizarImagem
from .forms import *

def registrar(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, willkommen! Ihr Konto wurde erfolgreich erstellt! :)')
            return redirect('login')
    else:
        form = FormularioRegistro()
    return render(request, 'users/registrar.html', {'form': form})

def login(request):
    pass

@login_required
def perfil(request):
    if request.method == 'POST':
        usuario_form = AtualizarUsuarioInfo(request.POST, instance=request.user)
        imagem_form = AtualizarImagem(request.POST, request.FILES, instance=request.user.perfil)
        if usuario_form.is_valid() and imagem_form.is_valid():
            usuario_form.save()
            imagem_form.save()
            messages.success(request, f'Ihr Konto wurde aktualisiert.')
            return redirect('perfil')  # stops warning message on refresh page
    else:
        usuario_form = AtualizarUsuarioInfo(instance=request.user)
        imagem_form = AtualizarImagem(instance=request.user.perfil)

    contexto = {
        'usuario_form': usuario_form,
        'imagem_form': imagem_form
    }

    return render(request, 'users/perfil.html', contexto)

# messages.debug
# messages.info
# messages.sucess
# messages.warning
# messages.error
