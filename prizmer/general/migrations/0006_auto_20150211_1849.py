# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_auto_20150114_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typesmeters',
            name='driver_name',
            field=models.CharField(max_length=50),
        ),
    ]
