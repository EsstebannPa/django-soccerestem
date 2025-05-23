from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import Jugadores, Equipos, Tecnicos, Posiciones


def infoequipos(request, id):
    equipo = get_object_or_404(Equipos, id_equipo=id)
    equipos = Equipos.objects.all()
    jugadores = Jugadores.objects.filter(id_equipo=id)
    posiciones = Posiciones.objects.all()
    tecnicos =Tecnicos.objects.filter(id_equipo=id)
    #try:
        #equipo = Equipos.objects.get(id_equipo=id)

    #except Equipos.DoesNotExist:
        #return HttpResponse(status=404)  
    return render(request, 'infoequipos.html', {'equipo': equipo, 'jugadores': jugadores, 
    'posiciones': posiciones, 'tecnicos': tecnicos, 'equipos': equipos})


def equipos(request):
    equipos =Equipos.objects.all()
    return render(request, 'index.html', {'equipos': equipos})


def tecnicos(request):
    tecnicos =Tecnicos.objects.all()
    return render(request, 'infoequipos.html', {'tecnicos': tecnicos})

