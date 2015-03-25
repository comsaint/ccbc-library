# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccbclib', '0006_auto_20150319_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='email',
            field=models.EmailField(null=True, max_length=75, default='no_email@no_email.com', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='borrow_date',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
