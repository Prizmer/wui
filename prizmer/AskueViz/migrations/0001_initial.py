# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0002_auto_20141016_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiagramDevices',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(max_length=38, serialize=False, editable=False, primary_key=True, blank=True)),
                ('deviceboxleft', models.IntegerField()),
                ('deviceboxtop', models.IntegerField()),
                ('deviceboxwidth', models.IntegerField()),
                ('deviceboxheight', models.IntegerField()),
            ],
            options={
                'db_table': 'diagram_devices',
                'verbose_name': '\u0423\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u043e \u043d\u0430 \u0434\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u0435',
                'verbose_name_plural': '\u0423\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430 \u043d\u0430 \u0434\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u0435',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DiagramMainframe',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(max_length=38, serialize=False, editable=False, primary_key=True, blank=True)),
                ('backgroundurl', models.CharField(max_length=20)),
                ('refreshmentTimeMS', models.IntegerField(default=3000)),
                ('mainframeleft', models.IntegerField()),
                ('mainframetop', models.IntegerField()),
                ('mainframewidth', models.IntegerField()),
                ('mainframeheight', models.IntegerField()),
            ],
            options={
                'db_table': 'diagram_mainframe',
                'verbose_name': '\u0413\u043b\u0430\u0432\u043d\u0430\u044f \u0434\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u0430',
                'verbose_name_plural': '\u0413\u043b\u0430\u0432\u043d\u044b\u0435 \u0434\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LinkMainframeAbonents',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(max_length=38, serialize=False, editable=False, primary_key=True, blank=True)),
                ('guid_abonents', models.ForeignKey(to='general.Abonents', db_column=b'guid_abonents')),
                ('guid_mainframe', models.ForeignKey(to='AskueViz.DiagramMainframe', db_column=b'guid_mainframe')),
            ],
            options={
                'db_table': 'link_mainframe_abonents',
                'verbose_name': '\u041f\u0440\u0438\u0432\u044f\u0437\u043a\u0430 \u0430\u0431\u043e\u043d\u0435\u043d\u0442\u0430 \u043a \u0433\u043b\u0430\u0432\u043d\u043e\u0439 \u0434\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u0435',
                'verbose_name_plural': '\u041f\u0440\u0438\u0432\u044f\u0437\u043a\u0438 \u0430\u0431\u043e\u043d\u0435\u043d\u0442\u043e\u0432 \u043a \u0433\u043b\u0430\u0432\u043d\u044b\u043c \u0434\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u0430\u043c',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LinkTakenParamDiagramDevices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=10)),
                ('showmain', models.IntegerField(default=1)),
                ('mvalleft', models.IntegerField()),
                ('mvalright', models.IntegerField()),
                ('guid_diagram_devices', models.ForeignKey(to='AskueViz.DiagramDevices', db_column=b'guid_diagram_devices')),
                ('guid_taken_params', models.ForeignKey(to='general.TakenParams', db_column=b'guid_taken_params', to_field=b'guid')),
            ],
            options={
                'db_table': 'link_taken_param_diagram_devices',
                'verbose_name': '\u041f\u0440\u0438\u0432\u044f\u0437\u043a\u0430 \u0441\u0447\u0438\u0442\u044b\u0432\u0430\u0435\u043c\u044b\u0445 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 \u043a \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430\u043c \u043d\u0430 \u0434\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u0435',
                'verbose_name_plural': '\u041f\u0440\u0438\u0432\u044f\u0437\u043a\u0438 \u0441\u0447\u0438\u0442\u044b\u0432\u0430\u0435\u043c\u044b\u0445 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 \u043a \u0443\u0441\u0442\u0440\u043e\u0439\u0441\u0442\u0432\u0430\u043c \u043d\u0430 \u0434\u0438\u0430\u0433\u0440\u0430\u043c\u043c\u0435',
            },
            bases=(models.Model,),
        ),
    ]
