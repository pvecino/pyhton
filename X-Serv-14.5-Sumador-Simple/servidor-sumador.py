#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""
#PAULA VECINO RODRIGUEZ GIST

import socket

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Let the port be reused if no process is actually using it
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind to the address corresponding to the main name of the host
mySocket.bind((socket.gethostbyname(socket.gethostname()), 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an almost-infinite loop; the loop can be stopped with Ctrl+C)


First = True
suma = 'Para realizar la suma, pon en la url /numero'
try:
    while True:
        print ('Waiting for connections')
        print (socket.gethostbyname(socket.gethostname()))
        (recvSocket, address) = mySocket.accept()
        print ('Request received:')

        peticion = recvSocket.recv(1024)
        print (peticion)
        #sumador
        numero = peticion.split()[1][1:]
        if (numero == 'favicon.ico') or (numero == ''):
            None
        else:
            if First == True:
                resultado = int(numero)
                suma = "Inserta otro numero"
                First = False
            else:
                resultado = int(numero) + resultado
                suma = 'El resultado de la suma es ' + str(resultado)
                suma += 'Inserta otro numero para realizar otra suma'
                First = True

        print ('Answering back...')

        html = '<html><body><h1>Hello World!</h1>'
        html += '<p>And in particular hello to you,'
        html += str(address[0]) + ' with port ' + str(address[1])
        html += '</p>'
        html += '<p><b>' + suma + '</b></p>'
        html += '</body></html>'

        recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" + html + "\r\n")
        recvSocket.close()
except KeyboardInterrupt:
    print ('Closing binded socket')
    mySocket.close()
except ValueError:
    print ('Inserta un numero, no un caracter')
    mySocket.close()
