# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20150707_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='Concentration',
        ),
        migrations.RemoveField(
            model_name='project_settings',
            name='Mass_Over_Charge',
        ),
    ]
