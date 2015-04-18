# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ccbclib', '0019_auto_20150408_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=128, null=True, default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='book_area',
            field=models.CharField(choices=[('信仰個人成長', 'A'), ('靈修', 'B'), ('宣教', 'C'), ('護教', 'D'), ('見證', 'E'), ('佈道', 'F'), ('家庭、兩性關係', 'G'), ('情緒', 'H'), ('祈禱', 'I'), ('敬拜', 'J'), ('兒童(宗教)', 'K'), ('兒童(其他)', 'L'), ('少年', 'M'), ('UNKNOWN', 'UN')], max_length=128, default='UNKNOWN'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='code_colour',
            field=models.CharField(choices=[('Blue', 'Blue'), ('Red', 'Red'), ('Black', 'Black'), ('Green', 'Green'), ('White', 'White'), ('Orange', 'Orange'), ('Yellow', 'Yellow'), ('Pink', 'Pink'), ('Gray', 'Gray'), ('Black lines', 'Black lines')], blank=True, max_length=16, null=True, default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='code_number',
            field=models.CharField(max_length=6, default=None, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='lang',
            field=models.CharField(choices=[('C', 'Chinese'), ('E', 'English')], max_length=8),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(blank=True, max_length=128, null=True, default=None),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='borrower',
            name='email',
            field=models.EmailField(blank=True, max_length=75, null=True, default=None),
            preserve_default=True,
        ),
    ]
