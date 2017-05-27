#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys
import string

def normalize_whitespace(text):
    return string.join(string.split(text), ' ')

class myContentHandler(ContentHandler):

    def __init__ (self):
        self.inContent = 0
        self.theContent = ""
        self.noticeContent = 0

    def startElement (self, name, attrs):
        if name == 'item':
            self.link = normalize_whitespace(attrs.get('rdf:about'))
            self.noticeContent = 1
        elif name == 'title':
            if self.noticeContent:
                self.inContent = 1

    def endElement (self, name):
        if self.inContent:
            self.theContent = normalize_whitespace(self.theContent)
        if name == 'item':
            print ('')
        elif name == 'title':
            if self.noticeContent:
                self.notice = '<p><a href="' + self.link + '">'
                self.notice += self.theContent + '</a></p><br>'
                print (self.notice)
        if self.inContent:
            self.inContent = 0
            self.noticeContent = 0
            self.theContent = ""

    def characters (self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars


if len(sys.argv)<2:
    print ("Usage: python xml-parser-barrapunto.py <document>")
    
    print (" <document>: file name of the document to parse")
    sys.exit(1)


theParser = make_parser()
theHandler = myContentHandler()
theParser.setContentHandler(theHandler)


xmlFile = open(sys.argv[1],"r")
theParser.parse(xmlFile)

print ("Parse complete")
