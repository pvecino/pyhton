#!/usr/bin/python3

import random


class Sumador:


    def parse(self, request, rest):
        try:
            primero = int(rest.split("/")[1])
            segundo = int(rest.split("/")[2])
        except ValueError:
            return "BAD"
        return (primero, segundo)


    def process(self, parsedRequest):
        if parsedRequest:
            resultado = int(parsedRequest[0]) + int(parsedRequest[1])
            htmlAnswer = "<html><body><h1>" + str(resultado) + "</h1></body></html>"

            return ("200 OK", htmlAnswer)
        else:
            htmlAnswer = "<html>" + "<body><h1>don't use suma so</h1>" + "</body></html>"
            return ("400 Error", )
