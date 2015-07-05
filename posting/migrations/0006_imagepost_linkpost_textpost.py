# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authenticating', '0004_auto_20150704_0152'),
        ('posting', '0005_auto_20150705_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagePost',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('file', models.ImageField(upload_to=b'posting/%Y/%m/%d')),
                ('user', models.ForeignKey(to='authenticating.Account')),
            ],
            options={
                'ordering': ['-timestamp'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LinkPost',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('user', models.ForeignKey(to='authenticating.Account')),
            ],
            options={
                'ordering': ['-timestamp'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TextPost',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('user', models.ForeignKey(to='authenticating.Account')),
            ],
            options={
                'ordering': ['-timestamp'],
                'abstract': False,
            },
        ),
    ]
