# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20150701_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='Project_Description',
            field=models.CharField(max_length=300, default=''),
        ),
    ]
