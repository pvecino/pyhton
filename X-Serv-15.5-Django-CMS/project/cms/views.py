from django.shortcuts import render
from .models import Pages
from django.conf.urls import patterns, include, url
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.

def contentapp(request,resourceName):
	response = '<h1>Welcome to Contentapp</h1>'
	try:
		content = Pages.objects.get(name=resourceName)
		return HttpResponse(response + content.page)
	except Pages.DoesNotExist:
			response += '<body> resource not found</body>'
			return HttpResponseNotFound(response)
