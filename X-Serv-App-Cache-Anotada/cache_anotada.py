#!/usr/bin/python3

import webapp
import urllib.request
import csv
import sys


class Writer (webapp.webApp):

    cabecera1 = ""

    def parse(self, request):
        print ("RECIBIDO_________ " + request)
        try:
            metodo = request.split()[0]
            recurso = request.split()[1]
            cuerpo = recurso.split('/')[1]
            self.cabecera1 = metodo + recurso
        except IndexError:
            return None
        return (cuerpo)

    def process(self, parsedRequest):
        if parsedRequest == 'favicon.ico':
            httpCode = ''
            htmlBody = ''
        else:
            try:
                url = "http://www." + parsedRequest
            except IndexError:
                httpCode = '400 Bad Request'
                htmlBody = 'Wrong request'
                return (httpCode, htmlBody)
            except TypeError:
                httpCode = ''
                htmlBody = ''
                return (httpCode, htmlBody)
            try:
                socket = urllib.request.urlopen(url)
            except IOError:
                httpCode = '404 Not Found'
                htmlBody = 'Pagina no encontrada'
                return (httpCode, htmlBody)
            try:
                httpBody = socket.read()
            except UnboundLocalError:
                httpCode = '105 ERR_NAME_NOT_RESOLVED'
                htmlBody = 'No se puede acceder a este sitio web'
                return (httpCode, htmlBody)
            s = '<body'
            httpCode = '200 OK'
            index_body = str(httpBody).find(s)
            index = index_body + len(s)
            preBody = httpBody[0: index]
            postBody = httpBody[index+1 : -1]
            insBody = "<a href=" + url  + "> enlace a web original</a><br>" \
                        +  self.cabecera1 + " = cabecera recibida<br>" \
                        + httpCode + " = cabecera enviada<br>"
            newpage = preBody + '>' + insBody + postBody
            htmlBody = newpage

        return (httpCode, htmlBody)


if __name__ == "__main__":
    WriterApp = Writer("localhost", 1234)
