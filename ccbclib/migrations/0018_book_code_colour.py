# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccbclib', '0017_auto_20150408_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='code_colour',
            field=models.CharField(max_length=16, default=None),
            preserve_default=True,
        ),
    ]
