# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticating', '0002_invitation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='handle',
            field=models.CharField(default=b'anon', max_length=100),
        ),
    ]
