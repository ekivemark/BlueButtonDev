# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appmgmt', '0005_auto_20151029_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='bbapplication',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='bbapplication',
            name='agree',
            field=models.BooleanField(verbose_name='Agreed to T&Cs', default=False),
        ),
        migrations.AlterField(
            model_name='bbapplication',
            name='agree_date',
            field=models.DateTimeField(null=True, verbose_name='Date T&C Agreed', blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='bbapplication',
            name='agree_version',
            field=models.CharField(null=True, max_length=10, blank=True, verbose_name='T&C Version'),
        ),
        migrations.AlterField(
            model_name='bbapplication',
            name='logo',
            field=models.ImageField(null=True, blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='bbapplication',
            name='privacy_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='bbapplication',
            name='support_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='owner',
            field=models.ForeignKey(related_name='+', to=settings.AUTH_USER_MODEL, null=True, verbose_name='Application Owner', blank=True),
        ),
    ]
