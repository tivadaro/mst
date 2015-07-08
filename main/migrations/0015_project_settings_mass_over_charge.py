# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_document_concentration'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_settings',
            name='Mass_Over_Charge',
            field=models.DecimalField(decimal_places=3, max_digits=5, default=0),
        ),
    ]
