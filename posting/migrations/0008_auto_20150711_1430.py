# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0007_auto_20150705_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=django_markdown.models.MarkdownField(null=True, blank=True),
        ),
    ]
