# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20150707_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='Concentration',
            field=models.DecimalField(decimal_places=3, max_digits=5, default=0),
        ),
    ]
