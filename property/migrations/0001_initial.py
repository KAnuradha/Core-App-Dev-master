# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property_details',
            fields=[
                ('property_id', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('property_title', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zip_code', models.IntegerField()),
                ('home_type', models.CharField(max_length=20)),
                ('beds', models.IntegerField()),
                ('baths', models.IntegerField()),
                ('rooms', models.IntegerField()),
                ('property_size', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('other_features', models.TextField()),
            ],
        ),
    ]
