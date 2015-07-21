from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages 

from simplemooc.core.utils import generate_hash_key
from simplemooc.courses.models import Enrollment

from .forms import RegisterForm, EditAccountForm, PasswordResetForm
from .models import PasswordReset

User = get_user_model()

@login_required
def dashboard(resquest):
    template_name = 'accounts/dashboard.html'
    context = {}
    return render(resquest, template_name, context)

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

def password_reset(resquest):
    template_name = 'accounts/password_reset.html'
    context = {}
    form = PasswordResetForm(resquest.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(resquest, template_name, context)

def password_reset_confirm(resquest, key):
    template_name = 'accounts/password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=resquest.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = True
    context['form'] = form
    return render(resquest, template_name, context)

@login_required
def edit(resquest):
    template_name = 'accounts/edit.html'
    context = {}
    if resquest.method == 'POST':
        form = EditAccountForm(resquest.POST, instance=resquest.user)
        if form.is_valid():
            form.save()
            messages.success(resquest, 'Os dados da sua conta foram alterados com sucesso.')
            return redirect('accounts:dashboard')
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