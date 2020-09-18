from django.urls import path
from .views import (
    ListadePostagem,
    PostagemDetalhada,
    CriarPost,
    EditarPost,
    DeletarPost,
    PostagensUsuario
    )
from . import views

urlpatterns = [
    path('', ListadePostagem.as_view(), name='blog-home'),
    path('user/<str:username>', PostagensUsuario.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostagemDetalhada.as_view(), name='post-detail'),
    path('post/new/', CriarPost.as_view(), name='post-create'),
    path('post/<int:pk>/update', EditarPost.as_view(), name='post-update'),
    path('post/<int:pk>/delete', DeletarPost.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('fragen/', views.fragen, name='blog-fragen')
]

# pk - primary key
