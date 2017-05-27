from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculadora(request, qs):
    splimas = qs.split('+')
    splimenos = qs.split('-')
    splipor = qs.split('*')
    splidiv = qs.split('/')


    if len(splimas) != 1:
        try:
            num1 = float(splimas[0])
            num2 = float(splimas[-1])
        except ValueError:
            respuesta = "Error en los parametros, tienen que ser numeros"
            return HttpResponse(respuesta)
        suma = num1 + num2
        respuesta = ("El resultado es: " + str(num1) + " + " + str(num2) + " = " + str(suma))
    elif len(splimenos) != 1:
        try:
            num1 = float(splimenos[0])
            num2 = float(splimenos[-1])
        except ValueError:
            respuesta = "Error en los parametros, tienen que ser numeros"
            return HttpResponse(respuesta)
        resta = num1 - num2
        respuesta = ("El resultado es: " + str(num1) + " - " + str(num2) + " = " + str(resta))
    elif len(splipor) != 1:
        try:
            num1 = float(splipor[0])
            num2 = float(splipor[1])
        except ValueError:
            respuesta = "Error en los parametros, tienen que ser numeros"
            return HttpResponse(respuesta)
        mult = num1 * num2
        respuesta = ("El resultado es: " + str(num1) + ' * ' + str(num2) + ' = ' + str(mult))
    elif len(splidiv) != 1:
        try:
            num1 = float(splidiv[0])
            num2 = float(splidiv[1])
        except ValueError:
            respuesta = "Error en los parametros, tienen que ser numeros"
            return HttpResponse(respuesta)
        try:
            div = num1 / num2
        except ZeroDivisionError:
            respuesta = "No puedes dividir entre cero"
            return HttpResponse(respuesta)
        respuesta  = ("El resultado es: " + str(num1) + ' / ' + str(num2) + ' = ' + str(div))
    else:
        respuesta = "Not found"

    return HttpResponse(respuesta)
