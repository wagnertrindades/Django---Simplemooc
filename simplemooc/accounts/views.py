from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import RegisterForm, EditAccountForm

@login_required
def dashboard(resquest):
    template_name = 'accounts/dashboard.html'
    return render(resquest, template_name)

def register(resquest):
    template_name = 'accounts/register.html'
    if resquest.method == 'POST':
        form = RegisterForm(resquest.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username, password=form.cleaned_data['password1']
            )
            login(resquest, user)
            return redirect('core:home')
    else:
        form = RegisterForm()
    context = {
        'form' : form
    }
    return render(resquest, template_name, context)

@login_required
def edit(resquest):
    template_name = 'accounts/edit.html'
    context = {}
    if resquest.method == 'POST':
        form = EditAccountForm(resquest.POST, instance=resquest.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=resquest.user)
            context['success'] = True 
    else:
        form = EditAccountForm(instance= resquest.user)
    context['form'] = form
    return render(resquest, template_name, context)

@login_required
def edit_password(resquest):
    template_name = 'accounts/edit_password.html'
    context = {}
    if resquest.method == 'POST':
        form = PasswordChangeForm(data=resquest.POST, user=resquest.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=resquest.user)
    context['form'] = form
    return render(resquest, template_name, context)