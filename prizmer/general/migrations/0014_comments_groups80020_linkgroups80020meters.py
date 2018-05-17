# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0013_auto_20170918_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(max_length=38, serialize=False, editable=False, primary_key=True, blank=True)),
                ('comment', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('guid_abonents', models.ForeignKey(to='general.Abonents', db_column=b'guid_abonents')),
            ],
            options={
                'db_table': 'comments',
                'verbose_name': '\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438',
                'verbose_name_plural': '\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438',
            },        
        ),
    ]
