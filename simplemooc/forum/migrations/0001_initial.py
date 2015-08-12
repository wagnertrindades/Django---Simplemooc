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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('reply', models.TextField(verbose_name='Resposta')),
                ('correct', models.BooleanField(verbose_name='Correta?', default=False)),
                ('created', models.DateTimeField(verbose_name='Criado em', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='Modificado em', auto_now=True)),
                ('author', models.ForeignKey(verbose_name='Autor', to=settings.AUTH_USER_MODEL, related_name='replies')),
            ],
            options={
                'ordering': ['-correct', 'created'],
                'verbose_name': 'Resposta',
                'verbose_name_plural': 'Respostas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='Título', max_length=100)),
                ('slug', models.SlugField(verbose_name='Identificador')),
                ('body', models.TextField(verbose_name='Mensagem')),
                ('views', models.IntegerField(verbose_name='Visualizações', default=0, blank=True)),
                ('answers', models.IntegerField(verbose_name='Respostas', default=0, blank=True)),
                ('created', models.DateTimeField(verbose_name='Criado em', auto_now_add=True)),
                ('modified', models.DateTimeField(verbose_name='Modificado em', auto_now=True)),
                ('author', models.ForeignKey(verbose_name='Autor', to=settings.AUTH_USER_MODEL, related_name='threads')),
                ('tags', taggit.managers.TaggableManager(verbose_name='Tags', to='taggit.Tag', help_text='A comma-separated list of tags.', through='taggit.TaggedItem')),
            ],
            options={
                'ordering': ['-modified'],
                'verbose_name': 'Tópico',
                'verbose_name_plural': 'Tópicos',
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
