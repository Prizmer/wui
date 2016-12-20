# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0010_auto_20151029_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkAbonentUser',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(max_length=38, serialize=False, editable=False, primary_key=True, blank=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('guid_abonent', models.ForeignKey(to='general.Abonents', db_column=b'guid_abonent')),
            ],
            options={
                'db_table': 'link_abon_user',
                'verbose_name': '\u041f\u0440\u0438\u0432\u044f\u0437\u043a\u0430 \u043a\u0432\u0430\u0440\u0442\u0438\u0440\u044b \u043a \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044e',
                'verbose_name_plural': '\u041f\u0440\u0438\u0432\u044f\u0437\u043a\u0438 \u043a\u0432\u0430\u0440\u0442\u0438\u0440 \u043a \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f\u043c',
            },
        ),
        migrations.CreateModel(
            name='LinkObjectUser',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(max_length=38, serialize=False, editable=False, primary_key=True, blank=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('guid_object', models.ForeignKey(to='general.Objects', db_column=b'guid_object')),
            ],
            options={
                'db_table': 'link_obj_user',
                'verbose_name': '\u041f\u0440\u0438\u0432\u044f\u0437\u043a\u0430 \u043e\u0431\u044a\u0435\u043a\u0442\u0430 \u043a \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044e',
                'verbose_name_plural': '\u041f\u0440\u0438\u0432\u044f\u0437\u043a\u0438 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432 \u043a \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f\u043c',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(max_length=38, serialize=False, editable=False, primary_key=True, blank=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'db_table': 'user',
                'verbose_name': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c',
                'verbose_name_plural': '\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438',
            },
        ),
        migrations.AddField(
            model_name='linkobjectuser',
            name='guid_user',
            field=models.ForeignKey(to='general.User', db_column=b'guid_user'),
        ),
        migrations.AddField(
            model_name='linkabonentuser',
            name='guid_user',
            field=models.ForeignKey(to='general.User', db_column=b'guid_user'),
        ),
    ]
