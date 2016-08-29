# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20160506_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hubree',
            fields=[
                ('userid', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=15)),
                ('verificationstatus', models.BooleanField(default=False)),
            ],
        ),
    ]
