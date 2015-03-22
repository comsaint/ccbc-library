# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccbclib', '0007_auto_20150319_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='book',
            field=models.ForeignKey(to='ccbclib.Book', related_name='book'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='borrower',
            field=models.ForeignKey(to='ccbclib.Borrower', related_name='borrower'),
            preserve_default=True,
        ),
    ]
