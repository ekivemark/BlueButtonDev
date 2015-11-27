# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmgmt', '0003_bbapplication_organization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='trusted_until',
            field=models.DateTimeField(blank=True),
        ),
    ]
