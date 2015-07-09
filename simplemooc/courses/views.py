from django.shortcuts import render

def index(resquest):
	template_name = 'courses/index.html'
	return render(resquest, template_name)