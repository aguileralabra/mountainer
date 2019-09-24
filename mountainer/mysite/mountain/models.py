from django.db import models

class Turist(models.Model):
    Nombre = models.CharField(max_length=200)
    Apellido = models.CharField(max_length=200)
    Opinion = models.TextField()
	
def __str__(self):
        return self.Nombre