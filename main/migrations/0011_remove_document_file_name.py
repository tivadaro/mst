# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_document_file_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='File_Name',
        ),
    ]
