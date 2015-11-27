# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('appmgmt', '0009_auto_20151105_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='developers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='+', blank=True),
        ),
    ]
