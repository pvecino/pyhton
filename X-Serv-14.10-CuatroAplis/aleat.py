#!/usr/bin/python3

import random


class Aleatorio:

    def parse(self, request, rest):

        return None

    def process(self, parsedRequest):

        rand = random.randint(1, 100000000)
        htmlAnswer = '<html><body><h1><a href=/aleat/' + str(rand)
        htmlAnswer = htmlAnswer + '>Dame otra</a></h1></body></html>'
        return("200 OK", htmlAnswer)
