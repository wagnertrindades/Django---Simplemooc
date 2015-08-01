# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('reply', models.TextField(verbose_name='Resposta')),
                ('correct', models.BooleanField(default=False, verbose_name='Correta?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('author', models.ForeignKey(verbose_name='Autor', related_name='replies', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Respostas',
                'verbose_name': 'Resposta',
                'ordering': ['-correct', 'created'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='Título', max_length=100)),
                ('body', models.TextField(verbose_name='Mensagem')),
                ('views', models.IntegerField(default=0, blank=True, verbose_name='Visualizações')),
                ('answers', models.IntegerField(default=0, blank=True, verbose_name='Respostas')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('author', models.ForeignKey(verbose_name='Autor', related_name='threads', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(through='taggit.TaggedItem', verbose_name='Tags', help_text='A comma-separated list of tags.', to='taggit.Tag')),
            ],
            options={
                'verbose_name_plural': 'Tópicos',
                'verbose_name': 'Tópico',
                'ordering': ['-modified'],
            },
            bases=(models.Model,),
        ),
    ]
