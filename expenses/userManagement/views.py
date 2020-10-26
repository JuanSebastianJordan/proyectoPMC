from django.shortcuts import get_object_or_404, render
from .models import XpensesUser
from .forms import XpensesUserForm
from .logic.logic_usuario import *
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

@login_required
def miCuenta(request, username):
    if(request.user != None):
        usuario = get_object_or_404(XpensesUser, username=username)
        return render(request, 'miCuenta.html', {'XpensesUser': usuario})
    else:
        return render(request,'registrarse.html')
    return ()
    
def sign_up(request):
    context = {}
    form = XpensesUserForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            usuario = create_usuario(form)
            login(request,usuario)
            return render(request,'home')
    context['form']=form
    return render(request,'registrarse.html',context)