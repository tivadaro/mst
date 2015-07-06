# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_projects_project_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='Project_Description',
        ),
    ]
