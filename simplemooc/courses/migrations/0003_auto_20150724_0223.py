# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0002_auto_20150720_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('content', models.TextField(verbose_name='Conteúdo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('course', models.ForeignKey(to='courses.Course', verbose_name='Curso')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name_plural': 'Anúncios',
                'verbose_name': 'Anúncio',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='Comentário')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('announcement', models.ForeignKey(to='courses.Announcement', verbose_name='Anúncio', related_name='comments')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'ordering': ['created_at'],
                'verbose_name_plural': 'Comentários',
                'verbose_name': 'Comentário',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='status',
            field=models.IntegerField(blank=True, default=1, verbose_name='Situação', choices=[(0, 'Pendente'), (1, 'Aprovado'), (2, 'Cancelado')]),
        ),
    ]
