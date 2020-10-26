from django.db import models

# Create your models here.

class Transaccion(models.Model):
    cantidad = models.IntegerField()
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.tipo + ", " + str(self.cantidad)