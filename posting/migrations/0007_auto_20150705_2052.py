# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authenticating', '0004_auto_20150704_0152'),
        ('posting', '0006_imagepost_linkpost_textpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField(null=True, blank=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('image_file', models.ImageField(null=True, upload_to=b'posting/%Y/%m/%d', blank=True)),
                ('user', models.ForeignKey(to='authenticating.Account')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.RemoveField(
            model_name='imagepost',
            name='user',
        ),
        migrations.RemoveField(
            model_name='linkpost',
            name='user',
        ),
        migrations.RemoveField(
            model_name='textpost',
            name='user',
        ),
        migrations.DeleteModel(
            name='ImagePost',
        ),
        migrations.DeleteModel(
            name='LinkPost',
        ),
        migrations.DeleteModel(
            name='TextPost',
        ),
    ]
