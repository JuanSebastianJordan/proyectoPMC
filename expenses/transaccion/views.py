from django.shortcuts import render
from .models import Transaccion
from django.db.models import Sum
from .forms import CreateTransaccion
from django.http import HttpResponseRedirect

# Create your views here.

def home(response):
    tr = Transaccion.objects.values('tipo').order_by('tipo').annotate(total=Sum('cantidad'))
    if response.method == "POST":
        form = CreateTransaccion(response.POST)
        if form.is_valid():
            tipo = form.cleaned_data["tipo"]
            cantidad = form.cleaned_data["cantidad"]
            tran = Transaccion(tipo=tipo, cantidad=cantidad)
            tran.save()

            return HttpResponseRedirect("/transacciones/")
    else:
        form = CreateTransaccion()
    return render(response, "transaccion/home.html",{"tr":tr, "form": form})
