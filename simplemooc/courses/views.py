from django.shortcuts import render
from .models import Course 

def index(resquest):
	courses = Course.objects.all()
	template_name = 'courses/index.html'
	context = {
		'courses' : courses
	}

	return render(resquest, template_name, context)

def details(resquest, pk):
	course = Course.objects.get(pk=pk)
	template_name = 'courses/details.html'
	context = {
		'course' : course
	}

	return render(resquest, template_name, context)