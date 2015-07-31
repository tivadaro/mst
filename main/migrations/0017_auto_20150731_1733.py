# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20150708_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_settings',
            name='Mass_Over_Charge',
            field=models.DecimalField(default=0, decimal_places=11, max_digits=15),
        ),
    ]
