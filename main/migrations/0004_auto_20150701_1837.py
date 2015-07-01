# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20150701_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='Test_ID',
            field=models.ForeignKey(null=True, to='main.Test_File', on_delete=django.db.models.deletion.SET_NULL, blank=True),
        ),
    ]
