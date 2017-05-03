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
                ('dogovor_number', models.CharField(default=10, max_length=50)),
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
                ('measuringpoint_code', models.DecimalField(max_digits=18, decimal_places=0)),
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
            name='address',
            field=models.IntegerField(verbose_name=b'\xd0\xa1\xd0\xb5\xd1\x82\xd0\xb5\xd0\xb2\xd0\xbe\xd0\xb9 \xd0\xb0\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81'),
        ),
        migrations.AlterField(
            model_name='meters',
            name='dt_install',
            field=models.DateTimeField(null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x83\xd1\x81\xd1\x82\xd0\xb0\xd0\xbd\xd0\xbe\xd0\xb2\xd0\xba\xd0\xb8', blank=True),
        ),
        migrations.AlterField(
            model_name='meters',
            name='dt_last_read',
            field=models.DateTimeField(null=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd0\xbe\xd1\x81\xd0\xbb\xd0\xb5\xd0\xb4\xd0\xbd\xd0\xb5\xd0\xb3\xd0\xbe \xd1\x83\xd0\xb4\xd0\xb0\xd1\x87\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd1\x87\xd1\x82\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xb4\xd0\xb0\xd0\xbd\xd0\xbd\xd1\x8b\xd1\x85', blank=True),
        ),
        migrations.AlterField(
            model_name='meters',
            name='factory_number_manual',
            field=models.CharField(max_length=16, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb2\xd0\xbe\xd0\xb4\xd1\x81\xd0\xba\xd0\xbe\xd0\xb9 \xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80(\xd0\xb2\xd1\x80\xd1\x83\xd1\x87\xd0\xbd\xd1\x83\xd1\x8e)'),
        ),
        migrations.AlterField(
            model_name='meters',
            name='factory_number_readed',
            field=models.CharField(max_length=16, null=True, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb2\xd0\xbe\xd0\xb4\xd1\x81\xd0\xba\xd0\xbe\xd0\xb9 \xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80(\xd0\xb8\xd0\xb7 \xd0\xbf\xd1\x80\xd0\xb8\xd0\xb1\xd0\xbe\xd1\x80\xd0\xb0)', blank=True),
        ),
        migrations.AlterField(
            model_name='meters',
            name='is_factory_numbers_equal',
            field=models.NullBooleanField(verbose_name=b'\xd0\xa1\xd0\xbe\xd0\xb2\xd0\xbf\xd0\xb0\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80\xd0\xbe\xd0\xb2'),
        ),
        migrations.AlterField(
            model_name='meters',
            name='name',
            field=models.CharField(unique=True, max_length=50, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f'),
        ),
        migrations.AlterField(
            model_name='meters',
            name='password',
            field=models.CharField(max_length=100, verbose_name=b'\xd0\x9f\xd0\xb0\xd1\x80\xd0\xbe\xd0\xbb\xd1\x8c', blank=True),
        ),
        migrations.AlterField(
            model_name='meters',
            name='password_type_hex',
            field=models.BooleanField(default=True, verbose_name=b'\xd0\x98\xd1\x81\xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd1\x8c HEX \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xbf\xd0\xb0\xd1\x80\xd0\xbe\xd0\xbb\xd1\x8f?'),
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
