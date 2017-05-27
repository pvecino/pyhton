from django.shortcuts import render
from django.http import HttpResponse
from models import Contenidos

# Create your views here.

def show (request):
    lista_contenidos = Contenidos.objects.all()
    respuesta = "lista de Contenidos " + "<ol>"
    for contenido in lista_contenidos:
        respuesta += '<li>'+ contenido.nombre + " ha introducido: " +  contenido.contenido
    respuesta += "</ol>"
    return HttpResponse(respuesta)

def nuevo (request, name, cont):
    contenido = Contenidos(nombre= name, contenido= cont)
    contenido.save()
    return HttpResponse ("nuevo contenido: " + cont)
