# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_auto_20150211_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='takenparams',
            name='name',
            field=models.CharField(max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
