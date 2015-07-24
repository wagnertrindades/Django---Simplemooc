# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20150724_0223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='Nome', max_length=100)),
                ('description', models.TextField(verbose_name='Descrição', blank=True)),
                ('number', models.IntegerField(default=0, verbose_name='Número (ordem)', blank=True)),
                ('release_date', models.DateField(null=True, verbose_name='Data de Liberação', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('course', models.ForeignKey(related_name='lessons', to='courses.Course', verbose_name='Curso')),
            ],
            options={
                'ordering': ['number'],
                'verbose_name': 'Aula',
                'verbose_name_plural': 'Aulas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='Nome', max_length=100)),
                ('embedded', models.TextField(verbose_name='Video embedded', blank=True)),
                ('archive', models.FileField(upload_to='lessons/materials', null=True, blank=True)),
                ('lesson', models.ForeignKey(related_name='materials', to='courses.Lesson', verbose_name='Aula')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materiais',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='course',
            field=models.ForeignKey(related_name='announcements', to='courses.Course', verbose_name='Curso'),
        ),
    ]
