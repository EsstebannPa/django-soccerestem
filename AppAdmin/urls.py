from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('infoequipos/<int:id>', views.infoequipos, name='infoequipos'),
    path('equipos/', views.equipos, name="equipos"),
    path("tecnicos/", views.tecnicos, name="tecnicos")

]
