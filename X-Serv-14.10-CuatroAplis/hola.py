#!/usr/bin/python3


class Hola:

    def parse(self, request, rest):

        return None

    def process(self, parsedRequest):

        return("200 OK", "<html><body><h1>Hola</html></body></h1>")


class Adios:

    def parse(self, request, rest):

        return None

    def process(self, parsedRequest):

        return("200 OK", "<html><body><h1>Adios</html></body></h1>")
