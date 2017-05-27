from django.shortcuts import render
from .models import Pages
from django.conf.urls import patterns, include, url
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context

# Create your views here.

def getform():
	form = "<form action='' method='POST'>\n"
	form += "Page: <input type='text' name='name' value=''><br>\n"
	form += "Content page: <input type='text' name='page'><br>\n"
	form += "<input type='submit' value='enviar'>\n"
	form += "</form>\n"
	return form

def getpage(request,resourceName):
	if request.method == "GET":
		try:
			content = Pages.objects.get(name=resourceName)
			return content.page
		except Pages.DoesNotExist:
			response = '<body> GET </body>'
			response += getform()
			return response
	elif request.method == "POST":
		response = '<body> POST </body>'
		newPage = Pages(name=request.POST['name'], page=request.POST['page'])
		newPage.save()
		response += "--Page: " + request.POST['name']
		response += ", Content Page: " + request.POST['page']
		return response
	elif request.method == "PUT":
		response = '<body> PUT </body>'
		(namePage, Page) = request.body.split(';')
		newPage = Page(name=namePage, page=Page)
		newPage.save()
		response += "--Page: " + request.POST['name']
		response += ", Content Page: " + request.POST['page']
		return response
	else:
		response = '<body> you do DELETE </body>'
		return response

def getlogged(request):
	if request.user.is_authenticated():
		logged = "<br><br>Logged in as " + request.user.username +\
                ". <a href='/admin/logout/'>Logout</a><br>"
	else:
		logged = "<br><br>Not logged. <a href='/admin/login/'>Login</a><br>"
	return logged

@csrf_exempt
def contentapp(request,resourceName):
	response = '<h1>Welcome to Contentapp</h1>'
	logged = response + str(getlogged(request))
	if request.user.is_authenticated():
	 	logged += str(getpage(request,resourceName))
	return HttpResponse(logged)

def templates(request,resourceName):
	if request.method == 'GET':
		template = get_template('index.html')
		logged = contentapp(request,resourceName)
		text = getpage(request,resourceName)
		if text == "":
			return HttpResponseNotFound("Page not found" + logged)
		c = Context({'logged': logged, 'text': text})
		render = template.render(c)
		return HttpResponse(render)
	else:
		return HttpResponse(status=403)
