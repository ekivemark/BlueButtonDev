# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmgmt', '0007_organization_developers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='trusted',
            field=models.BooleanField(default=False),
        ),
    ]
