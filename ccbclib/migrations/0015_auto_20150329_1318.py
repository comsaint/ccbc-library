# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccbclib', '0014_auto_20150324_1632'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='borrower',
            unique_together=set([('name', 'phone')]),
        ),
    ]
