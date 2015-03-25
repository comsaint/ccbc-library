# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccbclib', '0011_remove_book_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status_flag',
            field=models.CharField(max_length=16, default='NM', choices=[('NM', 'Normal'), ('SP', 'Special')]),
            preserve_default=True,
        ),
    ]
