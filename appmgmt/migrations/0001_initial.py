# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import oauth2_provider.generators
import oauth2_provider.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BBApplication',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('client_id', models.CharField(db_index=True, default=oauth2_provider.generators.generate_client_id, unique=True, max_length=100)),
                ('redirect_uris', models.TextField(help_text='Allowed URIs list, space separated', validators=[oauth2_provider.validators.validate_uris], blank=True)),
                ('client_type', models.CharField(choices=[('confidential', 'Confidential'), ('public', 'Public')], max_length=32)),
                ('authorization_grant_type', models.CharField(choices=[('authorization-code', 'Authorization code'), ('implicit', 'Implicit'), ('password', 'Resource owner password-based'), ('client-credentials', 'Client credentials')], max_length=32)),
                ('client_secret', models.CharField(db_index=True, default=oauth2_provider.generators.generate_client_secret, max_length=255, blank=True)),
                ('name', models.CharField(max_length=255, blank=True)),
                ('skip_authorization', models.BooleanField(default=False)),
                ('logo', models.ImageField(upload_to='', blank=True, null=True)),
                ('about', models.TextField(verbose_name='About this app', blank=True, null=True)),
                ('agree', models.BooleanField(default=False, verbose_name='Agreed to T&Cs')),
                ('agree_version', models.CharField(max_length=10, verbose_name='T&C Version', blank=True, null=True)),
                ('agree_date', models.DateTimeField(default=None, verbose_name='Date T&C Agreed', blank=True, null=True)),
                ('privacy_url', models.URLField(blank=True)),
                ('support_url', models.URLField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('role', models.CharField(choices=[('primary', 'Account Owner'), ('backup', 'Backup Owner'), ('developer', 'Developer'), ('none', 'NONE')], default='none', max_length=12)),
                ('comment', models.TextField(max_length=80, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Organization Name', max_length=100)),
                ('domain', models.URLField()),
                ('trusted', models.BooleanField(default=False)),
                ('trusted_until', models.DateTimeField(blank=True, null=True)),
                ('owner', models.ForeignKey(related_name='+', null=True, to=settings.AUTH_USER_MODEL, verbose_name='Application Owner', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='developer',
            name='organization',
            field=models.ForeignKey(null=True, to='appmgmt.Organization', blank=True),
        ),
        migrations.AddField(
            model_name='bbapplication',
            name='organization',
            field=models.ForeignKey(null=True, to='appmgmt.Organization', blank=True),
        ),
        migrations.AddField(
            model_name='bbapplication',
            name='owner',
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True),
        ),
        migrations.AddField(
            model_name='bbapplication',
            name='user',
            field=models.ForeignKey(related_name='appmgmt_bbapplication', to=settings.AUTH_USER_MODEL),
        ),
    ]
