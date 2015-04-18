# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccbclib', '0016_auto_20150408_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_area',
            field=models.CharField(max_length=32, default='TBC'),
            preserve_default=True,
        ),
    ]
