# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0008_params_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meters',
            name='factory_number_readed',
            field=models.CharField(max_length=16, null=True, blank=True),
        ),
    ]
