from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Course, Enrollment
from .forms import ContactCourse 

def index(resquest):
	courses = Course.objects.all()
	context = {
		'courses' : courses
	}
	template_name = 'courses/index.html'

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
	context = {}

	# Verifica se o metodo é post ai insere os dados senão retorna vazio
	if resquest.method == 'POST':
		form = ContactCourse(resquest.POST)
		if form.is_valid():
			context['is_valid'] = True
			form.send_mail(course)
			form = ContactCourse()
	else:
		form = ContactCourse()

	context['form'] = form
	context['course'] = course
	template_name = 'courses/details.html'

	return render(resquest, template_name, context)

@login_required
def enrollment(resquest, slug):
	course = get_object_or_404(Course, slug=slug)
	# Metodo get_or_create se passa um filtro para ele, no caso o usuario atual, e o curso
	enrollment, created = Enrollment.objects.get_or_create(
		user=resquest.user, course=course
	)
	#if created:
	#	enrollment.active()
	return redirect('accounts:dashboard')