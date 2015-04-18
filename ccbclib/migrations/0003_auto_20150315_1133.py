# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccbclib', '0002_auto_20150312_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='times_borrowed',
        ),
        migrations.RemoveField(
            model_name='book',
            name='times_overdued',
        ),
        migrations.RemoveField(
            model_name='borrower',
            name='borrow_count',
        ),
        migrations.RemoveField(
            model_name='borrower',
            name='overdue_count',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='due_date',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='borrow_date',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='borrow_manager',
            field=models.CharField(max_length=32, default=''),
            preserve_default=True,
        ),
    ]
