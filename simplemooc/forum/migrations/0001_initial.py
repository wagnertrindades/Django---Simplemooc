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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('reply', models.TextField(verbose_name='Resposta')),
                ('correct', models.BooleanField(verbose_name='Correta?', default=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(verbose_name='Modificado em', auto_now=True)),
                ('author', models.ForeignKey(verbose_name='Autor', to=settings.AUTH_USER_MODEL, related_name='replies')),
            ],
            options={
                'verbose_name': 'Resposta',
                'verbose_name_plural': 'Respostas',
                'ordering': ['-correct', 'created'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='Título', max_length=100)),
                ('slug', models.SlugField(unique=True, verbose_name='Identificador', max_length=100)),
                ('body', models.TextField(verbose_name='Mensagem')),
                ('views', models.IntegerField(verbose_name='Visualizações', default=0, blank=True)),
                ('answers', models.IntegerField(verbose_name='Respostas', default=0, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(verbose_name='Modificado em', auto_now=True)),
                ('author', models.ForeignKey(verbose_name='Autor', to=settings.AUTH_USER_MODEL, related_name='threads')),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', verbose_name='Tags', help_text='A comma-separated list of tags.', through='taggit.TaggedItem')),
            ],
            options={
                'verbose_name': 'Tópico',
                'verbose_name_plural': 'Tópicos',
                'ordering': ['-modified'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='reply',
            name='thread',
            field=models.ForeignKey(verbose_name='Tópico', to='forum.Thread', related_name='replies'),
            preserve_default=True,
        ),
    ]
