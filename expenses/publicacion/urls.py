from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.view, name="view"),
    path("home/", views.home, name="home"),
    path("publicaciones/", views.view2, name="view2"),
]
