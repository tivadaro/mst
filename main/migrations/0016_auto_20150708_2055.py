# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_project_settings_mass_over_charge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='Concentration',
            field=models.DecimalField(decimal_places=3, max_digits=9, default=0),
        ),
        migrations.AlterField(
            model_name='project_settings',
            name='Mass_Over_Charge',
            field=models.DecimalField(decimal_places=3, max_digits=9, default=0),
        ),
        migrations.AlterField(
            model_name='test_file',
            name='Concentration',
            field=models.DecimalField(decimal_places=3, max_digits=9, default=0),
        ),
    ]
