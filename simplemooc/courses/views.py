from django.shortcuts import render, get_object_or_404
from .models import Course 

def index(resquest):
	courses = Course.objects.all()
	template_name = 'courses/index.html'
	context = {
		'courses' : courses
	}

	return render(resquest, template_name, context)

# View com url por primary key
# def details(resquest, pk):
# 	course = get_object_or_404(Course, pk=pk)
# 	template_name = 'courses/details.html'
# 	context = {
# 		'course' : course
# 	}

# 	return render(resquest, template_name, context)

# View com url por slug
def details(resquest, slug):
	course = get_object_or_404(Course, slug=slug)
	template_name = 'courses/details.html'
	context = {
		'course' : course
	}

	return render(resquest, template_name, context)