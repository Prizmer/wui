# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0009_auto_20151026_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkabonentstakenparams',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='params',
            name='name',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='takenparams',
            name='name',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
