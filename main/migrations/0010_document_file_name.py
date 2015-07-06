# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_document_file_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='File_Name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
