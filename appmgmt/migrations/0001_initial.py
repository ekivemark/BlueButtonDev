# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import oauth2_provider.generators
import oauth2_provider.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BBApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('client_id', models.CharField(unique=True, default=oauth2_provider.generators.generate_client_id, db_index=True, max_length=100)),
                ('redirect_uris', models.TextField(validators=[oauth2_provider.validators.validate_uris], help_text='Allowed URIs list, space separated', blank=True)),
                ('client_type', models.CharField(choices=[('confidential', 'Confidential'), ('public', 'Public')], max_length=32)),
                ('authorization_grant_type', models.CharField(choices=[('authorization-code', 'Authorization code'), ('implicit', 'Implicit'), ('password', 'Resource owner password-based'), ('client-credentials', 'Client credentials')], max_length=32)),
                ('client_secret', models.CharField(blank=True, default=oauth2_provider.generators.generate_client_secret, db_index=True, max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('skip_authorization', models.BooleanField(default=False)),
                ('logo', models.ImageField(upload_to='')),
                ('agree', models.BooleanField(verbose_name='Agreed to T&Cs')),
                ('agree_version', models.CharField(max_length=10, verbose_name='T&C Version')),
                ('agree_date', models.DateTimeField(verbose_name='Date T&C Agreed')),
                ('privacy_url', models.URLField()),
                ('support_url', models.URLField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='appmgmt_bbapplication')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
