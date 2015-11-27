# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmgmt', '0002_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='bbapplication',
            name='organization',
            field=models.ForeignKey(blank=True, to='appmgmt.Organization', null=True),
        ),
    ]
