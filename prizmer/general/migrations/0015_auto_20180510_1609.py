# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0014_comments_groups80020_linkgroups80020meters'),
    ]

    operations = [
        
        migrations.AddField(
            model_name='comments',
            name='name',
            field=models.CharField(default=b'testdata', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(),
        ),
    ]
