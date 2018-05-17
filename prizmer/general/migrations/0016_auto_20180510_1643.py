# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0015_auto_20180510_1609'),
    ]

    operations = [
        
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbc\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb9'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xba\xd0\xbe\xd0\xbc\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='name',
            field=models.CharField(max_length=50, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f'),
        ),
    ]
