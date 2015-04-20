# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccbclib', '0008_auto_20150319_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='id',
        ),
        migrations.RemoveField(
            model_name='borrower',
            name='id',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='id',
        ),
        migrations.AddField(
            model_name='book',
            name='idbook',
            field=models.AutoField(primary_key=True, default=1, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='borrower',
            name='idborrower',
            field=models.AutoField(primary_key=True, default=1, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='idTransaction',
            field=models.AutoField(primary_key=True, default=1, serialize=False),
            preserve_default=False,
        ),
    ]
