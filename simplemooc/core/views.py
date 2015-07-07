from django.shortcuts import render
from django.http import HttpResponse

def home(resquest):
	return render(resquest, 'home.html')

def contact(resquest):
	return render(resquest, 'contact.html')