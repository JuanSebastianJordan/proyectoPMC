from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import XpensesUser

class XpensesUserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = XpensesUser
        fields = UserCreationForm.Meta.fields + ('presupuesto', 'universidad', 'carrera', 'semestre',)
