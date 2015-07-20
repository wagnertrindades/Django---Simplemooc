# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_passwordreset'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordreset',
            name='user',
            field=models.ForeignKey(verbose_name='Usuário', related_name='resets', to=settings.AUTH_USER_MODEL),
        ),
    ]
