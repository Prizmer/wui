# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_productcoefficientskilns_productinfokilns'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTypeKilns',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nm', models.CharField(max_length=80)),
                ('kind_id', models.IntegerField()),
            ],
            options={
                'db_table': 'product_type_kilns',
                'verbose_name': '\u0422\u0438\u043f\u044b \u043f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u0438',
            },
            bases=(models.Model,),
        ),
    ]
