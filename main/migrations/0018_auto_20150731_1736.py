# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20150731_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_settings',
            name='Mass_Over_Charge',
            field=models.DecimalField(decimal_places=9, max_digits=13, default=0),
        ),
        migrations.AlterField(
            model_name='test_file',
            name='Concentration',
            field=models.DecimalField(decimal_places=9, max_digits=13, default=0),
        ),
        migrations.AlterField(
            model_name='test_file',
            name='Mass_Over_Charge',
            field=models.DecimalField(decimal_places=9, max_digits=13, default=0),
        ),
    ]
