# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.utils.timezone
import re


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', default=django.utils.timezone.now)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(verbose_name='Nome de Usuário', unique=True, max_length=30, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$', 32), 'O nome de usuário só pode conter letras, digitos ou os seguintes caracteres: @/./+/-/_', 'invalid')])),
                ('email', models.EmailField(verbose_name='E-mail', unique=True, max_length=75)),
                ('name', models.CharField(verbose_name='Nome', max_length=100, blank=True)),
                ('is_active', models.BooleanField(verbose_name='Está ativo?', default=True)),
                ('is_staff', models.BooleanField(verbose_name='É da equipe?', default=False)),
                ('date_joined', models.DateTimeField(verbose_name='Data de Entrada', auto_now_add=True)),
                ('groups', models.ManyToManyField(to='auth.Group', related_name='user_set', related_query_name='user', blank=True, verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.')),
                ('user_permissions', models.ManyToManyField(to='auth.Permission', related_name='user_set', related_query_name='user', blank=True, verbose_name='user permissions', help_text='Specific permissions for this user.')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
            bases=(models.Model,),
        ),
    ]
