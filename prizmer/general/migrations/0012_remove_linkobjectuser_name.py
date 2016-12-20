# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0011_auto_20161004_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='linkobjectuser',
            name='name',
        ),
    ]
