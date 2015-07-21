from django.template import Library

register = Library()

from simplemooc.courses.models import Enrollment

# Decorator que registra essa função como um template tag, passando o html a ser renderizado
# Esse tipo de template tag você faz um html separado para renderizar nos outros
@register.inclusion_tag('courses/templatetags/my_courses.html')
def my_courses(user):
    enrollments = Enrollment.objects.filter(user=user)
    context = {
        'enrollments': enrollments
    }
    return context

# Forma mais simples de retornar a templatetag
# E forma de template tag você apenas leva os dados, no caso o Enrollments
# E no template que vai coloca-lo monta o html para renderizar, sem a necessidade de um html a parte
@register.assignment_tag
def load_my_courses(user):
    return Enrollment.objects.filter(user=user)