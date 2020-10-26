from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


#class XpensesUserForm(UserCreationForm):
    #class Meta(UserCreationForm.Meta):
       # model = XpensesUser
        #fields = UserCreationForm.Meta.fields + ('presupuesto', 'universidad', 'carrera', 'semestre',)

class RegisterUser(forms.Form):
    username = forms.CharField(label="UserName", max_length=80)

    presupuesto = forms.IntegerField(label="Presupuesto")
    universidad = forms.CharField(label="Universidad", max_length=80)
    carrera = forms.CharField(label="Carrera", max_length=120)
    semestre = forms.IntegerField(label="Semestre")


class RegisterLocal(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    direccion = forms.CharField(label="Direccion",max_length=100)
    password = forms.CharField(label="Password", max_length=100)
