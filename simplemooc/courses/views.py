from django.shortcuts import render
from .models import Course 

def index(resquest):
	courses = Course.objects.all()
	template_name = 'courses/index.html'
	context = {
		'courses' : courses
	}

	return render(resquest, template_name, context)