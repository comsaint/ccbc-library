# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccbclib', '0003_auto_20150315_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='renew_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='return_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
