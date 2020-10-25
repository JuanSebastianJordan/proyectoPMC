from django.db import models

# Create your models here.

class Publicacion(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre + " ,"+self.descripcion + " ," + self.codigo

