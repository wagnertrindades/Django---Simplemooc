from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

def register(resquest):
    template_name = 'accounts/register.html'
    if resquest.method == 'POST':
        form = UserCreationForm(resquest.POST)
        if form.is_valid:
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = UserCreationForm()
    context = {
        'form' : form
    }
    return render(resquest, template_name, context)
