from django.urls import path
from . import views

urlpatterns = [
path("profile/", views.miCuenta, name="cuenta"),
path('sign_up/',views.sign_up,name="registrarse"),
path('sign_up_local/',views.sign_up2,name="registrarseLocal"),
path("profile_local/", views.miCuentaLocal, name="cuentaLocal"),
 ]