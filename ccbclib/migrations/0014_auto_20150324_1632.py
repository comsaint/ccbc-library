# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccbclib', '0013_auto_20150324_1044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='idTransaction',
            new_name='idtransaction',
        ),
        migrations.RemoveField(
            model_name='book',
            name='area',
        ),
        migrations.AlterField(
            model_name='book',
            name='code',
            field=models.CharField(max_length=8),
            preserve_default=True,
        ),
    ]
