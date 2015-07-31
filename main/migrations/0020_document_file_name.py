# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20150731_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='file_name',
            field=models.CharField(max_length=100, default=''),
        ),
    ]
