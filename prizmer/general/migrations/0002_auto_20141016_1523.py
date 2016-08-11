# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkabonentstakenparams',
            name='coefficient_2',
            field=models.FloatField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='linkabonentstakenparams',
            name='coefficient_3',
            field=models.FloatField(default=1000),
            preserve_default=True,
        ),
    ]
