# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Page',
            new_name='Pages',
        ),
        migrations.RenameField(
            model_name='pages',
            old_name='url',
            new_name='page',
        ),
    ]
