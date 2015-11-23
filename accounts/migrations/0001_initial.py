# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import phonenumber_field.modelfields
import jsonfield.fields
from django.conf import settings
import oauth2_provider.validators
import oauth2_provider.generators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('username', models.CharField(verbose_name='user name', max_length=80, unique=True, db_index=True)),
                ('email', models.EmailField(verbose_name='email address', max_length=255, unique=True, db_index=True)),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('medicare_connected', models.BooleanField(default=False)),
                ('medicare_verified', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('notify_activity', models.CharField(choices=[('N', 'No Notifications'), ('E', 'Email Message'), ('T', 'Text Message')], verbose_name='Notify Account Activity', default='N', max_length=1)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
                ('carrier', models.CharField(choices=[('NONE', 'None'), ('3 river wireless', '3 river wireless(@sms.3rivers.net)'), ('acs wireless', 'acs wireless(@paging.acswireless.com)'), ('alltel', 'alltel(@message.alltel.com)'), ('at&t', 'at&t(@txt.att.net)'), ('bell canada', 'bell canada(@bellmobility.ca)'), ('bell mobility txt', 'bell mobility(@txt.bellmobility.ca)'), ('bell mobility (canada)', 'bell mobility (canada)(@txt.bell.ca)'), ('blue sky frog', 'blue sky frog(@blueskyfrog.com)'), ('bluegrass cellular', 'bluegrass cellular(@sms.bluecell.com)'), ('boost mobile', 'boost mobile(@myboostmobile.com)'), ('bpl mobile', 'bpl mobile(@bplmobile.com)'), ('carolina west wireless', 'carolina west wireless(@cwwsms.com)'), ('cellular one', 'cellular one(@mobile.celloneusa.com)'), ('cellular south', 'cellular south(@csouth1.com)'), ('centennial wireless', 'centennial wireless(@cwemail.com)'), ('centurytel', 'centurytel(@messaging.centurytel.net)'), ('cingular (now at&t)', 'cingular (now at&t)(@txt.att.net)'), ('clearnet', 'clearnet(@msg.clearnet.com)'), ('comcast', 'comcast(@comcastpcs.textmsg.com)'), ('corr wireless communications', 'corr wireless communications(@corrwireless.net)'), ('dobson', 'dobson(@mobile.dobson.net)'), ('edge wireless', 'edge wireless(@sms.edgewireless.com)'), ('fido', 'fido(@fido.ca)'), ('golden telecom', 'golden telecom(@sms.goldentele.com)'), ('helio', 'helio(@messaging.sprintpcs.com)'), ('houston cellular', 'houston cellular(@text.houstoncellular.net)'), ('idea cellular', 'idea cellular(@ideacellular.net)'), ('illinois valley cellular', 'illinois valley cellular(@ivctext.com)'), ('inland cellular telephone', 'inland cellular telephone(@inlandlink.com)'), ('mci', 'mci(@pagemci.com)'), ('metro pcs', 'metro pcs(@mymetropcs.com)'), ('metrocall', 'metrocall(@page.metrocall.com)'), ('metrocall 2-way', 'metrocall 2-way(@my2way.com)'), ('microcell', 'microcell(@fido.ca)'), ('midwest wireless', 'midwest wireless(@clearlydigital.com)'), ('mobilcomm', 'mobilcomm(@mobilecomm.net)'), ('mts', 'mts(@text.mtsmobility.com)'), ('nextel', 'nextel(@messaging.nextel.com)'), ('onlinebeep', 'onlinebeep(@onlinebeep.net)'), ('pcs one', 'pcs one(@pcsone.net)'), ('presidents choice', 'presidents choice(@txt.bell.ca)'), ('public service cellular', 'public service cellular(@sms.pscel.com)'), ('qwest', 'qwest(@qwestmp.com)'), ('rogers at&t wireless', 'rogers at&t wireless(@pcs.rogers.com)'), ('rogers canada', 'rogers canada(@pcs.rogers.com)'), ('satellink', 'satellink(@satellink.net)'), ('solo mobile', 'solo mobile(@txt.bell.ca)'), ('southwestern bell', 'southwestern bell(@email.swbw.com)'), ('sprint', 'sprint(@messaging.sprintpcs.com)'), ('sumcom', 'sumcom(@tms.suncom.com)'), ('surewest communications', 'surewest communications(@mobile.surewest.com)'), ('t-mobile', 't-mobile(@tmomail.net)'), ('telus', 'telus(@msg.telus.com)'), ('tracfone', 'tracfone(@txt.att.net)'), ('triton', 'triton(@tms.suncom.com)'), ('unicel', 'unicel(@utext.com)'), ('us cellular', 'us cellular(@email.uscc.net)'), ('us west', 'us west(@uswestdatamail.com)'), ('verizon', 'verizon(@vtext.com)'), ('virgin mobile', 'virgin mobile(@vmobl.com)'), ('virgin mobile canada', 'virgin mobile canada(@vmobile.ca)'), ('west central wireless', 'west central wireless(@sms.wcc.net)'), ('western wireless', 'western wireless(@cellularonewest.com)')], blank=True, default='None', max_length=100)),
                ('mfa', models.BooleanField(verbose_name='Send Login PIN Code?', default=False)),
                ('verified_mobile', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('client_id', models.CharField(db_index=True, default=oauth2_provider.generators.generate_client_id, max_length=100, unique=True)),
                ('redirect_uris', models.TextField(help_text='Allowed URIs list, space separated', validators=[oauth2_provider.validators.validate_uris], blank=True)),
                ('client_type', models.CharField(choices=[('confidential', 'Confidential'), ('public', 'Public')], max_length=32)),
                ('authorization_grant_type', models.CharField(choices=[('authorization-code', 'Authorization code'), ('implicit', 'Implicit'), ('password', 'Resource owner password-based'), ('client-credentials', 'Client credentials')], max_length=32)),
                ('client_secret', models.CharField(blank=True, db_index=True, default=oauth2_provider.generators.generate_client_secret, max_length=255)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('skip_authorization', models.BooleanField(default=False)),
                ('valid_until', models.DateTimeField(editable=False)),
                ('user', models.ForeignKey(related_name='accounts_application', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Crosswalk',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('guid', models.CharField(max_length=40)),
                ('hicn', models.CharField(blank=True, max_length=40)),
                ('mmg_user', models.CharField(blank=True, max_length=250)),
                ('mmg_pwd', models.CharField(blank=True, max_length=16)),
                ('mmg_name', models.CharField(blank=True, max_length=250)),
                ('mmg_email', models.EmailField(blank=True, max_length=250, null=True)),
                ('mmg_account', models.TextField(blank=True)),
                ('mmg_bbdata', models.TextField(blank=True)),
                ('mmg_bbjson', jsonfield.fields.JSONField(blank=True)),
                ('mmg_bbfhir', models.BooleanField(default=False)),
                ('fhir', models.CharField(blank=True, max_length=40)),
                ('fhir_url_id', models.CharField(blank=True, max_length=80)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ValidSMSCode',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('sms_code', models.CharField(blank=True, max_length=4)),
                ('expires', models.DateTimeField(default=datetime.datetime.now)),
                ('send_outcome', models.CharField(blank=True, max_length=250)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
