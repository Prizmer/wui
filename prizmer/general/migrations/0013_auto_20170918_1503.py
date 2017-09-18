# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0011_auto_20170723_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='comportsettings',
            name='gsm_init_string',
            field=models.CharField(default='at', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comportsettings',
            name='gsm_on',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\x98\xd1\x81\xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd1\x8c CSD \xd0\xba\xd0\xb0\xd0\xbd\xd0\xb0\xd0\xbb?'),
        ),
        migrations.AddField(
            model_name='comportsettings',
            name='gsm_phone_number',
            field=models.CharField(default='8', max_length=15),
            preserve_default=False,
        ),
    ]
