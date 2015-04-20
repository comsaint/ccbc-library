# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccbclib', '0018_book_code_colour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='code_colour',
            field=models.CharField(max_length=16, null=True, default=None, blank=True),
            preserve_default=True,
        ),
    ]
