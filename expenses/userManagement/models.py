from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MaxValueValidator, MinValueValidator
from transaccion.models import Transaccion

# Create your models here.

class XpensesUser(AbstractBaseUser):
    username=models.CharField(unique=True,blank=False,max_length=80)
    USERNAME_FIELD = 'username'
    feed = models.ForeignKey(Transaccion, on_delete=models.CASCADE)
    presupuesto = models.PositiveIntegerField(editable=True, validators=[MinValueValidator(1)],blank=False)
    universidad = models.CharField(blank=False,max_length=80)
    carrera = models.CharField(blank=False,max_length=120)
    semestre = models.PositiveIntegerField(validators=[MaxValueValidator(20)])

