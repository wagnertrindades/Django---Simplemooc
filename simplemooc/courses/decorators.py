from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from .models import Course, Enrollment

def enrollment_required(view_func):
    def _wrapper(resquest, *args, **kwargs):
        slug = kwargs['slug']
        course = get_object_or_404(Course, slug=slug)
        has_permission = resquest.user.is_staff
        if not has_permission:
            try:
                enrollment =  Enrollment.objects.get(
                    user=resquest.user, course=course
                )
            except Enrollment.DoesNotExist:
                message = 'Desculpe, mas você não tem permissão para acessar esta página.'
            else:
                if enrollment.is_approved():
                    has_permission = True
                else:
                    message = 'A sua inscrição ainda está pendente'
        if not has_permission:
            messages.error(resquest, message)
            return redirect('accounts:dashboard')
        resquest.course = course
        return view_func(resquest, *args, **kwargs)
    return _wrapper