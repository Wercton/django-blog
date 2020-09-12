from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioRegistro

def registrar(request):
    if request.method == 'POST':
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, willkommen! Ihr Konto wurde erfolgreich erstellt! :)')
            return redirect('blog-home')
    else:
        form = FormularioRegistro()
    return render(request, 'users/register.html', {'form': form})

# messages.debug
# messages.info
# messages.sucess
# messages.warning
# messages.error
