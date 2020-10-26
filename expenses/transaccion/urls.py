from django.urls import path
from . import views

urlpatterns = [
    path("transacciones/", views.home, name="home"),

]