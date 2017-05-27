#!/usr/bin/python3
# -*- coding: utf-8 -*-

# PAULA VECINO RODRIGUEZ GIST
# CURSO 2016/20178

fl = open("/etc/passwd","r")
user_line = fl.readlines()
dic = {}

for line in user_line:
    elements = line.split(':')
    user = elements[0]
    shell = elements[-1][:-1]
    dic[user] = shell

print (dic)
print ("el numero de usuarios es: " + str(len(user_line)))
fl.close()
