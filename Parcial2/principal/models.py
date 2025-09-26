from django.db import models

class Video(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    url = models.URLField()
    fecha_publicacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    carne = models.CharField(max_length=20, unique=True) 
    correo = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
