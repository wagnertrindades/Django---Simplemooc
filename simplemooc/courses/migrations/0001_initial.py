# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Nome', max_length=100)),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('description', models.TextField(verbose_name='Descrição Simples', blank=True)),
                ('about', models.TextField(verbose_name='Sobre o curso', blank=True)),
                ('start_date', models.DateField(verbose_name='Data de Início', null=True, blank=True)),
                ('image', models.ImageField(verbose_name='Imagem', upload_to='courses/images', null=True, blank=True)),
                ('created_at', models.DateTimeField(verbose_name='Criado em', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='Atualizado em', auto_now=True)),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
    ]
