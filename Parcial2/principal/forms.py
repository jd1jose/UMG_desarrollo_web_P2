from django import forms
from .models import Video, Usuario

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['titulo', 'descripcion', 'url']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre','carne','correo']
