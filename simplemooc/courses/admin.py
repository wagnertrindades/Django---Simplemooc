from django.contrib import admin

from .models import Course, Enrollment, Announcement, Comment, Lesson, Material

#Classe para customizar o admin do django
class CourseAdmin(admin.ModelAdmin):
	# Lista a aparecer no model do admin do django
	list_display = ['name', 'slug', 'start_date', 'created_at']
	# Campos para pesquizar
	search_fields = ['name', 'slug']
	# Preenchendo o slug automatico conforme o nome
	prepopulated_fields = {'slug' : ('name',)}

# Outro tipo de visulização no admin
#class MaterialInlineAdmin(admin.TabularInline):
class MaterialInlineAdmin(admin.StackedInline):

    model = Material

class LessonAdmin(admin.ModelAdmin):

    list_display = ['name', 'number', 'course', 'release_date']
    search_fields = ['name', 'description']
    list_filter = ['created_at']

    inlines = [
        MaterialInlineAdmin
    ]

#Registando o model para aparecer no admin
admin.site.register(Course, CourseAdmin)
admin.site.register([Enrollment, Announcement, Comment])
admin.site.register(Lesson, LessonAdmin)