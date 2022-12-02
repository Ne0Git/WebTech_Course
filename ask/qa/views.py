from django.shortcuts import render

def test(request, *args, **kwargs):
	return HttpResponse('OK')

def index(request):
	return HttpResponse('OK')

def login(request):
	return HttpResponse('OK')

def signup(request):
	return HttpResponse('OK')

def question(request, pk):
	return HttpResponse('OK')

def ask(request):
	return HttpResponse('OK')

def popular(request):
	return HttpResponse('OK')

def new(request):
	return HttpResponse('OK')
