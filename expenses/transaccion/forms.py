from django import forms

class CreateTransaccion(forms.Form):
    tipo = forms.CharField(label="Tipo", max_length=100)
    cantidad = forms.IntegerField(label='Cantidad')