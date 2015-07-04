# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import annoying.fields


class Migration(migrations.Migration):

    dependencies = [
        ('authenticating', '0003_auto_20150703_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='user',
            field=annoying.fields.AutoOneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
