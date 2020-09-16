from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import Perfil


class FormularioRegistro(UserCreationForm):
    username = forms.CharField(label=_('Vorname'))
    password1 = forms.CharField(label=_('Passwort'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Passwort Bestätigung'), widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class FormularioLogin(UserCreationForm):
    username = forms.CharField(label=_('Vorname'))
    password = forms.CharField(label=_('Passwort'))

    class Meta:
        model = User
        fields = ['username', 'password']


class AtualizarUsuarioInfo(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class AtualizarImagem(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['image']
