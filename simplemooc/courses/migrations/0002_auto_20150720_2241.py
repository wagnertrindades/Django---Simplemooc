# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('status', models.IntegerField(choices=[(0, 'Pendente'), (1, 'Aprovado'), (2, 'Cancelado')], blank=True, verbose_name='Situação', default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(verbose_name='Atualizado em', auto_now=True)),
                ('course', models.ForeignKey(verbose_name='Curso', related_name='enrollments', to='courses.Course')),
                ('user', models.ForeignKey(verbose_name='Usuário', related_name='enrollments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Inscrição',
                'verbose_name_plural': 'Inscrições',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together=set([('user', 'course')]),
        ),
    ]
