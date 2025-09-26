from django.shortcuts import render
#from .models import Persona

def index(request):
    #personas = Persona.objects.all()
    return render(request, "principal/index.html")#, {"personas": personas})

def about(request):
    return render(request, "principal/about.html")