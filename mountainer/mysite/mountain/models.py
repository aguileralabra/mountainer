from django.db import models

class Turist(models.Model):
    Nombre = models.CharField(max_length=50, null = True)
    Apellido = models.CharField(max_length=50, null = True)
    rut = models.IntegerField( null = True)
    telefono = models.IntegerField( null = True)
    pais = models.CharField(max_length=50, default="")
    lugar = models.CharField(max_length=50, default="")
    Opinion = models.TextField(null = True )

class Imagen(models.Model):
    link = models.CharField(max_length=200)
    Titulos = models.CharField(max_length=20)
    Descripcion = models.CharField(max_length=20)
	
def __str__(self):
        return self.Nombre
