"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registrieren/', user_views.registrar, name='register'),
    path('profil/', user_views.perfil, name='perfil'),
    path('loggen/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('ausloggen/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('passwort-zurucksetzen/',
        auth_views.PasswordResetView.as_view(template_name='users/resetar_senha.html'),
         name='password_reset'),
    path('passwort-zurucksetzen/fertig/',
        auth_views.PasswordResetDoneView.as_view(template_name='users/resetar_senha_sucesso.html'),
         name='password_reset_done'),
    path('passwort-zurucksetzen-bestatigung/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='users/resetar_senha_confirmacao.html'),
         name='password_reset_confirm'),
    path('passwort-zurucksetzen-fertig/',
        auth_views.PasswordResetCompleteView.as_view(template_name='users/resetar_senha_completo.html'),
         name='password_reset_complete'),
    path('', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
