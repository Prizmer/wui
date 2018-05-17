# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0016_auto_20180510_1643'),
    ]

    operations = [
        
        migrations.AlterField(
            model_name='comments',
            name='name',
            field=models.CharField(max_length=50, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f', blank=True),
        ),
    ]
