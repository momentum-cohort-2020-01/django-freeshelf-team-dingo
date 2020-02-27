from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse ("This is just a text response, unrelated to the database.") 

# Create your views here.
