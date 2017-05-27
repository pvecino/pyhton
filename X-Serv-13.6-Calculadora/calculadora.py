# !/usr/bin/python3
# -*- coding: utf-8 -*-

# PAULA VECINO RODRIGUEZ GIST
# CURSO 2016/2017
import sys
operaciones = ['sumar', 'restar', 'dividir', 'multiplicar']
try:
	operacion = sys.argv[1]
	num1 = float(sys.argv[2])
	num2 = float(sys.argv[3])
except IndexError:
	sys.exit("Forma correcta: calculadora.py <sumar/restar/dividir/multiplicar> <numero 1> <numero 2>")
except ValueError:
	sys.exit("solo numeros")
if len(sys.argv) == 4:
	if operacion == operaciones[0]:
		resultado = num1 + num2
	elif operacion == operaciones[1]:
		resultado = num1 - num2
	elif operacion == operaciones[2]:
		try:
			resultado = num1 / num2
		except ZeroDivisionError:
			sys.exit("No division entre 0")
	elif operacion == operaciones[3]:
		resultado = num1 * num2
	else:
 		sys.exit("Forma correcta: calculadora.py <sumar/restar/dividir/multiplicar> <numero 1> <numero 2>")
else:
	sys.exit("calculadora.py <sumar/restar/dividir/multiplicarn> <numero 1> <numero 2>")
print ("El resultado de la operacion es: " + str(resultado))
