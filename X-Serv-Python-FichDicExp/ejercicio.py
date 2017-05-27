#!/usr/bin/python3
# -*- coding: utf-8 -*-

# PAULA VECINO RODRIGUEZ GIST
# CURSO 2016/2017
fl = open('/etc/passwd', 'r')

user_line = fl.readlines()
dic = {}

for line in user_line:
    elements = line.split(':')
    user = elements[0]
    shell = elements[-1][:-1]
    dic[user] = shell

print (dic)
print ("TOTAL USERS: " + str(len(user_line)))

print ("root: " + dic["root"])

try:
	print ("imaginario: " + dic["imaginario"])
except KeyError:
	print ("INCORRECT WORD")
fl.close()
