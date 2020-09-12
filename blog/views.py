from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts' : Post.objects.all(),
        'title' : 'Hauptseite'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {
        'title' : 'Über'
    }
    return render(request, 'blog/about.html', context)

def fragen(request):
    context = {
        'title' : 'Fragen'
    }
    return render(request, 'blog/fragen.html', context)
