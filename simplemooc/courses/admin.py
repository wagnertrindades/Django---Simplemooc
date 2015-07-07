from django.contrib import admin

from .models import Course

#Registando o model para aparecer no admin
admin.site.register(Course)
