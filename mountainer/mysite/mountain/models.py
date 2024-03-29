from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid

class Turist(models.Model):
    Nombre = models.CharField(max_length=50, null = True)
    Apellido = models.CharField(max_length=50, null = True)
    telefono = models.IntegerField(null = True)
    pais = models.CharField(max_length=50, default="")
    lugar = models.CharField(max_length=50, default="")
    Opinion = models.TextField(null = True )

    def __str__(self):
        return self.Nombre

    def get_absolute_url(self):
        return reverse('turist-detail', kwargs={'pk': self.pk})

    class meta:
        verbose_name = "Turist"
        verbose_name_plural = "Turistas"

class Imagen(models.Model):
    link = models.CharField(max_length=200)
    Titulos = models.CharField(max_length=20)
    Descripcion = models.CharField(max_length=20)
	
    def __str__(self):
        return self.link

    def get_absolute_url(self):
         return reverse('imagen-detail', kwargs={'pk': self.pk})

    class meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imagenes"