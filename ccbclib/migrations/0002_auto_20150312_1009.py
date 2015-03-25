# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccbclib', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='renew_manager',
            field=models.CharField(max_length=32, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='borrower',
            name='email',
            field=models.EmailField(null=True, max_length=75),
            preserve_default=True,
        ),
    ]
