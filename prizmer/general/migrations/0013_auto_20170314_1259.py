# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0012_remove_linkobjectuser_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups80020',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(max_length=38, serialize=False, editable=False, primary_key=True, blank=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('name_sender', models.CharField(max_length=250)),
                ('inn_sender', models.CharField(max_length=250)),
                ('name_postavshik', models.CharField(max_length=250)),
                ('inn_postavshik', models.CharField(max_length=250)),
            ],
            options={
                'db_table': 'groups_80020',
                'verbose_name': '\u0413\u0440\u0443\u043f\u043f\u0430 \u043e\u0442\u0447\u0451\u0442\u043e\u0432 80020',
                'verbose_name_plural': '\u0413\u0440\u0443\u043f\u043f\u044b \u043e\u0442\u0447\u0451\u0442\u043e\u0432 80020',
            },
        ),
        migrations.CreateModel(
            name='LinkGroups80020Meters',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(max_length=38, serialize=False, editable=False, primary_key=True, blank=True)),
                ('measuringpoint_code', models.DecimalField(max_digits=15, decimal_places=0)),
                ('measuringpoint_name', models.CharField(max_length=250)),
                ('guid_groups_80020', models.ForeignKey(to='general.Groups80020', db_column=b'guid_groups_80020')),
            ],
            options={
                'db_table': 'link_groups_80020_meters',
                'verbose_name': '\u0421\u0432\u044f\u0437\u044c \u0441\u0447\u0451\u0442\u0447\u0438\u043a\u0430 \u0438 \u0413\u0440\u0443\u043f\u043f 80020',
                'verbose_name_plural': '\u0421\u0432\u044f\u0437\u0438 \u0441\u0447\u0451\u0442\u0447\u0438\u043a\u043e\u0432 \u0438 \u0413\u0440\u0443\u043f\u043f 80020',
            },
        ),
        migrations.RemoveField(
            model_name='linkabonentuser',
            name='guid_abonent',
        ),
        migrations.RemoveField(
            model_name='linkabonentuser',
            name='guid_user',
        ),
        migrations.RemoveField(
            model_name='linkobjectuser',
            name='guid_object',
        ),
        migrations.RemoveField(
            model_name='linkobjectuser',
            name='guid_user',
        ),
        migrations.AlterField(
            model_name='meters',
            name='password',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.DeleteModel(
            name='LinkAbonentUser',
        ),
        migrations.DeleteModel(
            name='LinkObjectUser',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='linkgroups80020meters',
            name='guid_meters',
            field=models.ForeignKey(to='general.Meters', db_column=b'guid_meters'),
        ),
    ]
