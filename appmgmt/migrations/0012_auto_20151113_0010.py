# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('appmgmt', '0011_bbapplication_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='developers',
            field=models.ManyToManyField(blank=True, related_name='developers', to=settings.AUTH_USER_MODEL),
        ),
    ]
