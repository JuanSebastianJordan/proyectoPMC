from django.db import models
from .models import Publicacion
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class XpensesUser(AbstractBaseUser):
    USERNAME_FIELD = 'username'

    feed = models.ForeignKey(models.Transaccion)
    presupuesto = models.PositiveIntegerField(editable=True, validators=[MinValueValidator(1)],blank=False)
    universidad = models.CharField(blank=False)
    carrera = models.CharField(blank=False)
    semestre = models.PositiveIntegerField(validators=[MaxValueValidator(20)])

