# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccbclib', '0015_auto_20150329_1318'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['code_number']},
        ),
        migrations.AlterModelOptions(
            name='borrower',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-idtransaction']},
        ),
        migrations.RemoveField(
            model_name='book',
            name='code',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=32, default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='book_area',
            field=models.CharField(max_length=32, default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='code_number',
            field=models.CharField(max_length=6, default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='lang',
            field=models.CharField(max_length=8, default=None),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=32, default=None, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
