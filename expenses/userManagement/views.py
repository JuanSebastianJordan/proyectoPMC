from django.shortcuts import get_object_or_404, render, redirect
from .models import ExpensesUser, Local
from .forms import RegisterUser, RegisterLocal
from .logic.logic_usuario import *
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

#@login_required
#def miCuenta(request):
    #if(request.user != None):
        #usuario = get_object_or_404(XpensesUser, username=username)
        #usuario = get_object_or_404(XpensesUser, id=1)
        #return render(request, 'miCuenta.html', {'XpensesUser': usuario})
    #else:
        #return render(request,'./registration/sign_up.html')
   # return ()


def miCuenta(request):
    us= ExpensesUser.objects.all()
    return render(request,'miCuenta.html',{"us":us})

def miCuentaLocal(request):
    lo = Local.objects.all()
    return render(request, 'registration/miCuentaLocal.html',{"lo":lo})
    
def sign_up(request):
    context = {}
    form = RegisterUser(request.POST)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data["username"]
            presupuesto = form.cleaned_data["presupuesto"]
            universidad = form.cleaned_data["universidad"]
            carrera = form.cleaned_data["carrera"]
            semestre = form.cleaned_data["semestre"]
            user = ExpensesUser(username=username,presupuesto=presupuesto,universidad=universidad,
                                carrera=carrera,semestre=semestre)
            user.save()
    return render(request, './registration/sign_up.html', {"form":form})

def sign_up2(request):
    form = RegisterLocal()
    if request.method == "POST":
        form = RegisterLocal(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            direccion = form.cleaned_data["direccion"]
            password = form.cleaned_data["password"]
            tran = Local(nombre=nombre, direccion=direccion, password=password)
            tran.save()

    return render(request,"registration/sign_up_local.html",{"form": form})