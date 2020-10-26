from django.shortcuts import render
from django.http import HttpResponse
from .models import Publicacion
# Create your views here.

def view (response, id):
    pu = Publicacion.objects.get(id=id)
    return render(response, "publicacion/base.html",{})

def view2(response):
    pu = Publicacion.objects.all()
    return render(response, "publicacion/publicaciones.html",{"pu":pu})

def home(response):
    return render(response, "publicacion/home.html",{})

def users(response):
    return render(response,"userManagement/users.html")