# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0004_producttypekilns'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkBalanceGroupsMeters',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(max_length=38, serialize=False, editable=False, primary_key=True, blank=True)),
                ('type', models.BooleanField(default=True, verbose_name="\u0417\u043d\u0430\u043a \u0432\u0445\u043e\u0434\u0430 \u0432 \u0433\u0440\u0443\u043f\u043f\u0443 '+' ?")),
                ('guid_balance_groups', models.ForeignKey(to='general.BalanceGroups', db_column=b'guid_balance_groups')),
                ('guid_meters', models.ForeignKey(to='general.Meters', db_column=b'guid_meters')),
            ],
            options={
                'db_table': 'link_balance_groups_meters',
                'verbose_name': '\u041f\u0440\u0438\u0432\u044f\u0437\u043a\u0430 \u0413\u0440\u0443\u043f\u043f \u043a \u0441\u0447\u0451\u0442\u0447\u0438\u043a\u0443',
                'verbose_name_plural': '\u041f\u0440\u0438\u0432\u044f\u0437\u043a\u0430 \u0413\u0440\u0443\u043f\u043f \u043a \u0441\u0447\u0435\u0442\u0447\u0438\u043a\u0430\u043c',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='linkbalancegroupstakenparams',
            name='guid_balance_groups',
        ),
        migrations.RemoveField(
            model_name='linkbalancegroupstakenparams',
            name='id_taken_params',
        ),
        migrations.DeleteModel(
            name='LinkBalanceGroupsTakenParams',
        ),
        migrations.RemoveField(
            model_name='balancegroups',
            name='guid_names_params',
        ),
    ]
