from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


class FormularioRegistro(UserCreationForm):
    username = forms.CharField(label=_('Vorname'))
    password1 = forms.CharField(label=_('Passwort'))
    password2 = forms.CharField(label=_('Passwort Bestätigung'))
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
