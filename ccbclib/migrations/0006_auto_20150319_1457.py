# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccbclib', '0005_auto_20150315_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='email',
            field=models.EmailField(max_length=75, blank=True, default=None, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='borrow_manager',
            field=models.CharField(max_length=32, default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='renew_date',
            field=models.DateField(blank=True, default=None, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='renew_manager',
            field=models.CharField(max_length=32, blank=True, default=None, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='return_date',
            field=models.DateField(blank=True, default=None, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='return_manager',
            field=models.CharField(max_length=32, blank=True, default=None, null=True),
            preserve_default=True,
        ),
    ]
