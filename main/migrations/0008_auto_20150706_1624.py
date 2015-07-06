# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_document_setting_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='File_Name',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to=main.models.user_directory_path),
        ),
    ]
