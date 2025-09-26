from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Video, Usuario
from .forms import VideoForm, UsuarioForm

def videos(request):
    videos = Video.objects.all()
    if request.method == "POST":
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('videos')
    else:
        form = VideoForm()
    return render(request, "principal/videos.html", {"videos": videos, "form": form})


def usuarios(request):
    usuarios = Usuario.objects.all()
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form = UsuarioForm()
    return render(request, "principal/usuarios.html", {"usuarios": usuarios, "form": form})


def creditos(request):
    return render(request, "principal/creditos.html")