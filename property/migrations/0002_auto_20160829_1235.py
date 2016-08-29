# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property_details',
            name='home_type',
            field=models.CharField(max_length=20, choices=[(b'present type', b'present type'), (b'past type', b'pasttype')]),
        ),
    ]
