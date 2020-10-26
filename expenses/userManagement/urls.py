from django.urls import path
from . import views

urlpatterns = [
path("users/<str:username>", views.miCuenta, name="cuenta"),
path('accounts/sign_up/',views.sign_up,name="registrarse")
 ]