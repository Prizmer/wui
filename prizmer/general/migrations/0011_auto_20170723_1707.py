# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0010_auto_20151029_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='meters',
            name='attr1',
            field=models.CharField(max_length=20, verbose_name=b'\xd0\x90\xd1\x82\xd1\x80\xd0\xb8\xd0\xb1\xd1\x83\xd1\x82 1', blank=True),
        ),
        migrations.AddField(
            model_name='meters',
            name='attr2',
            field=models.CharField(max_length=20, verbose_name=b'\xd0\x90\xd1\x82\xd1\x80\xd0\xb8\xd0\xb1\xd1\x83\xd1\x82 2', blank=True),
        ),
        migrations.AddField(
            model_name='meters',
            name='attr3',
            field=models.CharField(max_length=20, verbose_name=b'\xd0\x90\xd1\x82\xd1\x80\xd0\xb8\xd0\xb1\xd1\x83\xd1\x82 3', blank=True),
        ),
        migrations.AddField(
            model_name='meters',
            name='attr4',
            field=models.CharField(max_length=20, verbose_name=b'\xd0\x90\xd1\x82\xd1\x80\xd0\xb8\xd0\xb1\xd1\x83\xd1\x82 4', blank=True),
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
    ]
