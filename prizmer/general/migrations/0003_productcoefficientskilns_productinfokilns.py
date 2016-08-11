# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_auto_20141016_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCoefficientsKilns',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sfid', models.IntegerField()),
                ('coefficient', models.FloatField()),
            ],
            options={
                'db_table': 'product_coefficients_kilns',
                'verbose_name': '\u0423\u0434\u0435\u043b\u044c\u043d\u044b\u0439 \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430',
                'verbose_name_plural': '\u0423\u0434\u0435\u043b\u044c\u043d\u044b\u0435 \u043a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u044b \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u043e\u0432',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductInfoKilns',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dt', models.DateField()),
                ('kiln_code', models.IntegerField()),
                ('product_caption', models.CharField(max_length=50)),
                ('product_count', models.IntegerField()),
                ('product_coefficient', models.FloatField()),
                ('product_weight', models.FloatField()),
            ],
            options={
                'db_table': 'product_info_kilns',
                'verbose_name': '\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043f\u043e \u043f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u0438',
            },
            bases=(models.Model,),
        ),
    ]
