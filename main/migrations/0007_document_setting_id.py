# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_projects_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='Setting_ID',
            field=models.ForeignKey(null=True, to='main.Project_Settings', blank=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
