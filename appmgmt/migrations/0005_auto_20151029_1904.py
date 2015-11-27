# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmgmt', '0004_auto_20151029_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='trusted_until',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
