# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccbclib', '0012_book_status_flag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='status_flag',
            new_name='statusflag',
        ),
        migrations.RemoveField(
            model_name='borrower',
            name='status',
        ),
        migrations.AddField(
            model_name='borrower',
            name='statusflag',
            field=models.CharField(choices=[('NM', 'Normal'), ('SP', 'Special')], max_length=16, default='NM'),
            preserve_default=True,
        ),
    ]
