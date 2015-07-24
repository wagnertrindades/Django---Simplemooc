from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Course, Enrollment, Announcement, Lesson, Material
from .forms import ContactCourse, CommentForm 
from .decorators import enrollment_required	

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
	if created:
		#enrollment.active()
		messages.success(resquest, 'Você foi inscrito no curso com sucesso.')
	else:
		messages.info(resquest, 'Você já está inscrito no curso.')
	return redirect('accounts:dashboard')

@login_required
def undo_enrollment(resquest, slug):
	course = get_object_or_404(Course, slug=slug)
	enrollment= get_object_or_404(
		Enrollment, user=resquest.user, course=course
	)
	if resquest.method == 'POST':
		enrollment.delete()
		messages.success(resquest, 'Sua inscrição foi cancelada com sucesso.')
		return redirect('accounts:dashboard')
	template_name = 'courses/undo_enrollment.html'
	context = {
		'enrollment': enrollment,
		'course': course,
	}
	return render(resquest, template_name, context)

@login_required
@enrollment_required
def announcements(resquest, slug):
	# --- Jeito sem decorator
	# course = get_object_or_404(Course, slug=slug)
	# if not resquest.user.is_staff:
	# 	enrollment= get_object_or_404(
	# 		Enrollment, user=resquest.user, course=course
	# 	)
	# 	if not enrollment.is_approved():
	# 		messages.error(resquest, 'A sua inscrição está pendente')
	# 		return redirect('accounts:dashboard')
	course = resquest.course
	template_name = 'courses/announcements.html'
	context = {
		'course': course,
		'announcements': course.announcements.all()
	}
	return render(resquest, template_name, context)

@login_required
@enrollment_required
def show_announcement(resquest, slug, pk):
	# --- Jeito sem decorator
	# course = get_object_or_404(Course, slug=slug)
	# if not resquest.user.is_staff:
	# 	enrollment= get_object_or_404(
	# 		Enrollment, user=resquest.user, course=course
	# 	)
	# 	if not enrollment.is_approved():
	# 		messages.error(resquest, 'A sua inscrição está pendente')
	# 		return redirect('accounts:dashboard')
	announcement = get_object_or_404(course.announcements.all(), pk=pk)
	form = CommentForm(resquest.POST or None)
	if form.is_valid():
		comment = form.save(commit=False)
		comment.user = resquest.user
		comment.announcement = announcement
		comment.save()
		form = CommentForm()
		messages.success(resquest, 'Seu comentário foi enviado com sucesso.')
	template_name = 'courses/show_announcement.html'
	context = {
		'course': course,
		'announcement': announcement,
		'form': form,
	}
	return render(resquest, template_name, context)

@login_required
@enrollment_required
def lessons(resquest, slug):
	course = resquest.course
	template_name = 'courses/lessons.html'
	lessons = course.release_lessons()
	if resquest.user.is_staff:
		lessons = course.lessons.all()
	context = {
		'course': course,
		'lessons': lessons
	}
	return render(resquest, template_name, context)

@login_required
@enrollment_required
def show_lesson(resquest, slug, pk):
	course = resquest.course
	lesson = get_object_or_404(Lesson, pk=pk, course=course)
	if not resquest.user.is_staff and not lesson.is_available():
		messages.error(resquest, 'Esta aula não está disponível') 
		return redirect('courses:lessons', slug=course.slug)
	template_name = 'courses/show_lesson.html'
	context = {
		'course': course,
		'lesson': lesson
	}
	return render(resquest, template_name, context)

@login_required
@enrollment_required
def material(resquest, slug, pk):
	course = resquest.course
	material = get_object_or_404(Material, pk=pk, lesson__course=course)
	lesson = material.lesson
	if not resquest.user.is_staff and not lesson.is_available():
		messages.error(resquest, 'Esse material não está disponível') 
		return redirect('courses:lesson', slug=course.slug, pk=lesson.pk)
	if not material.is_embedded():
		return redirect( material.archive.url )
	template_name = 'courses/material.html'
	context = {
		'course': course,
		'material': material,
		'lesson': lesson
	}
	return render(resquest, template_name, context)