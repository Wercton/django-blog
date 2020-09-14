from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FormularioRegistro
from .forms import FormularioLogin

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
    return render(request, 'users/perfil.html')

# messages.debug
# messages.info
# messages.sucess
# messages.warning
# messages.error
