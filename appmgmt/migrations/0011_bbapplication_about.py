# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmgmt', '0010_auto_20151105_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='bbapplication',
            name='about',
            field=models.TextField(verbose_name='About this app', null=True, blank=True),
        ),
    ]
