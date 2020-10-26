from django import forms

class CreatePublicacion(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    codigo = forms.CharField(label="Codigo", max_length=100)
    descripcion = forms.CharField(label="Descripcion", max_length=100)
