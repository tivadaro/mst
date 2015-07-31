# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20150731_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='Concentration',
            field=models.DecimalField(default=0, decimal_places=9, max_digits=13),
        ),
    ]
