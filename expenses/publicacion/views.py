from django.shortcuts import render
from django.http import HttpResponse
from .models import Publicacion
from .forms import CreatePublicacion
from django.http import HttpResponseRedirect
# Create your views here.

def view (response, id):
    pu = Publicacion.objects.get(id=id)
    return render(response, "publicacion/base.html",{})

def view2(response):
    pu = Publicacion.objects.all()
    if response.method == "POST":
        form = CreatePublicacion(response.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            codigo = form.cleaned_data["codigo"]
            descripcion = form.cleaned_data["descripcion"]
            tran = Publicacion(nombre=nombre, codigo=codigo, descripcion=descripcion)
            tran.save()

            return HttpResponseRedirect("/publicaciones/")
    else:
        form = CreatePublicacion()
    return render(response, "publicacion/publicaciones.html",{"pu":pu, "form":form})

def home(response):
    return render(response, "publicacion/home.html",{})

def users(response):
    return render(response,"userManagement/users.html")