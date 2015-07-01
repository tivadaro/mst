# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20150619_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='Setting_ID',
            field=models.ForeignKey(null=True, to='main.Project_Settings', blank=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
