from django.contrib import admin

from .models import Course

#Classe para customizar o admin do django
class CourseAdmin(admin.ModelAdmin):
	# Lista a aparecer no model do admin do django
	list_display = ['name', 'slug', 'start_date', 'created_at']
	# Campos para pesquizar
	search_fields = ['name', 'slug']

#Registando o model para aparecer no admin
admin.site.register(Course, CourseAdmin)
