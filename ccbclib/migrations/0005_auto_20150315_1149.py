# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccbclib', '0004_auto_20150315_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='renew_manager',
            field=models.CharField(default='', blank=True, max_length=32, null=True),
            preserve_default=True,
        ),
    ]
